# Middleware Patterns

Auth middleware, error handling, rate limiting, request logging, CORS.

---

## 1. Auth Middleware

**When:** Protecting API routes — verifying tokens, checking permissions.

### Core Pattern (Next.js Middleware)

```ts
// middleware.ts
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { jwtVerify } from "jose";

const JWT_SECRET = new TextEncoder().encode(process.env.JWT_SECRET);

// Route definitions
const publicRoutes = ["/api/health", "/api/auth/login", "/api/auth/register"];
const adminRoutes = ["/api/admin"];
const protectedRoutes = ["/api/users", "/api/orders", "/api/settings"];

export async function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;

  // Skip public routes
  if (publicRoutes.some(route => pathname.startsWith(route))) {
    return NextResponse.next();
  }

  // Extract token
  const authHeader = request.headers.get("authorization");
  const token = authHeader?.startsWith("Bearer ") ? authHeader.slice(7) : null;

  if (!token) {
    return NextResponse.json(
      { error: "Authentication required", code: "UNAUTHORIZED" },
      { status: 401 }
    );
  }

  // Verify token
  try {
    const { payload } = await jwtVerify(token, JWT_SECRET);
    const userId = payload.sub;
    const role = payload.role as string;

    // Check admin routes
    if (adminRoutes.some(route => pathname.startsWith(route)) && role !== "admin") {
      return NextResponse.json(
        { error: "Admin access required", code: "FORBIDDEN" },
        { status: 403 }
      );
    }

    // Add user info to request headers for downstream use
    const requestHeaders = new Headers(request.headers);
    requestHeaders.set("x-user-id", userId as string);
    requestHeaders.set("x-user-role", role);

    return NextResponse.next({ request: { headers: requestHeaders } });
  } catch (error) {
    return NextResponse.json(
      { error: "Invalid or expired token", code: "UNAUTHORIZED" },
      { status: 401 }
    );
  }
}

export const config = {
  matcher: ["/api/:path*"],
};
```

### Route-Level Auth Helper

```ts
// lib/auth/helpers.ts
import { headers } from "next/headers";

export async function getCurrentUser() {
  const h = await headers();
  const userId = h.get("x-user-id");
  const role = h.get("x-user-role");

  if (!userId) return null;

  return { id: userId, role: role || "user" };
}

export async function requireAuth() {
  const user = await getCurrentUser();
  if (!user) throw new Error("Unauthorized");
  return user;
}

export async function requireAdmin() {
  const user = await getCurrentUser();
  if (!user || user.role !== "admin") throw new Error("Forbidden");
  return user;
}

// Usage in route handler
export async function GET() {
  try {
    const user = await requireAdmin();
    // ... admin-only logic
  } catch (error) {
    if (error.message === "Unauthorized") return unauthorized();
    if (error.message === "Forbidden") return forbidden();
    throw error;
  }
}
```

---

## 2. Error Handling Middleware

**When:** Centralized error catching — consistent error responses, logging, trace IDs.

### Global Error Handler

```ts
// lib/api/error-handler.ts
import { NextResponse } from "next/server";

export interface ApiError extends Error {
  statusCode?: number;
  code?: string;
  isOperational?: boolean; // true = expected error, false = bug
}

export function handleApiError(error: unknown, traceId?: string): NextResponse {
  const trace = traceId || crypto.randomUUID();

  if (error instanceof ApiError && error.isOperational) {
    // Expected error — return user-friendly message
    return NextResponse.json(
      {
        error: error.message,
        code: error.code || "API_ERROR",
        traceId: trace,
      },
      { status: error.statusCode || 500 }
    );
  }

  // Unexpected error — log details, return generic message
  console.error(`[API Error ${trace}]`, error);

  return NextResponse.json(
    {
      error: "An unexpected error occurred",
      code: "INTERNAL_ERROR",
      traceId: trace,
    },
    { status: 500 }
  );
}

// Custom error classes
export class BadRequestError extends ApiError {
  constructor(message: string) {
    super(message);
    this.statusCode = 400;
    this.code = "BAD_REQUEST";
    this.isOperational = true;
  }
}

export class NotFoundError extends ApiError {
  constructor(resource: string) {
    super(`${resource} not found`);
    this.statusCode = 404;
    this.code = "NOT_FOUND";
    this.isOperational = true;
  }
}

export class UnauthorizedError extends ApiError {
  constructor(message = "Authentication required") {
    super(message);
    this.statusCode = 401;
    this.code = "UNAUTHORIZED";
    this.isOperational = true;
  }
}

export class ForbiddenError extends ApiError {
  constructor(message = "Insufficient permissions") {
    super(message);
    this.statusCode = 403;
    this.code = "FORBIDDEN";
    this.isOperational = true;
  }
}

export class ConflictError extends ApiError {
  constructor(message: string) {
    super(message);
    this.statusCode = 409;
    this.code = "CONFLICT";
    this.isOperational = true;
  }
}
```

