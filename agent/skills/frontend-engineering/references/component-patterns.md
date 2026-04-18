# Component Patterns

Concrete, production-ready patterns for the 12 most common UI components.

Use these as starting points. Adapt to your project's token system, styling approach, and component library.

---

## 1. Data Table

**When:** Displaying tabular data with sorting, filtering, pagination, and row selection.

### Core Pattern

```tsx
// components/ui/data-table.tsx
"use client";

import { useState, useMemo, useCallback } from "react";
import {
  ColumnDef,
  flexRender,
  getCoreRowModel,
  getSortedRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  useReactTable,
  SortingState,
  ColumnFiltersState,
  RowSelectionState,
} from "@tanstack/react-table";

interface DataTableProps<TData> {
  columns: ColumnDef<TData>[];
  data: TData[];
  searchColumn?: string;
  searchPlaceholder?: string;
  pageSize?: number;
  onRowSelect?: (rows: TData[]) => void;
  isLoading?: boolean;
}

export function DataTable<TData>({
  columns,
  data,
  searchColumn,
  searchPlaceholder = "Search...",
  pageSize = 10,
  onRowSelect,
  isLoading,
}: DataTableProps<TData>) {
  const [sorting, setSorting] = useState<SortingState>([]);
  const [columnFilters, setColumnFilters] = useState<ColumnFiltersState>([]);
  const [rowSelection, setRowSelection] = useState<RowSelectionState>({});
  const [globalFilter, setGlobalFilter] = useState("");

  const table = useReactTable({
    data,
    columns,
    state: { sorting, columnFilters, rowSelection, globalFilter },
    onSortingChange: setSorting,
    onColumnFiltersChange: setColumnFilters,
    onRowSelectionChange: setRowSelection,
    onGlobalFilterChange: setGlobalFilter,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    initialState: { pagination: { pageSize } },
  });

  const selectedRows = table.getSelectedRowModel().rows.map((r) => r.original);

  return (
    <div className={styles.stack}>
      {/* Toolbar */}
      <div className={styles.gap}>
        {searchColumn && (
          <input
            type="text"
            placeholder={searchPlaceholder}
            value={globalFilter}
            onChange={(e) => setGlobalFilter(e.target.value)}
            className={styles.paddingX}
          />
        )}
        {selectedRows.length > 0 && (
          <span className={styles.text}>
            {selectedRows.length} row(s) selected
          </span>
        )}
      </div>

      {/* Table */}
      <div className={styles.rounded}>
        <table className={styles.text}>
          <thead>
            {table.getHeaderGroups().map((headerGroup) => (
              <tr key={headerGroup.id} className={styles.background}>
                {headerGroup.headers.map((header) => (
                  <th
                    key={header.id}
                    className={styles.paddingX}
                    onClick={header.column.getToggleSortingHandler()}
                  >
                    <div className={styles.gap}>
                      {flexRender(header.column.columnDef.header, header.getContext())}
                      {header.column.getIsSorted() && (
                        <span className={styles.text}>
                          {header.column.getIsSorted() === "asc" ? "↑" : "↓"}
                        </span>
                      )}
                    </div>
                  </th>
                ))}
              </tr>
            ))}
          </thead>
          <tbody>
            {isLoading ? (
              <tr>
                <td colSpan={columns.length} className={styles.height}>
                  Loading...
                </td>
              </tr>
            ) : table.getRowModel().rows.length === 0 ? (
              <tr>
                <td colSpan={columns.length} className={styles.textColor}>
                  No results found.
                </td>
              </tr>
            ) : (
              table.getRowModel().rows.map((row) => (
                <tr
                  key={row.id}
                  className={`border-b transition-colors ${
                    row.getIsSelected() ? "bg-muted" : "hover:bg-muted/50"
                  }`}
                  onClick={() => row.toggleSelected()}
                >
                  {row.getVisibleCells().map((cell) => (
                    <td key={cell.id} className={styles.paddingX}>
                      {flexRender(cell.column.columnDef.cell, cell.getContext())}
                    </td>
                  ))}
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>

      {/* Pagination */}
      <div className={styles.flex}>
        <span className={styles.text}>
          {table.getFilteredRowModel().rows.length} total
        </span>
        <div className={styles.gap}>
          <button
            onClick={() => table.previousPage()}
            disabled={!table.getCanPreviousPage()}
            className={styles.paddingX}
          >
            Previous
          </button>
          <span className={styles.text}>
            Page {table.getState().pagination.pageIndex + 1} of {table.getPageCount()}
          </span>
          <button
            onClick={() => table.nextPage()}
            disabled={!table.getCanNextPage()}
            className={styles.paddingX}
          >
            Next
          </button>
        </div>
      </div>
    </div>
  );
}
```

