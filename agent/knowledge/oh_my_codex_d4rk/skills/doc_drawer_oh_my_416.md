No TypeScript errors |
| `/ultraqa --custom "pattern"` | custom | Custom success pattern in output |

If no structured goal provided, interpret the argument as a custom goal.

## Cycle Workflow

### Cycle N (Max 5)

1. **RUN QA**: Execute verification based on goal type
   - `--tests`: Run the project's test command
   - `--build`: Run the project's build command
   - `--lint`: Run the project's lint command
   - `--typecheck`: Run the project's type check command
   - `--custom`: Run appropriate command and check for pattern
   - `--interactive`: Use qa-tester for interactive CLI/service testing:
     ```
     delegate(role="qa-tester", tier="STANDARD", task="TEST:
     Goal: [describe what to verify]
     Service: [how to start]
     Test cases: [specific scenarios to verify]")
     ```