### Route Wrapper Pattern

```ts
// lib/api/route-wrapper.ts
import { NextRequest, NextResponse } from "next/server";
import { handleApiError } from "./error-handler";

type RouteHandler = (request: NextRequest, params?: any) => Promise<NextResponse>;

export function withErrorHandling(handler: RouteHandler): RouteHandler {
  return async (request: NextRequest, params?: any) => {
    try {
      return await handler(request, params);
    } catch (error) {
      return handleApiError(error);
    }
  };
}

// Usage
export const GET = withErrorHandling(async (request: NextRequest) => {
  const users = await userRepository.list({});
  return NextResponse.json(users);
});
```

---

## 3. Rate Limiting

**When:** Preventing abuse — login attempts, API abuse, scraping.

### In-Memory Rate Limiter (Single Server)

```ts
// lib/rate-limiter.ts
interface RateLimitEntry {
  count: number;
  resetAt: number;
}

const store = new Map<string, RateLimitEntry>();

export interface RateLimitConfig {
  windowMs: number;    // Window size in ms
  maxRequests: number; // Max requests per window
}

export function rateLimit(key: string, config: RateLimitConfig): { allowed: boolean; remaining: number; resetAt: number } {
  const now = Date.now();
  const entry = store.get(key);

  if (!entry || now > entry.resetAt) {
    // New window
    store.set(key, { count: 1, resetAt: now + config.windowMs });
    return { allowed: true, remaining: config.maxRequests - 1, resetAt: now + config.windowMs };
  }

  if (entry.count >= config.maxRequests) {
    return { allowed: false, remaining: 0, resetAt: entry.resetAt };
  }

  entry.count++;
  return { allowed: true, remaining: config.maxRequests - entry.count, resetAt: entry.resetAt };
}

// Cleanup old entries periodically
setInterval(() => {
  const now = Date.now();
  for (const [key, entry] of store.entries()) {
    if (now > entry.resetAt) store.delete(key);
  }
}, 60_000); // Every minute
```

### Redis-Based Rate Limiter (Multi-Server)

```ts
// lib/rate-limiter-redis.ts
import { Redis } from "@upstash/redis";

const redis = new Redis({
  url: process.env.UPSTASH_REDIS_REST_URL,
  token: process.env.UPSTASH_REDIS_REST_TOKEN,
});

export async function checkRateLimit(
  key: string,
  { windowMs, maxRequests }: RateLimitConfig
) {
  const now = Date.now();
  const windowKey = `ratelimit:${key}:${Math.floor(now / windowMs)}`;

  const multi = redis.multi();
  multi.incr(windowKey);
  multi.expire(windowKey, Math.ceil(windowMs / 1000));

  const [count] = await multi.exec<number[]>();
  const current = count || 0;

  return {
    allowed: current <= maxRequests,
    remaining: Math.max(0, maxRequests - current),
    limit: maxRequests,
    resetAt: now + windowMs,
  };
}
```

### Usage in Routes

```ts
// app/api/auth/login/route.ts
import { rateLimit } from "@/lib/rate-limiter";

export async function POST(request: NextRequest) {
  const ip = request.ip || request.headers.get("x-forwarded-for") || "unknown";
  const limit = rateLimit(`login:${ip}`, { windowMs: 15 * 60 * 1000, maxRequests: 5 });

  if (!limit.allowed) {
    return NextResponse.json(
      { error: "Too many login attempts. Try again later.", code: "RATE_LIMITED" },
      {
        status: 429,
        headers: {
          "Retry-After": String(Math.ceil((limit.resetAt - Date.now()) / 1000)),
          "X-RateLimit-Limit": String(limit.limit),
          "X-RateLimit-Remaining": String(limit.remaining),
        },
      }
    );
  }

  // ... login logic
}
```

---

## 4. Request Logging

**When:** Debugging, auditing, monitoring — structured logs for every request.

### Structured Logger

