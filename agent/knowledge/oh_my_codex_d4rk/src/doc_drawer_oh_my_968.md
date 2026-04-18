subtasks: strongParts.map((part) => ({ subject: part.slice(0, 80), description: part })),
    };
  }

  // Commas / "and" only split when the overall input already looks like a flat task list.
  const weakParts = task.split(/(?:,\s+and\s+|,\s+|\s+and\s+)/i).map(s => s.trim()).filter(s => s.length > 0);
  if (canSafelySplitWeakTaskList(task, weakParts)) {
    return {
      strategy: 'conjunction',
      subtasks: weakParts.map((part) => ({ subject: part.slice(0, 80), description: part })),
    };
  }

  return {
    strategy: 'atomic',
    subtasks: [{ subject: task.slice(0, 80), description: task }],
  };
}