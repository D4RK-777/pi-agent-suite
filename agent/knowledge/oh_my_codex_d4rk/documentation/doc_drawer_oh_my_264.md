`$team` (or explicit `/prompts:*` sequencing) | Team is the default orchestrator pipeline surface. |
| `$ultrapilot` | `$team` | Use team-based parallel orchestration. |
| `$psm` / `$project-session-manager` | No in-repo replacement | Remove from automation or maintain out-of-tree tooling. |
| `$release` | No in-repo replacement | Use your project release process directly. |
| `$deepinit` | `omx agents-init [path]` | Lightweight CLI successor for AGENTS.md bootstrap only; immediate child directories only, unmanaged files preserved unless `--force`. |
| `$learn-about-omx` / `$learner` / `$writer-memory` | No in-repo replacement | Remove stale references from workflows/docs. |

## Verification checklist after upgrade

Run this checklist after pulling latest mainline: