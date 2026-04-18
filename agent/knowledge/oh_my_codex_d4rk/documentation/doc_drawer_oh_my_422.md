# Release notes — 0.11.8

## Summary

`0.11.8` is a hotfix release after `0.11.7` that disables all nudges while deep-interview state is active and hardens duplicate fresh-leader nudge prevention.

## Included fixes

- deep-interview state suppresses leader nudges, worker-idle nudges, Ralph continue-steers, and auto-nudges
- fallback watcher leader nudges remain stale-only instead of reacting to fresh mailbox activity
- notify-hook regression coverage now proves the same fresh mailbox message is not re-nudged on repeated runs
- release metadata is bumped to `0.11.8` across Node and Cargo packages

## Verification evidence

### Targeted regression suite