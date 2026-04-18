---
name: web-clone
description: URL-driven website cloning with visual + functional verification
---

<Purpose>
Clone a target website from its URL, replicating both visual appearance and core interactive functionality. Uses Playwright MCP for live page extraction, LLM-driven code generation, and iterative verification with `$visual-verdict` for visual scoring.
</Purpose>

<Use_When>
- User provides a target URL and wants the site replicated as working code
- User says "clone site", "clone website", "copy webpage", or "web-clone"
- Task requires both visual fidelity AND functional parity with the original
- Reference is a live URL (not a static screenshot — use `$visual-verdict` for screenshot-only tasks)
</Use_When>