# 08 — MiniMax Integration

Pi Agent Suite ships pre-configured for MiniMax as its default AI provider. MiniMax is a full multimodal platform — chat, image generation, video generation, TTS, voice cloning, and web search — all available via MCP tools directly in Claude Code and other clients.

---

## Why MiniMax

- **Full multimodal** — one API for chat, image, video, audio, embeddings
- **MCP server** — 10+ tools natively in Claude Code (`minimax_*`)
- **High capacity** — ~4,500 calls per 5-hour window on standard plan
- **Local-friendly** — works alongside your local MemPalace, no cloud lock-in
- **Cost-effective** — competitive pricing for the capability set

---

## Getting your API key

1. Sign up at [minimaxi.com](https://www.minimaxi.com/)
2. Go to **User Center** → **Basic Information** → **Interface Key**
3. Create a new API key and copy it
4. Also note your **Group ID** (shown on the same page)

---

## Setting up your API key

**Never commit your API key to git.** Add it to your environment instead.

### Copy the env template

```bash
cp config/env.template ~/.pi/env.sh
```

### Edit `~/.pi/env.sh` and fill in your key

```bash
export MINIMAX_API_KEY="your-actual-key-here"
export MINIMAX_GROUP_ID="your-group-id-here"
```

### Load on shell start

```bash
echo 'source ~/.pi/env.sh' >> ~/.bashrc   # or ~/.zshrc
source ~/.pi/env.sh
```

**Windows PowerShell:**
```powershell
# Create ~/.pi/env.ps1 with:
$env:MINIMAX_API_KEY = "your-actual-key-here"
$env:MINIMAX_GROUP_ID = "your-group-id-here"

# Add to your PowerShell profile:
'. "$env:USERPROFILE\.pi\env.ps1"' | Add-Content $PROFILE
```

---

## MCP server setup (Claude Code)

The MiniMax MCP server is pre-configured in `config/claude-settings.json`. After setting your API key, add the MCP server to Claude Code:

```bash
claude mcp add minimax npx -- -y @minimax/mcp-server
```

Or add manually to `~/.claude/settings.json`:

```json
"mcpServers": {
  "minimax": {
    "command": "npx",
    "args": ["-y", "@minimax/mcp-server"],
    "env": {
      "MINIMAX_API_KEY": "your-key-here",
      "MINIMAX_MCP_BASE_URL": "https://api.minimax.chat"
    }
  }
}
```

**Note:** The `env` block in `settings.json` is for MCP server env vars. Your shell env var (`MINIMAX_API_KEY`) also works if Claude Code inherits your shell environment.

---

## Available MiniMax MCP tools

Once configured, Claude Code gets these tools:

| Tool | Description |
|---|---|
| `minimax_text_to_image` | Generate images from text prompts |
| `minimax_generate_video` | Generate short videos from text |
| `minimax_text_to_audio` | Convert text to speech (HD quality) |
| `minimax_voice_clone` | Clone a voice from an audio sample |
| `minimax_voice_design` | Design a custom voice |
| `minimax_music_generation` | Generate music from text |
| `minimax_list_voices` | List available TTS voices |
| `minimax_play_audio` | Play audio locally |
| `minimax_web_search` | Web search via MiniMax |
| `minimax_understand_image` | Analyze and describe images |
| `minimax_query_video_generation` | Check video generation status |

---

## Usage examples

Once configured, just ask Claude Code (or your preferred AI client):

```
Generate an image of a futuristic dashboard with dark UI
```

```
Create a 5-second intro video for my product
```

```
Convert this text to speech using a professional male voice:
"Welcome to Pi Agent Suite. Your AI assistant with memory."
```

```
Search the web for the latest React 19 release notes
```

```
Analyze this screenshot and describe the UI elements
```

---

## MiniMax as chat model

To use MiniMax for code generation instead of (or alongside) Claude, update `config/providers.json`:

```json
{
  "default_provider": "minimax",
  "providers": {
    "minimax": {
      "enabled": true,
      "default_model": "abab6.5s-chat"
    }
  }
}
```

The Pi Harness reads `providers.json` to know which model to invoke for routing and planning tasks.

---

## Models reference

| Model ID | Best for | Context |
|---|---|---|
| `abab6.5s-chat` | Fast chat, code | 245K tokens |
| `abab6.5-chat` | Reasoning, complex tasks | 245K tokens |
| `image-01` | Image generation | — |
| `video-01` | Video generation | — |
| `speech-01-hd` | Text to speech (HD) | — |
| `embo-01` | Embeddings | 4096 tokens |

---

## Rate limits and budgeting

Standard plan: ~4,500 API calls per 5-hour window.

For background agents (auto-dream, raw-watcher, project-sync):
- Each mine/sync call uses minimal tokens (embedding only)
- Chat calls use 1 call unit each
- Image/video generation counts separately

Tips:
- Schedule `auto_dream.py` during off-hours
- Use `--limit` flag on `project_sync.py` to cap files per run
- Monitor usage at minimaxi.com → Usage Dashboard

---

## Troubleshooting

**"Invalid API key" error:**
```bash
echo $MINIMAX_API_KEY   # Verify it's set
python -c "import os; print(os.environ.get('MINIMAX_API_KEY', 'NOT SET'))"
```

**MCP tools not appearing in Claude Code:**
```bash
claude mcp list   # Check if minimax is listed
claude mcp add minimax npx -- -y @minimax/mcp-server   # Re-add
```

**Rate limit exceeded:**
Wait for the 5-hour window to reset, or upgrade your MiniMax plan.

**Video generation pending:**
Use `minimax_query_video_generation` with the task ID to check status — video generation is async and can take 1-3 minutes.
