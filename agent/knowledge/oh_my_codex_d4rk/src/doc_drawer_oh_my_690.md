ner changes or fix and retry before completion.',
    '</ralph_native_subagents>',
  ].join('\n');
}

async function writeRalphSessionFiles(
  cwd: string,
  task: string,
  options: { noDeslop: boolean; approvedHint?: ApprovedExecutionLaunchHint | null },
): Promise<RalphSessionFiles> {
  const dir = join(cwd, '.omx', 'ralph');
  await mkdir(dir, { recursive: true });
  const instructionsPath = join(dir, 'session-instructions.md');
  const changedFilesPath = join(dir, 'changed-files.txt');
  await writeFile(changedFilesPath, `${buildRalphChangedFilesSeedContents()}\n`);
  await writeFile(
    instructionsPath,
    `${buildRalphAppendInstructions(task, { changedFilesPath: '.omx/ralph/changed-files.txt', noDeslop: options.noDeslop, approvedHint: options.approvedHint ?? null })}\n`,
  );