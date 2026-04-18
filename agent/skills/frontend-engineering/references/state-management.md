# State Management

When to use what, with concrete patterns for every state scenario.

---

## Decision Tree

```
Is the state only used by ONE component?
├─ YES → useState or useReducer
└─ NO → Is it shared between components?
         ├─ YES, same branch of tree → Lift state up or Context
         └─ YES, across the app → Zustand or similar store

Is the state from a server/API?
├─ YES → TanStack Query / SWR (NOT useState + useEffect)
└─ NO → Is it form state?
         ├─ YES → React Hook Form (internal state)
         └─ NO → Follow the decision tree above

Does the state need to persist across page reloads?
├─ YES → localStorage + Zustand persist middleware
└─ NO → In-memory state

Does the state need URL sharing/bookmarking?
├─ YES → URL search params (useSearchParams)
└─ NO → In-memory state
```

---

## 1. Local State (useState)

**When:** Simple state owned by one component — toggles, input values, UI state.

```tsx
// Simple toggle
function Toggle() {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <button onClick={() => setIsOpen((prev) => !prev)} aria-expanded={isOpen}>
      {isOpen ? "Close" : "Open"}
    </button>
  );
}

// Input with validation
function ValidatedInput() {
  const [value, setValue] = useState("");
  const [touched, setTouched] = useState(false);
  const isValid = value.length >= 3;
  const showError = touched && !isValid;

  return (
    <input
      value={value}
      onChange={(e) => setValue(e.target.value)}
      onBlur={() => setTouched(true)}
      aria-invalid={showError}
    />
  );
}
```

### When to Lift State

```tsx
// BAD: Two components duplicating state
function Parent() {
  return (
    <>
      <SearchBar />   // has its own search state
      <ResultsList /> // has its own search state
    </>
  );
}

// GOOD: State lifted to parent
function Parent() {
  const [search, setSearch] = useState("");
  return (
    <>
      <SearchBar value={search} onChange={setSearch} />
      <ResultsList search={search} />
    </>
  );
}
```

---

## 2. Complex Local State (useReducer)

**When:** State has multiple sub-values, or next state depends on previous in complex ways.

```tsx
// Shopping cart with complex actions
type CartItem = { id: string; name: string; price: number; quantity: number };

type CartAction =
  | { type: "ADD"; item: Omit<CartItem, "quantity"> }
  | { type: "REMOVE"; id: string }
  | { type: "UPDATE_QUANTITY"; id: string; quantity: number }
  | { type: "CLEAR" };

function cartReducer(state: CartItem[], action: CartAction): CartItem[] {
  switch (action.type) {
    case "ADD": {
      const existing = state.find((i) => i.id === action.item.id);
      if (existing) {
        return state.map((i) =>
          i.id === action.item.id ? { ...i, quantity: i.quantity + 1 } : i
        );
      }
      return [...state, { ...action.item, quantity: 1 }];
    }
    case "REMOVE":
      return state.filter((i) => i.id !== action.id);
    case "UPDATE_QUANTITY":
      return action.quantity <= 0
        ? state.filter((i) => i.id !== action.id)
        : state.map((i) => (i.id === action.id ? { ...i, quantity: action.quantity } : i));
    case "CLEAR":
      return [];
    default:
      return state;
  }
}

function useCart() {
  const [items, dispatch] = useReducer(cartReducer, []);
  const total = items.reduce((sum, i) => sum + i.price * i.quantity, 0);
  const count = items.reduce((sum, i) => sum + i.quantity, 0);

  return { items, total, count, dispatch };
}
```

### When to Use useReducer vs useState

| Use `useState` | Use `useReducer` |
|---|---|
| Single value | Multiple related values |
| Simple updates | Complex transitions |
| Independent state | State depends on previous |
| One action | Many action types |

---

## 3. Shared State (Context)

**When:** State needed by multiple components in the same tree — theme, auth, locale.

```tsx
// contexts/theme-context.tsx
"use client";

import { createContext, useContext, useState, ReactNode } from "react";

type Theme = "light" | "dark";

interface ThemeContextType {
  theme: Theme;
  toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContextType | null>(null);

export function ThemeProvider({ children }: { children: ReactNode }) {
  const [theme, setTheme] = useState<Theme>("light");

  const toggleTheme = () => {
    setTheme((prev) => (prev === "light" ? "dark" : "light"));
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  const ctx = useContext(ThemeContext);
  if (!ctx) throw new Error("useTheme must be used within ThemeProvider");
  return ctx;
}
```

### Context Performance Rule

