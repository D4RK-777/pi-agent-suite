files in TypeScript"
   - GOOD: "This codebase uses custom path resolution requiring fileURLToPath"

2. **Context-Specific** - References actual files/errors from THIS codebase
   - BAD: "Use try/catch for error handling"
   - GOOD: "The aiohttp proxy in server.py:42 crashes on ClientDisconnectedError"

3. **Actionable with Precision** - Tells exactly WHAT to do and WHERE
   - BAD: "Handle edge cases"
   - GOOD: "When seeing 'Cannot find module' in dist/, check tsconfig.json moduleResolution"

4. **Hard-Won** - Required significant debugging effort
   - BAD: Generic programming patterns
   - GOOD: "Race condition in worker.ts - Promise.all at line 89 needs await"

---

## Related Skills