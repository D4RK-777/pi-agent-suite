# Observability Patterns

Tracing, structured logging, metrics collection, SLO/SLI patterns.

---

## 1. Distributed Tracing

### When to Use
- Multi-service requests
- Identifying bottlenecks
- Understanding request flow

### Trace Context Propagation

```ts
// lib/tracing.ts
import { AsyncLocalStorage } from "async_hooks";

interface TraceContext {
  traceId: string;
  spanId: string;
  parentSpanId?: string;
  attributes: Record<string, string>;
}

export const traceStorage = new AsyncLocalStorage<TraceContext>();

export function createTraceContext(): TraceContext {
  return {
    traceId: crypto.randomUUID(),
    spanId: crypto.randomUUID(),
    attributes: {},
  };
}

export function createChildSpan(parent: TraceContext): TraceContext {
  return {
    traceId: parent.traceId,
    spanId: crypto.randomUUID(),
    parentSpanId: parent.spanId,
    attributes: { ...parent.attributes },
  };
}

export function getCurrentTrace(): TraceContext | undefined {
  return traceStorage.getStore();
}
```

### Middleware Integration

```ts
// lib/api/tracing-middleware.ts
import { NextRequest, NextResponse } from "next/server";
import { traceStorage, createTraceContext } from "@/lib/tracing";
import { logger } from "@/lib/logger";

export async function withTracing(
  request: NextRequest,
  handler: () => Promise<NextResponse>
): Promise<NextResponse> {
  const traceId = request.headers.get("x-trace-id") || crypto.randomUUID();
  const context = {
    traceId,
    spanId: crypto.randomUUID(),
    attributes: {
      method: request.method,
      path: request.nextUrl.pathname,
    },
  };

  const start = Date.now();

  return traceStorage.run(context, async () => {
    const response = await handler();
    const duration = Date.now() - start;

    response.headers.set("x-trace-id", traceId);

    logger.info({
      traceId,
      message: `${request.method} ${request.nextUrl.pathname}`,
      duration,
      statusCode: response.status,
    });

    return response;
  });
}
```

### Outbound Request Tracing

```ts
// lib/api/traced-fetch.ts
import { getCurrentTrace } from "@/lib/tracing";

export async function tracedFetch(url: string, options: RequestInit = {}): Promise<Response> {
  const trace = getCurrentTrace();

  const headers = new Headers(options.headers);
  if (trace) {
    headers.set("x-trace-id", trace.traceId);
    headers.set("x-parent-span-id", trace.spanId);
  }

  const start = Date.now();
  const response = await fetch(url, { ...options, headers });
  const duration = Date.now() - start;

  if (trace) {
    logger.info({
      traceId: trace.traceId,
      message: `OUTBOUND ${url}`,
      duration,
      statusCode: response.status,
    });
  }

  return response;
}
```

---

## 2. Structured Logging

### Log Levels

| Level | When to Use | Example |
|---|---|---|
| `DEBUG` | Detailed diagnostic info | Query parameters, cache hits |
| `INFO` | Normal operational info | Request completed, user created |
| `WARN` | Unexpected but handled | Deprecated API used, slow query |
| `ERROR` | Operation failed | Database connection lost, API error |
| `FATAL` | System unusable | Out of memory, config invalid |

### Structured Log Pattern

```ts
// lib/logger.ts
export interface LogEntry {
  timestamp: string;
  level: "debug" | "info" | "warn" | "error" | "fatal";
  message: string;
  service: string;
  traceId?: string;
  userId?: string;
  requestId?: string;
  duration?: number;
  [key: string]: unknown;
}

function formatLog(entry: LogEntry): string {
  return JSON.stringify({
    ...entry,
    timestamp: entry.timestamp || new Date().toISOString(),
    service: entry.service || process.env.SERVICE_NAME || "unknown",
  });
}

export const logger = {
  debug(entry: Omit<LogEntry, "level" | "timestamp" | "service">) {
    if (process.env.LOG_LEVEL === "debug") {
      console.debug(formatLog({ ...entry, level: "debug" }));
    }
  },
  info(entry: Omit<LogEntry, "level" | "timestamp" | "service">) {
    console.log(formatLog({ ...entry, level: "info" }));
  },
  warn(entry: Omit<LogEntry, "level" | "timestamp" | "service">) {
    console.warn(formatLog({ ...entry, level: "warn" }));
  },
  error(entry: Omit<LogEntry, "level" | "timestamp" | "service">) {
    console.error(formatLog({ ...entry, level: "error" }));
  },
  fatal(entry: Omit<LogEntry, "level" | "timestamp" | "service">) {
    console.error(formatLog({ ...entry, level: "fatal" }));
    process.exit(1);
  },
};
```

### Usage Patterns

```ts
// Good: Structured, searchable logs
logger.info({
  message: "User created",
  userId: user.id,
  email: user.email,
  duration: 150,
});

// Bad: Unstructured, hard to search
console.log(`User ${user.id} created at ${new Date().toISOString()}`);
```

---

## 3. Metrics Collection

### Counter Pattern

