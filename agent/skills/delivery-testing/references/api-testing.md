# API Testing

Supertest patterns, fixture management, database seeding, assertion patterns.

---

## 1. Core Pattern

### Setup

```ts
// tests/helpers/api-test-utils.ts
import { describe, it, expect, beforeEach, afterEach } from "vitest";
import { execSync } from "child_process";

// Reset database before each test
beforeEach(async () => {
  execSync("npm run db:reset");
  execSync("npm run db:seed:test");
});

// Clean up after tests
afterEach(async () => {
  // Any cleanup needed
});
```

### Testing CRUD Endpoints

```ts
// tests/integration/api/users.test.ts
import { describe, it, expect } from "vitest";

const BASE_URL = process.env.TEST_BASE_URL || "http://localhost:3000";

async function apiCall(method: string, path: string, body?: unknown, headers?: Record<string, string>) {
  const response = await fetch(`${BASE_URL}${path}`, {
    method,
    headers: {
      "Content-Type": "application/json",
      ...headers,
    },
    body: body ? JSON.stringify(body) : undefined,
  });

  return {
    status: response.status,
    headers: response.headers,
    json: () => response.json(),
  };
}

describe("Users API", () => {
  describe("POST /api/users", () => {
    it("creates a user with valid input", async () => {
      const res = await apiCall("POST", "/api/users", {
        name: "Test User",
        email: "test@example.com",
        password: "Password123!",
      });

      expect(res.status).toBe(201);
      const data = await res.json();
      expect(data.data).toHaveProperty("id");
      expect(data.data.name).toBe("Test User");
      expect(data.data.email).toBe("test@example.com");
      expect(data.data).not.toHaveProperty("password"); // Never expose password
    });

    it("rejects duplicate email", async () => {
      // Create first user
      await apiCall("POST", "/api/users", {
        name: "First User",
        email: "duplicate@example.com",
        password: "Password123!",
      });

      // Try to create second user with same email
      const res = await apiCall("POST", "/api/users", {
        name: "Second User",
        email: "duplicate@example.com",
        password: "Password123!",
      });

      expect(res.status).toBe(409);
      const data = await res.json();
      expect(data.error).toMatch(/already exists/i);
    });

    it("rejects invalid input", async () => {
      const res = await apiCall("POST", "/api/users", {
        name: "A", // Too short
        email: "not-an-email",
        password: "short", // Too short
      });

      expect(res.status).toBe(400);
      const data = await res.json();
      expect(data.details).toHaveProperty("name");
      expect(data.details).toHaveProperty("email");
      expect(data.details).toHaveProperty("password");
    });
  });

  describe("GET /api/users/:id", () => {
    it("returns a user by ID", async () => {
      // Create user first
      const createRes = await apiCall("POST", "/api/users", {
        name: "Test User",
        email: "test@example.com",
        password: "Password123!",
      });
      const { data: user } = await createRes.json();

      // Fetch user
      const res = await apiCall("GET", `/api/users/${user.id}`);

      expect(res.status).toBe(200);
      const data = await res.json();
      expect(data.data.id).toBe(user.id);
      expect(data.data.name).toBe("Test User");
    });

    it("returns 404 for non-existent user", async () => {
      const res = await apiCall("GET", "/api/users/non-existent-id");

      expect(res.status).toBe(404);
    });
  });

  describe("PATCH /api/users/:id", () => {
    it("updates a user", async () => {
      // Create user
      const createRes = await apiCall("POST", "/api/users", {
        name: "Original Name",
        email: "test@example.com",
        password: "Password123!",
      });
      const { data: user } = await createRes.json();

      // Update user
      const res = await apiCall("PATCH", `/api/users/${user.id}`, {
        name: "Updated Name",
      });

      expect(res.status).toBe(200);
      const data = await res.json();
      expect(data.data.name).toBe("Updated Name");
      expect(data.data.email).toBe(user.email); // Unchanged
    });
  });

  describe("DELETE /api/users/:id", () => {
    it("deletes a user", async () => {
      // Create user
      const createRes = await apiCall("POST", "/api/users", {
        name: "To Delete",
        email: "delete@example.com",
        password: "Password123!",
      });
      const { data: user } = await createRes.json();

      // Delete user
      const res = await apiCall("DELETE", `/api/users/${user.id}`);

      expect(res.status).toBe(200);

      // Verify deletion
      const getRes = await apiCall("GET", `/api/users/${user.id}`);
      expect(getRes.status).toBe(404);
    });
  });
});
```

---

## 2. Authentication Testing

