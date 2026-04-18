---
name: visual-verdict
description: Structured visual QA verdict for screenshot-to-reference comparisons
---

<Purpose>
Use this skill to compare generated UI screenshots against one or more reference images and return a strict JSON verdict that can drive the next edit iteration.
</Purpose>

<Use_When>
- The task includes visual fidelity requirements (layout, spacing, typography, component styling)
- You have a generated screenshot and at least one reference image
- You need deterministic pass/fail guidance before continuing edits
</Use_When>

<Inputs>
- `reference_images[]` (one or more image paths)
- `generated_screenshot` (current output image)
- Optional: `category_hint` (e.g., `hackernews`, `sns-feed`, `dashboard`)
</Inputs>