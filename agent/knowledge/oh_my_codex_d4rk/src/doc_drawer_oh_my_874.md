kStatusById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.status] as const));
  const taskResultById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.result ?? null] as const));
  const taskErrorById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.error ?? null] as const));
  const taskVersionById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.version ?? null] as const));
  const taskCreatedAtById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.created_at ?? null] as const));
  const taskCompletedAtById = new Map((snapshot?.tasks.items ?? []).map((task) => [task.id, task.completed_at ?? null] as const));