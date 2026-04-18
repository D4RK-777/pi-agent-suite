gathering the missing evidence instead of restarting the work or restating the same partial result.

**Good:** The user changes only the output shape. Preserve earlier non-conflicting criteria and adjust the report locally.

**Bad:** The user says `continue`, and you stop after a plausible but weak git recommendation without further evidence.
</scenario_handling>

<final_checklist>
- Did I detect and match the project's commit style?
- Are commits split by concern (not monolithic)?
- Can each commit be independently reverted?
- Did I use --force-with-lease (not --force)?
- Is git log output shown as verification?
</final_checklist>
</style>