**Context re-renders ALL consumers when ANY value changes.** To avoid this:

```tsx
// BAD: One context, many consumers re-render on any change
const AppContext = createContext({ user, theme, notifications, settings });

// GOOD: Split by concern
const UserContext = createContext({ user, setUser });
const ThemeContext = createContext({ theme, toggleTheme });
const NotificationContext = createContext({ notifications, markRead });
```

### When Context Is NOT Enough

| Scenario | Use Context | Use Store |
|---|---|---|
| Theme, locale, auth | ✅ Yes | Overkill |
| Shopping cart, dashboard data | ❌ No | ✅ Zustand |
| Frequently updating state | ❌ No | ✅ Zustand |
| State needed across unrelated trees | ❌ No | ✅ Zustand |

---

## 4. Server State (TanStack Query)

**When:** Data from an API — lists, details, mutations, pagination.

### Core Pattern

```tsx
// hooks/use-users.ts
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { User } from "@/types";

const USERS_KEY = ["users"];

// Fetch function
async function fetchUsers(): Promise<User[]> {
  const res = await fetch("/api/users");
  if (!res.ok) throw new Error("Failed to fetch users");
  return res.json();
}

// Query hook
export function useUsers() {
  return useQuery({
    queryKey: USERS_KEY,
    queryFn: fetchUsers,
    staleTime: 1000 * 60 * 5, // 5 minutes
    retry: 2,
  });
}

// Mutation hook
export function useCreateUser() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (data: Omit<User, "id">) => {
      const res = await fetch("/api/users", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
      if (!res.ok) throw new Error("Failed to create user");
      return res.json();
    },
    onSuccess: () => {
      // Invalidate and refetch
      queryClient.invalidateQueries({ queryKey: USERS_KEY });
    },
  });
}

// Component usage
function UserList() {
  const { data: users, isLoading, error } = useUsers();
  const createUser = useCreateUser();

  if (isLoading) return <SkeletonList />;
  if (error) return <ErrorMessage error={error} />;
  if (!users?.length) return <EmptyState />;

  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

### Query Key Patterns

```tsx
// Hierarchical keys for granular invalidation
const userKeys = {
  all: ["users"] as const,
  lists: () => [...userKeys.all, "list"] as const,
  list: (filters: string) => [...userKeys.lists(), { filters }] as const,
  details: () => [...userKeys.all, "detail"] as const,
  detail: (id: string) => [...userKeys.details(), id] as const,
};

// Usage:
// Invalidate all users
queryClient.invalidateQueries({ queryKey: userKeys.all });

// Invalidate only the list (not details)
queryClient.invalidateQueries({ queryKey: userKeys.lists() });

// Invalidate one specific user
queryClient.invalidateQueries({ queryKey: userKeys.detail("user-123") });
```

### Optimistic Updates

```tsx
export function useUpdateUser() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async ({ id, ...data }: Partial<User> & { id: string }) => {
      const res = await fetch(`/api/users/${id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
      if (!res.ok) throw new Error("Failed to update");
      return res.json();
    },
    // Optimistic update
    onMutate: async (newData) => {
      // Cancel outgoing refetches
      await queryClient.cancelQueries({ queryKey: userKeys.all });

      // Snapshot previous value
      const previous = queryClient.getQueryData<User[]>(userKeys.all);

      // Optimistically update
      queryClient.setQueryData(userKeys.all, (old: User[] = []) =>
        old.map((u) => (u.id === newData.id ? { ...u, ...newData } : u))
      );

      return { previous };
    },
    // Rollback on error
    onError: (err, newData, context) => {
      if (context?.previous) {
        queryClient.setQueryData(userKeys.all, context.previous);
      }
    },
    // Always refetch after error or success
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: userKeys.all });
    },
  });
}
```

---

## 5. Global Store (Zustand)

**When:** Complex shared state that Context can't handle — dashboards, real-time data, multi-step flows.

```tsx
// stores/dashboard-store.ts
import { create } from "zustand";
import { persist } from "zustand/middleware";

interface DashboardState {
  // State
  dateRange: { start: string; end: string };
  selectedMetrics: string[];
  refreshInterval: number;
  isAutoRefresh: boolean;

  // Actions
  setDateRange: (range: { start: string; end: string }) => void;
  toggleMetric: (metric: string) => void;
  setRefreshInterval: (interval: number) => void;
  toggleAutoRefresh: () => void;
  reset: () => void;
}

const defaultState = {
  dateRange: { start: "2024-01-01", end: "2024-12-31" },
  selectedMetrics: ["revenue", "users", "conversions"],
  refreshInterval: 30000,
  isAutoRefresh: false,
};

export const useDashboardStore = create<DashboardState>()(
  persist(
    (set) => ({
      ...defaultState,
      setDateRange: (range) => set({ dateRange: range }),
      toggleMetric: (metric) =>
        set((state) => ({
          selectedMetrics: state.selectedMetrics.includes(metric)
            ? state.selectedMetrics.filter((m) => m !== metric)
            : [...state.selectedMetrics, metric],
        })),
      setRefreshInterval: (interval) => set({ refreshInterval: interval }),
      toggleAutoRefresh: () =>
        set((state) => ({ isAutoRefresh: !state.isAutoRefresh })),
      reset: () => set(defaultState),
    }),
    {
      name: "dashboard-storage", // localStorage key
      partialize: (state) => ({
        // Only persist these fields
        dateRange: state.dateRange,
        selectedMetrics: state.selectedMetrics,
        refreshInterval: state.refreshInterval,
      }),
    }
  )
);
```

### Selector Pattern (Performance)

```tsx
// BAD: Re-renders on ANY store change
const { dateRange, selectedMetrics } = useDashboardStore();

// GOOD: Only re-renders when THIS selector changes
const dateRange = useDashboardStore((state) => state.dateRange);
const selectedMetrics = useDashboardStore((state) => state.selectedMetrics);

// BEST: Memoized selector for derived state
const metricCount = useDashboardStore((state) => state.selectedMetrics.length);
```

---

## 6. URL State

**When:** State that should be shareable/bookmarkable — filters, pagination, tabs.

```tsx
// hooks/use-url-state.ts
import { useSearchParams, useRouter, usePathname } from "next/navigation";
import { useCallback } from "react";

export function useUrlState() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const pathname = usePathname();

  const setParam = useCallback(
    (key: string, value: string | null) => {
      const params = new URLSearchParams(searchParams);
      if (value) params.set(key, value);
      else params.delete(key);
      router.replace(`${pathname}?${params.toString()}`);
    },
    [router, pathname, searchParams]
  );

  const getParam = useCallback(
    (key: string, fallback?: string) => searchParams.get(key) || fallback,
    [searchParams]
  );

  const clearParams = useCallback(() => {
    router.replace(pathname);
  }, [router, pathname]);

  return { setParam, getParam, clearParams };
}
```

---

## State Anti-Patterns

### ❌ Prop Drilling
```tsx
// BAD: Passing through 4 levels
<App user={user} theme={theme}>
  <Layout user={user} theme={theme}>
    <Sidebar user={user} theme={theme}>
      <UserMenu user={user} theme={theme} />
    </Sidebar>
  </Layout>
</App>

// GOOD: Context or store
<ThemeProvider>
  <AuthProvider>
    <App />
  </AuthProvider>
</ThemeProvider>
```

### ❌ useEffect for Server State
```tsx
// BAD: Manual fetch + loading + error + cache
const [data, setData] = useState(null);
const [loading, setLoading] = useState(true);
useEffect(() => {
  fetch("/api/users").then(r => r.json()).then(setData).finally(() => setLoading(false));
}, []);

// GOOD: TanStack Query handles all of this
const { data, isLoading, error } = useQuery({ queryKey: ["users"], queryFn: fetchUsers });
```

### ❌ Stale Closures
```tsx
// BAD: count is stale in the callback
function Counter() {
  const [count, setCount] = useState(0);
  const onClick = useCallback(() => {
    console.log(count); // Always 0!
    setCount(count + 1);
  }, []); // Empty deps = stale closure
}

// GOOD: Use functional update
function Counter() {
  const [count, setCount] = useState(0);
  const onClick = useCallback(() => {
    setCount((prev) => prev + 1); // Always uses latest
  }, []);
}
```

---

## State Selection Guide

| Scenario | Best Tool | Why |
|---|---|---|
| Toggle, input, modal open | `useState` | Simple, local |
| Form with validation | `React Hook Form` | Handles validation, submission, errors |
| Theme, locale, auth | `Context` | Shared, rarely changes |
| API data (lists, details) | `TanStack Query` | Caching, refetching, mutations |
| Shopping cart, dashboard | `Zustand` | Complex, frequently updated |
| Filters, pagination, tabs | `URL params` | Shareable, bookmarkable |
| Multi-step wizard | `useReducer` or `Zustand` | Complex transitions |
| Real-time data | `Zustand` + WebSocket | Frequent updates, no refetching |
