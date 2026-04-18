void> {
  manifest.updated_at = nowIso();
  await writeJsonFile(manifest.manifest_file, manifest);
}

async function writeInstructionsFile(contract: AutoresearchMissionContract, manifest: AutoresearchRunManifest): Promise<void> {
  const instructionContext = await buildAutoresearchInstructionContext(manifest);
  await writeFile(
    manifest.instructions_file,
    `${buildAutoresearchInstructions(contract, {
      runId: manifest.run_id,
      iteration: manifest.iteration + 1,
      baselineCommit: manifest.baseline_commit,
      lastKeptCommit: manifest.last_kept_commit,
      lastKeptScore: manifest.last_kept_score,
      resultsFile: manifest.results_file,
      candidateFile: manifest.candidate_file,
      keepPolicy: manifest.keep_policy,