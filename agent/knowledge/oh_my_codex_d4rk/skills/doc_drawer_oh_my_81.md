ing, destructive, or preference-dependent.

Delegates to the `build-fixer` agent (STANDARD tier) to:

1. **Collect Errors**
   - Run the project's type check command (e.g., `tsc --noEmit`, `mypy`, `cargo check`, `go vet`)
   - Or run the project's build command to get build failures
   - Categorize errors by type and severity

2. **Fix Strategically**
   - Add type annotations where missing
   - Add null checks where needed
   - Fix import/export statements
   - Resolve module resolution issues
   - Fix linter errors blocking build

3. **Minimal Diff Strategy**
   - NO refactoring of unrelated code
   - NO architectural changes
   - NO performance optimizations
   - ONLY what's needed to make build pass