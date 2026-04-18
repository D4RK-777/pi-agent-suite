# Styling Methodology

How to actually implement design systems — CSS Modules, vanilla CSS, responsive, animation performance.

---

## 1. Design Token Architecture

### Token Hierarchy

```
Base Tokens (CSS Custom Properties)
├── Colors: --color-blue-500, --color-gray-900
├── Spacing: --spacing-1, --spacing-2, --spacing-4
├── Typography: --font-sans, --font-mono, --text-sm, --text-base
├── Radius: --radius-sm, --radius-md, --radius-lg
└── Shadows: --shadow-sm, --shadow-md, --shadow-lg

Semantic Tokens (Purpose-driven)
├── --bg-primary, --bg-secondary, --bg-muted
├── --text-primary, --text-secondary, --text-muted
├── --border-default, --border-focus, --border-error
├── --primary, --primary-foreground
├── --destructive, --destructive-foreground
└── --ring (focus ring color)

Component Tokens (Specific)
├── --button-height, --button-padding
├── --input-border, --input-focus-ring
└── --card-shadow, --card-radius
```

### CSS Variables Setup

```css
/* styles/tokens.css — Import once in your app entry point */
:root {
  /* Base colors */
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;

  /* Semantic colors */
  --card: 0 0% 100%;
  --card-foreground: 222.2 84% 4.9%;
  --popover: 0 0% 100%;
  --popover-foreground: 222.2 84% 4.9%;
  --primary: 222.2 47.4% 11.2%;
  --primary-foreground: 210 40% 98%;
  --secondary: 210 40% 96.1%;
  --secondary-foreground: 222.2 47.4% 11.2%;
  --muted: 210 40% 96.1%;
  --muted-foreground: 215.4 16.3% 46.9%;
  --accent: 210 40% 96.1%;
  --accent-foreground: 222.2 47.4% 11.2%;
  --destructive: 0 84.2% 60.2%;
  --destructive-foreground: 210 40% 98%;
  --border: 214.3 31.8% 91.4%;
  --input: 214.3 31.8% 91.4%;
  --ring: 222.2 84% 4.9%;

  /* Spacing scale */
  --spacing-1: 0.25rem;
  --spacing-2: 0.5rem;
  --spacing-3: 0.75rem;
  --spacing-4: 1rem;
  --spacing-6: 1.5rem;
  --spacing-8: 2rem;
  --spacing-12: 3rem;

  /* Radius */
  --radius-sm: 0.25rem;
  --radius-md: 0.375rem;
  --radius-lg: 0.5rem;
  --radius-xl: 0.75rem;

  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
}

.dark {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
  --card: 222.2 84% 4.9%;
  --card-foreground: 210 40% 98%;
  --primary: 210 40% 98%;
  --primary-foreground: 222.2 47.4% 11.2%;
  --secondary: 217.2 32.6% 17.5%;
  --secondary-foreground: 210 40% 98%;
  --muted: 217.2 32.6% 17.5%;
  --muted-foreground: 215 20.2% 65.1%;
  --accent: 217.2 32.6% 17.5%;
  --accent-foreground: 210 40% 98%;
  --destructive: 0 62.8% 30.6%;
  --destructive-foreground: 210 40% 98%;
  --border: 217.2 32.6% 17.5%;
  --input: 217.2 32.6% 17.5%;
  --ring: 212.7 26.8% 83.9%;
}

/* Base reset */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: var(--font-sans, system-ui, -apple-system, sans-serif);
  background-color: hsl(var(--background));
  color: hsl(var(--foreground));
  line-height: 1.5;
}
```

### Token Discipline Rules

1. **Never hardcode colors** — always use `hsl(var(--primary))`, `var(--text-muted)`, etc.
2. **Never hardcode spacing** — use CSS variables or the spacing scale.
3. **Never hardcode radius** — use `var(--radius-md)`, `var(--radius-lg)`, etc.
4. **Dark mode is automatic** — toggle `.dark` class on `<html>`, don't write separate dark styles.
5. **One token per purpose** — `--text-muted` for secondary text, not `#6b7280`.

---

## 2. CSS Modules Pattern

### Why CSS Modules
- **Scoped by default** — no class name collisions
- **Full CSS power** — no utility class limitations
- **TypeScript support** — import styles as typed objects
- **Zero runtime overhead** — compiled at build time
- **Works with any framework** — React, Next.js, Vite, etc.

### Core Pattern

```tsx
// components/ui/button.tsx
import styles from "./button.module.css";
import { cn } from "@/lib/utils";

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "default" | "destructive" | "outline" | "secondary" | "ghost" | "link";
  size?: "default" | "sm" | "lg" | "icon";
}

export function Button({
  className,
  variant = "default",
  size = "default",
  children,
  ...props
}: ButtonProps) {
  return (
    <button
      className={cn(
        styles.button,
        styles[`button--${variant}`],
        styles[`button--${size}`],
        className
      )}
      {...props}
    >
      {children}
    </button>
  );
}
```

