nsureParentDir(resultsFile);
  await writeFile(resultsFile, AUTORESEARCH_RESULTS_HEADER, 'utf-8');
}

async function appendAutoresearchResultsRow(
  resultsFile: string,
  row: {
    iteration: number;
    commit: string;
    pass?: boolean;
    score?: number | null;
    status: AutoresearchDecisionStatus;
    description: string;
  },
): Promise<void> {
  const existing = existsSync(resultsFile)
    ? await readFile(resultsFile, 'utf-8')
    : AUTORESEARCH_RESULTS_HEADER;
  await writeFile(
    resultsFile,
    `${existing}${row.iteration}\t${row.commit}\t${resultPassValue(row.pass)}\t${resultScoreValue(row.score)}\t${row.status}\t${row.description}\n`,
    'utf-8',
  );
}