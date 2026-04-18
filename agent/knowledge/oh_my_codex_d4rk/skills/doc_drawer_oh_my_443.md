nality (maps, embeds, chat widgets)
- Image/asset replication (use placeholders for external images)

**Legal notice**: Only clone sites you own or have explicit permission to replicate. Respect copyright and trademarks.
</Scope_Limits>

<Prerequisites>
Playwright MCP server must be available for browser automation.

1. Before first tool use, call `ToolSearch("browser")` or `ToolSearch("playwright")` to discover available browser tools.
2. If no browser tools are found, instruct the user:
   ```
   Playwright MCP is required. Configure it:
   codex mcp add playwright npx "@playwright/mcp@latest"
   ```
3. Required tools: `browser_navigate`, `browser_snapshot`, `browser_take_screenshot`, `browser_evaluate`, `browser_wait_for`. Optional: `browser_click`, `browser_network_requests`.