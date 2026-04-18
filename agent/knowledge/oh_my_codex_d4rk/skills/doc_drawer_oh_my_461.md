Use `browser_click` and `browser_snapshot` to verify state changes.

5. **Emit composite verdict**:

```json
{
  "visual": {
    "score": 82,
    "verdict": "revise",
    "category_match": true,
    "differences": ["Header spacing tighter than original"],
    "suggestions": ["Increase nav gap to 24px"]
  },
  "functional": {
    "tested": 3,
    "passed": 2,
    "failures": ["Dropdown does not open on click"]
  },
  "structure": {
    "landmark_match": true,
    "missing": [],
    "extra": []
  },
  "overall_verdict": "revise",
  "priority_fixes": [
    "Fix dropdown toggle interaction",
    "Increase header nav spacing"
  ]
}
```

## Pass 5 — Iterate

Fix highest-impact issues and re-verify.