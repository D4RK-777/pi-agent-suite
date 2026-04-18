Steps>

<Output_Contract>
After each verification pass, emit a **composite web-clone verdict** JSON:

```json
{
  "visual": {
    "score": 0,
    "verdict": "revise",
    "category_match": false,
    "differences": ["..."],
    "suggestions": ["..."],
    "reasoning": "short explanation"
  },
  "functional": {
    "tested": 0,
    "passed": 0,
    "failures": ["..."]
  },
  "structure": {
    "landmark_match": false,
    "missing": ["..."],
    "extra": ["..."]
  },
  "overall_verdict": "revise",
  "priority_fixes": ["..."]
}
```