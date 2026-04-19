#!/usr/bin/env bash
# Pi Agent Suite — Installer
# Installs MemPalace, the Pi Harness, hooks, and wires up Claude Code (or other AI clients).
#
# Usage:
#   bash install.sh                        # interactive
#   bash install.sh --non-interactive      # defaults, no prompts
#   bash install.sh --pi-home ~/my-pi      # custom install dir
#   bash install.sh --no-claude            # skip Claude Code settings patch

set -euo pipefail

# ─── Colors ──────────────────────────────────────────────────────────────────
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; BLUE='\033[0;34m'
BOLD='\033[1m'; RESET='\033[0m'
ok()   { echo -e "${GREEN}✓${RESET} $*"; }
info() { echo -e "${BLUE}ℹ${RESET} $*"; }
warn() { echo -e "${YELLOW}⚠${RESET} $*"; }
die()  { echo -e "${RED}✗${RESET} $*" >&2; exit 1; }

# ─── Defaults ────────────────────────────────────────────────────────────────
PI_HOME="${PI_AGENT_HOME:-$HOME/.pi}"
PALACE="${MEMPALACE_PALACE:-$HOME/.mempalace/palace}"
NON_INTERACTIVE=false
PATCH_CLAUDE=true
PATCH_CODEX=false
SETUP_VAULT=false

# ─── Arg parsing ─────────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
    case $1 in
        --non-interactive) NON_INTERACTIVE=true ;;
        --pi-home) PI_HOME="$2"; shift ;;
        --palace) PALACE="$2"; shift ;;
        --no-claude) PATCH_CLAUDE=false ;;
        --with-codex) PATCH_CODEX=true ;;
        --with-vault) SETUP_VAULT=true ;;
        *) warn "Unknown flag: $1" ;;
    esac
    shift
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SUITE_DIR="$(dirname "$SCRIPT_DIR")"

echo ""
echo -e "${BOLD}═══════════════════════════════════════════════════════════${RESET}"
echo -e "${BOLD}  Pi Agent Suite — Installer${RESET}"
echo -e "${BOLD}═══════════════════════════════════════════════════════════${RESET}"
echo ""

# ─── Interactive prompts ──────────────────────────────────────────────────────
if [[ "$NON_INTERACTIVE" == "false" ]]; then
    read -rp "Install directory [$PI_HOME]: " _pi && PI_HOME="${_pi:-$PI_HOME}"
    read -rp "MemPalace data directory [$PALACE]: " _pal && PALACE="${_pal:-$PALACE}"
    read -rp "Patch Claude Code settings.json? [Y/n]: " _cc
    [[ "${_cc:-Y}" =~ ^[Nn] ]] && PATCH_CLAUDE=false
    read -rp "Set up Obsidian vault template? [y/N]: " _vault
    [[ "${_vault:-N}" =~ ^[Yy] ]] && SETUP_VAULT=true
    echo ""
fi

# ─── Prerequisites ────────────────────────────────────────────────────────────
info "Checking prerequisites..."

command -v python3 >/dev/null || die "Python 3.9+ required. Install from python.org."
PY_VER=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3,9) else 1)' \
    || die "Python 3.9+ required (found $PY_VER)."
ok "Python $PY_VER"

command -v pip3 >/dev/null || command -v pip >/dev/null \
    || die "pip not found. Install it with your Python distribution."
ok "pip"

if [[ "$PATCH_CLAUDE" == "true" ]]; then
    command -v claude >/dev/null \
        && ok "Claude Code CLI" \
        || warn "claude CLI not found — will write settings template only"
fi

# ─── Install MemPalace ────────────────────────────────────────────────────────
echo ""
info "Installing MemPalace..."

if python3 -c "import mempalace" 2>/dev/null; then
    ok "MemPalace already installed"
else
    pip3 install mempalace --quiet || die "pip install mempalace failed"
    ok "MemPalace installed"
fi

MEMPAL_VER=$(python3 -c "import mempalace; print(mempalace.__version__)" 2>/dev/null || echo "unknown")
ok "MemPalace $MEMPAL_VER"

# ─── Create directory structure ───────────────────────────────────────────────
echo ""
info "Creating Pi Agent directory at $PI_HOME..."

mkdir -p \
    "$PI_HOME/agent/bin" \
    "$PI_HOME/agent/harness" \
    "$PI_HOME/agent/agents" \
    "$PI_HOME/agent/manifests" \
    "$PI_HOME/agent/skills" \
    "$PI_HOME/agent/adapters" \
    "$PI_HOME/hooks" \
    "$PALACE/../hook_state" \
    "$PALACE/../logs"

ok "Directories created"

# ─── Copy harness files ───────────────────────────────────────────────────────
info "Installing Pi Agent engine (harness, agents, manifests, adapters, bin)..."
cp -r "$SUITE_DIR/agent/"* "$PI_HOME/agent/"
ok "Agent engine installed"

info "Installing hook scripts..."
cp "$SUITE_DIR/hooks/mempal_save_hook.sh" "$PI_HOME/hooks/"
cp "$SUITE_DIR/hooks/mempal_precompact_hook.sh" "$PI_HOME/hooks/"
chmod +x "$PI_HOME/hooks/"*.sh
ok "Hook scripts"

# ─── Write env file ───────────────────────────────────────────────────────────
ENV_FILE="$PI_HOME/env.sh"
cat > "$ENV_FILE" << EOF
# Pi Agent Suite — environment variables
# Source this in your shell profile: source ~/.pi/env.sh

export PI_AGENT_HOME="$PI_HOME"
export MEMPALACE_PALACE="$PALACE"

# Uncomment to point at your Obsidian vault:
# export OBSIDIAN_VAULT="/path/to/your/vault"
# export OBSIDIAN_API_KEY="your-key-here"
EOF
ok "Env file written to $ENV_FILE"

