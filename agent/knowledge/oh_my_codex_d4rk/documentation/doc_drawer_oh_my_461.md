# oh-my-codex v0.8.5

Released: 2026-03-06

7 non-merge commits from `v0.8.4..dev`.
Contributors: [@Yeachan-Heo](https://github.com/Yeachan-Heo), [@HaD0Yun](https://github.com/HaD0Yun), [@sjals93](https://github.com/sjals93).

## Highlights

### Posture-aware agent routing (experimental)

Agents now carry Sisyphus-style posture metadata that separates three dimensions:

- **Role**: agent responsibility (`executor`, `planner`, `architect`)
- **Tier**: reasoning depth / cost (`LOW`, `STANDARD`, `THOROUGH`)
- **Posture**: operating style (`frontier-orchestrator`, `deep-worker`, `fast-lane`)

After `omx setup`, native agent configs in `~/.omx/agents/` include new sections:
`## OMX Posture Overlay`, `## Model-Class Guidance`, and `## OMX Agent Metadata`.