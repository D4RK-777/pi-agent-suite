Pass 4 verification**: Append the composite verdict to `.omx/state/{scope}/web-clone-verdicts.json`.
- **When running within ralph**: Also persist the `visual` portion of the composite verdict to `.omx/state/{scope}/ralph-progress.json` for ralph compatibility, mapping `visual.score` → top-level `score` and `visual.verdict` → top-level `verdict`.
- **On completion or failure**: Write final status with `completed_at` or `failed_at` timestamp.
</State_Management>

<Context_Budget>
Pass 1 extraction can produce very large data. Apply these limits proactively: