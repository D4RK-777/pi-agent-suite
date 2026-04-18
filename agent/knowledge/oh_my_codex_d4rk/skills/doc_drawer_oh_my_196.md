---
name: ecomode
description: Token-efficient model routing modifier
---

# Ecomode Skill

Token-efficient model routing. This is a **MODIFIER**, not a standalone execution mode.

## What Ecomode Does

Overrides default model selection to prefer cheaper tiers:

| Default Tier | Ecomode Override |
|--------------|------------------|
| THOROUGH | STANDARD, THOROUGH only if essential |
| STANDARD | LOW first, STANDARD if needed |
| LOW | LOW - no change |

## What Ecomode Does NOT Do

- **Persistence**: Use `ralph` for "don't stop until done"
- **Parallel Execution**: Use `ultrawork` for parallel agents
- **Delegation Enforcement**: Always active via core orchestration

## Combining Ecomode with Other Modes

Ecomode is a modifier that combines with execution modes: