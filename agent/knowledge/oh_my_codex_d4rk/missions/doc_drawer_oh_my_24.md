---
evaluator:
  command: PYTHONDONTWRITEBYTECODE=1 python3 scripts/eval-noisy-latent-subspace-discovery.py
  format: json
  keep_policy: score_improvement
---
Stay tightly scoped to `playground/bayesopt_latent_discovery_demo/`.

Allowed changes:
- search strategy
- screening / structure-discovery logic
- acquisition logic
- search hyperparameters and config
- small structural refactors in the demo if they directly support optimization

Avoid:
- unrelated repository edits
- adding new Python dependencies
- increasing the evaluation budget just to win the score