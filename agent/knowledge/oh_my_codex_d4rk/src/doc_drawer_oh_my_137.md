eFile}`);
  }
  return parseAutoresearchCandidateArtifact(await readFile(candidateFile, 'utf-8'));
}

async function finalizeRun(
  manifest: AutoresearchRunManifest,
  projectRoot: string,
  updates: { status: AutoresearchRunStatus; stopReason: string },
): Promise<void> {
  manifest.status = updates.status;
  manifest.stop_reason = updates.stopReason;
  manifest.completed_at = nowIso();
  await writeRunManifest(manifest);
  await updateModeState('autoresearch', {
    active: false,
    current_phase: updates.status,
    completed_at: manifest.completed_at,
    stop_reason: updates.stopReason,
  }, projectRoot);
  await deactivateAutoresearchRun(manifest);
}