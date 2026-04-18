#!/bin/bash
# MEMPALACE SAVE HOOK — Auto-save every N exchanges
#
# Claude Code "Stop" hook. After every assistant response:
# 1. Counts human messages in the session transcript
# 2. Every SAVE_INTERVAL messages, triggers background mining of the transcript
# 3. Returns a reason notifying the AI that saving happened in the background
#
# The pipeline (mempalace mine) handles classification — it knows which wing,
# room, and drawer to use based on content. No manual categorization needed.
#
# === INSTALL ===
# Add to ~/.claude/settings.json (or settings.local.json):
#
#   "hooks": {
#     "Stop": [{
#       "matcher": "",
#       "hooks": [{
#         "type": "command",
#         "command": "bash /path/to/mempal_save_hook.sh",
#         "timeout": 30
#       }]
#     }]
#   }
#
# For OpenAI Codex CLI, add to .codex/hooks.json:
#   "Stop": [{"type": "command", "command": "bash /path/to/mempal_save_hook.sh", "timeout": 30}]
#
# === HOW IT WORKS ===
#
# Claude Code sends JSON on stdin:
#   session_id       — unique session identifier
#   stop_hook_active — true when AI is already in a save cycle (prevents loops)
#   transcript_path  — path to the JSONL transcript file
#
# === CONFIGURATION ===

SAVE_INTERVAL=${MEMPAL_SAVE_INTERVAL:-15}  # Save every N human messages
STATE_DIR="${MEMPALACE_PALACE:-$HOME/.mempalace/palace}/../hook_state"
STATE_DIR="$(realpath "$STATE_DIR" 2>/dev/null || echo "$HOME/.mempalace/hook_state")"
mkdir -p "$STATE_DIR"

# Optional: set MEMPAL_DIR to a directory you want auto-ingested on each trigger.
# Leave empty to rely solely on transcript_path from Claude Code.
MEMPAL_DIR="${MEMPAL_INGEST_DIR:-}"

# Read JSON input from stdin
INPUT=$(cat)

# Parse all fields in a single Python call (faster than multiple invocations)
eval $(echo "$INPUT" | python3 -c "
import sys, json, re
data = json.load(sys.stdin)
sid = data.get('session_id', 'unknown')
sha = data.get('stop_hook_active', False)
tp = data.get('transcript_path', '')
safe = lambda s: re.sub(r'[^a-zA-Z0-9_/.\-~]', '', str(s))
print(f'SESSION_ID=\"{safe(sid)}\"')
print(f'STOP_HOOK_ACTIVE=\"{sha}\"')
print(f'TRANSCRIPT_PATH=\"{safe(tp)}\"')
" 2>/dev/null)

# Expand ~ in path
TRANSCRIPT_PATH="${TRANSCRIPT_PATH/#\~/$HOME}"

# If already in a save cycle, let the AI stop normally (prevents infinite loop)
if [ "$STOP_HOOK_ACTIVE" = "True" ] || [ "$STOP_HOOK_ACTIVE" = "true" ]; then
    echo "{}"
    exit 0
fi

# Count human messages in the JSONL transcript
if [ -f "$TRANSCRIPT_PATH" ]; then
    EXCHANGE_COUNT=$(python3 - "$TRANSCRIPT_PATH" <<'PYEOF'
import json, sys
count = 0
with open(sys.argv[1]) as f:
    for line in f:
        try:
            entry = json.loads(line)
            msg = entry.get('message', {})
            if isinstance(msg, dict) and msg.get('role') == 'user':
                content = msg.get('content', '')
                if isinstance(content, str) and '<command-message>' in content:
                    continue
                count += 1
        except:
            pass
print(count)
PYEOF
2>/dev/null)
else
    EXCHANGE_COUNT=0
fi

# Track last save point for this session
LAST_SAVE_FILE="$STATE_DIR/${SESSION_ID}_last_save"
LAST_SAVE=0
if [ -f "$LAST_SAVE_FILE" ]; then
    LAST_SAVE=$(cat "$LAST_SAVE_FILE")
fi

SINCE_LAST=$((EXCHANGE_COUNT - LAST_SAVE))

# Log for debugging: tail -f ~/.mempalace/hook_state/hook.log
echo "[$(date '+%H:%M:%S')] Session $SESSION_ID: $EXCHANGE_COUNT exchanges, $SINCE_LAST since last save" >> "$STATE_DIR/hook.log"

if [ "$SINCE_LAST" -ge "$SAVE_INTERVAL" ] && [ "$EXCHANGE_COUNT" -gt 0 ]; then
    echo "$EXCHANGE_COUNT" > "$LAST_SAVE_FILE"
    echo "[$(date '+%H:%M:%S')] TRIGGERING SAVE at exchange $EXCHANGE_COUNT" >> "$STATE_DIR/hook.log"

    PYTHON="$(command -v python3)"
    MINE_DIR=""

    if [ -n "$TRANSCRIPT_PATH" ] && [ -f "$TRANSCRIPT_PATH" ]; then
        MINE_DIR="$(dirname "$TRANSCRIPT_PATH")"
    fi
    if [ -n "$MEMPAL_DIR" ] && [ -d "$MEMPAL_DIR" ]; then
        MINE_DIR="$MEMPAL_DIR"
    fi
    if [ -n "$MINE_DIR" ]; then
        "$PYTHON" -m mempalace mine "$MINE_DIR" >> "$STATE_DIR/hook.log" 2>&1 &
    fi

    # Notify the AI — no action required from it; mining is background-only.
    cat << 'HOOKJSON'
{
  "decision": "allow",
  "reason": "MemPalace auto-save checkpoint. Your conversation is being saved verbatim in the background — no action needed from you. Continue working."
}
HOOKJSON
else
    # Not time yet — let AI stop normally
    echo "{}"
fi
