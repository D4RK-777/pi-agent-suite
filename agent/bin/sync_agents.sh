#!/usr/bin/env bash
# D4rk Agent Sync - Share the D4rk System with All Agents
# Run this to sync the D4rk harness to .agents for use by Claude, Codex, etc.

set -e

AGENTS_DIR="$HOME/.agents"
PI_DIR="$HOME/.pi/agent"

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║          D4rk Agent System — Agent Sync                      ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Verify directories exist
if [ ! -d "$PI_DIR" ]; then
    echo "❌ D4rk Agent System not found at $PI_DIR"
    exit 1
fi

if [ ! -d "$AGENTS_DIR" ]; then
    echo "❌ .agents directory not found at $AGENTS_DIR"
    echo "   Install agents-cli: npm install -g @swarmify/agents-cli"
    exit 1
fi

echo "Syncing D4rk skills to .agents..."
echo ""

# Skills to sync
SKILLS=(
    "expert-frontend"
    "expert-backend"
    "expert-auth"
    "expert-security"
    "expert-optimization"
    "expert-orchestration"
    "mempalace"
    "mempalace-workflow"
)

for skill in "${SKILLS[@]}"; do
    src="$PI_DIR/skills/$skill"
    dst="$AGENTS_DIR/skills/$skill"
    
    if [ -L "$dst" ]; then
        rm "$dst"
        echo "  ↻ Updated: $skill"
    elif [ -d "$dst" ]; then
        echo "  ⚠ Exists: $skill (not a symlink, skipping)"
        continue
    fi
    
    ln -sf "$src" "$dst"
    echo "  ✓ Linked: $skill"
done

# Sync bin directory
bin_src="$PI_DIR/bin"
bin_dst="$HOME/.local/bin/d4rk"

if [ ! -d "$(dirname $bin_dst)" ]; then
    mkdir -p "$(dirname $bin_dst)"
fi

if [ -L "$bin_dst" ] || [ ! -e "$bin_dst" ]; then
    rm -f "$bin_dst"
    ln -sf "$bin_src" "$bin_dst"
    echo ""
    echo "  ✓ Bin linked: $bin_dst"
fi

# Update AGENTS.md
AGENTS_MD="$AGENTS_DIR/memory/AGENTS.md"
if [ -f "$PI_DIR/SYSTEM.md" ]; then
    cat "$PI_DIR/SYSTEM.md" > "$AGENTS_MD"
    echo ""
    echo "  ✓ AGENTS.md updated"
fi

echo ""
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "✅ Sync complete!"
echo ""
echo "Next steps:"
echo "  1. Restart your agents (Claude, Codex, etc.)"
echo "  2. Verify skills: agents status"
echo "  3. Test MemPalace: mempalace search \"test\""
echo ""
echo "All agents will now have:"
echo "  • 6 expert domains (frontend, backend, auth, etc.)"
echo "  • Lightning-fast MemPalace (~20ms queries)"
echo "  • 5,000+ lines of production patterns"
echo ""
