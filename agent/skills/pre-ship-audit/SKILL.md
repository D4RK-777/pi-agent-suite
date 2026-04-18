---
name: pre-ship-audit
description: Use before declaring a feature complete, before opening a PR, or when the user asks "is this ready to ship?". Runs the full pre-merge checklist.
---

# pre-ship-audit

A feature isn't done when the code compiles. It's done when this checklist passes.

## The checklist

Run these in order. Don't skip. Don't mark "done" on items you didn't actually verify.

**Use the project's package manager** — check for `pnpm-lock.yaml`, `yarn.lock`, `bun.lock`, or `package-lock.json` first. Examples below use `<pm>` as a placeholder.

### 1. Type check
```
<pm> run typecheck   # or: <pm> tsc --noEmit
```
Zero errors. A new `any` warning is a new `any` that shouldn't exist — fix it.

### 2. Lint
```
<pm> run lint
```
New warnings are new bugs. Don't add `// eslint-disable-next-line` without a comment explaining *why*.

### 3. Test
Run the test command for this repo (check `package.json` scripts). Failed tests block. Skipped tests with `.skip` need a reason in the commit message.

### 4. Build
```
<pm> run build
```
A production build exposes errors a dev server hides (tree-shaking, dead code elimination, SSR issues).

### 5. Manual UI check — golden path
- Launch dev server.
- Walk through the happy path for the feature.
- Test in the default theme AND the opposite (dark/light).
- Check one viewport the user will actually use (mobile width ≤ 400px if applicable).

### 6. Manual UI check — edge cases
- Empty state (no data).
- Loading state (throttle network in devtools).
- Error state (break the API call deliberately).
- Keyboard-only navigation through the feature.

### 7. Regression scan
For every file you changed, scan callers for affected behavior:
```
grep -rn "nameOfChangedThing" src/
```
A change isn't safe because the feature works — it's safe when the *other* features still work.

### 8. Accessibility spot-check
- Every new interactive element has a label and focus ring?
- Color contrast meets 4.5:1 for text?
- Works with keyboard only?

### 9. Git hygiene
- Commits tell a story (one logical change per commit, imperative mood).
- No stray `console.log` or `debugger`.
- No commented-out code.
- No files added that shouldn't be (`.env`, lockfile churn from unrelated installs, build artifacts).

### 10. The "one hour later" test
Walk away mentally for a moment. Re-read your own diff. Would you accept this PR from someone else, or would you ask for changes? If the latter, make the changes before opening the PR.

## What NOT to do at ship time

- **Don't** add unrelated "while I'm here" cleanups. They make review harder and expand blast radius.
- **Don't** write tests after the fact just to hit a coverage number. Tests you wouldn't have written if coverage didn't demand them are noise.
- **Don't** skip the manual UI check because "the types check". TypeScript proves the code is consistent; it doesn't prove it's correct.
- **Don't** rubber-stamp your own work.

## What to tell the user

When reporting "ready to ship", be specific: *"Types pass, build succeeds, manually tested golden path + empty state + keyboard nav, scanned N callers."*

If you can't verify something (e.g. no browser available), **say so explicitly**: *"Can't test UI in this environment — user should do the visual walk-through before merging."*

Honesty about what you verified beats false confidence every time.
