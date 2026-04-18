nt output image)
- Optional: `category_hint` (e.g., `hackernews`, `sns-feed`, `dashboard`)
</Inputs>

<Output_Contract>
Return **JSON only** with this exact shape:

```json
{
  "score": 0,
  "verdict": "revise",
  "category_match": false,
  "differences": ["..."],
  "suggestions": ["..."],
  "reasoning": "short explanation"
}
```

Rules:
- `score`: integer 0-100
- `verdict`: short status (`pass`, `revise`, or `fail`)
- `category_match`: `true` when the generated screenshot matches the intended UI category/style
- `differences[]`: concrete visual mismatches (layout, spacing, typography, colors, hierarchy)
- `suggestions[]`: actionable next edits tied to the differences
- `reasoning`: 1-2 sentence summary