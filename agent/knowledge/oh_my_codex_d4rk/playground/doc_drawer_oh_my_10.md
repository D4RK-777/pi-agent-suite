the showcase

Example:

```bash
omx autoresearch missions/noisy-bayesopt-highdim
```

Then inspect:

```bash
RUN_ID=$(find .omx/logs/autoresearch -maxdepth 1 -mindepth 1 -type d -printf '%f\n' | sort | tail -n 1)
cat .omx/logs/autoresearch/$RUN_ID/manifest.json
cat .omx/logs/autoresearch/$RUN_ID/candidate.json
cat .omx/logs/autoresearch/$RUN_ID/iteration-ledger.json
```

You can also run evaluators directly without the supervisor:

```bash
node scripts/eval-in-action-cat-shellout-demo.js
python3 scripts/eval-ml-kaggle-model-optimization.py
python3 scripts/eval-noisy-bayesopt-highdim.py
python3 scripts/eval-noisy-latent-subspace-discovery.py
python3 scripts/eval-adaptive-sort-optimization.py
```

## Repository hygiene

These showcases are meant to stay lightweight.