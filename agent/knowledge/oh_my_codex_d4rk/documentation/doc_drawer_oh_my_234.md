# Hooks Extension (Custom Plugins)

OMX supports an additive hooks extension point for user plugins under `.omx/hooks/*.mjs`.

> Compatibility guarantee: `omx tmux-hook` remains fully supported and unchanged.
> The new `omx hooks` command group is additive and does **not** replace tmux-hook workflows.

## Quick start

```bash
omx hooks init
omx hooks status
omx hooks validate
omx hooks test
```

This creates a scaffold plugin at:

- `.omx/hooks/sample-plugin.mjs`

## Enablement model

Plugins are **enabled by default**.

Disable plugin dispatch explicitly:

```bash
export OMX_HOOK_PLUGINS=0
```

Optional timeout tuning (default: 1500ms):

```bash
export OMX_HOOK_PLUGIN_TIMEOUT_MS=1500
```

## Native event pipeline (v1)

Native events are emitted from existing lifecycle/notify paths: