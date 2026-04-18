uth2 flow")
```
Why good: Three independent tasks fired simultaneously at appropriate tiers.
</Good>

<Good>
Correct verification before completion:
```
1. Run: npm test           → Output: "42 passed, 0 failed"
2. Run: npm run build      → Output: "Build succeeded"
3. Run: lsp_diagnostics    → Output: 0 errors
4. Delegate to architect at STANDARD tier  → Verdict: "APPROVED"
5. Run /cancel
```
Why good: Fresh evidence at each step, architect verification, then clean exit.
</Good>

<Bad>
Claiming completion without verification:
"All the changes look good, the implementation should work correctly. Task complete."
Why bad: Uses "should" and "look good" -- no fresh test/build output, no architect verification.
</Bad>