as an
explicit follow-up, but there is no built-in `omx team ralph ...` linked launch
path anymore.

Legacy phase aliases may be normalized for compatibility, but persisted values MUST end in the frozen enum below.

## Frozen Ralph phase vocabulary

`current_phase` for Ralph MUST be one of:

- `starting`
- `executing`
- `verifying`
- `fixing`
- `complete`
- `failed`
- `cancelled`

Unknown phase values MUST be rejected.

Phase progression reference (illustrative):
starting
- `executing`
- `verifying`
- `fixing`
- `complete`

## Frozen scope policy