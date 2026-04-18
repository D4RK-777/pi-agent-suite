return 'refine';
  }
  throw new Error('Please choose either "launch" or "refine further".');
}

function ensureLaunchReadyEvaluator(command: string): void {
  if (!isLaunchReadyEvaluatorCommand(command)) {
    throw new Error('Evaluator command is still a placeholder/template. Refine further before launch.');
  }
}

export function buildAutoresearchDeepInterviewPrompt(
  seedInputs: AutoresearchSeedInputs = {},
): string {
  const seedLines = [
    `- topic: ${seedInputs.topic?.trim() || '(none)'}`,
    `- evaluator: ${seedInputs.evaluatorCommand?.trim() || '(none)'}`,
    `- keep_policy: ${seedInputs.keepPolicy || '(none)'}`,
    `- slug: ${seedInputs.slug?.trim() || '(none)'}`,
  ];