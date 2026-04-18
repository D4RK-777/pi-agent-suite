summary: staffingPlan.staffingSummary,
    staffing_allocations: staffingPlan.allocations,
  });

}


async function renderStartSummary(runtime: TeamRuntime, staffingPlan?: FollowupStaffingPlan): Promise<void> {
  console.log(`Team started: ${runtime.teamName}`);
  console.log(`tmux target: ${runtime.sessionName}`);
  console.log(`workers: ${runtime.config.worker_count}`);
  console.log(`agent_type: ${runtime.config.agent_type}`);
  if (runtime.config.workspace_mode) {
    console.log(`workspace_mode: ${runtime.config.workspace_mode}`);
  }
  if (staffingPlan) {
    console.log(`available_agent_types: ${staffingPlan.rosterSummary}`);
    console.log(`staffing_plan: ${staffingPlan.staffingSummary}`);
  }