```ts
// tests/integration/api/auth.test.ts
describe("Auth API", () => {
  describe("POST /api/auth/login", () => {
    it("returns tokens on successful login", async () => {
      // Create user
      await apiCall("POST", "/api/users", {
        name: "Test User",
        email: "test@example.com",
        password: "Password123!",
      });

      // Login
      const res = await apiCall("POST", "/api/auth/login", {
        email: "test@example.com",
        password: "Password123!",
      });

      expect(res.status).toBe(200);
      const data = await res.json();
      expect(data.data).toHaveProperty("accessToken");
      expect(data.data).toHaveProperty("refreshToken");
      expect(data.data.user).toHaveProperty("id");
      expect(data.data.user).not.toHaveProperty("password");
    });

    it("rejects invalid credentials", async () => {
      const res = await apiCall("POST", "/api/auth/login", {
        email: "test@example.com",
        password: "WrongPassword",
      });

      expect(res.status).toBe(401);
    });

    it("rate limits after failed attempts", async () => {
      // Make 5 failed attempts
      for (let i = 0; i < 5; i++) {
        await apiCall("POST", "/api/auth/login", {
          email: "test@example.com",
          password: "WrongPassword",
        });
      }

      // 6th attempt should be rate limited
      const res = await apiCall("POST", "/api/auth/login", {
        email: "test@example.com",
        password: "WrongPassword",
      });

      expect(res.status).toBe(429);
    });
  });

  describe("Protected endpoints", () => {
    it("rejects unauthenticated requests", async () => {
      const res = await apiCall("GET", "/api/users/me");
      expect(res.status).toBe(401);
    });

    it("accepts valid auth token", async () => {
      // Login
      const loginRes = await apiCall("POST", "/api/auth/login", {
        email: "test@example.com",
        password: "Password123!",
      });
      const { data: { accessToken } } = await loginRes.json();

      // Access protected endpoint
      const res = await apiCall("GET", "/api/users/me", undefined, {
        Authorization: `Bearer ${accessToken}`,
      });

      expect(res.status).toBe(200);
    });
  });
});
```

---

## 3. Fixture Management

```ts
// tests/fixtures/users.ts
export function createTestUser(overrides: Partial<TestUser> = {}): TestUser {
  return {
    id: crypto.randomUUID(),
    name: "Test User",
    email: `test-${crypto.randomUUID()}@example.com`,
    password: "Password123!",
    role: "user",
    ...overrides,
  };
}

export const adminUser = createTestUser({ role: "admin" });
export const regularUser = createTestUser({ role: "user" });
export const moderatorUser = createTestUser({ role: "moderator" });
```

### Database Seeding

```ts
// tests/helpers/seed-database.ts
import { db } from "@/lib/db";
import { users, products, orders } from "@/lib/db/schema";
import { createTestUser } from "@/fixtures/users";

export async function seedDatabase() {
  // Create users
  const admin = await db.insert(users).values(createTestUser({ role: "admin" })).returning();
  const user = await db.insert(users).values(createTestUser()).returning();

  // Create products
  const products = await db.insert(products).values([
    { name: "Product 1", price: 1000, stock: 100 },
    { name: "Product 2", price: 2000, stock: 50 },
  ]).returning();

  return { admin: admin[0], user: user[0], products };
}

export async function resetDatabase() {
  await db.delete(orders);
  await db.delete(products);
  await db.delete(users);
}
```

---

## 4. Assertion Patterns

### Response Shape

```ts
// Verify response structure
expect(data).toMatchObject({
  data: expect.objectContaining({
    id: expect.any(String),
    name: expect.any(String),
    email: expect.any(String),
  }),
});
```

### Error Response

```ts
// Verify error structure
expect(res.status).toBe(400);
expect(data).toMatchObject({
  error: expect.any(String),
  code: "VALIDATION_ERROR",
  details: expect.objectContaining({
    email: expect.arrayContaining([expect.any(String)]),
  }),
});
```

### Pagination

```ts
// Verify pagination structure
expect(data).toMatchObject({
  data: expect.any(Array),
  meta: {
    page: 1,
    limit: 20,
    total: expect.any(Number),
    totalPages: expect.any(Number),
    hasNext: expect.any(Boolean),
    hasPrev: expect.any(Boolean),
  },
});
```

---

## API Testing Anti-Patterns

### ❌ Testing Against Production
```ts
// BAD
const BASE_URL = "https://api.production.com";

// GOOD
const BASE_URL = process.env.TEST_BASE_URL || "http://localhost:3000";
```

### ❌ Shared Test State
```ts
// BAD: Tests depend on order
it("creates user", () => { /* creates user-1 */ });
it("updates user", () => { /* updates user-1 */ });

// GOOD: Each test is independent
it("creates and updates user", () => {
  // Create, then update in same test
});
```

### ❌ Hardcoded IDs
```ts
// BAD
const userId = "123e4567-e89b-12d3-a456-426614174000";

// GOOD: Use created resource's ID
const { data: user } = await createRes.json();
const userId = user.id;
```

### ❌ Testing Third-Party APIs
```ts
// BAD: Testing Stripe's behavior
it("creates Stripe customer", () => {
  // Testing Stripe's API, not yours
});

// GOOD: Testing your integration
it("calls Stripe to create customer", () => {
  // Verify your code calls Stripe correctly
});
```
