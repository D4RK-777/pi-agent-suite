unt: persistedWorkerCount,
      explicitWorkerCount: true,
      agentType: approvedHint.agentType,
      explicitAgentType: approvedHint.agentType != null,
    };
  }

  return {
    task: approvedHint.task,
    workerCount: approvedHint.workerCount ?? 3,
    explicitWorkerCount: approvedHint.workerCount != null,
    agentType: approvedHint.agentType,
    explicitAgentType: approvedHint.agentType != null,
  };
}