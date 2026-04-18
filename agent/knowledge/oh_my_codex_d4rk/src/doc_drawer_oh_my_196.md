ling evaluator branch$/m);
      assert.match(results, /^3\t.+\t\t\tdiscard\tparse error branch$/m);

      const ledger = JSON.parse(await readFile(runtime.ledgerFile, 'utf-8')) as {
        entries: Array<{ decision: string; decision_reason: string }>;
      };
      assert.equal(ledger.entries[1]?.decision, 'interrupted');
      assert.equal(ledger.entries[2]?.decision, 'discard');
      assert.equal(ledger.entries[3]?.decision, 'discard');
      assert.match(ledger.entries[3]?.decision_reason || '', /evaluator error/i);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });
});