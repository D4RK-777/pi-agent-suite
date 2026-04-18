# Data Display Patterns

How to show data at scale — lists, tables, trees, grids, charts, and real-time updates.

---

## 1. Virtual Lists

**When:** Rendering 100+ items — infinite scroll, large datasets, chat messages.

### Core Pattern (react-window)

```tsx
// components/ui/virtual-list.tsx
"use client";

import { FixedSizeList as List, ListChildComponentProps } from "react-window";
import AutoSizer from "react-virtualized-auto-sizer";
import { useCallback } from "react";

interface VirtualListProps<T> {
  items: T[];
  itemHeight: number;
  renderItem: (item: T, index: number) => React.ReactNode;
  loading?: boolean;
  onLoadMore?: () => void;
  threshold?: number; // items from end to trigger load
}

export function VirtualList<T>({
  items,
  itemHeight,
  renderItem,
  loading,
  onLoadMore,
  threshold = 20,
}: VirtualListProps<T>) {
  const handleItemsRendered = useCallback(
    ({ visibleStopIndex }: { visibleStopIndex: number }) => {
      if (onLoadMore && !loading && visibleStopIndex >= items.length - threshold) {
        onLoadMore();
      }
    },
    [onLoadMore, loading, items.length, threshold]
  );

  const Row = useCallback(
    ({ index, style }: ListChildComponentProps) => (
      <div style={style}>{renderItem(items[index], index)}</div>
    ),
    [items, renderItem]
  );

  return (
    <div className="h-full">
      <AutoSizer>
        {({ height, width }) => (
          <List
            height={height}
            width={width}
            itemCount={items.length}
            itemSize={itemHeight}
            onItemsRendered={handleItemsRendered}
          >
            {Row}
          </List>
        )}
      </AutoSizer>
      {loading && (
        <div className="py-4 text-center text-sm text-muted-foreground">
          Loading more...
        </div>
      )}
    </div>
  );
}
```

### When to Virtualize

| Item Count | Approach |
|---|---|
| < 50 | Regular map() |
| 50-200 | Regular map() with React.memo |
| 200-1000 | Virtual list |
| 1000+ | Virtual list + server-side pagination |

---

## 2. Tree Views

**When:** File explorers, nested categories, org charts, nested comments.

### Core Pattern

```tsx
// components/ui/tree-view.tsx
"use client";

import { useState, useCallback } from "react";
import { cn } from "@/lib/utils";

interface TreeNode {
  id: string;
  label: string;
  icon?: React.ReactNode;
  children?: TreeNode[];
  metadata?: Record<string, unknown>;
}

interface TreeViewProps {
  nodes: TreeNode[];
  onSelect?: (node: TreeNode) => void;
  selectedId?: string;
  defaultExpanded?: string[];
  level?: number;
}

export function TreeView({
  nodes,
  onSelect,
  selectedId,
  defaultExpanded = [],
  level = 0,
}: TreeViewProps) {
  const [expanded, setExpanded] = useState<Set<string>>(new Set(defaultExpanded));

  const toggle = useCallback((id: string) => {
    setExpanded((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  }, []);

  return (
    <ul className={cn("space-y-0.5", level > 0 && "ml-4 border-l pl-2")}>
      {nodes.map((node) => {
        const hasChildren = node.children && node.children.length > 0;
        const isExpanded = expanded.has(node.id);
        const isSelected = selectedId === node.id;

        return (
          <li key={node.id}>
            <button
              className={cn(
                "flex items-center gap-2 w-full px-2 py-1 rounded-md text-sm transition-colors text-left",
                isSelected
                  ? "bg-primary/10 text-primary font-medium"
                  : "hover:bg-muted/50"
              )}
              onClick={() => {
                if (hasChildren) toggle(node.id);
                onSelect?.(node);
              }}
              aria-expanded={hasChildren ? isExpanded : undefined}
            >
              {/* Expand/Collapse Icon */}
              <span className="w-4 h-4 flex items-center justify-center text-muted-foreground">
                {hasChildren ? (isExpanded ? "▾" : "▸") : "•"}
              </span>

              {/* Node Icon */}
              {node.icon && <span className="w-4 h-4">{node.icon}</span>}

              {/* Label */}
              <span className="truncate">{node.label}</span>
            </button>

            {/* Children */}
            {hasChildren && isExpanded && (
              <TreeView
                nodes={node.children!}
                onSelect={onSelect}
                selectedId={selectedId}
                defaultExpanded={defaultExpanded}
                level={level + 1}
              />
            )}
          </li>
        );
      })}
    </ul>
  );
}
```

### Lazy Loading Tree Nodes

