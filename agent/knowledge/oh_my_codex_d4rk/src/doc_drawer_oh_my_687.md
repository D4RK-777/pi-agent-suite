'# Step 7.5 must keep ai-slop-cleaner strictly scoped to the paths listed here.',
  ].join('\n');
}

export function buildRalphAppendInstructions(
  task: string,
  options: { changedFilesPath: string; noDeslop: boolean; approvedHint?: ApprovedExecutionLaunchHint | null },
): string {
  return [
    '<ralph_native_subagents>',
    'You are in OMX Ralph persistence mode.',
    `Primary task: ${task}`,
    'Parallelism guidance:',
    '- Prefer Codex native subagents for independent parallel subtasks.',
    '- Treat `.omx/state/subagent-tracking.json` as the native subagent activity ledger for this session.',
    '- Do not declare the task complete, and do not transition into final verification/completion, while active native subagent threads are still running.',