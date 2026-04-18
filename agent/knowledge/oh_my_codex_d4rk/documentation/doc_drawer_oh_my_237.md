```js
export async function onHookEvent(event, sdk) {
  // handle event
}
```

SDK surface includes:

- `sdk.tmux.sendKeys(...)`
- `sdk.log.info|warn|error(...)`
- `sdk.state.read|write|delete|all(...)` (plugin namespace scoped)
- `sdk.omx.session.read()`
- `sdk.omx.hud.read()`
- `sdk.omx.notifyFallback.read()`
- `sdk.omx.updateCheck.read()`

`sdk.omx` is intentionally narrow and read-only in pass one. These helpers read the
repo-root `.omx/state/*.json` runtime files for the current workspace.

Compatibility notes: