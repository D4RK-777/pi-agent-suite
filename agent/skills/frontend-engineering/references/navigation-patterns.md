# Navigation Patterns

How users move through the app — routes, breadcrumbs, tabs, deep linking, permissions.

---

## 1. Route Architecture (Next.js App Router)

### File-Based Routing Structure

```
app/
├── (auth)/                    # Route group — no URL prefix
│   ├── login/
│   │   └── page.tsx          # /login
│   ├── signup/
│   │   └── page.tsx          # /signup
│   └── layout.tsx            # Shared auth layout
├── (dashboard)/               # Route group — no URL prefix
│   ├── layout.tsx            # Dashboard layout (sidebar + header)
│   ├── page.tsx              # / (dashboard home)
│   ├── settings/
│   │   ├── page.tsx          # /settings
│   │   └── profile/
│   │       └── page.tsx      # /settings/profile
│   └── users/
│       ├── page.tsx          # /users
│       └── [id]/
│           ├── page.tsx      # /users/[id]
│           └── edit/
│               └── page.tsx  # /users/[id]/edit
├── api/                      # API routes
│   └── users/
│       └── route.ts
├── layout.tsx                # Root layout
└── page.tsx                  # Landing page (/)
```

### Dynamic Segments

```tsx
// app/users/[id]/page.tsx
interface PageProps {
  params: Promise<{ id: string }>;
  searchParams: Promise<{ tab?: string; view?: string }>;
}

export default async function UserPage({ params, searchParams }: PageProps) {
  const { id } = await params;
  const { tab = "overview", view = "default" } = await searchParams;

  const user = await fetchUser(id);

  return (
    <div>
      <UserHeader user={user} />
      <UserTabs activeTab={tab} userId={id} />
      {view === "edit" ? <UserEditForm user={user} /> : <UserOverview user={user} />}
    </div>
  );
}
```

### Catch-All Routes

```tsx
// app/docs/[...slug]/page.tsx
// Matches /docs, /docs/getting-started, /docs/getting-started/installation

interface PageProps {
  params: Promise<{ slug: string[] }>;
}

export default async function DocsPage({ params }: PageProps) {
  const { slug } = await params;
  const path = slug.join("/");
  const doc = await fetchDoc(path);

  return <DocContent doc={doc} />;
}
```

### Route Groups for Layouts

```tsx
// (marketing) group — shared layout, no URL prefix
app/(marketing)/layout.tsx
app/(marketing)/page.tsx           → /
app/(marketing)/pricing/page.tsx   → /pricing
app/(marketing)/about/page.tsx     → /about

// (app) group — different layout, no URL prefix
app/(app)/layout.tsx
app/(app)/dashboard/page.tsx       → /dashboard
app/(app)/settings/page.tsx        → /settings
```

---

## 2. Breadcrumbs

**When:** Deep navigation — showing where the user is in a hierarchy.

### Core Pattern

```tsx
// components/navigation/breadcrumbs.tsx
import Link from "next/link";
import { cn } from "@/lib/utils";

interface BreadcrumbItem {
  label: string;
  href?: string;
}

interface BreadcrumbsProps {
  items: BreadcrumbItem[];
  className?: string;
}

export function Breadcrumbs({ items, className }: BreadcrumbsProps) {
  return (
    <nav aria-label="Breadcrumb" className={cn("text-sm", className)}>
      <ol className="flex items-center gap-2">
        {items.map((item, index) => {
          const isLast = index === items.length - 1;

          return (
            <li key={item.href || item.label} className="flex items-center gap-2">
              {index > 0 && (
                <span className="text-muted-foreground" aria-hidden="true">
                  /
                </span>
              )}
              {item.href && !isLast ? (
                <Link
                  href={item.href}
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {item.label}
                </Link>
              ) : (
                <span
                  className={cn(isLast && "font-medium text-foreground")}
                  aria-current={isLast ? "page" : undefined}
                >
                  {item.label}
                </span>
              )}
            </li>
          );
        })}
      </ol>
    </nav>
  );
}
```

### Dynamic Breadcrumbs from Route

```tsx
// hooks/use-breadcrumbs.ts
import { usePathname } from "next/navigation";
import { useMemo } from "react";

const routeLabels: Record<string, string> = {
  "/": "Home",
  "/dashboard": "Dashboard",
  "/users": "Users",
  "/settings": "Settings",
  "/settings/profile": "Profile",
  "/settings/billing": "Billing",
};

export function useBreadcrumbs() {
  const pathname = usePathname();

  return useMemo(() => {
    const segments = pathname.split("/").filter(Boolean);
    const items = [{ label: "Home", href: "/" }];

    let path = "";
    for (const segment of segments) {
      path += `/${segment}`;
      const label = routeLabels[path] || segment.replace(/-/g, " ");
      items.push({
        label: label.charAt(0).toUpperCase() + label.slice(1),
        href: path,
      });
    }

    return items;
  }, [pathname]);
}
```

---

## 3. Tab Navigation

**When:** Switching between related views — settings pages, detail views, filtered lists.

### URL-Synced Tabs

```tsx
// components/navigation/url-tabs.tsx
"use client";

import Link from "next/link";
import { usePathname, useSearchParams } from "next/navigation";
import { cn } from "@/lib/utils";

interface TabDef {
  id: string;
  label: string;
  href: string;
  badge?: number;
}

interface UrlTabsProps {
  tabs: TabDef[];
  paramKey?: string; // default: "tab"
}

export function UrlTabs({ tabs, paramKey = "tab" }: UrlTabsProps) {
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const activeTab = searchParams.get(paramKey) || tabs[0]?.id;

  return (
    <div className="border-b">
      <nav className="flex gap-6 -mb-px" role="tablist">
        {tabs.map((tab) => {
          const isActive = tab.id === activeTab;
          // Build URL with tab param
          const params = new URLSearchParams(searchParams);
          params.set(paramKey, tab.id);
          const href = `${pathname}?${params.toString()}`;

          return (
            <Link
              key={tab.id}
              href={href}
              role="tab"
              aria-selected={isActive}
              className={cn(
                "pb-3 text-sm font-medium border-b-2 transition-colors",
                isActive
                  ? "border-primary text-primary"
                  : "border-transparent text-muted-foreground hover:text-foreground"
              )}
            >
              {tab.label}
              {tab.badge !== undefined && tab.badge > 0 && (
                <span className="ml-2 text-xs bg-muted px-2 py-0.5 rounded-full">
                  {tab.badge}
                </span>
              )}
            </Link>
          );
        })}
      </nav>
    </div>
  );
}
```

### Nested Tabs

```tsx
// Settings with nested tab groups
const settingsTabs: TabDef[] = [
  { id: "profile", label: "Profile", href: "/settings?tab=profile" },
  { id: "security", label: "Security", href: "/settings?tab=security" },
  { id: "notifications", label: "Notifications", href: "/settings?tab=notifications" },
  { id: "billing", label: "Billing", href: "/settings?tab=billing" },
];

const securitySubTabs: TabDef[] = [
  { id: "password", label: "Password", href: "/settings?tab=security&sub=password" },
  { id: "2fa", label: "Two-Factor Auth", href: "/settings?tab=security&sub=2fa" },
  { id: "sessions", label: "Active Sessions", href: "/settings?tab=security&sub=sessions" },
];

// Usage:
<Breadcrumbs items={[
  { label: "Home", href: "/" },
  { label: "Settings", href: "/settings" },
  { label: "Security" },
]} />
<UrlTabs tabs={settingsTabs} />
{activeTab === "security" && <UrlTabs tabs={securitySubTabs} paramKey="sub" />}
```

---

## 4. Deep Linking

**When:** Shareable URLs, state restoration, back button support.

### URL State Pattern

```tsx
// hooks/use-deep-link.ts
import { useSearchParams, useRouter, usePathname } from "next/navigation";
import { useCallback } from "react";

export function useDeepLink() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const pathname = usePathname();

  const setParams = useCallback(
    (updates: Record<string, string | null>) => {
      const params = new URLSearchParams(searchParams);
      for (const [key, value] of Object.entries(updates)) {
        if (value === null || value === "") params.delete(key);
        else params.set(key, value);
      }
      router.replace(`${pathname}?${params.toString()}`);
    },
    [router, pathname, searchParams]
  );

  const getParam = useCallback(
    (key: string, fallback?: string) => searchParams.get(key) || fallback,
    [searchParams]
  );

  const clearParams = useCallback(
    (...keys: string[]) => {
      const params = new URLSearchParams(searchParams);
      if (keys.length === 0) params.clear();
      else keys.forEach((k) => params.delete(k));
      router.replace(`${pathname}?${params.toString()}`);
    },
    [router, pathname, searchParams]
  );

  return { setParams, getParam, clearParams };
}
```

### State Restoration

```tsx
// Restore form state from URL
function SearchPage() {
  const { getParam } = useDeepLink();
  const query = getParam("q", "");
  const category = getParam("category", "");
  const page = parseInt(getParam("page", "1"), 10);

  // URL params drive the entire page state — bookmarkable, shareable
  return (
    <div>
      <SearchForm defaultQuery={query} defaultCategory={category} />
      <Results query={query} category={category} page={page} />
      <Pagination currentPage={page} />
    </div>
  );
}
```

---

## 5. Permission-Based Navigation

**When:** Different users see different nav items — admin vs user, role-based access.

### Core Pattern

```tsx
// components/navigation/permission-nav.tsx
"use client";

import Link from "next/link";
import { usePermissions } from "@/hooks/use-permissions";
import { cn } from "@/lib/utils";

interface NavItem {
  label: string;
  href: string;
  icon?: React.ReactNode;
  permission?: string; // Required permission to see this item
  badge?: number;
}

interface PermissionNavProps {
  items: NavItem[];
  activeHref: string;
}

export function PermissionNav({ items, activeHref }: PermissionNavProps) {
  const { hasPermission } = usePermissions();

  // Filter items based on permissions
  const visibleItems = items.filter(
    (item) => !item.permission || hasPermission(item.permission)
  );

  return (
    <nav className="space-y-1">
      {visibleItems.map((item) => {
        const isActive = activeHref === item.href;

        return (
          <Link
            key={item.href}
            href={item.href}
            className={cn(
              "flex items-center gap-3 px-3 py-2 rounded-md text-sm transition-colors",
              isActive
                ? "bg-primary/10 text-primary font-medium"
                : "text-muted-foreground hover:bg-muted/50 hover:text-foreground"
            )}
          >
            {item.icon}
            <span>{item.label}</span>
            {item.badge !== undefined && item.badge > 0 && (
              <span className="ml-auto text-xs bg-muted px-2 py-0.5 rounded-full">
                {item.badge}
              </span>
            )}
          </Link>
        );
      })}
    </nav>
  );
}
```

### Route Guards (Server-Side)

```tsx
// middleware.ts — Next.js middleware for route protection
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

const protectedRoutes = ["/dashboard", "/settings", "/admin"];
const adminRoutes = ["/admin"];
const authRoutes = ["/login", "/signup"];

export function middleware(request: NextRequest) {
  const token = request.cookies.get("auth-token")?.value;
  const role = request.cookies.get("user-role")?.value;
  const pathname = request.nextUrl.pathname;

  // Redirect to login if accessing protected route without token
  if (protectedRoutes.some((route) => pathname.startsWith(route)) && !token) {
    const url = new URL("/login", request.url);
    url.searchParams.set("redirect", pathname);
    return NextResponse.redirect(url);
  }

  // Redirect to dashboard if accessing auth routes with token
  if (authRoutes.some((route) => pathname.startsWith(route)) && token) {
    return NextResponse.redirect(new URL("/dashboard", request.url));
  }

  // Redirect to 403 if accessing admin route without admin role
  if (adminRoutes.some((route) => pathname.startsWith(route)) && role !== "admin") {
    return NextResponse.redirect(new URL("/403", request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*", "/settings/:path*", "/admin/:path*", "/login", "/signup"],
};
```

### 403 Page

