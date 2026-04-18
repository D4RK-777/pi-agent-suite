{
    strategy: 'atomic',
    subtasks: [{ subject: task.slice(0, 80), description: task }],
  };
}

/** Create aspect-scoped sub-tasks for an atomic task that can't be split. */
function createAspectSubtasks(
  task: string,
  workerCount: number,
): Array<{ subject: string; description: string }> {
  const aspects = [
    { subject: `Implement: ${task}`.slice(0, 80), description: `Implement the core functionality for: ${task}` },
    { subject: `Test: ${task}`.slice(0, 80), description: `Write tests and verify: ${task}` },
    { subject: `Review and document: ${task}`.slice(0, 80), description: `Review code quality and update documentation for: ${task}` },
  ];