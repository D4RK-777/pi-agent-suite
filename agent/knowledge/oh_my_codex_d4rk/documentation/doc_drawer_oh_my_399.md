e functional commits were found on `main` that are missing from `dev`.

## 2) Risk-Based Focus Areas

1. **Notify hook behavior**
   - Expanded stall phrase detection and new hot-zone detection logic.
   - All-workers-idle leader notification with cooldown/event logging.
2. **Tmux team UX/reliability**
   - Mouse scrolling enabled by default for team sessions.
   - `sendToWorker` timing changes around submit rounds.
3. **Config compatibility**
   - `collab` -> `multi_agent` migration in generated config + tests/docs.
4. **Lifecycle/process handling**
   - `bin/omx.js` now awaits `main(...)` and exits explicitly.

## 3) Automated QA

```bash
npm run test:run
```