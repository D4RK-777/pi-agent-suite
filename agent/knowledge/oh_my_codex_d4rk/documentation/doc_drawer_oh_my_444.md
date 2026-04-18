d

Hardcoded default frontier-model fallback references were replaced with `DEFAULT_FRONTIER_MODEL`.

Current behavior from this release:
- default frontier fallback now resolves through a single constant
- that constant is currently set to **`gpt-5.4`**
- low-complexity spark default remains **`gpt-5.3-codex-spark`**

**Why this matters:**
- fewer hidden fallback mismatches
- easier future model updates
- cleaner test and config semantics

### 3) Setup/install behavior is cleaner and safer