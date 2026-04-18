---
name: ask-claude
description: Ask Claude via local CLI and capture a reusable artifact
---

# Ask Claude (Local CLI)

Use the locally installed Claude CLI as a direct external advisor for focused questions, reviews, or second opinions.

## Usage

```bash
/ask-claude <question or task>
```

## Routing

### Preferred: Local CLI execution
Run Claude through the canonical OMX CLI command path (no MCP routing):

```bash
omx ask claude "{{ARGUMENTS}}"
```

Exact non-interactive Claude CLI command from `claude --help`:

```bash
claude -p "{{ARGUMENTS}}"
# equivalent: claude --print "{{ARGUMENTS}}"
```

If needed, adapt to the user's installed Claude CLI variant while keeping local execution as the default path.