SHELL_RC=""
for rc in "$HOME/.bashrc" "$HOME/.zshrc" "$HOME/.profile"; do
    [[ -f "$rc" ]] && SHELL_RC="$rc" && break
done

if [[ -n "$SHELL_RC" ]] && ! grep -q "PI_AGENT_HOME" "$SHELL_RC" 2>/dev/null; then
    echo "" >> "$SHELL_RC"
    echo "# Pi Agent Suite" >> "$SHELL_RC"
    echo "source \"$ENV_FILE\"" >> "$SHELL_RC"
    ok "Added env to $SHELL_RC"
fi

# ─── Patch Claude Code settings ───────────────────────────────────────────────
if [[ "$PATCH_CLAUDE" == "true" ]]; then
    echo ""
    info "Wiring up Claude Code hooks and MCP server..."

    CLAUDE_SETTINGS="$HOME/.claude/settings.json"
    CLAUDE_SETTINGS_LOCAL="$HOME/.claude/settings.local.json"

    HOOK_CMD_PROMPT="python3 $PI_HOME/agent/bin/mempalace_prompt_hook.py"
    HOOK_CMD_STOP="bash $PI_HOME/hooks/mempal_save_hook.sh"
    HOOK_CMD_COMPACT="bash $PI_HOME/hooks/mempal_precompact_hook.sh"

    if [[ -f "$CLAUDE_SETTINGS" ]]; then
        warn "Claude Code settings.json already exists at $CLAUDE_SETTINGS"
        warn "Writing hooks to settings.local.json instead (safe — won't overwrite your existing config)"
        TARGET="$CLAUDE_SETTINGS_LOCAL"
    else
        mkdir -p "$(dirname "$CLAUDE_SETTINGS")"
        TARGET="$CLAUDE_SETTINGS"
    fi

    python3 << PYEOF
import json, os
from pathlib import Path

target = Path("$TARGET")
data = {}
if target.exists():
    try:
        data = json.loads(target.read_text())
    except Exception:
        data = {}

hooks = data.setdefault("hooks", {})

def set_hook(event, cmd, timeout=2):
    hooks.setdefault(event, [])
    # Check if already present
    for entry in hooks[event]:
        for h in entry.get("hooks", []):
            if h.get("command", "").startswith(cmd.split()[0]):
                return  # already configured
    hooks[event].append({
        "matcher": "",
        "hooks": [{"type": "command", "command": cmd, "timeout": timeout}]
    })

set_hook("UserPromptSubmit", "$HOOK_CMD_PROMPT", 2)
set_hook("Stop", "$HOOK_CMD_STOP", 30)
set_hook("PreCompact", "$HOOK_CMD_COMPACT", 30)

# Add MemPalace MCP server
mcp = data.setdefault("mcpServers", {})
if "mempalace" not in mcp:
    mcp["mempalace"] = {
        "command": "python3",
        "args": ["-m", "mempalace.mcp_server", "--palace", "$PALACE"],
    }

target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(data, indent=2))
print(f"Wrote {target}")
PYEOF
    ok "Claude Code hooks and MCP server configured"
fi

# ─── Vault template ───────────────────────────────────────────────────────────
if [[ "$SETUP_VAULT" == "true" ]]; then
    echo ""
    read -rp "Obsidian vault path (new directory will be created): " VAULT_PATH
    VAULT_PATH="${VAULT_PATH/#\~/$HOME}"

    if [[ -d "$VAULT_PATH" ]]; then
        warn "Directory already exists: $VAULT_PATH"
        read -rp "Copy vault template into it anyway? [y/N]: " _y
        [[ ! "${_y:-N}" =~ ^[Yy] ]] && info "Skipping vault setup." || \
            cp -rn "$SUITE_DIR/vault-template/"* "$VAULT_PATH/"
    else
        cp -r "$SUITE_DIR/vault-template" "$VAULT_PATH"
        ok "Vault created at $VAULT_PATH"
    fi

    echo ""
    info "Next steps for Obsidian:"
    info "1. Open Obsidian → Add vault → $VAULT_PATH"
    info "2. Install 'Local REST API' community plugin"
    info "3. Copy the API key into ~/.pi/env.sh (OBSIDIAN_API_KEY)"
    info "4. Install 'obsidian-mcp-server' for Claude Code MCP integration"
fi

# ─── Initial palace check ─────────────────────────────────────────────────────
echo ""
info "Checking MemPalace..."
python3 "$PI_HOME/agent/bin/mempalace_fast.py" || warn "Palace is empty — run: mempalace mine <your-project-dir>"

# ─── Done ─────────────────────────────────────────────────────────────────────
echo ""
echo -e "${BOLD}═══════════════════════════════════════════════════════════${RESET}"
echo -e "${GREEN}${BOLD}  Installation complete!${RESET}"
echo -e "${BOLD}═══════════════════════════════════════════════════════════${RESET}"
echo ""
echo "Next steps:"
echo "  1. Reload your shell:    source $SHELL_RC  (or open a new terminal)"
echo "  2. Mine a project:       mempalace mine ~/your-project"
echo "  3. Test the harness:     python3 -m harness route 'build a login form'"
echo "  4. Open Claude Code — hooks fire automatically"
echo ""
echo "Docs: https://github.com/YOUR_ORG/pi-agent-suite"
echo ""

# ─── Welcome picker (buddy + theme) ──────────────────────────────────────────
echo ""
info "Launching personalisation picker..."
python3 "$PI_HOME/agent/bin/pi_welcome.py" || warn "Welcome picker skipped (re-run: python3 ~/.pi/agent/bin/pi_welcome.py)"
