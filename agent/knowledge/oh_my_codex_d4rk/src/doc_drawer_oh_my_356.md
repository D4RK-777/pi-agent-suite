s.push('Evaluator command is still a placeholder/template and must be replaced before launch.');
  }

  if (blockedReasons.length === 0) {
    parseSandboxContract(buildSandboxContent(evaluatorCommand, input.keepPolicy));
  }

  const launchReady = blockedReasons.length === 0;
  const specsDir = join(input.repoRoot, '.omx', 'specs');
  await mkdir(specsDir, { recursive: true });
  const path = buildDraftArtifactPath(input.repoRoot, slug);
  const content = buildAutoresearchDraftArtifactContent(compileTarget, input.seedInputs || {}, launchReady, blockedReasons);
  await writeFile(path, content, 'utf-8');

  return { compileTarget, path, content, launchReady, blockedReasons };
}