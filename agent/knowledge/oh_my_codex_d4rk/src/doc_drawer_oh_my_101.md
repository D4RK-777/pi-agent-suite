' ? entry.evaluator.score : null,
      description: trimContent(entry.description, 120),
    }));
}

async function buildAutoresearchInstructionContext(manifest: AutoresearchRunManifest): Promise<{
  previousIterationOutcome: string | null;
  recentLedgerSummary: AutoresearchInstructionLedgerSummary[];
}> {
  const entries = await readAutoresearchLedgerEntries(manifest.ledger_file);
  const previous = entries.at(-1);
  return {
    previousIterationOutcome: previous
      ? `${previous.decision}:${trimContent(previous.decision_reason, 160)}`
      : null,
    recentLedgerSummary: formatAutoresearchInstructionSummary(entries),
  };
}