### Column Definition Pattern

```tsx
// columns/user-columns.tsx
import { ColumnDef } from "@tanstack/react-table";
import { User } from "@/types";
import { Badge } from "@/components/ui/badge";
import { formatDate } from "@/lib/utils";

export const userColumns: ColumnDef<User>[] = [
  {
    accessorKey: "name",
    header: "Name",
    cell: ({ row }) => (
      <div className={styles.font}>{row.getValue("name")}</div>
    ),
  },
  {
    accessorKey: "email",
    header: "Email",
  },
  {
    accessorKey: "role",
    header: "Role",
    cell: ({ row }) => {
      const role = row.getValue("role") as string;
      return (
        <Badge variant={role === "admin" ? "destructive" : "secondary"}>
          {role}
        </Badge>
      );
    },
  },
  {
    accessorKey: "createdAt",
    header: "Created",
    cell: ({ row }) => formatDate(row.getValue("createdAt")),
  },
  {
    id: "actions",
    cell: ({ row }) => <RowActions row={row.original} />,
  },
];
```

### Key Decisions

- **Client-side vs server-side:** Use `@tanstack/react-table` for client-side. For server-side pagination/sorting, pass `manualPagination`, `manualSorting` to `useReactTable` and handle API calls yourself.
- **Row selection:** Use checkboxes for multi-select, click-to-select for single-select.
- **Empty state:** Always show a meaningful empty state, not just blank space.
- **Loading state:** Show skeleton rows, not a spinner over the whole table.

---

## 2. Modal / Dialog

**When:** Focused interaction that requires user attention — confirmations, forms, detail views.

### Core Pattern

```tsx
// components/ui/dialog.tsx
"use client";

import { useEffect, useRef, useCallback, ReactNode } from "react";
import { createPortal } from "react-dom";

interface DialogProps {
  open: boolean;
  onClose: () => void;
  title: string;
  description?: string;
  children: ReactNode;
  size?: "sm" | "md" | "lg" | "xl" | "full";
  closeOnOverlay?: boolean;
}

const sizeClasses = {
  sm: "max-w-sm",
  md: "max-w-md",
  lg: "max-w-lg",
  xl: "max-w-xl",
  full: "max-w-4xl",
};

export function Dialog({
  open,
  onClose,
  title,
  description,
  children,
  size = "md",
  closeOnOverlay = true,
}: DialogProps) {
  const overlayRef = useRef<HTMLDivElement>(null);
  const contentRef = useRef<HTMLDivElement>(null);
  const previousFocusRef = useRef<HTMLElement | null>(null);

  // Save and restore focus
  useEffect(() => {
    if (open) {
      previousFocusRef.current = document.activeElement as HTMLElement;
      contentRef.current?.focus();
    } else {
      previousFocusRef.current?.focus();
    }
  }, [open]);

  // Trap focus inside dialog
  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent) => {
      if (e.key === "Escape") {
        onClose();
        return;
      }

      if (e.key !== "Tab") return;

      const content = contentRef.current;
      if (!content) return;

      const focusable = content.querySelectorAll<HTMLElement>(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      );
      const first = focusable[0];
      const last = focusable[focusable.length - 1];

      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    },
    [onClose]
  );

  // Prevent body scroll
  useEffect(() => {
    if (open) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
    }
    return () => {
      document.body.style.overflow = "";
    };
  }, [open]);

  if (!open) return null;

  return createPortal(
    <div
      ref={overlayRef}
      className={styles.padding}
      onClick={closeOnOverlay ? onClose : undefined}
      role="presentation"
    >
      <div
        ref={contentRef}
        className={`relative w-full ${sizeClasses[size]} bg-background rounded-lg shadow-lg outline-none`}
        role="dialog"
        aria-modal="true"
        aria-labelledby="dialog-title"
        aria-describedby={description ? "dialog-description" : undefined}
        tabIndex={-1}
        onKeyDown={handleKeyDown}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className={styles.paddingX}>
          <div>
            <h2 id="dialog-title" className={styles.text}>
              {title}
            </h2>
            {description && (
              <p id="dialog-description" className={styles.text}>
                {description}
              </p>
            )}
          </div>
          <button
            onClick={onClose}
            className={styles.rounded}
            aria-label="Close dialog"
          >
            ✕
          </button>
        </div>

        {/* Content */}
        <div className={styles.paddingX}>{children}</div>
      </div>
    </div>,
    document.body
  );
}
```

