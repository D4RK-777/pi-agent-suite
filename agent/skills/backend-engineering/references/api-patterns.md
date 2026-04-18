# API Patterns

Concrete, production-ready patterns for REST APIs, pagination, filtering, error responses, and versioning.

---

## 1. REST Resource Controller

**When:** CRUD endpoints for any resource — users, products, orders, posts.

### Core Pattern (Next.js Route Handlers)

```ts
// app/api/users/route.ts
import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { db } from "@/lib/db";
import { users } from "@/lib/db/schema";
import { eq } from "drizzle-orm";
import { auth } from "@/lib/auth";

// Request schemas
const createUserSchema = z.object({
  name: z.string().min(2).max(100),
  email: z.string().email(),
  role: z.enum(["user", "admin"]).default("user"),
});

const updateUserSchema = createUserSchema.partial();

// GET /api/users — List with pagination
export async function GET(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url);
    const page = parseInt(searchParams.get("page") || "1", 10);
    const limit = parseInt(searchParams.get("limit") || "20", 10);
    const search = searchParams.get("search") || "";
    const sort = searchParams.get("sort") || "createdAt";
    const order = searchParams.get("order") === "asc" ? "asc" : "desc";

    // Validate pagination
    if (page < 1 || limit < 1 || limit > 100) {
      return NextResponse.json(
        { error: "Invalid pagination. page >= 1, 1 <= limit <= 100" },
        { status: 400 }
      );
    }

    const offset = (page - 1) * limit;

    // Build query
    let query = db.select().from(users);

    if (search) {
      query = query.where(
        users.name.like(`%${search}%`).or(users.email.like(`%${search}%`))
      );
    }

    // Get total count for pagination metadata
    const [{ count }] = await db.select({ count: users.id }).from(users);

    const results = await query.limit(limit).offset(offset).orderBy(
      order === "asc" ? users[sort as keyof typeof users] : users[sort as keyof typeof users].desc()
    );

    return NextResponse.json({
      data: results,
      meta: {
        page,
        limit,
        total: count,
        totalPages: Math.ceil(count / limit),
        hasNext: page * limit < count,
        hasPrev: page > 1,
      },
    });
  } catch (error) {
    console.error("Failed to fetch users:", error);
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 }
    );
  }
}

// POST /api/users — Create
export async function POST(request: NextRequest) {
  try {
    const session = await auth();
    if (!session?.user) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
    }

    const body = await request.json();
    const validated = createUserSchema.safeParse(body);

    if (!validated.success) {
      return NextResponse.json(
        {
          error: "Validation failed",
          details: validated.error.flatten().fieldErrors,
        },
        { status: 400 }
      );
    }

    const { name, email, role } = validated.data;

    // Check for duplicate email
    const existing = await db.select().from(users).where(eq(users.email, email)).limit(1);
    if (existing.length > 0) {
      return NextResponse.json(
        { error: "A user with this email already exists" },
        { status: 409 }
      );
    }

    const [newUser] = await db
      .insert(users)
      .values({ name, email, role, createdAt: new Date() })
      .returning();

    return NextResponse.json({ data: newUser }, { status: 201 });
  } catch (error) {
    console.error("Failed to create user:", error);
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 }
    );
  }
}
```

### Single Resource Pattern

```ts
// app/api/users/[id]/route.ts
import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { db } from "@/lib/db";
import { users } from "@/lib/db/schema";
import { eq } from "drizzle-orm";

const updateUserSchema = z.object({
  name: z.string().min(2).max(100).optional(),
  email: z.string().email().optional(),
  role: z.enum(["user", "admin"]).optional(),
});

// GET /api/users/[id]
export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  try {
    const { id } = await params;
    const [user] = await db.select().from(users).where(eq(users.id, id)).limit(1);

    if (!user) {
      return NextResponse.json(
        { error: "User not found" },
        { status: 404 }
      );
    }

    return NextResponse.json({ data: user });
  } catch (error) {
    console.error("Failed to fetch user:", error);
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 }
    );
  }
}

// PATCH /api/users/[id]
export async function PATCH(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  try {
    const { id } = await params;
    const body = await request.json();
    const validated = updateUserSchema.safeParse(body);

    if (!validated.success) {
      return NextResponse.json(
        {
          error: "Validation failed",
          details: validated.error.flatten().fieldErrors,
        },
        { status: 400 }
      );
    }

    const [updated] = await db
      .update(users)
      .set({ ...validated.data, updatedAt: new Date() })
      .where(eq(users.id, id))
      .returning();

    if (!updated) {
      return NextResponse.json(
        { error: "User not found" },
        { status: 404 }
      );
    }

    return NextResponse.json({ data: updated });
  } catch (error) {
    console.error("Failed to update user:", error);
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 }
    );
  }
}

// DELETE /api/users/[id]
export async function DELETE(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  try {
    const { id } = await params;
    const [deleted] = await db
      .delete(users)
      .where(eq(users.id, id))
      .returning();

    if (!deleted) {
      return NextResponse.json(
        { error: "User not found" },
        { status: 404 }
      );
    }

    return NextResponse.json({ data: { id: deleted.id } }, { status: 200 });
  } catch (error) {
    console.error("Failed to delete user:", error);
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 }
    );
  }
}
```

