*
- Confirm the recovery/inspection command shown by the tool is sufficient when followed literally.

**Setup**
1. Pick one direct-command scenario and one tmux-pane scenario.
2. Record the exact next-step command suggested by the tool.
3. Follow that command without editing it first.

Useful direct-command baseline:

```bash
node bin/omx.js sparkshell --help
node bin/omx.js explore --help
```

**Evidence to capture**
- original tool output,
- copied next-step command,
- result of running that command,
- whether additional hidden knowledge was needed.

**Failure signal**
- the suggested command is syntactically wrong,
- the command is directionally wrong for the scenario,
- the operator must guess undocumented extra context to recover.

## Verification glue checklist