### Stacking Dialogs

```tsx
// hooks/use-dialog-stack.ts
import { useState, useCallback } from "react";

interface DialogEntry {
  id: string;
  zIndex: number;
}

const BASE_Z_INDEX = 1000;
const Z_INDEX_STEP = 10;

export function useDialogStack() {
  const [dialogs, setDialogs] = useState<DialogEntry[]>([]);

  const open = useCallback((id: string) => {
    setDialogs((prev) => [
      ...prev,
      { id, zIndex: BASE_Z_INDEX + prev.length * Z_INDEX_STEP },
    ]);
  }, []);

  const close = useCallback((id: string) => {
    setDialogs((prev) => prev.filter((d) => d.id !== id));
  }, []);

  const getZIndex = useCallback(
    (id: string) => dialogs.find((d) => d.id === id)?.zIndex ?? BASE_Z_INDEX,
    [dialogs]
  );

  return { dialogs, open, close, getZIndex };
}
```

### Key Decisions

- **Focus trapping is mandatory** — without it, keyboard users can tab behind the dialog.
- **Portal to body** — prevents CSS stacking context issues.
- **Prevent body scroll** — avoids confusing scroll behavior.
- **Close on Escape** — expected keyboard behavior.
- **Stacking:** Use z-index increments, not nested portals, for predictable layering.

---

## 3. Card System

**When:** Content containers that group related information — products, profiles, stats, articles.

### Core Pattern

```tsx
// components/ui/card.tsx
import { ReactNode, HTMLAttributes } from "react";
import { cn } from "@/lib/utils";

function Card({ className, children, ...props }: HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={cn("rounded-lg border bg-card text-card-foreground shadow-sm", className)}
      {...props}
    >
      {children}
    </div>
  );
}

function CardHeader({ className, children, ...props }: HTMLAttributes<HTMLDivElement>) {
  return (
    <div className={cn("flex flex-col space-y-1.5 p-6", className)} {...props}>
      {children}
    </div>
  );
}

function CardTitle({ className, children, ...props }: HTMLAttributes<HTMLHeadingElement>) {
  return (
    <h3 className={cn("text-lg font-semibold leading-none tracking-tight", className)} {...props}>
      {children}
    </h3>
  );
}

function CardDescription({ className, children, ...props }: HTMLAttributes<HTMLParagraphElement>) {
  return (
    <p className={cn("text-sm text-muted-foreground", className)} {...props}>
      {children}
    </p>
  );
}

function CardContent({ className, children, ...props }: HTMLAttributes<HTMLDivElement>) {
  return (
    <div className={cn("p-6 pt-0", className)} {...props}>
      {children}
    </div>
  );
}

function CardFooter({ className, children, ...props }: HTMLAttributes<HTMLDivElement>) {
  return (
    <div className={cn("flex items-center p-6 pt-0", className)} {...props}>
      {children}
    </div>
  );
}

export { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent };
```

### Card Variants

