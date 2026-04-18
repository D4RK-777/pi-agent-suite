["..."],
    "extra": ["..."]
  },
  "overall_verdict": "revise",
  "priority_fixes": ["..."]
}
```

Rules:
- `visual` follows the `VisualVerdict` shape from `$visual-verdict`
- `functional.tested/passed` are counts; `failures` list specific interaction failures
- `structure.landmark_match` is `true` when all major HTML landmarks (nav, main, footer, forms) are present
- `overall_verdict`: `pass` when visual.score >= 85 AND functional.failures is empty AND structure.landmark_match is true
- `priority_fixes`: ordered by impact, drives the next iteration
</Output_Contract>