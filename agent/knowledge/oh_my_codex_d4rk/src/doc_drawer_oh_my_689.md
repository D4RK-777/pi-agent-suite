Deslop
      ? '- Do not run ai-slop-cleaner unless the user explicitly re-enables the deslop pass.'
      : '- Keep the cleaner scope bounded to that file list; do not widen the pass to the full codebase or unrelated files.',
    options.noDeslop
      ? '- Step 7.6 stays satisfied by the latest successful pre-deslop verification evidence because this run opted out of the deslop pass.'
      : '- Step 7.6 must rerun the current tests/build/lint verification after ai-slop-cleaner; if regression fails, roll back cleaner changes or fix and retry before completion.',
    '</ralph_native_subagents>',
  ].join('\n');
}