```tsx
// Variant: Interactive card (clickable, hoverable)
function InteractiveCard({
  onClick,
  children,
  className,
  ...props
}: HTMLAttributes<HTMLDivElement> & { onClick?: () => void }) {
  return (
    <Card
      className={cn(
        "cursor-pointer transition-all hover:shadow-md hover:border-primary/50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
        className
      )}
      onClick={onClick}
      role={onClick ? "button" : undefined}
      tabIndex={onClick ? 0 : undefined}
      onKeyDown={onClick ? (e) => e.key === "Enter" && onClick() : undefined}
      {...props}
    >
      {children}
    </Card>
  );
}

// Variant: Media card (image + content)
function MediaCard({
  image,
  imageAlt,
  children,
  className,
}: {
  image: string;
  imageAlt: string;
  children: ReactNode;
  className?: string;
}) {
  return (
    <Card className={cn("overflow-hidden", className)}>
      <div className={styles.background}>
        <img
          src={image}
          alt={imageAlt}
          className={styles.wFull}
          loading="lazy"
        />
      </div>
      {children}
    </Card>
  );
}
```

### Key Decisions

- **Compound components** (Card.Header, Card.Content) are better than props-based cards — they compose naturally.
- **Interactive cards** need keyboard support (role="button", tabIndex, Enter key).
- **Media cards** need `loading="lazy"` and `object-cover` for consistent sizing.
- **Never hardcode card widths** — use grid or flex with responsive breakpoints.

---

## 4. Navigation Bar

**When:** Primary site navigation — desktop horizontal, mobile hamburger.

### Core Pattern

```tsx
// components/layout/navbar.tsx
"use client";

import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { cn } from "@/lib/utils";

interface NavItem {
  label: string;
  href: string;
  icon?: React.ReactNode;
  children?: NavItem[];
}

interface NavbarProps {
  items: NavItem[];
  logo: React.ReactNode;
  actions?: React.ReactNode;
}

export function Navbar({ items, logo, actions }: NavbarProps) {
  const pathname = usePathname();
  const [mobileOpen, setMobileOpen] = useState(false);

  return (
    <header className={styles.background}>
      <div className={styles.flex}>
        {/* Logo */}
        <div className={styles.flex}>{logo}</div>

        {/* Desktop Nav */}
        <nav className={styles.desktopFlex}>
          {items.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className={cn(
                "transition-colors hover:text-foreground/80",
                pathname === item.href
                  ? "text-foreground font-medium"
                  : "text-foreground/60"
              )}
            >
              {item.label}
            </Link>
          ))}
        </nav>

        {/* Actions */}
        <div className={styles.desktopFlex}>
          {actions}
        </div>

        {/* Mobile Toggle */}
        <button
          className={styles.mobileOnly}
          onClick={() => setMobileOpen(!mobileOpen)}
          aria-label="Toggle menu"
          aria-expanded={mobileOpen}
        >
          {mobileOpen ? "✕" : "☰"}
        </button>
      </div>

      {/* Mobile Menu */}
      {mobileOpen && (
        <div className={styles.mobileOnly}>
          <nav className={styles.stack}>
            {items.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className={cn(
                  "block py-2 text-sm transition-colors hover:text-foreground/80",
                  pathname === item.href
                    ? "text-foreground font-medium"
                    : "text-foreground/60"
                )}
                onClick={() => setMobileOpen(false)}
              >
                {item.label}
              </Link>
            ))}
            {actions && (
              <div className={styles.border}>{actions}</div>
            )}
          </nav>
        </div>
      )}
    </header>
  );
}
```

### Key Decisions

- **Sticky header** with `backdrop-blur` — modern, doesn't hide content.
- **Active state** from `usePathname()` — no manual tracking needed.
- **Mobile menu** closes on navigation — prevents stale open state.
- **Actions slot** — lets you inject auth buttons, search, etc. without modifying the navbar.

---

## 5. Sidebar

**When:** Secondary navigation — collapsible, nested, with icons and active routing.

### Core Pattern

