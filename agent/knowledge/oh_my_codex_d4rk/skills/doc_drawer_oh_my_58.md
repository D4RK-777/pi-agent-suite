---
name: ask-gemini
description: Ask Gemini via local CLI and capture a reusable artifact
---

# Ask Gemini (Local CLI)

Use the locally installed Gemini CLI as a direct external advisor for brainstorming, design feedback, and second opinions.

## Usage

```bash
/ask-gemini <question or task>
```

## Routing

### Preferred: Local CLI execution
Run Gemini through the canonical OMX CLI command path (no MCP routing):

```bash
omx ask gemini "{{ARGUMENTS}}"
```

Exact non-interactive Gemini CLI command from `gemini --help`:

```bash
gemini -p "{{ARGUMENTS}}"
# equivalent: gemini --prompt "{{ARGUMENTS}}"
```

If needed, adapt to the user's installed Gemini CLI variant while keeping local execution as the default path.