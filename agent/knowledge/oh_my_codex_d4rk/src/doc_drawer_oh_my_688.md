sition into final verification/completion, while active native subagent threads are still running.',
    '- Before closing a verification wave, confirm that active native subagent threads have drained.',
    ...buildRalphApprovedContextLines(options.approvedHint ?? null),
    'Final deslop guidance:',
    options.noDeslop
      ? '- `--no-deslop` is active for this Ralph run, so skip the mandatory ai-slop-cleaner final pass and use the latest successful pre-deslop verification evidence.'
      : `- Step 7.5 must run oh-my-codex:ai-slop-cleaner in standard mode on changed files only, using the repo-relative paths listed in \`${options.changedFilesPath}\`.`,
    options.noDeslop
      ? '- Do not run ai-slop-cleaner unless the user explicitly re-enables the deslop pass.'