, 80),
      description: `Continue implementation work on: ${task}`,
    });
  }
  return result;
}

/** Distribute tasks across workers using an inspectable allocation policy. */
function distributeTasksToWorkers(
  tasks: Array<{ subject: string; description: string; role?: string; blocked_by?: string[] }>,
  workerCount: number,
  workerRole?: string,
): Array<{ subject: string; description: string; owner: string; role?: string }> {
  const workers = Array.from({ length: workerCount }, (_, index) => ({
    name: `worker-${index + 1}`,
    role: workerRole,
  }));
  return allocateTasksToWorkers(tasks, workers).map(({ allocation_reason: _allocationReason, ...task }) => task);
}