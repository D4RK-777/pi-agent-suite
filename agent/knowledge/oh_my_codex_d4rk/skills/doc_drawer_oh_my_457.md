Adapt to `tech_stack` if specified (React components, Vue SFCs, etc.).

## Pass 3 — Generate Clone

Implement the clone from the plan. Work component-by-component.

1. **Scaffold**: Create the directory structure and base files.
2. **Design tokens first**: Implement CSS custom properties or Tailwind config from extracted tokens.
3. **Layout shell**: Build the page-level layout matching the original's flexbox/grid structure.
4. **Components**: Implement each region top-down:
   - Match DOM structure from extraction (semantic tags, landmark roles)
   - Apply computed styles — prioritize layout properties, then typography, then decorative
   - Use actual extracted text content; use placeholder `<img>` for external images
5. **Interactions**: Wire up detected behaviors: