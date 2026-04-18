m**: parallel coordinated agents
6. Execution begins with a clear, bounded plan

### Troubleshooting

| Issue | Solution |
|-------|----------|
| Gate fires on a well-specified prompt | Add a file reference, function name, or issue number to anchor the request |
| Want to bypass the gate | Prefix with `force:` or `!` (e.g., `force: ralph fix it`) |
| Gate does not fire on a vague prompt | The gate only catches prompts with <=15 effective words and no concrete anchors; add more detail or use `$ralplan` explicitly |
| Redirected to ralplan but want to skip planning | In the ralplan workflow, say "just do it" or "skip planning" to transition directly to execution |

## Scenario Examples