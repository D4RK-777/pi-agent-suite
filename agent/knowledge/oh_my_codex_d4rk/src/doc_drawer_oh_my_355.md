topic = input.topic.trim();
  if (!topic) {
    throw new Error('Research topic is required.');
  }

  const slug = slugifyMissionName(input.slug?.trim() || topic);
  const evaluatorCommand = (input.evaluatorCommand?.trim() || defaultDraftEvaluator(topic)).replace(/[\r\n]+/g, ' ').trim();
  const compileTarget: AutoresearchDraftCompileTarget = {
    topic,
    evaluatorCommand,
    keepPolicy: input.keepPolicy,
    slug,
    repoRoot: input.repoRoot,
  };

  const blockedReasons: string[] = [];
  if (!isLaunchReadyEvaluatorCommand(evaluatorCommand)) {
    blockedReasons.push('Evaluator command is still a placeholder/template and must be replaced before launch.');
  }