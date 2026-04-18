ailable.
- Plans must meet quality standards: 80%+ claims cite file/line, 90%+ criteria are testable
- Implementation step count must be right-sized to task scope; avoid defaulting to exactly five steps when the work is clearly smaller or larger
- Consensus mode outputs the final plan by default; add `--interactive` to enable execution handoff
- Consensus mode uses RALPLAN-DR short mode by default; switch to deliberate mode with `--deliberate` or when the request explicitly signals high risk (auth/security, data migration, destructive/irreversible changes, production incident, compliance/PII, public API breakage)
- Default to concise, evidence-dense progress and completion reporting unless the user or risk level requires more detail