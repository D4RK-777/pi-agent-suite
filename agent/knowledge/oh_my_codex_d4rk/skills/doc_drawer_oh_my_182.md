eep-interview-{slug}.md`
- [ ] Brownfield questions use evidence-backed confirmation when applicable
- [ ] Handoff options provided (`$ralplan`, `$autopilot`, `$ralph`, `$team`)
- [ ] No direct implementation performed in this mode
</Final_Checklist>

<Advanced>
## Suggested Config (optional)

```toml
[omx.deepInterview]
defaultProfile = "standard"
quickThreshold = 0.30
standardThreshold = 0.20
deepThreshold = 0.15
quickMaxRounds = 5
standardMaxRounds = 12
deepMaxRounds = 20
enableChallengeModes = true
```

## Resume

If interrupted, rerun `$deep-interview`. Resume from persisted mode state via `state_read(mode="deep-interview")`.

## Recommended 3-Stage Pipeline

```
deep-interview -> ralplan -> autopilot
```