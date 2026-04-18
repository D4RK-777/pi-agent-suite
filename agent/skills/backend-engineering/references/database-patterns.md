# Database Patterns

Repository pattern, migrations, transactions, indexing strategies, N+1 prevention.

---

## 1. Repository Pattern

**When:** Abstracting database access behind a clean interface — testable, swappable, consistent.

### Core Pattern (Drizzle ORM)

```ts
// lib/repositories/users.ts
import { db } from "@/lib/db";
import { users, type User, type NewUser, type UpdateUser } from "@/lib/db/schema";
import { eq, like, and, desc, asc, count, SQL } from "drizzle-orm";

export interface UserFilters {
  search?: string;
  role?: string;
  status?: string;
}

export interface UserSort {
  field: keyof User;
  order: "asc" | "desc";
}

export interface PaginationParams {
  page: number;
  limit: number;
}

export interface PaginatedResult<T> {
  data: T[];
  meta: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
    hasNext: boolean;
    hasPrev: boolean;
  };
}

export const userRepository = {
  // Find by ID
  async findById(id: string): Promise<User | null> {
    const [user] = await db
      .select()
      .from(users)
      .where(eq(users.id, id))
      .limit(1);
    return user || null;
  },

  // Find by email
  async findByEmail(email: string): Promise<User | null> {
    const [user] = await db
      .select()
      .from(users)
      .where(eq(users.email, email))
      .limit(1);
    return user || null;
  },

  // List with filters, sorting, pagination
  async list({
    filters = {},
    sort = { field: "createdAt", order: "desc" },
    pagination = { page: 1, limit: 20 },
  }: {
    filters?: UserFilters;
    sort?: UserSort;
    pagination?: PaginationParams;
  }): Promise<PaginatedResult<User>> {
    const { page, limit } = pagination;
    const offset = (page - 1) * limit;

    // Build where conditions
    const conditions: SQL[] = [];
    if (filters.search) {
      conditions.push(
        like(users.name, `%${filters.search}%`).or(like(users.email, `%${filters.search}%`))
      );
    }
    if (filters.role) {
      conditions.push(eq(users.role, filters.role));
    }
    if (filters.status) {
      conditions.push(eq(users.status, filters.status));
    }

    const where = conditions.length > 0 ? and(...conditions) : undefined;

    // Get total count
    const [{ total }] = await db
      .select({ total: count() })
      .from(users)
      .where(where);

    // Get paginated results
    const orderBy = sort.order === "asc"
      ? asc(users[sort.field])
      : desc(users[sort.field]);

    const data = await db
      .select()
      .from(users)
      .where(where)
      .orderBy(orderBy)
      .limit(limit)
      .offset(offset);

    return {
      data,
      meta: {
        page,
        limit,
        total,
        totalPages: Math.ceil(total / limit),
        hasNext: page * limit < total,
        hasPrev: page > 1,
      },
    };
  },

  // Create
  async create(data: NewUser): Promise<User> {
    const [user] = await db
      .insert(users)
      .values({ ...data, createdAt: new Date(), updatedAt: new Date() })
      .returning();
    return user;
  },

  // Update
  async update(id: string, data: UpdateUser): Promise<User | null> {
    const [user] = await db
      .update(users)
      .set({ ...data, updatedAt: new Date() })
      .where(eq(users.id, id))
      .returning();
    return user || null;
  },

  // Delete
  async delete(id: string): Promise<boolean> {
    const [result] = await db
      .delete(users)
      .where(eq(users.id, id))
      .returning({ id: users.id });
    return !!result;
  },

  // Check existence
  async exists(id: string): Promise<boolean> {
    const [result] = await db
      .select({ id: users.id })
      .from(users)
      .where(eq(users.id, id))
      .limit(1);
    return !!result;
  },
};
```

### Usage

```ts
// app/api/users/route.ts
import { userRepository } from "@/lib/repositories/users";

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);

  const result = await userRepository.list({
    filters: {
      search: searchParams.get("search") || undefined,
      role: searchParams.get("role") || undefined,
    },
    sort: {
      field: (searchParams.get("sort") as keyof User) || "createdAt",
      order: (searchParams.get("order") as "asc" | "desc") || "desc",
    },
    pagination: {
      page: parseInt(searchParams.get("page") || "1", 10),
      limit: Math.min(parseInt(searchParams.get("limit") || "20", 10), 100),
    },
  });

  return NextResponse.json(result);
}
```

---

## 2. Migration Patterns

**When:** Schema changes — adding columns, changing types, backfilling data.

