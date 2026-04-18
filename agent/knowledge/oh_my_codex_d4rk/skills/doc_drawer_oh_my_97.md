e tools report no active session. Swarm remains a shared SQLite/marker mode outside session scoping.
4. Any cancellation logic in this doc mirrors the dependency order discovered via state tools (autopilot → ralph → …).

### 3A. Force Mode (if --force or --all)

Use force mode to clear every session plus legacy artifacts via `state_clear`. Direct file removal is reserved for legacy cleanup when the state tools report no active sessions.

### 3B. Smart Cancellation (default)

#### If Team Active (tmux-based)

Teams are detected by checking for config files in `.omx/state/team/`:

```bash
# Check for active teams
ls .omx/state/team/*/config.json 2>/dev/null
```

**Two-pass cancellation protocol:**