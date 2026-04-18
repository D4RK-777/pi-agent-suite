esearchLedgerEntry[] }>(ledgerFile);
  return Array.isArray(parsed.entries) ? parsed.entries : [];
}

export async function countTrailingAutoresearchNoops(ledgerFile: string): Promise<number> {
  const entries = await readAutoresearchLedgerEntries(ledgerFile);
  let count = 0;
  for (let index = entries.length - 1; index >= 0; index -= 1) {
    const entry = entries[index];
    if (!entry || entry.kind !== 'iteration' || entry.decision !== 'noop') break;
    count += 1;
  }
  return count;
}