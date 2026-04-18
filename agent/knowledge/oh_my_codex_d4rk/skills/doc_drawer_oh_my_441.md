s a live URL (not a static screenshot — use `$visual-verdict` for screenshot-only tasks)
</Use_When>

<Do_Not_Use_When>
- User only has screenshot references without a live URL — use `$visual-verdict` directly
- User wants to modify, redesign, or "improve" the site — use standard implementation flow
- Target requires authentication, payment flows, or backend API parity — out of scope for v1
- Multi-page / multi-route deep cloning — v1 handles single-page scope only
</Do_Not_Use_When>

<Scope_Limits>
**v1 scope**: Single page clone of the provided URL.