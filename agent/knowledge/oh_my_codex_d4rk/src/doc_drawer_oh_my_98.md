parsed.schema_version : 1,
    run_id: parsed.run_id,
    created_at: parsed.created_at || nowIso(),
    updated_at: nowIso(),
    entries,
  });
}

async function readAutoresearchLedgerEntries(ledgerFile: string): Promise<AutoresearchLedgerEntry[]> {
  if (!existsSync(ledgerFile)) return [];
  const parsed = await readJsonFile<{ entries?: AutoresearchLedgerEntry[] }>(ledgerFile);
  return Array.isArray(parsed.entries) ? parsed.entries : [];
}