else root scope)
3. Parse the task (everything after `--prd` flag)
4. Break down into user stories:

```json
{
  "project": "[Project Name]",
  "branchName": "ralph/[feature-name]",
  "description": "[Feature description]",
  "userStories": [
    {
      "id": "US-001",
      "title": "[Short title]",
      "description": "As a [user], I want to [action] so that [benefit].",
      "acceptanceCriteria": ["Criterion 1", "Typecheck passes"],
      "priority": 1,
      "passes": false
    }
  ]
}
```

5. Initialize canonical progress ledger at `.omx/state/{scope}/ralph-progress.json`
6. Guidelines: right-sized stories (one session each), verifiable criteria, independent stories, priority order (foundational work first)
7. Proceed to normal ralph loop using user stories as the task list