---

## 2. Standardized Error Responses

**When:** Every API endpoint — consistent error format for frontend consumption.

### Error Response Schema

```ts
// lib/api/errors.ts
import { NextResponse } from "next/server";

// Standard error format
export interface ApiError {
  error: string;           // Human-readable message
  code?: string;           // Machine-readable error code
  details?: Record<string, string[]>; // Field-level errors
  traceId?: string;        // For support/debugging
}

// Error factory functions
export function badRequest(message: string, details?: Record<string, string[]>) {
  return NextResponse.json<ApiError>(
    { error: message, code: "BAD_REQUEST", details },
    { status: 400 }
  );
}

export function unauthorized(message = "Authentication required") {
  return NextResponse.json<ApiError>(
    { error: message, code: "UNAUTHORIZED" },
    { status: 401 }
  );
}

export function forbidden(message = "Insufficient permissions") {
  return NextResponse.json<ApiError>(
    { error: message, code: "FORBIDDEN" },
    { status: 403 }
  );
}

export function notFound(resource: string) {
  return NextResponse.json<ApiError>(
    { error: `${resource} not found`, code: "NOT_FOUND" },
    { status: 404 }
  );
}

export function conflict(message: string) {
  return NextResponse.json<ApiError>(
    { error: message, code: "CONFLICT" },
    { status: 409 }
  );
}

export function rateLimited(retryAfter: number) {
  return NextResponse.json<ApiError>(
    { error: "Too many requests", code: "RATE_LIMITED" },
    {
      status: 429,
      headers: { "Retry-After": String(retryAfter) },
    }
  );
}

export function internalError(message = "Internal server error", traceId?: string) {
  console.error(`[${traceId || "unknown"}] ${message}`);
  return NextResponse.json<ApiError>(
    {
      error: message,
      code: "INTERNAL_ERROR",
      traceId,
    },
    { status: 500 }
  );
}

// Validation error helper
export function validationError(fieldErrors: Record<string, string[]>) {
  return NextResponse.json<ApiError>(
    {
      error: "Validation failed",
      code: "VALIDATION_ERROR",
      details: fieldErrors,
    },
    { status: 400 }
  );
}
```

### Usage in Routes

```ts
// app/api/orders/route.ts
import { badRequest, unauthorized, notFound, internalError, validationError } from "@/lib/api/errors";

export async function POST(request: NextRequest) {
  try {
    const session = await auth();
    if (!session?.user) return unauthorized();

    const body = await request.json();
    const validated = createOrderSchema.safeParse(body);
    if (!validated.success) {
      return validationError(validated.error.flatten().fieldErrors);
    }

    const product = await db.query.products.findFirst({
      where: eq(products.id, validated.data.productId),
    });
    if (!product) return notFound("Product");

    // ... create order

    return NextResponse.json({ data: order }, { status: 201 });
  } catch (error) {
    return internalError("Failed to create order", crypto.randomUUID());
  }
}
```

---

## 3. Pagination Patterns

### Cursor-Based Pagination (Better for infinite scroll)

```ts
// app/api/posts/route.ts
export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const limit = parseInt(searchParams.get("limit") || "20", 10);
  const cursor = searchParams.get("cursor"); // ISO timestamp or ID

  let query = db.select().from(posts).orderBy(posts.createdAt.desc()).limit(limit + 1);

  if (cursor) {
    query = query.where(lt(posts.createdAt, new Date(cursor)));
  }

  const results = await query;
  const hasNext = results.length > limit;
  const items = results.slice(0, limit);
  const nextCursor = hasNext ? items[items.length - 1].createdAt.toISOString() : null;

  return NextResponse.json({
    data: items,
    meta: {
      hasNext,
      nextCursor,
      limit,
    },
  });
}
```

