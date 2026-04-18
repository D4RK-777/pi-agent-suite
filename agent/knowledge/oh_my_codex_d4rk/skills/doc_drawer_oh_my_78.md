supports resume from the last
incomplete stage. See `src/pipeline/orchestrator.ts` for the full API.

## Troubleshooting

**Stuck in a phase?** Check TODO list for blocked tasks, run `state_read({mode: "autopilot"})`, or cancel and resume.

**QA cycles exhausted?** The same error 3 times indicates a fundamental issue. Review the error pattern; manual intervention may be needed.

**Validation keeps failing?** Review the specific issues. Requirements may have been too vague -- cancel and provide more detail.
</Advanced>