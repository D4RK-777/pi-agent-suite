onst task = explicitTask === 'ralph-cli-launch' ? approvedHint?.task ?? explicitTask : explicitTask;
  const noDeslop = normalizedArgs.some((arg) => arg.toLowerCase() === '--no-deslop');
  const availableAgentTypes = await resolveAvailableAgentTypes(cwd);
  const staffingPlan = buildFollowupStaffingPlan('ralph', task, availableAgentTypes);
  await startMode('ralph', task, 50);
  const sessionFiles = await writeRalphSessionFiles(cwd, task, { noDeslop, approvedHint });
  await updateModeState('ralph', {
    current_phase: 'starting',
    canonical_progress_path: artifacts.canonicalProgressPath,
    available_agent_types: availableAgentTypes,
    staffing_summary: staffingPlan.staffingSummary,
    staffing_allocations: staffingPlan.allocations,
    native_subagents_enabled: true,