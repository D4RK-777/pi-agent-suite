filtered for Gemini workers

Gemini workers no longer inherit non-Gemini default models by accident.

Current behavior from this release:
- explicit Gemini models still pass through
- non-Gemini defaults are omitted for Gemini workers
- mixed-provider team configs avoid invalid startup argument combinations

**Why this matters:**
- prevents invalid provider/model pairings during worker launch
- preserves cleaner mixed-provider CLI interoperability
- reduces surprising failures in prompt-mode and mapped-worker setups

### 3) Regression coverage was expanded for the hotfix path

This release adds focused tests covering:
- prompt-mode Gemini startup argument construction
- runtime startup behavior for prompt-launched Gemini workers
- translation behavior when default models are non-Gemini