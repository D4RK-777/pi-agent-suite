# oh-my-codex v0.8.2

Released: **2026-03-06**

This is a **targeted patch release** focused on team-provider expansion, safer defaults, setup hygiene, and correctness fixes across setup, keyword handling, and OpenClaw hook templating.

---

## TL;DR

- `$team` / team runtime can now launch **Gemini CLI workers** alongside Codex and Claude (`#576`, `#579`, related issue `#573`).
- Default frontier-model fallback is now routed through **`DEFAULT_FRONTIER_MODEL`** instead of hardcoded model strings (`#583`).
- Setup/install is stricter about shipping only the right skills, now ships **`configure-notifications`** canonically, and cleans stale legacy skill dirs on `--force` (`#575`, `#580`, `#584`, closes `#574`).