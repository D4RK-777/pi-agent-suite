athPart}${teamManifestPathPart}${teamEventsPathPart}${teamDispatchPathPart}${teamPhasePathPart}${teamMonitorSnapshotPathPart}${teamSummarySnapshotPathPart} reason=${item.reason}${statePart} command=${item.command}`);
  }

  for (const [target, command] of Object.entries(paneStatus.sparkshell_commands)) {
    console.log(`inspect_${target}: ${command}`);
  }
}

function parseTeamArgs(args: string[], cwd: string = process.cwd()): ParsedTeamArgs {
  const tokens = [...args];
  let workerCount = 3;
  let agentType = 'executor';
  let explicitAgentType = false;
  let explicitWorkerCount = false;

  if (tokens[0]?.toLowerCase() === 'ralph') {
    throw new Error('Deprecated usage: `omx team ralph ...` has been removed. Use `omx team ...` or run `omx ralph ...` separately.');
  }