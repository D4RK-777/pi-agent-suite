hot`, `browser_evaluate`, `browser_wait_for`. Optional: `browser_click`, `browser_network_requests`.
</Prerequisites>

<Inputs>
- `target_url` (required): The URL to clone
- `output_dir` (optional, default: current working directory): Where to generate the clone project
- `tech_stack` (optional, inferred from project context): HTML/CSS/JS, React, Vue, Svelte, etc.
</Inputs>

<Tool_Usage>
- Before first MCP tool use, call `ToolSearch("browser")` or `ToolSearch("playwright")` to discover deferred Playwright MCP tools.
- If no browser tools are found, stop immediately and instruct the user to configure Playwright MCP.
- Use `browser_snapshot` (accessibility tree) for structural understanding — it is far more token-efficient than screenshots.