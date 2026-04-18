s
- **Max iterations**: 5 (report best achieved result if threshold not met)
</Iteration_Thresholds>

<Error_Handling>
- **Playwright MCP unavailable**: Stop. Instruct user to configure it. Do not attempt to clone without browser tools.
- **Page fails to load**: Report the URL and HTTP status. Suggest the user verify the URL is accessible.
- **browser_evaluate returns empty**: The page may use heavy client-side rendering. Wait longer (`browser_wait_for` with extended timeout) and retry once.
- **Visual score stuck below threshold after 3 iterations**: Report the current state as best-effort. List the unresolved differences for the user.