```css
/* components/ui/button.module.css */
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-md);
  font-size: 0.875rem;
  font-weight: 500;
  transition: background-color 0.2s, color 0.2s;
  cursor: pointer;
  border: none;
  outline: none;
}

.button:focus-visible {
  outline: 2px solid hsl(var(--ring));
  outline-offset: 2px;
}

.button:disabled {
  pointer-events: none;
  opacity: 0.5;
}

/* Variants */
.button--default {
  background-color: hsl(var(--primary));
  color: hsl(var(--primary-foreground));
}

.button--default:hover {
  background-color: hsl(var(--primary) / 0.9);
}

.button--destructive {
  background-color: hsl(var(--destructive));
  color: hsl(var(--destructive-foreground));
}

.button--destructive:hover {
  background-color: hsl(var(--destructive) / 0.9);
}

.button--outline {
  border: 1px solid hsl(var(--border));
  background-color: hsl(var(--background));
  color: hsl(var(--foreground));
}

.button--outline:hover {
  background-color: hsl(var(--accent));
  color: hsl(var(--accent-foreground));
}

.button--secondary {
  background-color: hsl(var(--secondary));
  color: hsl(var(--secondary-foreground));
}

.button--secondary:hover {
  background-color: hsl(var(--secondary) / 0.8);
}

.button--ghost {
  background-color: transparent;
  color: hsl(var(--foreground));
}

.button--ghost:hover {
  background-color: hsl(var(--accent));
  color: hsl(var(--accent-foreground));
}

.button--link {
  background-color: transparent;
  color: hsl(var(--primary));
  text-decoration: underline;
  text-underline-offset: 4px;
}

.button--link:hover {
  text-decoration: none;
}

/* Sizes */
.button--default {
  height: 2.5rem;
  padding: 0 1rem;
}

.button--sm {
  height: 2.25rem;
  padding: 0 0.75rem;
  border-radius: var(--radius-sm);
}

.button--lg {
  height: 2.75rem;
  padding: 0 2rem;
  border-radius: var(--radius-lg);
}

.button--icon {
  height: 2.5rem;
  width: 2.5rem;
}
```

### Utility Function (cn)

```ts
// lib/utils.ts
import { type ClassValue, clsx } from "clsx";

export function cn(...inputs: ClassValue[]) {
  return clsx(inputs);
}
```

### When to Extract Components

```tsx
// DON'T extract: One-off usage
<div className={styles.card}>
  <Avatar src={user.avatar} alt={user.name} />
  <span>{user.name}</span>
</div>

// DO extract: Repeated 3+ times
// components/ui/card.tsx
import styles from "./card.module.css";
import { cn } from "@/lib/utils";

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {}

export function Card({ className, children, ...props }: CardProps) {
  return (
    <div className={cn(styles.card, className)} {...props}>
      {children}
    </div>
  );
}
```

```css
/* components/ui/card.module.css */
.card {
  border-radius: var(--radius-lg);
  border: 1px solid hsl(var(--border));
  background-color: hsl(var(--card));
  color: hsl(var(--card-foreground));
  box-shadow: var(--shadow-sm);
  padding: 1.5rem;
}
```

---

## 3. Vanilla CSS Pattern (Alternative)

**When:** Simple projects, no build step needed, or you prefer global styles.

### BEM Naming Convention

```css
/* styles/components/button.css */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-md);
  font-size: 0.875rem;
  font-weight: 500;
  transition: background-color 0.2s, color 0.2s;
  cursor: pointer;
  border: none;
}

.btn--primary {
  background-color: hsl(var(--primary));
  color: hsl(var(--primary-foreground));
}

.btn--primary:hover {
  background-color: hsl(var(--primary) / 0.9);
}

.btn--sm {
  height: 2.25rem;
  padding: 0 0.75rem;
}

.btn__icon {
  width: 1rem;
  height: 1rem;
  margin-right: 0.5rem;
}
```

```tsx
// Usage
import "@/styles/components/button.css";

function MyButton() {
  return (
    <button className="btn btn--primary btn--sm">
      <span className="btn__icon">🔔</span>
      Click me
    </button>
  );
}
```

---

## 4. Responsive Breakpoint Strategy

### Mobile-First Approach

```css
/* Default = mobile, then add breakpoints upward */
.responsive-grid {
  display: grid;
  grid-template-columns: 1fr; /* mobile: 1 column */
  gap: 1rem;
}

@media (min-width: 768px) {
  .responsive-grid {
    grid-template-columns: repeat(2, 1fr); /* tablet: 2 columns */
  }
}

@media (min-width: 1024px) {
  .responsive-grid {
    grid-template-columns: repeat(3, 1fr); /* desktop: 3 columns */
  }
}

@media (min-width: 1280px) {
  .responsive-grid {
    grid-template-columns: repeat(4, 1fr); /* wide: 4 columns */
  }
}
```

### Breakpoint Guide

| Breakpoint | Width | Use For |
|---|---|---|
| Default | < 768px | Mobile, single column |
| `768px` | Tablet | 2-column layouts |
| `1024px` | Laptop | 3-column layouts |
| `1280px` | Desktop | 4-column layouts |
| `1536px` | Wide screens | Max-width containers |

### Responsive Text

