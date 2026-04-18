|
| AVOID | THOROUGH tier - only for planning/critique if essential |

## Agent Selection in Ecomode

**FIRST ACTION:** Before delegating any work, read the agent reference file:
```
Read file: docs/shared/agent-tiers.md
```
This provides the complete agent tier matrix, MCP tool assignments, and selection guidance.

**Ecomode preference order:**

```
// PREFERRED - Use for most tasks
delegate(role="executor", tier="LOW", task="...")
delegate(role="explore", tier="LOW", task="...")
delegate(role="architect", tier="LOW", task="...")

// FALLBACK - Only if LOW fails
delegate(role="executor", tier="STANDARD", task="...")
delegate(role="architect", tier="STANDARD", task="...")

// AVOID - Only for planning/critique if essential
delegate(role="planner", tier="THOROUGH", task="...")
```