```tsx
// For large trees, load children on demand
function LazyTreeNode({ node }: { node: TreeNode }) {
  const [children, setChildren] = useState<TreeNode[] | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isExpanded, setIsExpanded] = useState(false);

  const handleExpand = async () => {
    if (!isExpanded && !children) {
      setIsLoading(true);
      const loaded = await fetchNodeChildren(node.id);
      setChildren(loaded);
      setIsLoading(false);
    }
    setIsExpanded(!isExpanded);
  };

  return (
    <li>
      <button onClick={handleExpand}>
        {isLoading ? "⏳" : isExpanded ? "▾" : "▸"}
        {node.icon}
        {node.label}
      </button>
      {isExpanded && children && (
        <ul className="ml-4">
          {children.map((child) => (
            <LazyTreeNode key={child.id} node={child} />
          ))}
        </ul>
      )}
    </li>
  );
}
```

---

## 3. Grid Layouts

**When:** Image galleries, product grids, card layouts, dashboards.

### Responsive Grid

```tsx
// components/ui/responsive-grid.tsx
import { ReactNode } from "react";
import { cn } from "@/lib/utils";

interface GridProps {
  children: ReactNode;
  columns?: {
    sm?: number; // mobile
    md?: number; // tablet
    lg?: number; // desktop
    xl?: number; // wide
  };
  gap?: "sm" | "md" | "lg";
  className?: string;
}

const gapClasses = {
  sm: "gap-2",
  md: "gap-4",
  lg: "gap-6",
};

export function Grid({
  children,
  columns = { sm: 1, md: 2, lg: 3, xl: 4 },
  gap = "md",
  className,
}: GridProps) {
  return (
    <div
      className={cn(
        "grid",
        gapClasses[gap],
        `grid-cols-${columns.sm}`,
        `md:grid-cols-${columns.md}`,
        `lg:grid-cols-${columns.lg}`,
        `xl:grid-cols-${columns.xl}`,
        className
      )}
    >
      {children}
    </div>
  );
}

// Usage:
<Grid columns={{ sm: 1, md: 2, lg: 3, xl: 4 }} gap="md">
  {products.map((p) => <ProductCard key={p.id} product={p} />)}
</Grid>
```

### Masonry Layout (CSS-only)

```tsx
// components/ui/masonry-grid.tsx
function MasonryGrid({ children, columns = 3 }: { children: ReactNode; columns?: number }) {
  return (
    <div
      className="columns-1 md:columns-2 lg:columns-3 xl:columns-4 gap-4 space-y-4"
      style={{ columnCount: columns }}
    >
      {children}
    </div>
  );
}

// Items must be inline-block to work with columns
function MasonryItem({ children }: { children: ReactNode }) {
  return (
    <div className="inline-block w-full break-inside-avoid mb-4">
      {children}
    </div>
  );
}
```

---

## 4. Charts and Graphs

**When:** Analytics, dashboards, trends, comparisons.

### Chart Selection Guide

| Data Type | Best Chart | Library |
|---|---|---|
| Trends over time | Line chart | Recharts, Chart.js |
| Comparisons | Bar chart | Recharts, Chart.js |
| Proportions | Pie/donut chart | Recharts |
| Distributions | Histogram, box plot | D3, Chart.js |
| Relationships | Scatter plot | D3, Recharts |
| Hierarchical | Tree map | D3 |
| Geographic | Map | D3, Leaflet |
| Real-time | Live line chart | Recharts + WebSocket |

### Recharts Pattern

```tsx
// components/charts/line-chart.tsx
"use client";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
} from "recharts";

interface DataPoint {
  date: string;
  value: number;
  previous?: number;
}

interface TrendChartProps {
  data: DataPoint[];
  title: string;
  valueLabel?: string;
  previousLabel?: string;
}

export function TrendChart({
  data,
  title,
  valueLabel = "Current",
  previousLabel = "Previous",
}: TrendChartProps) {
  return (
    <div className="rounded-lg border bg-card p-6">
      <h3 className="text-sm font-medium mb-4">{title}</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" className="stroke-muted" />
          <XAxis
            dataKey="date"
            className="text-xs"
            tick={{ fill: "currentColor" }}
          />
          <YAxis className="text-xs" tick={{ fill: "currentColor" }} />
          <Tooltip
            contentStyle={{
              backgroundColor: "hsl(var(--card))",
              border: "1px solid hsl(var(--border))",
              borderRadius: "8px",
            }}
          />
          <Legend />
          <Line
            type="monotone"
            dataKey="value"
            stroke="hsl(var(--primary))"
            strokeWidth={2}
            dot={false}
            name={valueLabel}
          />
          {data[0]?.previous !== undefined && (
            <Line
              type="monotone"
              dataKey="previous"
              stroke="hsl(var(--muted-foreground))"
              strokeWidth={2}
              strokeDasharray="5 5"
              dot={false}
              name={previousLabel}
            />
          )}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
```

---

## 5. Real-Time Updates