### Migration Structure

```ts
// drizzle/migrations/0001_create_users.ts
import { pgTable, text, timestamp, uuid, varchar } from "drizzle-orm/pg-core";

export const users = pgTable("users", {
  id: uuid("id").defaultRandom().primaryKey(),
  name: varchar("name", { length: 100 }).notNull(),
  email: varchar("email", { length: 255 }).notNull().unique(),
  role: varchar("role", { length: 20 }).notNull().default("user"),
  status: varchar("status", { length: 20 }).notNull().default("active"),
  passwordHash: text("password_hash").notNull(),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  updatedAt: timestamp("updated_at").notNull().defaultNow(),
});
```

### Safe Migration Patterns

```ts
// Adding a column with a default — safe
// drizzle/migrations/0002_add_last_login.ts
import { timestamp } from "drizzle-orm/pg-core";
import { users } from "../schema";

// Add nullable first, then backfill, then make required if needed
export const lastLogin = timestamp("last_login");

// Backfill migration
// drizzle/migrations/0003_backfill_last_login.ts
import { db } from "@/lib/db";
import { users } from "@/lib/db/schema";
import { eq, isNull } from "drizzle-orm";

export async function up() {
  // Set default for existing rows
  await db
    .update(users)
    .set({ lastLogin: users.createdAt })
    .where(isNull(users.lastLogin));
}
```

### Migration Safety Rules

1. **Never drop columns in production** — deprecate first, remove later
2. **Never change column types** — add new column, migrate data, swap
3. **Always add indexes for new query patterns** — but measure impact
4. **Test migrations on a copy of production data** — never on live
5. **Make migrations reversible** — have a `down()` function

---

## 3. Transaction Patterns

**When:** Multiple operations that must succeed or fail together — orders, transfers, multi-table updates.

### Core Pattern

```ts
// lib/services/orders.ts
import { db } from "@/lib/db";
import { orders, orderItems, products, inventory } from "@/lib/db/schema";
import { eq, lt, and, sql } from "drizzle-orm";

export async function createOrder(userId: string, items: { productId: string; quantity: number }[]) {
  return await db.transaction(async (tx) => {
    // 1. Validate all products exist and have sufficient stock
    const productsData = await tx
      .select()
      .from(products)
      .where(
        and(
          eq(products.id, sql`ANY(${items.map(i => i.productId)})`),
          sql`${products.stock} >= ANY(${items.map(i => i.quantity)})`
        )
      );

    if (productsData.length !== items.length) {
      tx.rollback();
      throw new Error("One or more products are unavailable");
    }

    // 2. Create order
    const total = items.reduce((sum, item) => {
      const product = productsData.find(p => p.id === item.productId)!;
      return sum + product.price * item.quantity;
    }, 0);

    const [order] = await tx
      .insert(orders)
      .values({
        userId,
        total,
        status: "pending",
        createdAt: new Date(),
      })
      .returning();

    // 3. Create order items
    const orderItemsData = items.map(item => ({
      orderId: order.id,
      productId: item.productId,
      quantity: item.quantity,
      price: productsData.find(p => p.id === item.productId)!.price,
    }));

    await tx.insert(orderItems).values(orderItemsData);

    // 4. Update inventory
    for (const item of items) {
      await tx
        .update(products)
        .set({
          stock: sql`${products.stock} - ${item.quantity}`,
          updatedAt: new Date(),
        })
        .where(eq(products.id, item.productId));
    }

    // 5. Return complete order
    const completeOrder = await tx.query.orders.findFirst({
      where: eq(orders.id, order.id),
      with: { items: true },
    });

    return completeOrder;
  });
}
```

### Transaction Anti-Patterns

```ts
// BAD: Multiple independent queries — partial failure possible
await db.insert(orders).values(orderData);
await db.insert(orderItems).values(itemsData); // If this fails, order exists without items
await db.update(products).set({ stock: newStock }); // If this fails, stock is wrong

// GOOD: All or nothing
await db.transaction(async (tx) => {
  await tx.insert(orders).values(orderData);
  await tx.insert(orderItems).values(itemsData);
  await tx.update(products).set({ stock: newStock });
});
```

---

## 4. Indexing Strategies

### When to Add Indexes

