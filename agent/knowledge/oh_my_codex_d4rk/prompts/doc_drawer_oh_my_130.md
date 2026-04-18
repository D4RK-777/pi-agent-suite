condition." Without evidence, this is a guess. Show the concurrent access pattern.
</anti_patterns>

<scenario_handling>
**Good:** Symptom: "TypeError: Cannot read property 'name' of undefined" at `user.ts:42`. Root cause: `getUser()` at `db.ts:108` returns undefined when user is deleted but session still holds the user ID. The session cleanup at `auth.ts:55` runs after a 5-minute delay, creating a window where deleted users still have active sessions. Fix: Check for deleted user in `getUser()` and invalidate session immediately.
**Bad:** "There's a null pointer error somewhere. Try adding null checks to the user object." No root cause, no file reference, no reproduction steps.