help/test wording now matches the thin-supervisor parity wording.

## Remaining review notes / risks

1. `runAutoresearchLoop()` currently reads the run id back from the manifest file via `execFileSync('cat', ...)` + `JSON.parse(...)` on each iteration. That works, but it is a slightly awkward implementation detail and could be simplified to avoid shelling out to `cat`.
2. Focused tests cover the main parity surfaces, but there is still room for broader runtime coverage around `noop`, `abort`, `interrupted`, and explicit `pass_only` policy branches if the lead wants even tighter semantic locking.
3. I verified focused parity coverage and build status, not the entire repository-wide test suite/lint suite.

## Reviewer conclusion