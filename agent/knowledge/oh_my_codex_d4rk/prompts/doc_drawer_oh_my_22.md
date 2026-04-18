│
│              ┌──────────┴──────────┐                        │
│              │  Shared Task Queue   │                        │
│              │  (durable state)     │                        │
│              └─────────────────────┘                        │
└─────────────────────────────────────────────────────────────┘
```

**Key Features:**
- **Mixed CLI Workers**: Combines OpenAI Codex and Anthropic Claude agents in one team
- **Durable State**: Task assignments persist across session interruptions
- **Claim-Safe Lifecycle**: Prevents race conditions with versioned task claims
- **Mailbox Communication**: Structured message passing between workers

### Quick Start

Use a deterministic task slug so the team name is predictable: