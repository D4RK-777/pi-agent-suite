/team/scaling.ts`, `src/team/worker-bootstrap.ts`, targeted native/runtime/scaling/bootstrap tests |
| role/tier/posture routing | `README.md:133-179`, `docs/shared/agent-tiers.md:7-56`, `src/agents/native-config.ts:12-40` |

If a change only affects posture overlays or native agent metadata, document it in the routing docs rather than expanding this contract unnecessarily.

## Canonical role prompts vs specialized behavior prompts

The main role catalog is the installable specialized-agent set used by `/prompts:name` and native agent generation.