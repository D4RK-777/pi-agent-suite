nifest(manifest);
    await writeInstructionsFile(contract, manifest);
    return 'interrupted';
  }

  await recordAutoresearchIteration(manifest, {
    status: 'noop',
    decisionReason: 'candidate reported noop',
    ...sharedEntry,
  });
  await writeRunManifest(manifest);
  await writeInstructionsFile(contract, manifest);
  return 'noop';
}

export async function processAutoresearchCandidate(
  contract: AutoresearchMissionContract,
  manifest: AutoresearchRunManifest,
  projectRoot: string,
): Promise<AutoresearchDecisionStatus> {
  manifest.iteration += 1;
  let candidate: AutoresearchCandidateArtifact;
  try {
    candidate = await readCandidateArtifact(manifest.candidate_file);
  } catch (error) {
    return failAutoresearchIteration(
      manifest,
      projectRoot,