```tsx
// components/layout/sidebar.tsx
"use client";

import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { cn } from "@/lib/utils";

interface SidebarItem {
  label: string;
  href: string;
  icon?: React.ReactNode;
  badge?: string | number;
  children?: SidebarItem[];
}

interface SidebarProps {
  items: SidebarItem[];
  collapsible?: boolean;
  defaultCollapsed?: boolean;
}

export function Sidebar({ items, collapsible = true, defaultCollapsed = false }: SidebarProps) {
  const pathname = usePathname();
  const [collapsed, setCollapsed] = useState(defaultCollapsed);
  const [expandedSections, setExpandedSections] = useState<Set<string>>(new Set());

  const toggleSection = (label: string) => {
    setExpandedSections((prev) => {
      const next = new Set(prev);
      if (next.has(label)) next.delete(label);
      else next.add(label);
      return next;
    });
  };

  return (
    <aside
      className={cn(
        "flex flex-col border-r bg-background transition-all duration-200",
        collapsed ? "w-16" : "w-64"
      )}
    >
      {/* Collapse Toggle */}
      {collapsible && (
        <button
          className={styles.padding}
          onClick={() => setCollapsed(!collapsed)}
          aria-label={collapsed ? "Expand sidebar" : "Collapse sidebar"}
        >
          {collapsed ? "→" : "←"}
        </button>
      )}

      {/* Nav Items */}
      <nav className={styles.paddingY}>
        {items.map((item) => (
          <SidebarGroup
            key={item.href}
            item={item}
            pathname={pathname}
            collapsed={collapsed}
            isExpanded={expandedSections.has(item.label)}
            onToggle={() => toggleSection(item.label)}
          />
        ))}
      </nav>
    </aside>
  );
}

function SidebarGroup({
  item,
  pathname,
  collapsed,
  isExpanded,
  onToggle,
}: {
  item: SidebarItem;
  pathname: string;
  collapsed: boolean;
  isExpanded: boolean;
  onToggle: () => void;
}) {
  const isActive = pathname === item.href;
  const hasChildren = item.children && item.children.length > 0;

  if (collapsed) {
    return (
      <Link
        href={item.href}
        className={cn(
          "flex items-center justify-center h-10 mx-2 rounded-md transition-colors",
          isActive ? "bg-muted text-foreground" : "text-muted-foreground hover:bg-muted/50"
        )}
        title={item.label}
      >
        {item.icon}
      </Link>
    );
  }

  return (
    <div>
      <div
        className={cn(
          "flex items-center justify-between h-10 px-3 rounded-md cursor-pointer transition-colors",
          isActive ? "bg-muted text-foreground" : "text-muted-foreground hover:bg-muted/50"
        )}
        onClick={hasChildren ? onToggle : undefined}
      >
        <Link href={item.href} className={styles.gap}>
          {item.icon}
          <span className={styles.text}>{item.label}</span>
        </Link>
        {item.badge && (
          <span className={styles.paddingX}>
            {item.badge}
          </span>
        )}
        {hasChildren && <span className={styles.text}>{isExpanded ? "▾" : "▸"}</span>}
      </div>

      {hasChildren && isExpanded && (
        <div className={styles.stack}>
          {item.children!.map((child) => (
            <Link
              key={child.href}
              href={child.href}
              className={cn(
                "block h-8 px-3 text-sm rounded-md transition-colors",
                pathname === child.href
                  ? "bg-muted text-foreground"
                  : "text-muted-foreground/70 hover:bg-muted/50"
              )}
            >
              {child.label}
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}
```

### Key Decisions

- **Collapsible** — collapses to icon-only mode, not hidden entirely.
- **Nested sections** — expand/collapse, not always visible.
- **Active state** — from `usePathname()`, no manual tracking.
- **Badge support** — for notifications, counts, status indicators.

---

## 6. Dashboard Layout

**When:** Multi-widget overview pages — analytics, admin panels, monitoring dashboards.

### Core Pattern

```tsx
// components/layout/dashboard.tsx
import { ReactNode } from "react";
import { cn } from "@/lib/utils";

interface DashboardProps {
  children: ReactNode;
  title: string;
  description?: string;
  actions?: ReactNode;
}

export function Dashboard({ children, title, description, actions }: DashboardProps) {
  return (
    <div className={styles.stack}>
      {/* Header */}
      <div className={styles.stack}>
        <div>
          <h2 className={styles.text}>{title}</h2>
          {description && (
            <p className={styles.textColor}>{description}</p>
          )}
        </div>
        {actions && <div className={styles.gap}>{actions}</div>}
      </div>

      {/* Content */}
      <div className={styles.stack}>{children}</div>
    </div>
  );
}

// Stat cards row
export function StatGrid({ children }: { children: ReactNode }) {
  return (
    <div className={styles.grid}>{children}</div>
  );
}

// Main content area with sidebar
export function DashboardContent({
  sidebar,
  main,
}: {
  sidebar: ReactNode;
  main: ReactNode;
}) {
  return (
    <div className={styles.grid}>
      <div className={styles.colSpan}>{sidebar}</div>
      <div className={styles.colSpan}>{main}</div>
    </div>
  );
}

// Full-width chart area
export function ChartArea({ children }: { children: ReactNode }) {
  return (
    <div className={styles.padding}>{children}</div>
  );
}
```