### Offset vs Cursor Selection Guide

| Pattern | Best For | Pros | Cons |
|---|---|---|---|
| Offset (`page`/`limit`) | Admin tables, paginated views | Simple, jump to any page | Slow on large datasets |
| Cursor (`cursor`/`limit`) | Infinite scroll, feeds | Fast, consistent performance | Can't jump to page N |
| Keyset (`after_id`) | Real-time lists | Very fast, no duplicates | Requires ordered column |

---

## 4. Filtering and Sorting

### Query Builder Pattern

```ts
// lib/api/query-builder.ts
import { SQL, eq, like, asc, desc, and, or } from "drizzle-orm";

interface FilterConfig<T> {
  searchableFields: (keyof T)[];
  sortableFields: (keyof T)[];
  filterableFields: (keyof T)[];
}

export function buildQuery<T extends Record<string, unknown>>(
  table: any,
  config: FilterConfig<T>,
  params: URLSearchParams
) {
  const conditions: SQL[] = [];

  // Search
  const search = params.get("search");
  if (search) {
    const searchConditions = config.searchableFields.map((field) =>
      like(table[field as string], `%${search}%`)
    );
    conditions.push(or(...searchConditions));
  }

  // Filters
  for (const field of config.filterableFields) {
    const value = params.get(`filter.${String(field)}`);
    if (value) {
      conditions.push(eq(table[field as string], value));
    }
  }

  // Sort
  const sortField = params.get("sort") as keyof T;
  const sortOrder = params.get("order") === "asc" ? "asc" : "desc";
  const orderBy = config.sortableFields.includes(sortField)
    ? (sortOrder === "asc" ? asc : desc)(table[sortField as string])
    : desc(table.createdAt);

  return { where: conditions.length > 0 ? and(...conditions) : undefined, orderBy };
}
```

---

## 5. API Versioning

### URL Versioning

```ts
// app/api/v1/users/route.ts — Current version
// app/api/v2/users/route.ts — New version (breaking changes)

// Middleware to redirect old versions
export function middleware(request: NextRequest) {
  const pathname = request.nextUrl.pathname;

  // Redirect /api/users to /api/v1/users
  if (pathname.startsWith("/api/") && !pathname.match(/\/api\/v\d+\//)) {
    const newUrl = new URL(request.url);
    newUrl.pathname = pathname.replace("/api/", "/api/v1/");
    return NextResponse.redirect(newUrl);
  }

  return NextResponse.next();
}
```

### Response Envelope Pattern

```ts
// Always wrap responses in a consistent envelope
export function successResponse<T>(data: T, status = 200) {
  return NextResponse.json(
    {
      success: true,
      data,
      meta: {
        timestamp: new Date().toISOString(),
        version: "v1",
      },
    },
    { status }
  );
}

export function errorResponse(error: ApiError, status: number) {
  return NextResponse.json(
    {
      success: false,
      error,
      meta: {
        timestamp: new Date().toISOString(),
        version: "v1",
      },
    },
    { status }
  );
}
```

---

## API Anti-Patterns

### ❌ Inconsistent Error Formats
```ts
// BAD: Different endpoints return different error shapes
return NextResponse.json({ message: "Not found" });
return NextResponse.json({ error: "User not found", status: 404 });
return NextResponse.json({ errors: ["Email required"] });

// GOOD: Always use standardized format
return notFound("User");
return validationError({ email: ["Email is required"] });
```

### ❌ Leaking Internal Details
```ts
// BAD: Exposes stack traces, DB errors
return NextResponse.json({ error: err.message, stack: err.stack });

// GOOD: Generic message, log internally
console.error("Failed to process:", err);
return internalError("Failed to process request", traceId);
```

### ❌ No Pagination Limits
```ts
// BAD: Returns all records
const users = await db.select().from(users);

// GOOD: Enforce limits
const limit = Math.min(parseInt(params.get("limit") || "20"), 100);
const users = await db.select().from(users).limit(limit);
```

---

## API Selection Guide

| Scenario | Best Pattern |
|---|---|
| CRUD resource | REST controller (GET/POST/PATCH/DELETE) |
| Complex query | GET with filter params |
| Bulk operation | POST with array payload |
| File upload | POST with FormData |
| Real-time updates | WebSocket or SSE |
| Long-running job | POST → returns job ID → GET /jobs/[id] for status |
| Batch operations | POST /batch with array of operations |
| Export data | GET with `Accept: text/csv` header |
