fication summary

Release verification evidence is recorded in `docs/qa/release-readiness-0.8.3.md`.

Planned release gates:
- `npm run build`
- `npm test`
- `npm run check:no-unused`
- CLI smoke checks (`--help`, `version`, `status`, `doctor`, `setup --dry-run`, `cancel`)
- Gemini-targeted regression checks from PR `#585`

---

Thanks for using **oh-my-codex**. If anything regresses, please open an issue with reproduction steps, logs, and your CLI/runtime details.