### Responsive Breakpoints

```tsx
// Dashboard grid behavior at each breakpoint:
// Mobile (default): 1 column, stacked
// Tablet (md:768px): 2 columns for stats, 7-col grid for content
// Desktop (lg:1024px): 4 columns for stats, full layout
// Wide (xl:1280px): Same as desktop, wider content area
```

### Key Decisions

- **Composable layout** — Dashboard, StatGrid, DashboardContent, ChartArea compose freely.
- **Actions slot** — date pickers, export buttons, filters go here.
- **Responsive grid** — stats go 1→2→4 columns, content goes stacked→sidebar.
- **Never hardcode widget sizes** — use the grid system.

---

## 7. Button System

**When:** Interactive triggers — primary actions, secondary actions, destructive, icon-only.

### Core Pattern

```tsx
// components/ui/button.tsx
import { ButtonHTMLAttributes, forwardRef } from "react";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";

const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
        outline: "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
        secondary: "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
        lg: "h-11 rounded-md px-8",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
);

export interface ButtonProps
  extends ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {}

const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, ...props }, ref) => {
    return (
      <button
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    );
  }
);
Button.displayName = "Button";

export { Button, buttonVariants };
```

### Key Decisions

- **CVA (class-variance-authority)** — type-safe variant system, no prop drilling.
- **6 variants** cover 99% of button needs. Add custom variants per project.
- **Icon button** is a size variant, not a separate component.
- **Focus ring** is mandatory — never remove `focus-visible:ring`.

---

## 8. Badge / Tag System

**When:** Status indicators, categories, labels, counts.

```tsx
// components/ui/badge.tsx
import { HTMLAttributes } from "react";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";

const badgeVariants = cva(
  "inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors",
  {
    variants: {
      variant: {
        default: "border-transparent bg-primary text-primary-foreground",
        secondary: "border-transparent bg-secondary text-secondary-foreground",
        destructive: "border-transparent bg-destructive text-destructive-foreground",
        outline: "text-foreground",
        success: "border-transparent bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-100",
        warning: "border-transparent bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-100",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
);

export interface BadgeProps extends HTMLAttributes<HTMLDivElement>, VariantProps<typeof badgeVariants> {}

export function Badge({ className, variant, ...props }: BadgeProps) {
  return <div className={cn(badgeVariants({ variant }), className)} {...props} />;
}
```

---

## 9. Tabs System

**When:** Switching between related content views — settings pages, detail views, filtered lists.

