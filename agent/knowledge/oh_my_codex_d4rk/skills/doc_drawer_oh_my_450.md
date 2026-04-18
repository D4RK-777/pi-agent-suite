## Pass 1 — Extract

Capture the target page's structure, styles, interactions, and visual baseline.

1. **Navigate**: `browser_navigate` to `target_url`.
2. **Wait for render**: `browser_wait_for` with appropriate condition (network idle or timeout of 5s) to ensure full render including lazy-loaded content.
3. **Accessibility snapshot**: `browser_snapshot` — captures the semantic tree (roles, names, values, interactive states). This is your primary structural reference.
4. **Full-page screenshot**: `browser_take_screenshot` with `fullPage: true` — save as reference baseline `target-full.png`.
5. **DOM + computed styles**: `browser_evaluate` with the following script. **COPY THIS SCRIPT EXACTLY — do not modify it**:
   ```javascript
   (() => {
     const walk = (el, depth = 0) => {