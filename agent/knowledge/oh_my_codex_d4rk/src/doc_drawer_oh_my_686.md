filtered;
}

interface RalphSessionFiles {
  instructionsPath: string;
  changedFilesPath: string;
}

export function buildRalphChangedFilesSeedContents(): string {
  return [
    '# Ralph changed files for the mandatory final ai-slop-cleaner pass',
    '# Add one repo-relative path per line as Ralph edits files during the session.',
    '# Step 7.5 must keep ai-slop-cleaner strictly scoped to the paths listed here.',
  ].join('\n');
}