```css
.responsive-heading {
  font-size: 1.5rem; /* mobile */
  font-weight: 700;
  line-height: 1.2;
}

@media (min-width: 768px) {
  .responsive-heading {
    font-size: 1.875rem; /* tablet */
  }
}

@media (min-width: 1024px) {
  .responsive-heading {
    font-size: 2.25rem; /* desktop */
  }
}
```

### Responsive Visibility

```css
/* Show on mobile, hide on desktop */
.mobile-only {
  display: block;
}

@media (min-width: 768px) {
  .mobile-only {
    display: none;
  }
}

/* Hide on mobile, show on desktop */
.desktop-only {
  display: none;
}

@media (min-width: 768px) {
  .desktop-only {
    display: block;
  }
}
```

---

## 5. Animation Performance

### GPU-Accelerated Properties

**Only animate these properties for smooth 60fps animations:**

| Property | GPU Accelerated | Why |
|---|---|---|
| `transform` | ✅ Yes | Composited, doesn't trigger layout |
| `opacity` | ✅ Yes | Composited, cheap |
| `filter` | ⚠️ Sometimes | Can cause repaint |
| `width/height` | ❌ No | Triggers layout |
| `top/left` | ❌ No | Triggers layout |
| `margin/padding` | ❌ No | Triggers layout |

### Correct Animation Pattern

```css
/* GOOD: Uses transform and opacity */
.fade-in {
  animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(0.5rem);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* BAD: Animates width/height */
.bad-expand {
  transition: height 0.3s;
  height: 0;
}

.bad-expand.open {
  height: auto; /* Doesn't animate smoothly */
}
```

### Transition Utilities

```css
.transition-colors {
  transition-property: background-color, border-color, color, fill, stroke;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 200ms;
}

.transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 300ms;
}

.hover-lift {
  transition: transform 0.2s ease-out;
}

.hover-lift:hover {
  transform: translateY(-2px);
}
```

### will-change Usage

```css
/* Use sparingly — tells browser to optimize in advance */
.will-animate-transform {
  will-change: transform;
}

/* Remove after animation completes */
/* will-change is expensive — don't leave it on permanently */
```

---

## 6. Dark Mode Implementation

### Toggle Pattern

```tsx
// components/theme-toggle.tsx
"use client";

import { useEffect, useState } from "react";

export function ThemeToggle() {
  const [theme, setTheme] = useState<"light" | "dark">("light");

  useEffect(() => {
    // Check system preference or stored preference
    const stored = localStorage.getItem("theme");
    const system = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const initial = stored || (system ? "dark" : "light");
    setTheme(initial as "light" | "dark");
    document.documentElement.classList.toggle("dark", initial === "dark");
  }, []);

  const toggle = () => {
    const next = theme === "light" ? "dark" : "light";
    setTheme(next);
    document.documentElement.classList.toggle("dark", next === "dark");
    localStorage.setItem("theme", next);
  };

  return (
    <button onClick={toggle} aria-label={`Switch to ${theme === "light" ? "dark" : "light"} mode`}>
      {theme === "light" ? "🌙" : "☀️"}
    </button>
  );
}
```

### Dark Mode CSS Strategy

```css
/* All dark mode styles use the .dark class on <html> */
.dark {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
  /* ... all semantic tokens flip */
}

/* Images that need dark mode adjustment */
.dark .logo-light { display: none; }
.dark .logo-dark { display: block; }
.logo-light { display: block; }
.logo-dark { display: none; }
```

---

## Styling Anti-Patterns

### ❌ Hardcoded Colors
```css
/* BAD */
.card {
  color: #3B82F6;
  background-color: #F3F4F6;
}

/* GOOD */
.card {
  color: hsl(var(--primary));
  background-color: hsl(var(--muted));
}
```

### ❌ Inconsistent Spacing
```css
/* BAD: Random values */
.card {
  padding: 13px;
  margin-bottom: 17px;
  gap: 7px;
}

/* GOOD: Use the scale */
.card {
  padding: var(--spacing-3);
  margin-bottom: var(--spacing-4);
  gap: var(--spacing-2);
}
```

### ❌ Magic Numbers
```css
/* BAD */
.container {
  width: 347px;
  height: 213px;
}

/* GOOD: Use responsive grid or max-width */
.container {
  width: 100%;
  max-width: 28rem;
  aspect-ratio: 16 / 9;
}
```

### ❌ Global Class Name Collisions
```css
/* BAD: Global class — might conflict with other components */
.button {
  /* ... */
}

/* GOOD: CSS Modules — scoped automatically */
/* button.module.css */
.button {
  /* ... */
}
```

---

## Styling Selection Guide

| Scenario | Best Approach |
|---|---|
| One-off component | CSS Modules |
| Reused component | CSS Modules + extract to shared file |
| Multiple variants | CSS Modules with BEM-like naming (`button--primary`) |
| Design system tokens | CSS variables + semantic naming |
| Dark mode | `.dark` class + semantic tokens |
| Animations | `transform` + `opacity` only |
| Responsive layouts | Mobile-first + media queries |
| Shared component library | CSS Modules + tokens + strict variant system |
