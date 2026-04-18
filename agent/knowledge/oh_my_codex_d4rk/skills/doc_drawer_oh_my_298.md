changes, production incidents, compliance/PII, public API breakage).

## Usage with interactive mode

```
$ralplan --interactive "task description"
```

## Behavior

## GPT-5.4 Guidance Alignment

- Default to concise, evidence-dense progress and completion reporting unless the user or risk level requires more detail.
- Treat newer user task updates as local overrides for the active workflow branch while preserving earlier non-conflicting constraints.
- If correctness depends on additional inspection, retrieval, execution, or verification, keep using the relevant tools until the consensus-planning flow is grounded.
- Right-size implementation steps and PRD story counts to the actual scope; do not default to exactly five steps when the task is clearly smaller or larger.