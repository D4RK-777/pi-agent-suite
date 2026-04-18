#!/usr/bin/env bash
# D4rk Mind — Load Agent Prompts
# Run this to load the D4rk Mind system into your agent

set -e

PI_DIR="$HOME/.pi/agent"
PROMPTS_DIR="$PI_DIR/prompts"

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║          D4rk Mind — Agent Prompt Loader                   ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Check if prompts exist
if [ ! -d "$PROMPTS_DIR" ]; then
    echo "❌ Prompts directory not found: $PROMPTS_DIR"
    exit 1
fi

# List available prompts
echo "Available prompts:"
echo ""
for prompt in "$PROMPTS_DIR"/*.md; do
    if [ -f "$prompt" ]; then
        name=$(basename "$prompt" .md)
        size=$(wc -c < "$prompt")
        echo "  📄 $name ($size bytes)"
    fi
done

echo ""
echo "─────────────────────────────────────────────────────────────────"
echo ""

# Show the quick reference
if [ -f "$PROMPTS_DIR/QUICK_REFERENCE.md" ]; then
    echo "QUICK REFERENCE:"
    echo ""
    cat "$PROMPTS_DIR/QUICK_REFERENCE.md"
else
    echo "Quick reference not found."
fi

echo ""
echo "─────────────────────────────────────────────────────────────────"
echo ""

# Show rules
if [ -f "$PROMPTS_DIR/RULES_OF_ENGAGEMENT.md" ]; then
    echo "RULES OF ENGAGEMENT:"
    echo ""
    head -50 "$PROMPTS_DIR/RULES_OF_ENGAGEMENT.md"
else
    echo "Rules of engagement not found."
fi

echo ""
echo "─────────────────────────────────────────────────────────────────"
echo ""
echo "To load a specific prompt into your agent, reference:"
echo "  $PROMPTS_DIR/<prompt-name>.md"
echo ""
echo "For example, in Claude Code:"
echo "  /claude-load-prompt $PROMPTS_DIR/CLAUDE_PROMPT.md"
echo ""
echo "Or in Codex:"
echo "  /prompt load $PROMPTS_DIR/CODEX_PROMPT.md"
