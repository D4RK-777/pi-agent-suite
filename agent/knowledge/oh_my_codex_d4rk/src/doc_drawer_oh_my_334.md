sion directory already exists: ${missionDir}`);
  }

  await mkdir(missionDir, { recursive: true });

  const missionContent = buildMissionContent(opts.topic);
  const sandboxContent = buildSandboxContent(opts.evaluatorCommand, opts.keepPolicy);

  parseSandboxContract(sandboxContent);

  await writeFile(join(missionDir, 'mission.md'), missionContent, 'utf-8');
  await writeFile(join(missionDir, 'sandbox.md'), sandboxContent, 'utf-8');

  return { missionDir, slug: opts.slug };
}