across different AI CLI tools (Codex + Claude) in a single tmux session.

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    tmux Session "omx-team"                   │
│  ┌──────────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│  │   Leader     │  │ Worker 1 │  │ Worker 2 │  │ Worker N │ │
│  │  (main pane) │  │ (codex)  │  │ (codex)  │  │ (claude) │ │
│  └──────────────┘  └──────────┘  └──────────┘  └──────────┘ │
│         │               │              │              │     │
│         └───────────────┴──────────────┴──────────────┘     │
│                         │                                   │
│              ┌──────────┴──────────┐                        │