"""Auto-Dream — nightly memory consolidation for pi.

Reads the last 24h of JSONL session logs from ~/.pi/sessions/logs/, produces a
markdown report under ~/.pi/sessions/reports/auto-dream-YYYY-MM-DD.md with:

  * activity summary (sessions, turns, tool calls, errors)
  * recurring topics (which wings were hit most, what keywords spiked)
  * MemPalace coverage gaps (wings with few drawers vs what's trending)
  * vault-promotion candidates (topics mentioned 3+ times with no obvious
    existing wiki/decisions/ note)

DOES NOT auto-write to MemPalace or the vault. This script is suggest-only —
the user reviews the report and promotes by hand. Auto-writing risks quality
drift (every bad chat becomes a vault note); a human-in-the-loop keeps the
knowledge surface curated.

Thin-data contract:
  If there are fewer than 10 substantive user messages in the window, the
  report still renders but flags the window as thin. That's expected behavior
  for the first week or two — don't panic.

Run manually:  python ~/.pi/agent/bin/auto_dream.py
Schedule:      see register_auto_dream.ps1 alongside this file.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Iterable

import os

_pi_home = Path(os.environ.get("PI_AGENT_HOME", Path.home() / ".pi"))
ROOT = _pi_home / "sessions"
LOG_DIR = ROOT / "logs"
REPORT_DIR = ROOT / "reports"
RECALL_LOG = Path.home() / ".mempalace" / "hook_state" / "recalls.jsonl"
_vault_env = os.environ.get("OBSIDIAN_VAULT", "")
VAULT_ROOT = Path(_vault_env).expanduser() if _vault_env else Path.home() / "ObsidianVault"
WIKI_ROOT = VAULT_ROOT / "wiki"

WINDOW_HOURS = 24
RECENT_DRAWER_DAYS = 14
DEADWEIGHT_DAYS = 30
MIN_SUBSTANTIVE_USER_MSGS = 10
HOT_TOPIC_THRESHOLD = 3
SYNTHESIS_MIN_CLUSTER = 5
CONTRADICTION_MIN_SIM = 0.78
CONTRADICTION_MAX_JACCARD = 0.55
MISSING_LINK_TOP_K = 5

# Mirror the stop-hook routing table so reports use the same wing vocabulary.
WING_RULES = [
    ("konekt_nextjs", re.compile(r"\b(gloss|konekt|next\.?js|react|tsx?|tailwind|mui|phosphor|nextauth|radix)\b", re.I)),
    ("expert-knowledge", re.compile(r"\b(obsidian|vault|omegad4rkmynd|shadowvault|wiki|karpathy|frontmatter|dataview)\b", re.I)),
    ("mempalace", re.compile(r"\b(mempalace|chroma|embedding|hnsw|bm25|drawer|daemon|pi\s+agent|minimax)\b", re.I)),
    ("expert-orchestration", re.compile(r"\b(hook|skill|claude\s*code|agent|subagent|extension)\b", re.I)),
    ("expert-security", re.compile(r"\b(security|auth|jwt|session|token|xss|sql|csrf|wcag|a11y)\b", re.I)),
]

STOP_WORDS = set(
    "the a an and or but if when then that this those these to of in on at for with from by is are was "
    "were be been being do does did i you we he she it they them us our your their my me mine his her "
    "have has had will would could should may might can so just like as into about over out up down "
    "not no yes very much really actually maybe pretty quite some any all one two"
    .split()
)
# Programming-language noise — adding to STOP_WORDS keeps synthesis clustering
# from flagging language keywords as "topics." Covers TS/JS/Python/Go/Rust/CSS
# plus common identifiers that mean nothing as topical signals.
STOP_WORDS.update(
    "const let var function return null true false void class interface enum type typeof "
    "import export default export_default module require from async await new this self "
    "static public private protected abstract readonly extends implements namespace as "
    "typeof instanceof throw catch finally try else switch case break continue while for "
    "each each_with of_length length size count index first last head tail "
    "string number boolean object array list map set tuple dict none undefined nil "
    "color colors tokens token text display name value values key keys item items "
    "props state children className style styles render component components react next "
    "div span button input form label event handler onclick onchange onsubmit "
    "fn pub impl trait mut dyn struct "
    "def pass yield lambda global nonlocal raise assert with elif "
    "func go_ defer chan select map_ "
    "public_class private_class static_final void_main "
    "www com http https www2 html utf encoding unicode "
    # Markdown/README/doc boilerplate noise — appears in every doc.
    "page pages file files folder folders path paths what when where which why how "
    "also only just here there thing things way ways part parts section sections "
    "status session sessions example examples usage using use used note notes "
    "info details description overview summary introduction contents content "
    "line lines item items option options step steps feature features "
    "must should need needs make made makes making get gets got getting set sets "
    "add adds added adding check checks checking run runs running build builds".split()
)


def iter_recent_lines(since: datetime) -> Iterable[dict]:
    """Yield JSONL events from any daily log file that overlaps the window."""
    if not LOG_DIR.exists():
        return
    # Look at today and yesterday's files to cover any 24h window cleanly.
    candidates = sorted(LOG_DIR.glob("*.jsonl"))[-3:]
    for path in candidates:
        try:
            with path.open("r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        obj = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    ts_raw = obj.get("ts", "")
                    try:
                        ts = datetime.fromisoformat(ts_raw.replace("Z", "+00:00"))
                    except ValueError:
                        continue
                    # Normalize to naive local-ish by dropping tz for comparison.
                    ts_naive = ts.replace(tzinfo=None)
                    if ts_naive >= since:
                        obj["_ts"] = ts_naive
                        yield obj
        except OSError:
            continue


def route_wing(text: str) -> str:
    for wing, rx in WING_RULES:
        if rx.search(text):
            return wing
    return "mempalace"


def keywords(text: str) -> list[str]:
    # Dead-simple tokenizer; we're doing trend-spotting not linguistics.
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9_\-]{2,}", text.lower())
    return [t for t in tokens if t not in STOP_WORDS and len(t) >= 4]


def fetch_mempalace_wing_counts() -> dict[str, int]:
    """Best-effort read of per-wing drawer counts. Returns {} on any error."""
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from mempalace_fast import PALACE  # type: ignore
        from mempalace.backends.chroma import ChromaBackend  # type: ignore

        backend = ChromaBackend()
        col = backend.get_collection(PALACE, "mempalace_drawers", create=False)
        got = col.get(include=["metadatas"])
        metas = got.get("metadatas") or []
        counts: dict[str, int] = {}
        for m in metas:
            if not m:
                continue
            w = m.get("wing") or "(none)"
            counts[w] = counts.get(w, 0) + 1
        return counts
    except Exception:
        return {}


# ---------------------------------------------------------------------------
# Tier 1/2 augmentations — read-only analysis that turns the dream from a
# diary into a worklist. Each function below returns a list of finding dicts;
# render_* helpers below format them for the report. All are suggest-only —
# NOTHING writes to the palace or vault.
# ---------------------------------------------------------------------------


def recall_key(wing: str, room: str, text: str) -> str:
    """Mirror mempalace_prompt_hook._recall_key. Keep these in lockstep."""
    h = hashlib.sha1(f"{wing}::{room}::{text[:200]}".encode("utf-8")).hexdigest()
    return h[:16]


def fetch_drawers_with_metadata():
    """Return (ids, metadatas, documents) from the palace, or (None,None,None)."""
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from mempalace_fast import PALACE  # type: ignore
        from mempalace.backends.chroma import ChromaBackend  # type: ignore

        backend = ChromaBackend()
        col = backend.get_collection(PALACE, "mempalace_drawers", create=False)
        got = col.get(include=["metadatas", "documents"])
        return got.get("ids") or [], got.get("metadatas") or [], got.get("documents") or []
    except Exception:
        return None, None, None


_CODE_EXTS = {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".py", ".pyw", ".go",
              ".rs", ".java", ".kt", ".c", ".cc", ".cpp", ".h", ".hpp", ".cs",
              ".rb", ".php", ".swift", ".scala", ".css", ".scss", ".sass", ".less",
              ".html", ".xml", ".yml", ".yaml", ".toml", ".lock", ".json",
              ".sql", ".sh", ".bash", ".ps1", ".bat", ".cmd"}


def _is_code_drawer(meta: dict) -> bool:
    """Drawers mined from source code are noise for synthesis clustering —
    their tokens are language keywords, not ideas. Filter them out so
    clusters reflect decisions, prose, and curated notes instead.
    """
    src = str(meta.get("source_file", "")).lower()
    if not src:
        return False
    for ext in _CODE_EXTS:
        if src.endswith(ext):
            return True
    return False


def _list_md_files(root: Path) -> list[Path]:
    if not root.is_dir():
        return []
    return [p for p in root.rglob("*.md") if p.is_file() and not p.name.startswith("_")]


def _jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


# 1. GAP DETECTOR — hot topics with no vault anchor -------------------------
def detect_vault_gaps(hot_topics: list[tuple[str, int, str]]) -> list[dict]:
    """For each hot topic keyword, check if the vault has any file mentioning it.

    A 'gap' is a keyword that appears 3+ times in recent chat but has zero hits
    in the vault — meaning your thinking is ahead of your written knowledge.
    """
    if not VAULT_ROOT.is_dir() or not hot_topics:
        return []

    # One-pass index: lowercase concat of all vault md content + filenames.
    try:
        index_text = []
        for p in VAULT_ROOT.rglob("*.md"):
            # Skip raw/ — it's immutable cache, shouldn't influence gap detection.
            if "raw" in p.parts:
                continue
            try:
                index_text.append(p.stem.lower())
                index_text.append(p.read_text(encoding="utf-8", errors="ignore").lower())
            except OSError:
                continue
        haystack = "\n".join(index_text)
    except Exception:
        return []

    findings = []
    for kw, count, wing in hot_topics:
        kw_lc = kw.lower()
        # Require whole-word match to avoid 'react' matching 'reacted'.
        hits = len(re.findall(rf"\b{re.escape(kw_lc)}\b", haystack))
        if hits == 0:
            findings.append({
                "keyword": kw,
                "mentions": count,
                "wing": wing,
                "vault_hits": 0,
                "suggestion": f"wiki/concepts/{kw_lc}.md or wiki/syntheses/{kw_lc}.md",
            })
        elif hits < 3 and count >= 5:
            # Mentioned a lot in chat, barely in vault — soft gap.
            findings.append({
                "keyword": kw,
                "mentions": count,
                "wing": wing,
                "vault_hits": hits,
                "suggestion": "expand existing coverage — barely referenced in vault",
            })
    return findings


# 2. SYNTHESIS CANDIDATES — drawer clusters worth a synthesis page ----------
def detect_synthesis_candidates(ids, metadatas, documents, since_dt: datetime) -> list[dict]:
    """Cluster recent drawers by shared keywords; flag coherent clusters.

    Cheap substitute for HNSW clustering: group drawers by their most-frequent
    shared non-stopword token. Clusters with ≥SYNTHESIS_MIN_CLUSTER drawers on
    a wing get flagged as synthesis candidates. Honest about limits — this is
    keyword co-occurrence, not semantic clustering.
    """
    if not ids:
        return []

    # (wing, keyword) -> list of (drawer_id, source)
    buckets: dict[tuple[str, str], list[tuple[str, str]]] = defaultdict(list)

    for did, meta, doc in zip(ids, metadatas or [], documents or []):
        if not meta or not doc:
            continue
        # Skip code drawers — their tokens are language keywords, not topics.
        if _is_code_drawer(meta):
            continue
        filed_raw = meta.get("filed_at", "")
        try:
            filed = datetime.fromisoformat(filed_raw)
        except (TypeError, ValueError):
            continue
        if filed < since_dt:
            continue
        wing = meta.get("wing", "?")
        for kw in set(keywords(doc[:1200])):  # cap per-drawer work
            buckets[(wing, kw)].append((did, str(meta.get("source_file", ""))))

    findings = []
    # Check if a synthesis page already exists for this keyword.
    existing_syntheses = {p.stem.lower() for p in _list_md_files(WIKI_ROOT / "syntheses")}
    existing_concepts = {p.stem.lower() for p in _list_md_files(WIKI_ROOT / "concepts")}

    seen_keywords = set()
    for (wing, kw), drawers in sorted(buckets.items(), key=lambda x: -len(x[1])):
        if len(drawers) < SYNTHESIS_MIN_CLUSTER:
            continue
        if kw in seen_keywords:
            continue
        seen_keywords.add(kw)
        has_synthesis = kw.lower() in existing_syntheses
        has_concept = kw.lower() in existing_concepts
        findings.append({
            "keyword": kw,
            "wing": wing,
            "cluster_size": len(drawers),
            "has_synthesis": has_synthesis,
            "has_concept": has_concept,
            "sample_ids": [d[0] for d in drawers[:3]],
            "sample_sources": list({d[1] for d in drawers if d[1]})[:3],
        })
        if len(findings) >= 12:
            break
    # Prioritize: no synthesis AND no concept = strongest candidate.
    findings.sort(key=lambda f: (f["has_synthesis"], f["has_concept"], -f["cluster_size"]))
    return findings


# 3. CONTRADICTION DETECTOR — drawer vs wiki divergence ---------------------
def detect_contradictions(ids, metadatas, documents, since_dt: datetime) -> list[dict]:
    """Flag recent drawers that overlap heavily with a wiki page but differ.

    Heuristic: token-set Jaccard as a cheap similarity proxy. A drawer and a
    wiki page sharing 40-55% of their tokens (high topic overlap, substantial
    wording divergence) are 'review candidates' — not proven contradictions.

    This is intentionally wide-net + suggest-only. Real NLI would need an LLM;
    we'd rather over-flag than miss a drift.
    """
    if not ids or not WIKI_ROOT.is_dir():
        return []

    wiki_pages = []
    for p in WIKI_ROOT.rglob("*.md"):
        if "raw" in p.parts or p.name.startswith("_") or p.name in {"index.md", "log.md", "hot.md", "overview.md"}:
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        tokens = set(keywords(text))
        if len(tokens) >= 10:
            wiki_pages.append((p, tokens))
    if not wiki_pages:
        return []

    findings = []
    for did, meta, doc in zip(ids, metadatas or [], documents or []):
        if not meta or not doc:
            continue
        # Code drawers share generic lang-keyword overlap with any page; skip.
        if _is_code_drawer(meta):
            continue
        filed_raw = meta.get("filed_at", "")
        try:
            filed = datetime.fromisoformat(filed_raw)
        except (TypeError, ValueError):
            continue
        if filed < since_dt:
            continue
        drawer_tokens = set(keywords(doc[:2000]))
        if len(drawer_tokens) < 10:
            continue

        for page, page_tokens in wiki_pages:
            jac = _jaccard(drawer_tokens, page_tokens)
            # Overlap "high enough to be the same topic" but not identical.
            if 0.35 <= jac <= CONTRADICTION_MAX_JACCARD:
                findings.append({
                    "drawer_id": did,
                    "drawer_wing": meta.get("wing", "?"),
                    "drawer_source": str(meta.get("source_file", "")),
                    "wiki_page": str(page.relative_to(VAULT_ROOT)),
                    "jaccard": round(jac, 2),
                    "drawer_preview": doc[:200].replace("\n", " "),
                })
                break  # one flag per drawer is enough
        if len(findings) >= 15:
            break

    return findings


# 4. MISSING-LINK SUGGESTIONS — Karpathy-wiki neighbor gaps -----------------
_WIKILINK_RX = re.compile(r"\[\[([^\]|#]+?)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def detect_missing_links() -> list[dict]:
    """For each wiki concept/synthesis page, find its top-K nearest pages by
    shared-keyword overlap and flag any that aren't already [[linked]].

    Keyword overlap is a cheap proxy for embedding similarity. It catches the
    obvious misses; it won't catch semantic-but-lexically-different links.
    Still the single highest-leverage wiki operation if you're running the
    Karpathy pattern (links = knowledge).
    """
    if not WIKI_ROOT.is_dir():
        return []

    pages: list[tuple[Path, set[str], set[str]]] = []  # (path, tokens, existing_links)
    for sub in ("concepts", "syntheses", "entities"):
        for p in _list_md_files(WIKI_ROOT / sub):
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            tokens = set(keywords(text))
            if len(tokens) < 8:
                continue
            links = {m.group(1).strip().lower() for m in _WIKILINK_RX.finditer(text)}
            pages.append((p, tokens, links))

    if len(pages) < 2:
        return []

    findings = []
    for i, (path_a, tokens_a, links_a) in enumerate(pages):
        scored = []
        for j, (path_b, tokens_b, _) in enumerate(pages):
            if i == j:
                continue
            jac = _jaccard(tokens_a, tokens_b)
            if jac >= 0.15:
                scored.append((jac, path_b))
        scored.sort(reverse=True)

        missing = []
        for score, path_b in scored[:MISSING_LINK_TOP_K]:
            slug = path_b.stem.lower()
            if slug in links_a:
                continue
            missing.append({
                "target": path_b.stem,
                "target_path": str(path_b.relative_to(VAULT_ROOT)),
                "overlap": round(score, 2),
            })
        if missing:
            findings.append({
                "page": str(path_a.relative_to(VAULT_ROOT)),
                "suggestions": missing,
            })
        if len(findings) >= 10:
            break

    return findings


# 5. RECALL-WEIGHTED DEADWEIGHT ---------------------------------------------
def analyze_recall_weights(ids, metadatas) -> dict:
    """Count recalls per drawer key across the recall log.

    Returns:
      {
        "recall_log_exists": bool,
        "recall_log_days": int,
        "dead_drawers": [{drawer_id, wing, source_file}],  # never recalled
        "hot_drawers": [{drawer_id, wing, source, recall_count}],  # top 10
        "total_recalls": int,
        "unique_recalled": int,
      }
    """
    if not RECALL_LOG.exists():
        return {
            "recall_log_exists": False,
            "note": "Recall logging just enabled — this section will populate as "
                    "the prompt hook records injections. Check back in a week.",
        }

    # Build key -> recall_count from log
    recall_counts: Counter[str] = Counter()
    first_ts = None
    last_ts = None
    total = 0
    try:
        with RECALL_LOG.open("r", encoding="utf-8") as f:
            for line in f:
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError:
                    continue
                ts_raw = entry.get("ts", "")
                try:
                    ts = datetime.fromisoformat(ts_raw)
                    if first_ts is None or ts < first_ts:
                        first_ts = ts
                    if last_ts is None or ts > last_ts:
                        last_ts = ts
                except ValueError:
                    pass
                for k in entry.get("keys") or []:
                    recall_counts[k] += 1
                    total += 1
    except OSError:
        return {"recall_log_exists": False, "note": "Could not read recall log."}

    if first_ts is None or total == 0:
        return {
            "recall_log_exists": True,
            "recall_log_days": 0,
            "total_recalls": 0,
            "note": "Recall log exists but empty — wait for the hook to run.",
        }

    days_of_data = max(1, (last_ts - first_ts).days + 1)

    # Compute dead drawers: in palace, never recalled. Only meaningful after
    # enough data accumulates — gate on DEADWEIGHT_DAYS of history.
    dead = []
    hot_list = []
    if ids and metadatas:
        for did, meta in zip(ids, metadatas):
            if not meta:
                continue
            key = recall_key(meta.get("wing", "?"), meta.get("room", "?"), "")
            # The hash depends on text too; we need the doc to match. Skip
            # here — we can't match drawers to recall keys without documents.
            # See build_dead_list in main for the text-aware version.
            pass

    # Find most-recalled keys (don't need drawer match)
    for k, c in recall_counts.most_common(10):
        hot_list.append({"key": k, "recall_count": c})

    return {
        "recall_log_exists": True,
        "recall_log_days": days_of_data,
        "total_recalls": total,
        "unique_recalled": len(recall_counts),
        "hot_keys": hot_list,
        "recall_counts": recall_counts,  # raw, for deadweight pass
        "enough_data_for_deadweight": days_of_data >= DEADWEIGHT_DAYS,
    }


def build_deadweight_list(ids, metadatas, documents, recall_counts: Counter) -> list[dict]:
    """Drawers in the palace that were never recalled by the hook.

    Only called when we have enough recall history to make deadweight claims.
    """
    dead = []
    for did, meta, doc in zip(ids or [], metadatas or [], documents or []):
        if not meta or not doc:
            continue
        key = recall_key(meta.get("wing", "?"), meta.get("room", "?"), doc)
        if key in recall_counts:
            continue
        dead.append({
            "drawer_id": did,
            "wing": meta.get("wing", "?"),
            "room": meta.get("room", "?"),
            "source": str(meta.get("source_file", ""))[-60:],
        })
        if len(dead) >= 50:
            break
    return dead


def main() -> int:
    now = datetime.now()
    since = now - timedelta(hours=WINDOW_HOURS)

    # Collectors
    sessions_seen: set[str] = set()
    tool_counter: Counter[str] = Counter()
    tool_errors: Counter[str] = Counter()
    user_msgs: list[str] = []
    assistant_msg_count = 0
    wing_hits: Counter[str] = Counter()
    keyword_counts: Counter[str] = Counter()
    per_wing_keywords: dict[str, Counter[str]] = defaultdict(Counter)

    for event in iter_recent_lines(since):
        sid = event.get("session_id")
        if sid:
            sessions_seen.add(sid)
        t = event.get("type")
        if t == "tool":
            tool_counter[event.get("tool", "?")] += 1
            if event.get("is_error"):
                tool_errors[event.get("tool", "?")] += 1
        elif t == "message":
            role = event.get("role")
            text = event.get("text_excerpt", "") or ""
            if role == "user" and len(text) >= 40:
                user_msgs.append(text)
                w = route_wing(text)
                wing_hits[w] += 1
                kws = keywords(text)
                keyword_counts.update(kws)
                per_wing_keywords[w].update(kws)
            elif role == "assistant":
                assistant_msg_count += 1

    wing_counts_live = fetch_mempalace_wing_counts()
    thin_data = len(user_msgs) < MIN_SUBSTANTIVE_USER_MSGS

    # Detect hot topics: keywords spiking in the window with low coverage.
    hot_topics: list[tuple[str, int, str]] = []  # (keyword, count, primary_wing)
    for kw, count in keyword_counts.most_common(30):
        if count < HOT_TOPIC_THRESHOLD:
            break
        # Which wing does this keyword land in most?
        primary = max(
            ((wing, per_wing_keywords[wing][kw]) for wing in per_wing_keywords),
            key=lambda x: x[1],
            default=("mempalace", 0),
        )[0]
        hot_topics.append((kw, count, primary))

    # Coverage gaps: wing with high recent activity but low total drawers.
    coverage_gaps: list[tuple[str, int, int]] = []  # (wing, recent_hits, drawer_count)
    for wing, hits in wing_hits.most_common():
        drawers = wing_counts_live.get(wing, 0)
        if hits >= 3 and drawers < 20:
            coverage_gaps.append((wing, hits, drawers))

    # Build report
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORT_DIR / f"auto-dream-{now.strftime('%Y-%m-%d')}.md"

    lines: list[str] = []
    lines.append(f"# Auto-Dream Report — {now.strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append(f"Window: last {WINDOW_HOURS}h ({since.strftime('%Y-%m-%d %H:%M')} → now)")
    lines.append("")

    if thin_data:
        lines.append(
            f"> **Thin data:** only {len(user_msgs)} substantive user messages in window "
            f"(threshold {MIN_SUBSTANTIVE_USER_MSGS}). Trend-spotting below is weakly supported. "
            "This is normal in the first week or two."
        )
        lines.append("")

    # Activity summary
    lines.append("## Activity")
    lines.append("")
    lines.append(f"- Sessions: {len(sessions_seen)}")
    lines.append(f"- Substantive user messages: {len(user_msgs)}")
    lines.append(f"- Assistant messages: {assistant_msg_count}")
    lines.append(f"- Tool calls: {sum(tool_counter.values())}")
    if tool_counter:
        top_tools = ", ".join(f"{n}×`{t}`" for t, n in tool_counter.most_common(8))
        lines.append(f"  - Top tools: {top_tools}")
    if tool_errors:
        err_tools = ", ".join(f"{n}×`{t}`" for t, n in tool_errors.most_common(5))
        lines.append(f"  - Errors: {err_tools}")
    lines.append("")

    # Wing activity
    lines.append("## Wing activity (this window)")
    lines.append("")
    if not wing_hits:
        lines.append("_No routable user messages._")
    else:
        lines.append("| wing | recent hits | drawers in palace |")
        lines.append("|---|---:|---:|")
        for wing, hits in wing_hits.most_common():
            lines.append(f"| {wing} | {hits} | {wing_counts_live.get(wing, '?')} |")
    lines.append("")

    # Hot topics
    lines.append("## Hot topics (keywords ≥3 mentions)")
    lines.append("")
    if not hot_topics:
        lines.append("_None — window is quiet or below threshold._")
    else:
        for kw, count, wing in hot_topics[:15]:
            lines.append(f"- `{kw}` — {count}× (primary wing: **{wing}**)")
    lines.append("")

    # Coverage gaps → vault promotion candidates
    lines.append("## Vault promotion candidates")
    lines.append("")
    lines.append(
        "_Wings hit 3+ times in window with < 20 existing drawers. "
        "Consider writing a wiki/decisions/patterns note to anchor this topic._"
    )
    lines.append("")
    if not coverage_gaps:
        lines.append("_None — coverage looks OK for active topics._")
    else:
        for wing, hits, drawers in coverage_gaps:
            lines.append(f"- **{wing}**: {hits} recent hits, only {drawers} drawers → consider a vault anchor note.")
    lines.append("")

    # Sample user messages per top wing (for human review)
    lines.append("## Sample messages per hot wing")
    lines.append("")
    for wing, _ in wing_hits.most_common(3):
        samples = [m for m in user_msgs if route_wing(m) == wing][:2]
        if not samples:
            continue
        lines.append(f"### {wing}")
        for s in samples:
            excerpt = s.replace("\n", " ").strip()
            if len(excerpt) > 240:
                excerpt = excerpt[:240] + "…"
            lines.append(f"> {excerpt}")
            lines.append("")

    # ----------------------------------------------------------------
    # Tier 1/2 augmentations — consolidate, surface gaps, flag drift.
    # Each section below is suggest-only; nothing writes to palace/vault.
    # ----------------------------------------------------------------
    recent_drawer_since = now - timedelta(days=RECENT_DRAWER_DAYS)
    ids, metas, docs = fetch_drawers_with_metadata()

    # --- 1. Vault gaps (hot topic has no wiki coverage) ---
    vault_gaps = detect_vault_gaps(hot_topics)
    lines.append("## Vault gaps — concepts you're thinking about but haven't written")
    lines.append("")
    if not vault_gaps:
        lines.append("_No gaps detected. Vault coverage matches current chat topics._")
    else:
        lines.append("_Keywords spiking in chat but absent/thin in the vault. "
                     "Each one is a concrete authoring candidate._")
        lines.append("")
        lines.append("| keyword | mentions | wing | vault hits | suggestion |")
        lines.append("|---|---:|---|---:|---|")
        for g in vault_gaps:
            lines.append(f"| `{g['keyword']}` | {g['mentions']} | {g['wing']} | "
                         f"{g['vault_hits']} | {g['suggestion']} |")
    lines.append("")

    # --- 2. Synthesis candidates (drawer clusters → wiki synthesis page) ---
    syntheses = detect_synthesis_candidates(ids or [], metas or [], docs or [], recent_drawer_since)
    lines.append(f"## Synthesis candidates — drawer clusters (last {RECENT_DRAWER_DAYS}d)")
    lines.append("")
    if ids is None:
        lines.append("_Palace unavailable — skipped._")
    elif not syntheses:
        lines.append("_No clusters of ≥5 recent drawers sharing a keyword. Either the window is "
                     "quiet or clusters already have synthesis pages._")
    else:
        lines.append("_Clusters of drawers around a shared keyword. Consider writing a "
                     "`wiki/syntheses/{keyword}.md` to consolidate verbatim drawers into a stable summary._")
        lines.append("")
        for s in syntheses:
            status_marks = []
            if s["has_synthesis"]:
                status_marks.append("✔synthesis exists")
            if s["has_concept"]:
                status_marks.append("✔concept exists")
            status = " · ".join(status_marks) or "**no page yet**"
            lines.append(f"- **{s['keyword']}** ({s['wing']}) — {s['cluster_size']} drawers · {status}")
            for src in s["sample_sources"][:2]:
                lines.append(f"    - source hint: `{src[-60:]}`")
    lines.append("")

    # --- 3. Contradiction review candidates ---
    contradictions = detect_contradictions(ids or [], metas or [], docs or [], recent_drawer_since)
    lines.append(f"## Contradiction review — drawer vs wiki (last {RECENT_DRAWER_DAYS}d)")
    lines.append("")
    lines.append("_Drawers with 35-55% keyword overlap with a wiki page. That's 'same topic, "
                 "different wording' — sometimes a real drift, sometimes a harmless rephrase. "
                 "**Review each**; Obsidian wins by doctrine, so either update the page or "
                 "discard the drawer._")
    lines.append("")
    if ids is None:
        lines.append("_Palace unavailable — skipped._")
    elif not contradictions:
        lines.append("_No review candidates in window._")
    else:
        for c in contradictions:
            lines.append(f"- **{c['wiki_page']}** ↔ drawer `{c['drawer_id'][:30]}…` "
                         f"({c['drawer_wing']}, jaccard={c['jaccard']})")
            lines.append(f"    > {c['drawer_preview'][:180]}…")
    lines.append("")

    # --- 4. Missing wiki links ---
    missing_links = detect_missing_links()
    lines.append("## Missing wiki links — neighbors that aren't [[linked]]")
    lines.append("")
    if not missing_links:
        lines.append("_Not enough wiki pages yet (need 2+ concept/synthesis/entity pages), "
                     "or all nearest neighbors are already linked._")
    else:
        lines.append("_Each page's top-K nearest pages (by keyword overlap) that aren't in "
                     "its `[[wikilinks]]`. The Karpathy pattern says links ARE the knowledge — "
                     "every missing one is value left on the table._")
        lines.append("")
        for ml in missing_links:
            lines.append(f"- `{ml['page']}`")
            for s in ml["suggestions"]:
                lines.append(f"    - → `[[{s['target']}]]` (overlap={s['overlap']}, at `{s['target_path']}`)")
    lines.append("")

    # --- 5. Recall-weighted deadweight + hot drawers ---
    recall = analyze_recall_weights(ids or [], metas or [])
    lines.append(f"## Drawer recall health (last {DEADWEIGHT_DAYS}d target window)")
    lines.append("")
    if not recall.get("recall_log_exists"):
        lines.append(f"_{recall.get('note', 'No recall log.')}_")
    else:
        days = recall.get("recall_log_days", 0)
        lines.append(f"- Recall log: {days} day(s) of data, {recall.get('total_recalls', 0):,} total recalls, "
                     f"{recall.get('unique_recalled', 0):,} unique drawers touched.")
        if recall.get("hot_keys"):
            lines.append("")
            lines.append("**Hot drawers (most-often recalled):**")
            for h in recall["hot_keys"][:5]:
                lines.append(f"- `{h['key']}` — recalled {h['recall_count']}×")
        if not recall.get("enough_data_for_deadweight"):
            lines.append("")
            lines.append(f"_Deadweight detection gated until {DEADWEIGHT_DAYS} days of recall history "
                         f"accumulates (have {days}). Avoids false 'never recalled' claims on drawers "
                         "whose topics just haven't come up yet._")
        elif ids and metas and docs and recall.get("recall_counts"):
            dead = build_deadweight_list(ids, metas, docs, recall["recall_counts"])
            lines.append("")
            lines.append(f"**Deadweight candidates** (drawers never recalled in last {days}d — up to 50 shown):")
            if not dead:
                lines.append("_None — every drawer has been pulled at least once. Palace is lean._")
            else:
                by_wing: dict[str, int] = Counter()
                for d in dead:
                    by_wing[d["wing"]] += 1
                lines.append(f"- By wing: " + ", ".join(f"{n}×{w}" for w, n in by_wing.most_common()))
                lines.append("- Sample deadweight:")
                for d in dead[:10]:
                    lines.append(f"    - `{d['drawer_id']}` ({d['wing']}/{d['room']}) — {d['source']}")
                lines.append("")
                lines.append("_Doctrine check: MemPalace promises verbatim retention. "
                             "Do NOT auto-prune. This list is for periodic human review only._")
    lines.append("")

    lines.append("---")
    lines.append(
        "_Generated by auto_dream.py. This report is suggest-only; no drawers or vault notes were written._"
    )

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[auto-dream] report -> {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
