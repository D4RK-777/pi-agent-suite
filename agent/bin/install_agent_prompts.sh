#!/usr/bin/env bash
# D4rk Mind — Install Agent Prompts
# Installs D4rk Mind prompts for all your agents

set -e

PI_DIR="$HOME/.pi/agent"
PROMPTS_DIR="$PI_DIR/prompts"
AGENTS_DIR="$HOME/.agents"

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║          D4rk Mind — Agent Prompt Installer              ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Verify prompts exist
if [ ! -d "$PROMPTS_DIR" ]; then
    echo "❌ Prompts directory not found: $PROMPTS_DIR"
    exit 1
fi

echo "Found prompts:"
for f in "$PROMPTS_DIR"/*.md; do
    echo "  - $(basename "$f")"
done

echo ""

# Function to update a file with prompt inclusion
update_prompt() {
    local target_file="$1"
    local prompt_ref="$2"
    local description="$3"
    
    if [ -f "$target_file" ]; then
        echo "  📝 Updating $description: $target_file"
        
        # Check if already included
        if grep -q "D4rk Mind" "$target_file" 2>/dev/null; then
            echo "     ✓ Already has D4rk Mind reference"
            return 0
        fi
        
        # Append prompt reference
        echo "" >> "$target_file"
        echo "" >> "$target_file"
        echo "# D4rk Mind Integration" >> "$target_file"
        echo "See: $prompt_ref" >> "$target_file"
        
        echo "     ✓ Updated"
    else
        echo "  ⚠️  Not found: $target_file"
    fi
}

# Install to Claude
echo ""
echo "Installing to Claude..."
if [ -f "$HOME/.claude/CLAUDE.md" ]; then
    cat >> "$HOME/.claude/CLAUDE.md" << 'EOF'

# D4rk Mind Integration

You have access to the D4rk Mind knowledge system.

## Quick Start
1. Search: `mempalace_fast.search("query")`
2. Read: `~/.pi/agent/skills/expert-*/knowledge/`
3. Code: Follow retrieved patterns
4. File: `echo "..." | mine --wing expert-frontend`

## Rules
- Search before coding
- TypeScript strict, no any
- WCAG 2.2 AA + ARIA
- Design tokens only
- One task, then "Done."
- Never loop

## Reference
Full prompt: ~/.pi/agent/prompts/CLAUDE_PROMPT.md
EOF
    echo "  ✓ Installed to Claude"
else
    echo "  ⚠️  Claude CLAUDE.md not found"
fi

# Install to .agents/memory/AGENTS.md
echo ""
echo "Installing to .agents..."
if [ -d "$AGENTS_DIR/memory" ]; then
    AGENTS_MD="$AGENTS_DIR/memory/AGENTS.md"
    
    if [ -f "$AGENTS_MD" ]; then
        # Backup
        cp "$AGENTS_MD" "$AGENTS_MD.bak"
        
        # Prepend D4rk Mind header
        cat > "$AGENTS_MD" << 'EOF'
# D4rk Mind — Agent System

You have access to the D4rk Mind knowledge and context system.

## System Overview
- **Infinite Context**: 2M+ tokens via semantic retrieval
- **Fast Search**: ~20ms MemPalace queries
- **27K+ Patterns**: From curated sources (Radix, shadcn, OWASP, etc.)

## Core Rules
1. **Search First** — Always search MemPalace before coding
2. **Track Context** — Use context_tracker for conversation history
3. **File Decisions** — Log architectural choices to MemPalace
4. **One Task** — Finish it, say "Done."
5. **Never Loop** — Same tool 3x = STOP

## Quick Commands
```bash
# Fast search (~20ms)
mempalace_fast.search("query")

# Context display
tracker.get_display()

# File decision
echo "Built: X. From: Y. Files: Z" | mine --wing expert-frontend
```

## Expert Domains
| Domain | Wing | Triggers |
|--------|------|----------|
| Frontend | expert-frontend | ui, react, css |
| Backend | expert-backend | api, database |
| Auth | expert-auth | jwt, oauth, login |
| Security | expert-security | xss, csrf, owasp |
| Optimization | expert-optimization | speed, latency |
| Orchestration | expert-orchestration | docker, k8s |

## Files
- System: ~/.pi/agent/SYSTEM.md
- Prompts: ~/.pi/agent/prompts/
- Skills: ~/.pi/agent/skills/
- Quick Ref: ~/.pi/agent/prompts/QUICK_REFERENCE.md

---

EOF
        
        # Append backup content (without NEUTRALIZED line)
        grep -v "NEUTRALIZED" "$AGENTS_MD.bak" >> "$AGENTS_MD"
        rm "$AGENTS_MD.bak"
        
        echo "  ✓ Installed to .agents"
    else
        echo "  ⚠️  AGENTS.md not found"
    fi
fi

# Install to Codex (oh-my-codex style)
echo ""
echo "Installing to Codex..."
if [ -f "$HOME/.codex/CLAUDE.md" ]; then
    cat >> "$HOME/.codex/CLAUDE.md" << 'EOF'

# D4rk Mind Integration

Before any coding task, search MemPalace:
```bash
mempalace_fast.search("your query")
```

Rules:
- Search before coding
- TypeScript strict, no any
- WCAG 2.2 AA
- Design tokens only
- One task, "Done."

See: ~/.pi/agent/prompts/CODEX_PROMPT.md
EOF
    echo "  ✓ Installed to Codex"
fi

# Create symlinks in agents directory
echo ""
echo "Creating symlinks..."
mkdir -p "$AGENTS_DIR/prompts"
for f in "$PROMPTS_DIR"/*.md; do
    name=$(basename "$f")
    link="$AGENTS_DIR/prompts/$name"
    
    if [ -L "$link" ]; then
        rm "$link"
    fi
    
    ln -sf "$f" "$link"
    echo "  ✓ $name"
done

echo ""
echo "─────────────────────────────────────────────────────────────────"
echo ""
echo "✅ D4rk Mind prompts installed!"
echo ""
echo "Next steps:"
echo "  1. Restart your agents"
echo "  2. Verify: agents status"
echo "  3. Test: mempalace_fast.search(\"test\")"
echo ""
echo "Quick reference:"
cat "$PROMPTS_DIR/QUICK_REFERENCE.md"
