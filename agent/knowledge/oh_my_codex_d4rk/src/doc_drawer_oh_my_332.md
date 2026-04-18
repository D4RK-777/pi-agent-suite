}/mission.md`',
    '- `autoresearch-{slug}/sandbox.md`',
    '- `autoresearch-{slug}/result.json`',
    'Use the contract and helper functions in `src/cli/autoresearch-intake.ts` for the artifact shape.',
    'If the evaluator command still contains placeholders or the user has not confirmed launch, keep refining instead of finalizing launch-ready output.',
    '',
    'Seed inputs:',
    ...seedLines,
  ].join('\n');
}

export async function materializeAutoresearchDeepInterviewResult(
  result: AutoresearchDeepInterviewResult,
): Promise<InitAutoresearchResult> {
  ensureLaunchReadyEvaluator(result.compileTarget.evaluatorCommand);
  return initAutoresearchMission(result.compileTarget);
}