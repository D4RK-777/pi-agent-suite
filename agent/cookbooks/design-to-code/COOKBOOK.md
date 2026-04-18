# Design to Code

## Purpose

Translate design intent into production code with minimal drift. This cookbook is the step-by-step process for going from a Figma file, screenshot, or design reference to a shipped component.

## Use When

- Implementing from Figma files, screenshots, or reference mocks
- Translating a design system into code
- Building a new page or feature from visual specs

## Prerequisites

Read these skills before starting:
- `skills/frontend-engineering/SKILL.md` — component patterns, styling, TypeScript
- `skills/frontend-quality/SKILL.md` — accessibility and responsive checks
- `skills/gsap/SKILL.md` — if the design includes animation

## Steps

### 1. Inventory the Design

Before writing any code:

- Identify every unique element: typography variants, colors, spacing values, icons, images
- Map each element to existing design tokens — note any NEW tokens needed
- Count breakpoints shown (mobile, tablet, desktop)
- Identify interactive states: hover, focus, active, disabled, loading, empty, error
- Identify animations or transitions implied by the design
- Note any accessibility requirements (focus order, aria labels, contrast)

### 2. Decompose into Components

Break the design into a component tree:

```
Page
├── Header (existing shared component?)
├── HeroSection
│   ├── HeroHeading (typography + animation)
│   └── HeroCTA (button variant)
├── FeatureGrid
│   └── FeatureCard (repeated 3x — shared primitive)
├── TestimonialCarousel
│   └── TestimonialSlide
└── Footer (existing shared component?)
```

**Decision rules:**
- Used 3+ times across the app? → Shared component in `src/components/`
- Used only in this feature? → Feature component in `src/features/<name>/components/`
- Already exists in the codebase? → Reuse, don't recreate
- Is it a layout container? → Use existing primitives (Box, Stack, Grid)

### 3. Define the Data Shape

Before building UI, define what data each component needs:

```tsx
interface FeatureCardProps {
  title: string;
  description: string;
  icon: ReactNode;
  href: string;
}
```

Decide where data comes from:
- Static content? → Hardcode or pull from CMS
- Dynamic? → Server Component fetch or client-side SWR
- User-specific? → Client component with auth context

### 4. Build Structure First

Implement the component tree with semantic HTML and correct layout. NO styling yet:

```tsx
export function FeatureGrid({ features }: { features: Feature[] }) {
  return (
    <section aria-label="Features">
      <h2>Our Features</h2>
      <div>
        {features.map((f) => (
          <article key={f.id}>
            <h3>{f.title}</h3>
            <p>{f.description}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
```

### 5. Apply Styling with Tokens

Add styling using the project's token system. Match the design pixel-for-pixel:

```tsx
<Box
  component="section"
  aria-label="Features"
  sx={{
    py: tokens.space.xxl,
    px: tokens.space.lg,
  }}
>
  <Typography variant="h2" sx={{ mb: tokens.space.lg }}>
    Our Features
  </Typography>
  <Box
    sx={{
      display: 'grid',
      gridTemplateColumns: { xs: '1fr', md: '1fr 1fr 1fr' },
      gap: tokens.space.lg,
    }}
  >
    {features.map((f) => (
      <FeatureCard key={f.id} {...f} />
    ))}
  </Box>
</Box>
```

### 6. Add Interactivity and Animation

Layer in hover states, transitions, and scroll animations AFTER the static layout is correct:

- Hover/focus states on interactive elements
- Page-load animations (fade-in, stagger)
- Scroll-triggered animations (use GSAP skill patterns)
- Transition animations for state changes

### 7. Responsive Verification

Test at every breakpoint (320px, 375px, 768px, 1024px, 1440px, 1920px+):

- Does the layout adapt correctly?
- Are touch targets 44px+ on mobile?
- Does text remain readable?
- Are images responsive (no overflow, correct aspect ratio)?
- Does the navigation switch appropriately?

### 8. Accessibility Verification

- Tab through the entire component — is focus order logical?
- Are all interactive elements keyboard-accessible?
- Do images have alt text?
- Is contrast 4.5:1 for text, 3:1 for large text?
- Are dynamic changes announced to screen readers?

### 9. Document Deviations

If you intentionally deviate from the design (technical constraint, accessibility improvement, performance tradeoff), document it:

```
DEVIATION: Design shows 4-column grid at 768px.
IMPLEMENTATION: 2-column at 768px, 4-column at 1024px.
REASON: 4 columns at 768px makes cards too narrow for readable text.
```

## Output

- Implemented components following the project's architecture
- Token-driven styling matching the design
- Responsive behavior verified at all breakpoints
- Accessibility verified against WCAG 2.1 AA
- List of any intentional deviations with reasoning
