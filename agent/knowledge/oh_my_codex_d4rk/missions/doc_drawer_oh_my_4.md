ersal.js
node scripts/eval-in-action-cat-shellout-demo.js
```

To see a real end-to-end run, launch:

```bash
omx autoresearch missions/in-action-cat-shellout-demo
```

Then inspect `.omx/logs/autoresearch/<run-id>/manifest.json`, `candidate.json`, and `iteration-ledger.json` to see the supervisor's keep/discard/stop decisions.

These bundles are designed to be first-class `omx autoresearch` missions rather than generic prose examples.