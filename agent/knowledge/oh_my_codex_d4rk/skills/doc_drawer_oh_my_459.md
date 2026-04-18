sponsive rules.

## Pass 4 — Verify

Compare the clone against the original across three dimensions.

1. **Serve the clone**: Start a local server for the generated project:
   ```bash
   npx serve {output_dir} -l 3456 --no-clipboard
   ```
   If `npx serve` is unavailable, fall back to: `python3 -m http.server 3456 -d {output_dir}`.
   The clone will be accessible at `http://localhost:3456`.
2. **Visual verification**:
   - Navigate to the clone with Playwright: `browser_navigate` to clone URL.
   - Take full-page screenshot of clone.
   - Run `$visual-verdict` with: `reference_images=["target-full.png"]`, `generated_screenshot="clone-full.png"`, `category_hint="web-clone"`.
   - The visual portion of the verdict feeds directly into the composite verdict below.