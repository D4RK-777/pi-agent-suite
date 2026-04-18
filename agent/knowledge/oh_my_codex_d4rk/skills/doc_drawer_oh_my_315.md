---
name: review
description: Reviewer-only pass for /plan --review and cleanup artifact review
---

# Review (Reviewer-Only Pass)

Review is a shorthand alias for `/plan --review`. It triggers Critic evaluation of an existing plan and is intended to preserve writer/reviewer separation.

## Usage

```
/review
/review "path/to/plan.md"
```

## Behavior

This skill invokes the Plan skill in review mode:

```
/plan --review <arguments>
```