recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (approvalRecordByTaskId.get(taskId)?.decision_reason ?? null) : null];
    }),
  );
  const recommendedInspectApprovalDecidedAt = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (approvalRecordByTaskId.get(taskId)?.decided_at ?? null) : null];
    }),
  );
  const recommendedInspectApprovalRecordPresent = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? approvalRecordByTaskId.get(taskId) !== null : null];
    }),
  );