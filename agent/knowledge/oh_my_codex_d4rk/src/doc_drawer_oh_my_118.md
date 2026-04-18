iagnostic.
  }

  return {
    ...contract,
    missionDir,
    missionFile,
    sandboxFile,
  };
}

export async function loadAutoresearchRunManifest(projectRoot: string, runId: string): Promise<AutoresearchRunManifest> {
  const manifestFile = join(projectRoot, '.omx', 'logs', 'autoresearch', runId, 'manifest.json');
  if (!existsSync(manifestFile)) {
    throw new Error(`autoresearch_resume_manifest_missing:${runId}`);
  }
  return readJsonFile<AutoresearchRunManifest>(manifestFile);
}

async function writeRunManifest(manifest: AutoresearchRunManifest): Promise<void> {
  manifest.updated_at = nowIso();
  await writeJsonFile(manifest.manifest_file, manifest);
}