ing for the notify-fallback watcher so full-suite release validation remains stable under load.

---

## What changed

### 1) Gemini prompt-mode workers now start with an explicit initial prompt

Gemini workers launched through OMX team prompt mode are now started with an explicit initial instruction:

- `--approval-mode yolo`
- `-i "Read and follow the instructions in .../inbox.md"`

**Why this matters:**
- removes dependence on stdin-delivered bootstrap text for Gemini startup
- aligns worker bootstrap with Gemini CLI expectations in prompt mode
- fixes the broken worker bring-up path reported in the hotfix PR

### 2) Non-Gemini default model passthrough is filtered for Gemini workers

Gemini workers no longer inherit non-Gemini default models by accident.