```tsx
// app/403/page.tsx
import Link from "next/link";

export default function ForbiddenPage() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh] text-center">
      <h1 className="text-6xl font-bold text-muted-foreground">403</h1>
      <h2 className="mt-4 text-xl font-semibold">Access Denied</h2>
      <p className="mt-2 text-muted-foreground">
        You don't have permission to access this page.
      </p>
      <div className="mt-6 flex gap-4">
        <Link href="/dashboard" className="text-primary hover:underline">
          Go to Dashboard
        </Link>
        <Link href="/" className="text-muted-foreground hover:text-foreground">
          Go Home
        </Link>
      </div>
    </div>
  );
}
```

---

## 6. Back Button Handling

**When:** Multi-step flows, modals, filtered views — preserving navigation history.

### Modal as Route

```tsx
// app/users/[id]/edit/page.tsx — Edit as a route, not a modal
// This way back button works naturally

// OR: Modal with URL sync
"use client";

import { useRouter, usePathname } from "next/navigation";
import { Dialog } from "@/components/ui/dialog";

function UserList() {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const editingId = searchParams.get("edit");

  const closeEdit = () => {
    const params = new URLSearchParams(searchParams);
    params.delete("edit");
    router.replace(`${pathname}?${params.toString()}`);
  };

  return (
    <>
      <UserTable onEdit={(id) => router.push(`${pathname}?edit=${id}`)} />
      <Dialog open={!!editingId} onClose={closeEdit}>
        {editingId && <UserEditForm userId={editingId} onSave={closeEdit} />}
      </Dialog>
    </>
  );
}
```

### Confirm Navigation

```tsx
// hooks/use-confirm-navigation.ts
import { useEffect } from "react";

export function useConfirmNavigation(shouldConfirm: boolean, message = "You have unsaved changes. Leave anyway?") {
  useEffect(() => {
    if (!shouldConfirm) return;

    const handleBeforeUnload = (e: BeforeUnloadEvent) => {
      e.preventDefault();
      e.returnValue = message;
    };

    window.addEventListener("beforeunload", handleBeforeUnload);
    return () => window.removeEventListener("beforeunload", handleBeforeUnload);
  }, [shouldConfirm, message]);
}

// Usage in form
function EditForm() {
  const { isDirty } = useForm();
  useConfirmNavigation(isDirty);
  // ...
}
```

---

## Navigation Selection Guide

| Scenario | Best Pattern |
|---|---|
| Primary site nav | Navbar (horizontal) |
| App navigation | Sidebar (collapsible) |
| Deep hierarchy | Breadcrumbs |
| Related views | Tabs (URL-synced) |
| Nested settings | Nested tabs |
| Shareable state | URL params |
| Role-based access | Permission-nav + middleware |
| Multi-step flow | Wizard with back button |
| Modal detail view | Modal with URL param |
| Full-page edit | Separate route |
| Unsaved changes | Confirm navigation hook |

---

## Navigation Anti-Patterns

### ❌ Client-Side Route Guards
```tsx
// BAD: Flash of content before redirect
function AdminRoute({ children }) {
  const { user } = useAuth();
  if (!user?.isAdmin) return <Navigate to="/403" />;
  return children;
}

// GOOD: Server-side middleware
// middleware.ts handles it before the page renders
```

### ❌ Hardcoded Navigation
```tsx
// BAD: Nav items hardcoded in every page
function Page() {
  return (
    <>
      <nav>
        <Link href="/dashboard">Dashboard</Link>
        <Link href="/users">Users</Link>
        {/* Duplicated everywhere */}
      </nav>
    </>
  );
}

// GOOD: Data-driven nav
const navItems = [
  { label: "Dashboard", href: "/dashboard", icon: <HomeIcon /> },
  { label: "Users", href: "/users", icon: <UsersIcon />, permission: "admin" },
];
<PermissionNav items={navItems} activeHref={pathname} />
```

### ❌ Losing State on Navigation
```tsx
// BAD: Search state lost when navigating
router.push(`/results`);

// GOOD: Preserve state in URL
router.push(`/results?q=${query}&page=${page}&sort=${sort}`);
```