```tsx
// components/ui/tabs.tsx
"use client";

import { useState, ReactNode } from "react";
import { cn } from "@/lib/utils";

interface Tab {
  id: string;
  label: string;
  content: ReactNode;
  disabled?: boolean;
  badge?: string | number;
}

interface TabsProps {
  tabs: Tab[];
  defaultTab?: string;
  onTabChange?: (tabId: string) => void;
  variant?: "default" | "underline" | "pills";
}

export function Tabs({ tabs, defaultTab, onTabChange, variant = "default" }: TabsProps) {
  const [activeTab, setActiveTab] = useState(defaultTab || tabs[0]?.id);

  const handleTabChange = (tabId: string) => {
    const tab = tabs.find((t) => t.id === tabId);
    if (tab?.disabled) return;
    setActiveTab(tabId);
    onTabChange?.(tabId);
  };

  const activeContent = tabs.find((t) => t.id === activeTab)?.content;

  return (
    <div>
      {/* Tab List */}
      <div
        className={cn(
          "flex",
          variant === "underline" && "border-b",
          variant === "pills" && "gap-1"
        )}
        role="tablist"
      >
        {tabs.map((tab) => (
          <button
            key={tab.id}
            role="tab"
            aria-selected={activeTab === tab.id}
            aria-controls={`panel-${tab.id}`}
            disabled={tab.disabled}
            className={cn(
              "px-4 py-2 text-sm font-medium transition-colors disabled:opacity-50",
              variant === "default" && "rounded-md",
              variant === "underline" && "border-b-2 -mb-px",
              variant === "pills" && "rounded-full",
              activeTab === tab.id
                ? "text-foreground bg-muted"
                : "text-muted-foreground hover:text-foreground"
            )}
            onClick={() => handleTabChange(tab.id)}
          >
            {tab.label}
            {tab.badge && (
              <span className={styles.paddingX}>
                {tab.badge}
              </span>
            )}
          </button>
        ))}
      </div>

      {/* Tab Panel */}
      <div
        id={`panel-${activeTab}`}
        role="tabpanel"
        aria-labelledby={activeTab}
        className={styles.paddingY}
      >
        {activeContent}
      </div>
    </div>
  );
}
```

---

## 10. Toast / Notification System

**When:** Transient feedback — success, error, warning, info messages.

```tsx
// components/ui/toast.tsx
"use client";

import { createContext, useContext, useState, useCallback, ReactNode } from "react";
import { cn } from "@/lib/utils";

type ToastType = "success" | "error" | "warning" | "info";

interface Toast {
  id: string;
  type: ToastType;
  title: string;
  description?: string;
  duration?: number;
}

interface ToastContextType {
  toasts: Toast[];
  addToast: (toast: Omit<Toast, "id">) => void;
  removeToast: (id: string) => void;
}

const ToastContext = createContext<ToastContextType | null>(null);

export function ToastProvider({ children }: { children: ReactNode }) {
  const [toasts, setToasts] = useState<Toast[]>([]);

  const addToast = useCallback((toast: Omit<Toast, "id">) => {
    const id = Math.random().toString(36).slice(2);
    setToasts((prev) => [...prev, { ...toast, id }]);

    if (toast.duration !== 0) {
      setTimeout(() => {
        setToasts((prev) => prev.filter((t) => t.id !== id));
      }, toast.duration ?? 5000);
    }
  }, []);

  const removeToast = useCallback((id: string) => {
    setToasts((prev) => prev.filter((t) => t.id !== id));
  }, []);

  return (
    <ToastContext.Provider value={{ toasts, addToast, removeToast }}>
      {children}
      <ToastContainer />
    </ToastContext.Provider>
  );
}

function ToastContainer() {
  const ctx = useContext(ToastContext);
  if (!ctx) return null;

  const typeStyles: Record<ToastType, string> = {
    success: "border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-100",
    error: "border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-100",
    warning: "border-yellow-500 bg-yellow-50 text-yellow-900 dark:bg-yellow-950 dark:text-yellow-100",
    info: "border-blue-500 bg-blue-50 text-blue-900 dark:bg-blue-950 dark:text-blue-100",
  };

  return (
    <div className={styles.stack}>
      {ctx.toasts.map((toast) => (
        <div
          key={toast.id}
          className={cn(
            "rounded-lg border-l-4 p-4 shadow-lg animate-in slide-in-from-right",
            typeStyles[toast.type]
          )}
          role="alert"
        >
          <div className={styles.font}>{toast.title}</div>
          {toast.description && (
            <div className={styles.text}>{toast.description}</div>
          )}
          <button
            className={styles.text}
            onClick={() => ctx.removeToast(toast.id)}
            aria-label="Dismiss"
          >
            ✕
          </button>
        </div>
      ))}
    </div>
  );
}

export function useToast() {
  const ctx = useContext(ToastContext);
  if (!ctx) throw new Error("useToast must be used within ToastProvider");
  return ctx;
}
```

---

## 11. Avatar System

**When:** User representation — profile pictures, initials, status indicators.