```ts
// lib/logger.ts
export interface LogEntry {
  timestamp: string;
  level: "info" | "warn" | "error";
  message: string;
  method?: string;
  path?: string;
  statusCode?: number;
  duration?: number;
  userId?: string;
  traceId?: string;
  [key: string]: unknown;
}

function formatLog(entry: LogEntry): string {
  return JSON.stringify({
    ...entry,
    timestamp: entry.timestamp || new Date().toISOString(),
  });
}

export const logger = {
  info(entry: Omit<LogEntry, "level">) {
    console.log(formatLog({ ...entry, level: "info" }));
  },
  warn(entry: Omit<LogEntry, "level">) {
    console.warn(formatLog({ ...entry, level: "warn" }));
  },
  error(entry: Omit<LogEntry, "level">) {
    console.error(formatLog({ ...entry, level: "error" }));
  },
};

// Request logging middleware
export async function logRequest(
  request: NextRequest,
  response: NextResponse,
  duration: number
) {
  const traceId = request.headers.get("x-trace-id") || crypto.randomUUID();
  const userId = request.headers.get("x-user-id") || undefined;

  logger.info({
    traceId,
    userId,
    method: request.method,
    path: request.nextUrl.pathname,
    statusCode: response.status,
    duration,
    userAgent: request.headers.get("user-agent") || undefined,
    ip: request.ip || undefined,
  });
}
```

### Usage with Route Wrapper

```ts
// lib/api/route-wrapper.ts (updated)
export function withLogging(handler: RouteHandler): RouteHandler {
  return async (request: NextRequest, params?: any) => {
    const start = Date.now();
    const traceId = crypto.randomUUID();

    const requestHeaders = new Headers(request.headers);
    requestHeaders.set("x-trace-id", traceId);

    const response = await handler(
      new NextRequest(request.url, { headers: requestHeaders, ...request }),
      params
    );

    const duration = Date.now() - start;
    await logRequest(request, response, duration);

    return response;
  };
}
```

---

## 5. CORS Configuration

**When:** API accessed from different origins — frontend on different domain, mobile apps.

### CORS Middleware

```ts
// lib/api/cors.ts
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

interface CorsConfig {
  allowedOrigins: string[];
  allowedMethods: string[];
  allowedHeaders: string[];
  maxAge?: number;
  credentials?: boolean;
}

const defaultConfig: CorsConfig = {
  allowedOrigins: process.env.ALLOWED_ORIGINS?.split(",") || ["http://localhost:3000"],
  allowedMethods: ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
  allowedHeaders: ["Content-Type", "Authorization", "X-Requested-With"],
  maxAge: 86400, // 24 hours
  credentials: true,
};

export function cors(request: NextRequest, config: Partial<CorsConfig> = {}) {
  const cfg = { ...defaultConfig, ...config };
  const origin = request.headers.get("origin");

  const response = NextResponse.next();

  // Check if origin is allowed
  if (origin && cfg.allowedOrigins.includes(origin)) {
    response.headers.set("Access-Control-Allow-Origin", origin);
  }

  if (cfg.credentials) {
    response.headers.set("Access-Control-Allow-Credentials", "true");
  }

  // Handle preflight
  if (request.method === "OPTIONS") {
    response.headers.set("Access-Control-Allow-Methods", cfg.allowedMethods.join(", "));
    response.headers.set("Access-Control-Allow-Headers", cfg.allowedHeaders.join(", "));
    if (cfg.maxAge) {
      response.headers.set("Access-Control-Max-Age", String(cfg.maxAge));
    }
    return new NextResponse(null, { status: 204, headers: response.headers });
  }

  response.headers.set("Access-Control-Expose-Headers", "X-RateLimit-Limit, X-RateLimit-Remaining");

  return response;
}
```

---

## Middleware Selection Guide

| Scenario | Best Pattern |
|---|---|
| Route protection | Auth middleware (middleware.ts) |
| Consistent errors | Error handler wrapper |
| API abuse prevention | Rate limiter (Redis for production) |
| Debugging/auditing | Structured request logging |
| Cross-origin access | CORS middleware |
| Request validation | Zod schema validation before handler |
| Response compression | Next.js built-in or edge middleware |
| Caching | Cache-Control headers + CDN |

---

## Middleware Anti-Patterns

### ❌ Scattered Auth Checks
```ts
// BAD: Auth logic duplicated in every route
const session = await auth();
if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

// GOOD: Centralized middleware
// middleware.ts handles it once for all protected routes
```

### ❌ Swallowing Errors
```ts
// BAD: Silent failures
try {
  await doSomething();
} catch (e) {
  // Nothing logged
}

// GOOD: Structured error handling
catch (error) {
  logger.error({ message: "Failed to do something", error: String(error), traceId });
  return internalError("Operation failed", traceId);
}
```

### ❌ No Rate Limits on Auth Endpoints
```ts
// BAD: Unlimited login attempts — brute force vulnerable
export async function POST(request: NextRequest) {
  const { email, password } = await request.json();
  // ... login logic
}

// GOOD: Rate limited
export async function POST(request: NextRequest) {
  const limit = checkRateLimit(`login:${request.ip}`, { windowMs: 900000, maxRequests: 5 });
  if (!limit.allowed) return rateLimited(limit.resetAt);
  // ... login logic
}
```
