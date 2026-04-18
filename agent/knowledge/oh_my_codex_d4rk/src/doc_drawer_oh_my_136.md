description: record.description,
    notes: record.notes,
    created_at: record.created_at,
  };
}

async function readCandidateArtifact(candidateFile: string): Promise<AutoresearchCandidateArtifact> {
  if (!existsSync(candidateFile)) {
    throw new Error(`autoresearch_candidate_missing:${candidateFile}`);
  }
  return parseAutoresearchCandidateArtifact(await readFile(candidateFile, 'utf-8'));
}