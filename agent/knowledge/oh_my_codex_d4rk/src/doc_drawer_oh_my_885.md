mmendedInspectApprovalRequired = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (approvalRecordByTaskId.get(taskId)?.required ?? null) : null];
    }),
  );
  const recommendedInspectApprovalReviewers = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (approvalRecordByTaskId.get(taskId)?.reviewer ?? null) : null];
    }),
  );
  const recommendedInspectApprovalReasons = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];