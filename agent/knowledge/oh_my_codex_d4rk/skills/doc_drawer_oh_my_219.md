older than 7 days |
| `/note --clear` | Clear Working Memory (keep Priority + MANUAL) |

## Sections

### Priority Context (500 char limit)
- **Always** injected on session start
- Use for critical facts: "Project uses pnpm", "API in src/api/client.ts"
- Keep it SHORT - this eats into your context budget

### Working Memory
- Timestamped session notes
- Auto-pruned after 7 days
- Good for: debugging breadcrumbs, temporary findings

### MANUAL
- Never auto-pruned
- User-controlled permanent notes
- Good for: team contacts, deployment info

## Examples

```
/note Found auth bug in UserContext - missing useEffect dependency
/note --priority Project uses TypeScript strict mode, all files in src/
/note --manual Contact: api-team@company.com for backend questions
/note --show
/note --prune
```