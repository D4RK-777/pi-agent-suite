x.js` now awaits `main(...)` and exits explicitly.

## 3) Automated QA

```bash
npm run test:run
```

Pass criteria:
- Full suite passes.
- New/updated suites specifically pass:
  - `src/hooks/__tests__/notify-hook-all-workers-idle.test.ts`
  - `src/hooks/__tests__/notify-hook-auto-nudge.test.ts`
  - `src/team/__tests__/tmux-session.test.ts`
  - `src/config/__tests__/generator-notify.test.ts`
  - newly added extensibility/HUD/utils/verifier test files

## 4) Manual QA Checklist

### A. All workers idle notification
- Start a team session with >=2 workers.
- Let all workers transition to `idle` or `done`.
- Verify leader receives one idle-summary prompt.
- Re-trigger within cooldown window: verify no duplicate notification spam.
- Verify event/log entries are emitted.