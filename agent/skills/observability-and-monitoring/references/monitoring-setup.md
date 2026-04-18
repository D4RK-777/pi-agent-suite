# Monitoring Setup

Health checks, alerting thresholds, log aggregation, dashboard patterns.

---

## 1. Health Check Endpoints

### Core Pattern

```ts
// app/api/health/route.ts
import { NextResponse } from "next/server";
import { db } from "@/lib/db";
import { redis } from "@/lib/redis";

export async function GET() {
  const checks: Record<string, { status: string; latency?: number }> = {};

  // Database check
  try {
    const start = Date.now();
    await db.execute(sql`SELECT 1`);
    checks.database = { status: "healthy", latency: Date.now() - start };
  } catch {
    checks.database = { status: "unhealthy" };
  }

  // Redis check
  try {
    const start = Date.now();
    await redis.ping();
    checks.redis = { status: "healthy", latency: Date.now() - start };
  } catch {
    checks.redis = { status: "unhealthy" };
  }

  const isHealthy = Object.values(checks).every(c => c.status === "healthy");

  return NextResponse.json(
    {
      status: isHealthy ? "healthy" : "degraded",
      timestamp: new Date().toISOString(),
      checks,
    },
    { status: isHealthy ? 200 : 503 }
  );
}
```

### Kubernetes Health Probes

```yaml
# deployment.yaml
livenessProbe:
  httpGet:
    path: /api/health
    port: 3000
  initialDelaySeconds: 30
  periodSeconds: 10
  timeoutSeconds: 5
  failureThreshold: 3

readinessProbe:
  httpGet:
    path: /api/health
    port: 3000
  initialDelaySeconds: 5
  periodSeconds: 5
  timeoutSeconds: 3
  failureThreshold: 3
```

---

## 2. Alerting Thresholds

### Response Time Alerts

| Metric | Warning | Critical | Action |
|---|---|---|---|
| p50 response time | > 200ms | > 500ms | Investigate slow queries |
| p95 response time | > 500ms | > 2s | Scale up or optimize |
| p99 response time | > 1s | > 5s | Immediate investigation |

### Error Rate Alerts

| Metric | Warning | Critical | Action |
|---|---|---|---|
| 5xx rate | > 1% | > 5% | Check recent deployments |
| 4xx rate | > 10% | > 25% | Check for broken links/clients |
| Timeout rate | > 0.5% | > 2% | Check downstream dependencies |

### Resource Alerts

| Metric | Warning | Critical | Action |
|---|---|---|---|
| CPU usage | > 70% | > 90% | Scale up or optimize |
| Memory usage | > 75% | > 90% | Check for memory leaks |
| Disk usage | > 70% | > 85% | Clean up or expand volume |
| Connection pool | > 80% | > 95% | Increase pool size |

### Business Alerts

| Metric | Warning | Critical | Action |
|---|---|---|---|
| Failed logins/min | > 50 | > 200 | Check for brute force |
| Orders/min | < 50% of baseline | < 25% of baseline | Check checkout flow |
| Active users | < 70% of expected | < 50% of expected | Check frontend errors |

---

## 3. Log Aggregation

### Structured Logging

```ts
// lib/logger.ts
export interface LogEntry {
  timestamp: string;
  level: "info" | "warn" | "error" | "fatal";
  message: string;
  service: string;
  traceId?: string;
  userId?: string;
  requestId?: string;
  duration?: number;
  [key: string]: unknown;
}

export const logger = {
  info(entry: Omit<LogEntry, "level" | "timestamp" | "service">) {
    console.log(JSON.stringify({
      ...entry,
      level: "info",
      timestamp: new Date().toISOString(),
      service: process.env.SERVICE_NAME || "api",
    }));
  },
  warn(entry: Omit<LogEntry, "level" | "timestamp" | "service">) {
    console.warn(JSON.stringify({
      ...entry,
      level: "warn",
      timestamp: new Date().toISOString(),
      service: process.env.SERVICE_NAME || "api",
    }));
  },
  error(entry: Omit<LogEntry, "level" | "timestamp" | "service">) {
    console.error(JSON.stringify({
      ...entry,
      level: "error",
      timestamp: new Date().toISOString(),
      service: process.env.SERVICE_NAME || "api",
    }));
  },
};
```

