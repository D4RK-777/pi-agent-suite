at: entry.createdAt ?? nowIso(),
    notes: entry.notes,
    description: entry.description,
  });
}

async function appendAutoresearchLedgerEntry(ledgerFile: string, entry: AutoresearchLedgerEntry): Promise<void> {
  const parsed = existsSync(ledgerFile)
    ? await readJsonFile<{
      schema_version?: number;
      run_id?: string;
      created_at?: string;
      updated_at?: string;
      entries?: AutoresearchLedgerEntry[];
    }>(ledgerFile)
    : { schema_version: 1, entries: [] };
  const entries = Array.isArray(parsed.entries) ? parsed.entries : [];
  entries.push(entry);
  await writeJsonFile(ledgerFile, {
    schema_version: typeof parsed.schema_version === 'number' ? parsed.schema_version : 1,
    run_id: parsed.run_id,
    created_at: parsed.created_at || nowIso(),