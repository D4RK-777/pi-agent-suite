new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.completed_at ?? null] as const));
  const taskDependsOnById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.depends_on ?? task.blocked_by ?? []] as const));
  const taskClaimPresentById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.claim != null] as const));
  const taskClaimOwnerById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.claim?.owner ?? null] as const));
  const taskClaimTokenById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.claim?.token ?? null] as const));
  const taskClaimLeaseById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.claim?.leased_until ?? null] as const));