): string {
  return !explicitAgentType && agentType === 'executor' ? 'team-executor' : agentType;
}

function looksLikeLowConfidenceAnalysisTask(task: string): boolean {
  const normalized = task.trim();
  return ANALYSIS_TASK_PREFIX.test(normalized)
    && (ANALYSIS_DELIVERABLE_SIGNAL.test(normalized)
      || countWords(normalized) > 18
      || CONTEXTUAL_DECOMPOSITION_CLAUSE.test(normalized));
}

function resolveTeamFanoutLimit(
  task: string,
  requestedWorkerCount: number,
  explicitAgentType: boolean,
  explicitWorkerCount: boolean,
  plan: DecompositionPlan,
): number {
  if (requestedWorkerCount <= 1 || explicitAgentType || explicitWorkerCount || plan.strategy === 'numbered' || plan.strategy === 'bulleted') {
    return requestedWorkerCount;
  }