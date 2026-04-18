off to execution |
| Review | `--review`, "review this plan" | Critic evaluation of existing plan |

### Interview Mode (broad/vague requests)

1. **Classify the request**: Broad (vague verbs, no specific files, touches 3+ areas) triggers interview mode
2. **Ask one focused question** using `AskUserQuestion` for preferences, scope, and constraints
3. **Gather codebase facts first**: Before asking "what patterns does your code use?", spawn an `explore` agent to find out, then ask informed follow-up questions
4. **Build on answers**: Each question builds on the previous answer
5. **Consult Analyst** (THOROUGH tier) for hidden requirements, edge cases, and risks
6. **Create plan** when the user signals readiness: "create the plan", "I'm ready", "make it a work plan"