```ts
// lib/metrics.ts
class MetricsCollector {
  private counters = new Map<string, number>();
  private histograms = new Map<string, number[]>();
  private gauges = new Map<string, number>();

  increment(name: string, value: number = 1) {
    const current = this.counters.get(name) || 0;
    this.counters.set(name, current + value);
  }

  histogram(name: string, value: number) {
    const values = this.histograms.get(name) || [];
    values.push(value);
    this.histograms.set(name, values);
  }

  gauge(name: string, value: number) {
    this.gauges.set(name, value);
  }

  getCounter(name: string): number {
    return this.counters.get(name) || 0;
  }

  getHistogramPercentile(name: string, percentile: number): number {
    const values = this.histograms.get(name) || [];
    if (values.length === 0) return 0;
    values.sort((a, b) => a - b);
    const index = Math.ceil((percentile / 100) * values.length) - 1;
    return values[index];
  }

  reset() {
    this.counters.clear();
    this.histograms.clear();
    this.gauges.clear();
  }
}

export const metrics = new MetricsCollector();
```

### Key Metrics to Track

```ts
// Request metrics
metrics.increment("http.requests.total");
metrics.histogram("http.request.duration", duration);
metrics.increment(`http.responses.${statusCode}`);

// Business metrics
metrics.increment("users.created");
metrics.increment("orders.completed");
metrics.increment("payments.processed");

// Error metrics
metrics.increment("errors.database");
metrics.increment("errors.external_api");
metrics.increment("errors.validation");
```

### Prometheus Export

```ts
// app/api/metrics/route.ts
import { NextResponse } from "next/server";
import { metrics } from "@/lib/metrics";

export async function GET() {
  const lines: string[] = [];

  // Export counters
  for (const [name, value] of metrics.counters) {
    lines.push(`${name.replace(/\./g, "_")} ${value}`);
  }

  // Export histogram percentiles
  for (const [name] of metrics.histograms) {
    const p50 = metrics.getHistogramPercentile(name, 50);
    const p95 = metrics.getHistogramPercentile(name, 95);
    const p99 = metrics.getHistogramPercentile(name, 99);
    lines.push(`${name.replace(/\./g, "_")}_p50 ${p50}`);
    lines.push(`${name.replace(/\./g, "_")}_p95 ${p95}`);
    lines.push(`${name.replace(/\./g, "_")}_p99 ${p99}`);
  }

  return new Response(lines.join("\n") + "\n", {
    headers: { "Content-Type": "text/plain" },
  });
}
```

---

## 4. SLO/SLI Patterns

### Definitions

| Term | Definition | Example |
|---|---|---|
| **SLI** (Service Level Indicator) | What you measure | Request latency, error rate |
| **SLO** (Service Level Objective) | Target for the SLI | 99.9% of requests < 200ms |
| **SLA** (Service Level Agreement) | Contract with users | 99.9% uptime or credit |
| **Error Budget** | 100% - SLO | 0.1% = 43 minutes/month |

### Common SLOs

| Service | SLI | SLO | Error Budget |
|---|---|---|---|
| API | Availability | 99.9% | 43 min/month |
| API | Latency (p95) | < 200ms | N/A |
| API | Error rate | < 0.1% | N/A |
| Database | Availability | 99.99% | 4 min/month |
| Frontend | Page load (p95) | < 3s | N/A |

### SLO Monitoring

```ts
// lib/slo.ts
interface SLO {
  name: string;
  target: number; // percentage
  window: number; // milliseconds
  measure: () => Promise<number>;
}

export const apiSLOs: SLO[] = [
  {
    name: "api_availability",
    target: 99.9,
    window: 30 * 24 * 60 * 60 * 1000, // 30 days
    measure: async () => {
      const total = metrics.getCounter("http_requests_total");
      const errors = metrics.getCounter("http_errors_5xx");
      return total > 0 ? ((total - errors) / total) * 100 : 100;
    },
  },
  {
    name: "api_latency_p95",
    target: 95, // 95% of requests under threshold
    window: 60 * 60 * 1000, // 1 hour
    measure: async () => {
      return metrics.getHistogramPercentile("http_request_duration", 95);
    },
  },
];

export async function checkSLOs(): Promise<{ name: string; met: boolean; actual: number; target: number }[]> {
  const results = [];
  for (const slo of apiSLOs) {
    const actual = await slo.measure();
    results.push({
      name: slo.name,
      met: actual >= slo.target,
      actual,
      target: slo.target,
    });
  }
  return results;
}
```

---

## Observability Selection Guide

| Scenario | Best Approach |
|---|---|
| Single service | Structured logging + basic metrics |
| Multi-service | Distributed tracing + centralized logs |
| High-traffic | Sampling + aggregation + SLOs |
| Compliance | Audit logs + retention + access controls |
| On-call | Alerting + runbooks + dashboards |

---

## Observability Anti-Patterns

### ❌ Logging Everything
```ts
// BAD: Too much noise
logger.debug({ query: sql, params, result: rows });

// GOOD: Log what matters
logger.info({ message: "Query completed", duration, rowCount });
```

### ❌ No Trace Correlation
```ts
// BAD: Each log is isolated
console.log("Request received");
console.log("Database query");
console.log("Response sent");

// GOOD: Correlated by trace ID
logger.info({ traceId, message: "Request received" });
logger.info({ traceId, message: "Database query", duration });
logger.info({ traceId, message: "Response sent", statusCode });
```

### ❌ Vanity Metrics
```ts
// BAD: Total requests (always increasing)
metrics.increment("total_requests");

// GOOD: Rate-based metrics
metrics.increment("requests_per_minute");
metrics.histogram("request_duration_p95");
```

### ❌ No Error Budget
```
BAD: "We need 100% uptime" (impossible, expensive)
GOOD: "We have 43 minutes of error budget this month" (realistic, actionable)
```
