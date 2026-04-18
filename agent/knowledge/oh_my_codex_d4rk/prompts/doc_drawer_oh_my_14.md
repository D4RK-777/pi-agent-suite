# oh-my-codex Demo Guide

## Prerequisites

- Node.js >= 20
- [Codex CLI](https://github.com/openai/codex) installed (`npm install -g @openai/codex`)
- OpenAI API key configured

## Setup (< 2 minutes)

```bash
# Clone and install
git clone https://github.com/Yeachan-Heo/oh-my-codex.git
cd oh-my-codex
npm install
npm run build
npm link

# Run setup (installs prompts, skills, configures Codex CLI)
omx setup
```

**Expected output:**
```
oh-my-codex setup
=================

[1/7] Creating directories...
  Done.

[2/7] Installing agent prompts...
  Installed 30 agent prompts.

[3/7] Installing skills...
  Installed 40 skills.

[4/7] Updating config.toml...
  Done.