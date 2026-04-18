ter search on a deterministic tabular classification benchmark with a score-improvement keep policy.

### 3. Noisy high-dimensional Bayes-opt demo
- Demo code: `playground/bayesopt_highdim_demo/`
- Mission: `missions/noisy-bayesopt-highdim/`
- Evaluator: `scripts/eval-noisy-bayesopt-highdim.py`
- What it demonstrates: a harder black-box optimization task with noise, limited evaluation budget, and curse-of-dimensionality pressure. The successful autoresearch run switched from random search to a subspace-aware fixed-kernel GP with denoised incumbent selection.