```tsx
// components/ui/avatar.tsx
import { HTMLAttributes } from "react";
import { cn } from "@/lib/utils";

interface AvatarProps extends HTMLAttributes<HTMLDivElement> {
  src?: string;
  alt: string;
  fallback?: string;
  size?: "sm" | "md" | "lg";
  status?: "online" | "offline" | "busy" | "away";
}

const sizeClasses = {
  sm: "h-8 w-8 text-xs",
  md: "h-10 w-10 text-sm",
  lg: "h-14 w-14 text-base",
};

const statusColors = {
  online: "bg-green-500",
  offline: "bg-gray-400",
  busy: "bg-red-500",
  away: "bg-yellow-500",
};

export function Avatar({ src, alt, fallback, size = "md", status, className, ...props }: AvatarProps) {
  const initials = fallback || alt.split(" ").map((n) => n[0]).join("").toUpperCase().slice(0, 2);

  return (
    <div className={cn("relative inline-flex", className)} {...props}>
      <div
        className={cn(
          "relative flex items-center justify-center rounded-full bg-muted overflow-hidden",
          sizeClasses[size]
        )}
      >
        {src ? (
          <img src={src} alt={alt} className={styles.wFull} />
        ) : (
          <span className={styles.font}>{initials}</span>
        )}
      </div>
      {status && (
        <span
          className={cn(
            "absolute bottom-0 right-0 block rounded-full ring-2 ring-background",
            statusColors[status],
            size === "sm" ? "h-2 w-2" : size === "md" ? "h-2.5 w-2.5" : "h-3 w-3"
          )}
          aria-label={`Status: ${status}`}
        />
      )}
    </div>
  );
}
```

---

## 12. Empty State System

**When:** No data, no results, first-time experience, error recovery.

```tsx
// components/ui/empty-state.tsx
import { ReactNode } from "react";
import { Button } from "./button";
import { cn } from "@/lib/utils";

interface EmptyStateProps {
  icon?: ReactNode;
  title: string;
  description?: string;
  action?: {
    label: string;
    onClick: () => void;
    variant?: "default" | "outline" | "secondary";
  };
  secondaryAction?: {
    label: string;
    onClick: () => void;
  };
  className?: string;
}

export function EmptyState({
  icon,
  title,
  description,
  action,
  secondaryAction,
  className,
}: EmptyStateProps) {
  return (
    <div className={cn("flex flex-col items-center justify-center py-12 text-center", className)}>
      {icon && (
        <div className={styles.textColor}>{icon}</div>
      )}
      <h3 className={styles.text}>{title}</h3>
      {description && (
        <p className={styles.text}>{description}</p>
      )}
      <div className={styles.gap}>
        {action && (
          <Button onClick={action.onClick} variant={action.variant}>
            {action.label}
          </Button>
        )}
        {secondaryAction && (
          <Button variant="outline" onClick={secondaryAction.onClick}>
            {secondaryAction.label}
          </Button>
        )}
      </div>
    </div>
  );
}
```

### Empty State Variants

| Scenario | Title Example | Action |
|---|---|---|
| No data yet | "No projects created" | "Create your first project" |
| No search results | "No results for 'xyz'" | "Clear search" or "Try different terms" |
| No permissions | "You don't have access" | "Request access" |
| Error state | "Something went wrong" | "Try again" + "Contact support" |
| First-time | "Welcome! Get started" | "Take a tour" or "Create something" |

---

## Design Unification Principles

When you receive a messy design or need to unify existing UI:

### 1. Audit First
- List every unique color value → consolidate to tokens
- List every unique spacing value → map to spacing scale
- List every unique border-radius → reduce to 2-3 values
- List every unique font size → map to type scale

### 2. Establish Hierarchy
- **Primary actions** → one color, one weight
- **Secondary actions** → outline or ghost variant
- **Destructive actions** → red, always distinct
- **Information hierarchy** → heading, body, caption, muted

### 3. Consistency Rules
- Same component type = same variant everywhere
- Same data type = same display pattern everywhere
- Same interaction = same feedback pattern everywhere
- Never introduce a new pattern without replacing all instances of the old one

### 4. Progressive Enhancement
- Start with structure (layout, grid, spacing)
- Add typography (headings, body, hierarchy)
- Add color (tokens, semantic colors)
- Add interaction (hover, focus, active states)
- Add motion (transitions, micro-interactions)
