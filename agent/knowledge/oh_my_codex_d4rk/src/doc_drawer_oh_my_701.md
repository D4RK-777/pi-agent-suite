').trim();
  if (options.query === '') {
    throw new Error(`Missing search query.\n${HELP}`);
  }

  return { options, json };
}

function formatReport(report: SessionSearchReport): string {
  if (report.results.length === 0) {
    return `No session history matches for "${report.query}". Searched ${report.searched_files} transcript(s).`;
  }

  const lines = [
    `Found ${report.results.length} match(es) across ${report.matched_sessions} session(s) in ${report.searched_files} transcript(s).`,
  ];