### Request Logging Middleware

```ts
// lib/api/request-logger.ts
import { NextRequest, NextResponse } from "next/server";
import { logger } from "@/lib/logger";

export async function logRequest(
  request: NextRequest,
  response: NextResponse,
  duration: number
) {
  const traceId = request.headers.get("x-trace-id") || crypto.randomUUID();
  const userId = request.headers.get("x-user-id") || undefined;

  const level = response.status >= 500 ? "error" : response.status >= 400 ? "warn" : "info";

  logger[level]({
    traceId,
    userId,
    message: `${request.method} ${request.nextUrl.pathname}`,
    method: request.method,
    path: request.nextUrl.pathname,
    statusCode: response.status,
    duration,
    userAgent: request.headers.get("user-agent") || undefined,
    ip: request.ip || undefined,
  });
}
```

### Log Query Patterns

```bash
# Find all errors for a specific user
jq 'select(.userId == "user-123" and .level == "error")' app.log

# Find slow requests (> 1s)
jq 'select(.duration > 1000)' app.log | jq -s 'sort_by(.duration) | reverse | .[:10]'

# Find error rate by endpoint
jq 'select(.level == "error")' app.log | jq -r '.path' | sort | uniq -c | sort -rn

# Find trace of a specific request
jq 'select(.traceId == "abc-123")' app.log
```

---

## 4. Dashboard Patterns

### Service Health Dashboard

```
┌─────────────────────────────────────────────────────────────┐
│  Service Health Dashboard                    Last 1 hour    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Requests/sec    ████████████████████░░░░  1,234/s         │
│  Error Rate      ████░░░░░░░░░░░░░░░░░░░░  0.3%            │
│  p95 Latency     ████████████░░░░░░░░░░░░  245ms           │
│  CPU Usage       ████████████░░░░░░░░░░░░  45%             │
│  Memory Usage    ████████████████░░░░░░░░  62%             │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  Top Endpoints (by latency)                                 │
│  POST /api/orders      p95: 450ms  ████████████████         │
│  GET  /api/products    p95: 120ms  ████                     │
│  GET  /api/users       p95: 85ms   ███                      │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  Recent Errors                                              │
│  14:32  POST /api/orders  500  "Database connection timeout" │
│  14:28  GET /api/users   502  "Upstream service unavailable"│
│  14:15  POST /api/login  429  "Rate limit exceeded"         │
└─────────────────────────────────────────────────────────────┘
```

### Deployment Dashboard

```
┌─────────────────────────────────────────────────────────────┐
│  Deployment Status                                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  v2.4.1  ✅  Deployed 14:00  Error rate: 0.2%              │
│  v2.4.0  ✅  Deployed 12:00  Error rate: 0.3%              │
│  v2.3.9  ✅  Deployed 09:00  Error rate: 0.5%              │
│                                                             │
│  Current: v2.4.1  |  Uptime: 99.97%  |  Rollbacks: 0       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Monitoring Selection Guide

| Scenario | Best Approach |
|---|---|
| Simple app | Health endpoint + error logs |
| Production app | Health + metrics + alerts |
| Multi-service | Distributed tracing + centralized logs |
| High-traffic | Sampling + aggregation + dashboards |
| Compliance | Audit logs + retention + access controls |

---

## Monitoring Anti-Patterns

### ❌ Alert Fatigue
```
BAD: Alert on every 404 (expected behavior for missing resources)
GOOD: Alert on 5xx rate > 1% (indicates real problems)
```

### ❌ No Baseline
```
BAD: "CPU is at 60%" — is that normal?
GOOD: "CPU is 3x the baseline of 20%" — clear anomaly
```

### ❌ Missing Context
```
BAD: "Error: connection refused" — where? when? why?
GOOD: "Error: connection refused to postgres:5432 at 14:32, 3rd attempt, after deployment v2.4.1"
```

### ❌ No Runbook
```
BAD: Alert fires, nobody knows what to do
GOOD: Alert includes link to runbook with step-by-step resolution
```
