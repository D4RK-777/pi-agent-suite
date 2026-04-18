);
  const approvalRecordByTaskId = new Map<string, Awaited<ReturnType<typeof readTaskApproval>>>();
  for (const taskId of new Set(Object.values(recommendedInspectTasks).filter((value): value is string => typeof value === 'string' && value.length > 0))) {
    approvalRecordByTaskId.set(taskId, snapshot?.teamName ? await readTaskApproval(snapshot.teamName, taskId, cwd) : null);
  }
  const recommendedInspectApprovalStatuses = Object.fromEntries(
    recommendedInspectTargets.map((target) => {
      const taskId = recommendedInspectTasks[target];
      return [target, taskId ? (approvalRecordByTaskId.get(taskId)?.status ?? null) : null];
    }),
  );
  const recommendedInspectApprovalRequired = Object.fromEntries(
    recommendedInspectTargets.map((target) => {