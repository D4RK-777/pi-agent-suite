plementation phases
3. **Link to Ralph** so that `/ralph` can use the PRD as its completion criteria
4. **Initialize/ensure canonical progress ledger** at `.omx/state/{scope}/ralph-progress.json` (session scope if active session exists)

### Canonical source contract

- Canonical PRD source of truth is `.omx/plans/prd-{slug}.md`.
- Ralph progress source of truth is `.omx/state/{scope}/ralph-progress.json` (session scope when available).
- Legacy `.omx/prd.json` / `.omx/progress.txt` inputs are compatibility-only and migrate one-way into canonical artifacts.

## Output

A structured PRD file saved to `.omx/plans/` that serves as the definition of done for Ralph execution.

## Next Steps

After creating the PRD, start execution with:
```
/ralph "implement the PRD"
```