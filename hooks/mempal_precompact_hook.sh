#!/bin/bash
# MEMPALACE PRE-COMPACT HOOK — Save before context compression
#
# Claude Code "PreCompact" hook. Fires RIGHT BEFORE the conversation
# gets compressed to free up context window space.
#
# When compaction happens, the AI loses detailed context about what was
# discussed. This hook triggers a background mining run first, so the
# palace is updated before that context disappears.
#
# === INSTALL ===
# Add to ~/.claude/settings.json (or settings.local.json):
#
#   "hooks": {
#     "PreCompact": [{
#       "matcher": "",
#       "hooks": [{
#         "type": "command",
#         "command": "bash /path/to/mempal_precompact_hook.sh",
#         "timeout": 30
#       }]
#     }]
#   }
#
# For OpenAI Codex CLI, add to .codex/hooks.json:
#   "PreCompact": [{"type": "command", "command": "bash /path/to/mempal_precompact_hook.sh", "timeout": 30}]
#
# === HOW IT WORKS ===
#
# Claude Code sends JSON on stdin:
#   session_id — unique session identifier
#   trigger    — why compaction was triggered ("token_limit" etc.)
#
# === CONFIGURATION ===

STATE_DIR="${MEMPALACE_PALACE:-$HOME/.mempalace/palace}/../hook_state"
STATE_DIR="$(realpath "$STATE_DIR" 2>/dev/null || echo "$HOME/.mempalace/hook_state")"
mkdir -p "$STATE_DIR"

# Optional: set MEMPAL_INGEST_DIR to auto-ingest before compaction.
# Leave empty to skip (mining will happen at the next Stop hook instead).
MEMPAL_DIR="${MEMPAL_INGEST_DIR:-}"

# Read JSON input from stdin
INPUT=$(cat)

SESSION_ID=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('session_id','unknown'))" 2>/dev/null)

echo "[$(date '+%H:%M:%S')] PRE-COMPACT triggered for session $SESSION_ID" >> "$STATE_DIR/hook.log"

# Run mining synchronously if MEMPAL_DIR is set (blocks until done, within timeout)
if [ -n "$MEMPAL_DIR" ] && [ -d "$MEMPAL_DIR" ]; then
    python3 -m mempalace mine "$MEMPAL_DIR" >> "$STATE_DIR/hook.log" 2>&1
fi

# Allow compaction to proceed — mining is either done or will catch up at next Stop hook.
cat << 'HOOKJSON'
{
  "decision": "allow",
  "reason": "MemPalace pre-compaction checkpoint. Conversation saved in background. Compaction can proceed safely."
}
HOOKJSON
