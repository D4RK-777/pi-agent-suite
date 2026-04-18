l, run local entrypoint:

```bash
node bin/omx.js setup --force --verbose
node bin/omx.js doctor
```

- If AGENTS.md was not overwritten during `--force`, stop active OMX session and rerun setup.