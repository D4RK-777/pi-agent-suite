h(es) across ${report.matched_sessions} session(s) in ${report.searched_files} transcript(s).`,
  ];

  for (const result of report.results) {
    lines.push('');
    lines.push(`session: ${result.session_id}`);
    lines.push(`time: ${result.timestamp ?? 'unknown'}`);
    lines.push(`cwd: ${result.cwd ?? 'unknown'}`);
    lines.push(`source: ${result.transcript_path}:${result.line_number} (${result.record_type})`);
    lines.push(`snippet: ${result.snippet}`);
  }

  return lines.join('\n');
}

export async function sessionCommand(args: string[]): Promise<void> {
  const subcommand = args[0];
  if (!subcommand || HELP_TOKENS.has(subcommand)) {
    console.log(HELP.trim());
    return;
  }