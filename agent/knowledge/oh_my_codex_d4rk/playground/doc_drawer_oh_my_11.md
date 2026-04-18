tive-sort-optimization.py
```

## Repository hygiene

These showcases are meant to stay lightweight.

Please avoid committing:
- downloaded datasets
- large model artifacts
- benchmark output dumps
- generated caches like `__pycache__/`
- runtime autoresearch logs under `.omx/logs/`

Keep research state in code, configs, missions, and evaluator scripts; keep bulky runtime outputs local.