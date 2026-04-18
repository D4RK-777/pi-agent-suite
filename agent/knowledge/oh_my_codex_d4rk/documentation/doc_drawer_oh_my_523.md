ntime-generated files must be excluded via worktree-local `.git/info/exclude`

## Candidate artifact

The launched session must write repo-root `candidate.json` with:
- `status`: `candidate | noop | abort | interrupted`
- `candidate_commit`: string or `null`
- `base_commit`: string
- `description`: string
- `notes`: string[]
- `created_at`: ISO timestamp

Integrity rules:
- `status=candidate` requires a non-null `candidate_commit`
- `candidate_commit` must resolve in git and match the worktree `HEAD` commit on exit
- `base_commit` must resolve in git and match the supervisor-provided `last_kept_commit`