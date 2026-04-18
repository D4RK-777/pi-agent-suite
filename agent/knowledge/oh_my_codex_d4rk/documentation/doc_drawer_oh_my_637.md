io,
- the operator must guess undocumented extra context to recover.

## Verification glue checklist

Use this checklist after both deterministic and heavy/manual work are present.

### Deterministic lane
- [ ] `npm run test:explore`
- [ ] `npm run test:sparkshell`
- [ ] deterministic tests assert semantic fact preservation with predeclared must-preserve facts
- [ ] deterministic tests assert fallback path selection or actionable failure output
- [ ] deterministic tests assert sparkshell guidance/help remains actionable