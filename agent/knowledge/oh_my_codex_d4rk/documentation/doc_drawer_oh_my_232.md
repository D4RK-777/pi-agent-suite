p + blocked-state rules | write task result + status updates | mailbox polling + shutdown handling |
| `skills/worker/SKILL.md` + worker inbox | worker role framing | worker protocol principles | startup ACK/task lifecycle steps | claim-first + path/id safety rules | completion writeback requirements | mailbox/shutdown loop |

## Adoption Notes

- Prefer additive wording updates over structural removals during rollout.
- Preserve all marker-bounded overlay text contracts while aligning language to this schema.
- Role prompts should recommend handoffs upward to the orchestrator instead of spawning or requesting other agents directly.
- Root orchestration surfaces should choose one mode clearly (`$deep-interview`, `$ralplan`, `$team`, or solo execute) before mixing lanes.