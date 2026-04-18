`omx team ralph ...` has been removed. Use `omx team ...` or run `omx ralph ...` separately.');
  }

  const first = tokens[0] || '';
  const match = first.match(/^(\d+)(?::([a-z][a-z0-9-]*))?$/i);
  if (match) {
    const count = Number.parseInt(match[1], 10);
    if (!Number.isFinite(count) || count < MIN_WORKER_COUNT || count > DEFAULT_MAX_WORKERS) {
      throw new Error(`Invalid worker count "${match[1]}". Expected ${MIN_WORKER_COUNT}-${DEFAULT_MAX_WORKERS}.`);
    }
    workerCount = count;
    explicitWorkerCount = true;
    if (match[2]) {
      agentType = match[2];
      explicitAgentType = true;
    }
    tokens.shift();
  }

  const task = tokens.join(' ').trim();
  if (!task) {
    throw new Error('Usage: omx team [N:agent-type] "<task description>"');
  }