**When:** Live dashboards, chat, notifications, collaborative editing.

### WebSocket Pattern

```tsx
// hooks/use-realtime.ts
"use client";

import { useEffect, useRef, useState, useCallback } from "react";

interface UseRealtimeOptions<T> {
  url: string;
  onMessage: (data: T) => void;
  reconnectInterval?: number;
  maxReconnects?: number;
}

export function useRealtime<T>({
  url,
  onMessage,
  reconnectInterval = 3000,
  maxReconnects = 5,
}: UseRealtimeOptions<T>) {
  const [isConnected, setIsConnected] = useState(false);
  const [reconnectCount, setReconnectCount] = useState(0);
  const wsRef = useRef<WebSocket | null>(null);
  const reconnectTimerRef = useRef<NodeJS.Timeout | null>(null);

  const connect = useCallback(() => {
    if (wsRef.current?.readyState === WebSocket.OPEN) return;

    const ws = new WebSocket(url);
    wsRef.current = ws;

    ws.onopen = () => {
      setIsConnected(true);
      setReconnectCount(0);
    };

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      onMessage(data);
    };

    ws.onclose = () => {
      setIsConnected(false);
      if (reconnectCount < maxReconnects) {
        reconnectTimerRef.current = setTimeout(() => {
          setReconnectCount((prev) => prev + 1);
          connect();
        }, reconnectInterval);
      }
    };

    ws.onerror = () => {
      ws.close();
    };
  }, [url, onMessage, reconnectInterval, maxReconnects, reconnectCount]);

  useEffect(() => {
    connect();
    return () => {
      wsRef.current?.close();
      if (reconnectTimerRef.current) clearTimeout(reconnectTimerRef.current);
    };
  }, [connect]);

  const send = useCallback((data: unknown) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify(data));
    }
  }, []);

  return { isConnected, send, reconnectCount };
}
```

### Server-Sent Events (Simpler Alternative)

```tsx
// hooks/use-sse.ts
"use client";

import { useEffect, useRef, useState, useCallback } from "react";

export function useSSE<T>(url: string, onMessage: (data: T) => void) {
  const [isConnected, setIsConnected] = useState(false);
  const esRef = useRef<EventSource | null>(null);

  useEffect(() => {
    const es = new EventSource(url);
    esRef.current = es;

    es.onopen = () => setIsConnected(true);
    es.onmessage = (event) => {
      const data = JSON.parse(event.data);
      onMessage(data);
    };
    es.onerror = () => setIsConnected(false);

    return () => {
      es.close();
    };
  }, [url, onMessage]);

  return { isConnected };
}
```

### When to Use What

| Scenario | Best Approach | Why |
|---|---|---|
| Chat, live collaboration | WebSocket | Bidirectional, low latency |
| Notifications, live feed | SSE | Simpler, auto-reconnects |
| Dashboard updates | Polling (30s) | Simple, no server changes |
| Presence indicators | WebSocket | Real-time, frequent updates |
| Stock prices, sports scores | WebSocket | Sub-second updates |

---

## Data Display Anti-Patterns

### ❌ Rendering Thousands of DOM Nodes
```tsx
// BAD: 10,000 divs will freeze the browser
{items.map(item => <div key={item.id}>{item.name}</div>)}

// GOOD: Virtualize
<VirtualList items={items} itemHeight={40} renderItem={(item) => <div>{item.name}</div>} />
```

### ❌ Loading Everything at Once
```tsx
// BAD: Fetches 10,000 records
const { data } = useQuery({ queryKey: ["items"], queryFn: () => fetch("/api/items") });

// GOOD: Paginate or infinite scroll
const { data, fetchNextPage, hasNextPage } = useInfiniteQuery({
  queryKey: ["items"],
  queryFn: ({ pageParam }) => fetch(`/api/items?page=${pageParam}`),
  getNextPageParam: (lastPage) => lastPage.nextPage,
});
```

### ❌ Not Handling Empty States
```tsx
// BAD: Blank page when no data
{data?.map(item => <Item key={item.id} item={item} />)}

// GOOD: Always handle empty
{!data || data.length === 0 ? (
  <EmptyState title="No items found" action={{ label: "Create one", onClick: create }} />
) : (
  data.map(item => <Item key={item.id} item={item} />)
)}
```

---

## Data Display Selection Guide

| Data Shape | Best Pattern |
|---|---|
| Flat list, < 200 items | Regular map() |
| Flat list, 200+ items | Virtual list |
| Flat list, paginated | Server-side pagination |
| Nested/hierarchical | Tree view |
| Cards/images | Responsive grid |
| Variable height cards | Masonry |
| Tabular data | Data table |
| Trends over time | Line chart |
| Comparisons | Bar chart |
| Proportions | Pie/donut chart |
| Live updates | WebSocket or SSE |
| Geographic | Map |
