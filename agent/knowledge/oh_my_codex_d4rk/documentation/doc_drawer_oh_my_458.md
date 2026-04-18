hen setup replaces managed artifacts, it now does so with stronger backup behavior where applicable.

**Why this matters:**
- lowers risk when refreshing existing local OMX-managed files
- gives users a clearer recovery path if they need to inspect prior state
- makes setup automation less destructive

### 3) Setup now prompts before model upgrade rewrites

When managed configuration refreshes would upgrade Codex model references from `gpt-5.3-codex` to `gpt-5.4`, setup now asks before making that change.

**Why this matters:**
- avoids surprising model upgrades during routine refreshes
- preserves user trust when setup wants to modify existing config
- keeps managed defaults modern without forcing silent rewrites

### 4) Regression coverage expanded for refresh and idempotency