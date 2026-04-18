---
name: ralph-init
description: Initialize a PRD (Product Requirements Document) for structured ralph-loop execution
---

# Ralph Init

Initialize a PRD (Product Requirements Document) for structured ralph-loop execution. Creates a structured requirements document that Ralph can use for goal-driven iteration.

## Usage

```
/ralph-init "project or feature description"
```

## Behavior

1. **Gather requirements** via interactive interview or from the provided description
2. **Create PRD** at `.omx/plans/prd-{slug}.md` with:
   - Problem statement
   - Goals and non-goals
   - Acceptance criteria (testable)
   - Technical constraints
   - Implementation phases
3. **Link to Ralph** so that `/ralph` can use the PRD as its completion criteria