tions.idleCooldownSeconds`

### Profiles
- `notifications.profiles`
- `notifications.defaultProfile`

### Reply listener
- `notifications.reply.enabled`
- env gates: `OMX_REPLY_ENABLED=true`, and for Discord `OMX_REPLY_DISCORD_USER_IDS=...`

## Step 6: Disable All Notifications

```bash
jq '.notifications.enabled = false' "$CONFIG_FILE" > "$CONFIG_FILE.tmp" && mv "$CONFIG_FILE.tmp" "$CONFIG_FILE"
```

## Step 7: Verification Guidance

After writing config, run a smoke check:

```bash
npm run build
```

For OpenClaw-like HTTP integrations, verify both:
- `/hooks/wake` smoke test
- `/hooks/agent` delivery verification

## Final Summary Template