Analysis

Analyze your oh-my-codex usage and get tailored recommendations to improve your workflow.

> Note: This replaces the former `/learn-about-omc` skill.

### What It Does

1. Reads token tracking from `~/.omx/state/token-tracking.jsonl`
2. Reads session history from `.omx/state/session-history.json`
3. Analyzes agent usage patterns
4. Identifies underutilized features
5. Recommends configuration changes

### Step 1: Gather Data

```bash
# Check for token tracking data
TOKEN_FILE="$HOME/.omx/state/token-tracking.jsonl"
SESSION_FILE=".omx/state/session-history.json"
CONFIG_FILE="$HOME/.codex/.omx-config.json"

echo "Analyzing OMX Usage..."
echo ""

# Check what data is available
HAS_TOKENS=false
HAS_SESSIONS=false
HAS_CONFIG=false