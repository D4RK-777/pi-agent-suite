vior appears implemented and the previously noted shared help/test wording mismatch is now resolved.

The branch now matches the PRD/test-spec shape much more closely than the earlier scaffold review:

- `omx autoresearch` exposes both fresh launch and `--resume <run-id>` flows.
- the runtime owns a thin-supervisor loop boundary via repo-root candidate handoff + post-session evaluator decisions.
- repo-root active-run locking and authoritative per-run manifests are present.
- fresh launches create run-tagged autoresearch lanes instead of silently reusing one long-lived lane.
- docs/help/contracts describe keep/discard/reset semantics instead of the earlier v1 scaffold.

## Verified evidence

### Build
- `npm run build` → PASS