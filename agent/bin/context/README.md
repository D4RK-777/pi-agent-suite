# D4rk Mind — Infinite Context System

Gives AI agents **effectively unlimited context** via semantic retrieval from MemPalace.

## The Concept

Instead of:
```
[Traditional] "205K tokens remaining" ← Hits limit
```

You get:
```
[D4rk Mind] "2.1M effective context" ← Infinite via retrieval
```

As you chat, old conversations are offloaded to MemPalace. When relevant, they're retrieved in ~20ms.

## Quick Start

```bash
# Show context display
python display.py --size ultra

# Live updating display
python display.py --live

# Run tests
python context_tracker.py --demo
```

## Components

### context_tracker.py
Tracks conversation history and manages offloading.

```python
from context_tracker import ContextTracker, create_tracker

tracker = create_tracker(max_tokens=200000)

# Track messages
tracker.add_user_message("build a modal")
tracker.add_assistant_message("Here's the code...")

# Get effective context
print(tracker.get_display())
# ╔════════════════════════════════════════════════════════════════╗
# ║  Effective Context:        2.1M tokens                        ║
# ║  Actual in memory:       45K tokens                          ║
# ║  Offloaded:              120K tokens                         ║
# ║  Retrievable patterns:   500 segments                        ║
# ╚════════════════════════════════════════════════════════════════╝

# Auto-offload when needed
if tracker.should_offload():
    tracker.offload_oldest()

# Retrieve relevant history
history = tracker.retrieve_history("modal animation")
```

### context_manager.py
Main orchestrator for building context.

```python
from context_manager import ContextManager

ctx = ContextManager()

# Build context for query
response = ctx.build_context("explain the auth system")

print(response.context)      # Relevant patterns
print(response.sources)     # Source references
print(response.stats)       # Performance stats
```

### integrate.py
Beautiful display components.

```bash
# Compact (single line)
python integrate.py --size compact
# 💭 Effective: 2.1M | Free: 155K | Patterns: 500 | 23ms

# Medium
python integrate.py --size medium

# Large with details
python integrate.py --size large

# Ultra (showoff mode)
python integrate.py --size ultra

# Live updating
python integrate.py --live --interval 5
```

## How It Works

```
┌─────────────────────────────────────────────────────────────────────┐
│                     CONVERSATION FLOW                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   User: "build me a modal"                                          │
│         │                                                            │
│         ▼                                                            │
│   ┌─────────────────────────────────────────────────────────┐      │
│   │              CONTEXT TRACKER                             │      │
│   │                                                          │      │
│   │   Track: actual_tokens = 1000                           │      │
│   │                                                          │      │
│   │   If > threshold:                                        │      │
│   │     • Summarize oldest messages                         │      │
│   │     • Offload to MemPalace                             │      │
│   │     • actual_tokens -= offloaded                        │      │
│   └─────────────────────────────────────────────────────────┘      │
│         │                                                            │
│         ▼                                                            │
│   ┌─────────────────────────────────────────────────────────┐      │
│   │              MEMPALACE                                   │      │
│   │                                                          │      │
│   │   Collection: conversation_history                        │      │
│   │   • 500+ conversation segments stored                   │      │
│   │   • Semantic search on retrieval                         │      │
│   │   • 20ms query time                                    │      │
│   └─────────────────────────────────────────────────────────┘      │
│         │                                                            │
│         ▼                                                            │
│   ┌─────────────────────────────────────────────────────────┐      │
│   │              EFFECTIVE CONTEXT                           │      │
│   │                                                          │      │
│   │   actual_tokens:          45,000                         │      │
│   │   retrievable_patterns:  500 segments                    │      │
│   │   avg_tokens_per:        500                             │      │
│   │                                                          │      │
│   │   EFFECTIVE = 45K + (500 × 500) = 2,045,000 tokens     │      │
│   └─────────────────────────────────────────────────────────┘      │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

## Integration with Agent Harness

### Step 1: Initialize Tracker

```python
# At session start
from context_tracker import create_tracker

tracker = create_tracker(max_tokens=200000)
```

### Step 2: Track Messages

```python
# Before sending to model
tracker.add_user_message(user_input)

# After receiving response
tracker.add_assistant_message(model_response)

# Check if offload needed
if tracker.should_offload():
    tracker.offload_oldest()
```

### Step 3: Display Status

```python
# In UI or logs
print(tracker.get_display())
# Shows: Effective Context: 2.1M tokens
```

### Step 4: Retrieve When Needed

```python
# When user asks about something from earlier
history = tracker.retrieve_history("that modal you built")
for h in history:
    print(h.content)
```

## Display Options

| Size | Description |
|------|-------------|
| `compact` | Single line: `💭 Effective: 2.1M \| Free: 155K` |
| `medium` | Box: `╔══════╗ ... ╚══════╝` |
| `large` | Full details with progress bar |
| `ultra` | ASCII art with full features |

```bash
# Watch it update live
python integrate.py --live --size large

# Or in your code
from integrate import get_display_large
print(get_display_large())
```

## Performance

| Metric | Value |
|--------|-------|
| Retrieval time | ~20ms |
| Offload time | ~50ms |
| Compression ratio | 5-10x |
| Max effective context | ~10M tokens |

## Architecture

```
context/
├── __init__.py          # Main exports
├── context_manager.py    # Orchestrator
├── context_tracker.py    # Conversation tracking
├── integrate.py         # UI displays
└── server.py            # HTTP API (optional)
```

## Status Line

Get a single-line status for status bars:

```python
from context_tracker import get_status_line

print(get_status_line(tracker))
# Context: 2.1M (100% | 500 patterns | 23ms)
```

## Tips

1. **Start tracking early** — Initialize at session start
2. **Offload aggressively** — Better to offload too early
3. **Query relevant** — "show me the modal code" retrieves modal discussions
4. **Keep system prompt** — Never offload core instructions

## Files Created

```
~/.mempalace/
├── palace/                      # Vector DB
├── conversation_offload/        # Offloaded conversations
│   ├── abc123.json            # Conversation segments
│   └── def456.json
└── ...
```

## License

MIT