```sql
-- ALWAYS index:
-- Primary keys (automatic)
-- Foreign keys
-- Columns used in WHERE clauses
-- Columns used in JOIN conditions
-- Columns used in ORDER BY

-- NEVER index:
-- Columns with few unique values (boolean, status enums with 2-3 values)
-- Small tables (< 1000 rows)
-- Columns that are frequently updated (index maintenance cost)

-- Composite indexes for multi-column queries
CREATE INDEX idx_users_role_status ON users(role, status);
-- Order matters: most selective first

-- Partial indexes for filtered queries
CREATE INDEX idx_active_users ON users(email) WHERE status = 'active';

-- Covering indexes for specific queries
CREATE INDEX idx_orders_user_total ON orders(user_id) INCLUDE (total, status);
```

### N+1 Prevention

```ts
// BAD: N+1 query — 1 query for orders, N queries for items
const orders = await db.select().from(orders).where(eq(orders.userId, userId));
for (const order of orders) {
  const items = await db.select().from(orderItems).where(eq(orderItems.orderId, order.id));
  order.items = items;
}

// GOOD: Single query with JOIN
const orders = await db.query.orders.findMany({
  where: eq(orders.userId, userId),
  with: {
    items: true,
  },
});

// GOOD: Manual JOIN with IN clause
const orders = await db.select().from(orders).where(eq(orders.userId, userId));
const orderIds = orders.map(o => o.id);
const items = await db
  .select()
  .from(orderItems)
  .where(inArray(orderItems.orderId, orderIds));

// Group items by order ID
const itemsByOrder = new Map();
for (const item of items) {
  if (!itemsByOrder.has(item.orderId)) itemsByOrder.set(item.orderId, []);
  itemsByOrder.get(item.orderId).push(item);
}

// Attach to orders
for (const order of orders) {
  order.items = itemsByOrder.get(order.id) || [];
}
```

---

## 5. Query Optimization

### EXPLAIN ANALYZE Pattern

```ts
// Before optimizing, always measure
const result = await db.execute(sql`
  EXPLAIN ANALYZE
  SELECT * FROM orders
  WHERE user_id = ${userId}
  ORDER BY created_at DESC
  LIMIT 20
`);
console.log(result);
```

### Common Query Patterns

```ts
// Pagination with total count (single query using window function)
const result = await db.execute(sql`
  SELECT *, COUNT(*) OVER() as total_count
  FROM orders
  WHERE user_id = ${userId}
  ORDER BY created_at DESC
  LIMIT ${limit} OFFSET ${offset}
`);

// Upsert (insert or update)
await db.execute(sql`
  INSERT INTO user_preferences (user_id, theme, language)
  VALUES (${userId}, ${theme}, ${language})
  ON CONFLICT (user_id) DO UPDATE
  SET theme = ${theme}, language = ${language}, updated_at = NOW()
`);

// Batch insert
await db.insert(users).values(usersArray).onConflictDoNothing();

// Conditional update
const [updated] = await db
  .update(orders)
  .set({ status: "shipped", shippedAt: new Date() })
  .where(and(eq(orders.id, orderId), eq(orders.status, "pending")))
  .returning();

if (!updated) {
  throw new Error("Order cannot be shipped — not in pending status");
}
```

---

## Database Selection Guide

| Scenario | Best Pattern |
|---|---|
| Simple CRUD | Repository pattern |
| Multi-table write | Transaction |
| Large dataset queries | Pagination + indexes |
| Real-time data | Materialized views + refresh |
| Audit trail | Soft deletes + updated_at |
| Multi-tenant | Row-level security or tenant_id column |
| Full-text search | PostgreSQL tsvector or external search engine |
| Analytics | Separate read replica, materialized views |

---

## Database Anti-Patterns

### ❌ Raw SQL in Route Handlers
```ts
// BAD: Scattered SQL, no abstraction
const result = await db.execute(sql`SELECT * FROM users WHERE email = ${email}`);

// GOOD: Repository pattern
const user = await userRepository.findByEmail(email);
```

### ❌ Missing Indexes on Foreign Keys
```sql
-- BAD: No index on orders.user_id — every user lookup scans entire table
CREATE TABLE orders (id UUID PRIMARY KEY, user_id UUID REFERENCES users(id), ...);

-- GOOD: Index foreign keys
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

### ❌ SELECT * in Production
```ts
// BAD: Fetches all columns including large text fields
const users = await db.select().from(users);

// GOOD: Select only needed columns
const users = await db.select({ id: users.id, name: users.name, email: users.email }).from(users);
```

### ❌ Unbounded Queries
```ts
// BAD: No limit — could return millions of rows
const orders = await db.select().from(orders).where(eq(orders.status, "pending"));

// GOOD: Always limit
const orders = await db.select().from(orders).where(eq(orders.status, "pending")).limit(1000);
```
