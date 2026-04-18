[]): void {
  if (agents.length === 0) {
    console.log('No native agents found.');
    return;
  }

  const rows = [
    ['scope', 'name', 'model', 'description'],
    ...agents.map((agent) => [
      agent.scope,
      agent.name,
      agent.model ?? '-',
      agent.description || '-',
    ]),
  ];
  const widths = rows[0]!.map((_, column) => Math.max(...rows.map((row) => row[column]!.length)));

  for (const row of rows) {
    console.log(row.map((cell, column) => cell.padEnd(widths[column]!)).join('  '));
  }
}

export async function agentsCommand(args: string[]): Promise<void> {
  if (args.length === 0 || args.includes('--help') || args.includes('-h')) {
    console.log(AGENTS_USAGE);
    return;
  }