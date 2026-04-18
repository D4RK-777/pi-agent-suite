web-clone"`.
   - The visual portion of the verdict feeds directly into the composite verdict below.
   - Visual pass threshold: **score >= 85**.

3. **Structural verification**: Compare landmark counts:
   - Count `<nav>`, `<main>`, `<footer>`, `<form>`, `<button>`, `<a>` in both original and clone.
   - Structure passes when all major landmarks exist (missing landmarks = fail).

4. **Functional spot-check**: Test 2–3 detected interactions via Playwright:
   - Click a navigation link → verify URL change or scroll behavior
   - Toggle a dropdown/modal → verify visibility change
   - Interact with a form field → verify it accepts input
   - Use `browser_click` and `browser_snapshot` to verify state changes.

5. **Emit composite verdict**: