---
name: gloss-quality-bar
description: Use when writing, reviewing, or refactoring frontend code for the Gloss product (Next.js + React + TypeScript). Enforces the quality bar that ships.
---

# gloss-quality-bar

These rules are non-negotiable for Gloss frontend code. Violating them is a regression, not a style choice.

## Product naming (critical)

- User-facing strings say **"Gloss"**. Never "Konekt", "Glass", or anything else.
- Wings, folder names, and legacy identifiers may still say `konekt_nextjs` — those are frozen implementation details. Leave them alone.
- If you're writing a UI label, marketing copy, email template, or docstring visible to a user: it's Gloss.

## TypeScript

- **Strict mode always**. No `any` unless there's a doc comment explaining why. Prefer `unknown` + narrowing.
- No `// @ts-ignore` or `// @ts-expect-error` without a linked issue or a one-line explanation of the escape hatch.
- Types live alongside implementation. Don't invent a `types/` megafile.
- Prefer discriminated unions over optional properties for state machines.

## Accessibility (WCAG 2.2 AA minimum)

- Every interactive element must be keyboard-reachable and have a visible focus ring.
- Every form control needs an accessible label. `placeholder` is not a label.
- Contrast: 4.5:1 for body text, 3:1 for large text and UI components.
- ARIA only when native semantics aren't enough. `<button>` beats `<div role="button">` every time.
- Modals: focus trap, ESC to close, focus returns to trigger on close. Use Radix Dialog or equivalent — don't roll your own.

## Design tokens

- Hardcoded hex values are a bug. Colors come from the token system.
- Same for spacing, radii, shadows, motion. If you're typing `padding: 16px`, you're almost certainly wrong — use the spacing token.
- Dark mode works because of tokens. Break the tokens → break dark mode.

## Banned

- **Inter font.** Pick another sans-serif from the token system.
- **Purple gradients.** The product's visual identity is not purple-gradient era.
- Icon libraries other than the project's chosen set (Phosphor for Gloss).

## Testing floor

Before declaring a UI change "done":
- Start the dev server and click through the feature in a browser.
- Test keyboard-only navigation.
- Test with the system color scheme toggled (dark ↔ light).
- Check at least 320px width (mobile) and 1440px+ (desktop).

If you can't test in a browser, **say so explicitly** in your reply. Don't claim the UI works when you haven't looked at it.

## Red flags in review

- `useEffect` fetching data (use a real data layer — React Query, server components, or a framework primitive).
- Component files over ~300 lines without a clear reason.
- Inline styles mixed with Tailwind/token classes.
- Props named `data` or `children` carrying anything more complex than text/nodes.
- State stored in a URL query param that isn't user-meaningful.

## When you're not sure

Check `OmegaD4rkMynd/patterns/` and `OmegaD4rkMynd/decisions/` via `obsidian_search` — patterns that have survived review are stored there. If a pattern exists, follow it; if it doesn't, follow this skill and suggest the user add it.
