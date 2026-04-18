# Mocking Strategy

What to mock, what not to mock, factory patterns, test doubles.

---

## 1. What to Mock

### Mock These

| What | Why | How |
|---|---|---|
| External APIs | Don't test their behavior | `vi.mock("fetch")` |
| Database | Use test DB or mock | Test DB preferred |
| File system | Don't touch real files | `vi.mock("fs")` |
| Time | Make tests deterministic | `vi.useFakeTimers()` |
| Random | Make tests predictable | `vi.spyOn(Math, "random")` |
| Network requests | Don't make real calls | Mock `fetch` or `axios` |

### Don't Mock These

| What | Why |
|---|---|
| Your own business logic | Test the real thing |
| React components | Use React Testing Library |
| Pure functions | They're deterministic |
| Utility functions | Test them directly |

---

## 2. Mocking External APIs

### Pattern

```ts
// tests/mocks/stripe.ts
import { vi } from "vitest";

export function mockStripe() {
  const customers = {
    create: vi.fn().mockResolvedValue({ id: "cus_test123" }),
    retrieve: vi.fn().mockResolvedValue({ id: "cus_test123", email: "test@example.com" }),
  };

  const subscriptions = {
    create: vi.fn().mockResolvedValue({ id: "sub_test123", status: "active" }),
    cancel: vi.fn().mockResolvedValue({ id: "sub_test123", status: "canceled" }),
  };

  const stripe = {
    customers,
    subscriptions,
    webhooks: {
      constructEvent: vi.fn().mockReturnValue({ type: "invoice.payment_succeeded" }),
    },
  };

  return stripe;
}

vi.mock("stripe", () => {
  const Stripe = vi.fn();
  Stripe.mockImplementation(() => mockStripe());
  return { default: Stripe };
});
```

### Usage

```ts
// tests/integration/api/payments.test.ts
import { mockStripe } from "@/mocks/stripe";

describe("Payments API", () => {
  it("creates a Stripe customer on first payment", async () => {
    const stripe = mockStripe();

    await apiCall("POST", "/api/payments", {
      amount: 1000,
      currency: "usd",
    });

    expect(stripe.customers.create).toHaveBeenCalledWith({
      email: "test@example.com",
    });
  });
});
```

---

## 3. Mocking Time

### Pattern

```ts
// tests/unit/hooks/use-session-timeout.test.ts
import { renderHook } from "@testing-library/react";
import { vi } from "vitest";

describe("useSessionTimeout", () => {
  beforeEach(() => {
    vi.useFakeTimers();
  });

  afterEach(() => {
    vi.useRealTimers();
  });

  it("logs out after 30 minutes of inactivity", () => {
    const onTimeout = vi.fn();
    renderHook(() => useSessionTimeout({ timeoutMs: 30 * 60 * 1000, onTimeout }));

    // Fast-forward 29 minutes — should not timeout
    vi.advanceTimersByTime(29 * 60 * 1000);
    expect(onTimeout).not.toHaveBeenCalled();

    // Fast-forward 1 more minute — should timeout
    vi.advanceTimersByTime(60 * 1000);
    expect(onTimeout).toHaveBeenCalled();
  });
});
```

---

## 4. Factory Pattern

### Test Data Factories

```ts
// tests/factories/user-factory.ts
let idCounter = 0;

export function createUserFactory() {
  return (overrides: Partial<User> = {}): User => ({
    id: `user-${++idCounter}`,
    name: `Test User ${idCounter}`,
    email: `user${idCounter}@example.com`,
    password: "Password123!",
    role: "user",
    createdAt: new Date(),
    updatedAt: new Date(),
    ...overrides,
  });
}

// Usage
const createUser = createUserFactory();
const admin = createUser({ role: "admin", name: "Admin User" });
const user = createUser(); // Auto-incrementing ID and email
```

### API Response Factories

```ts
// tests/factories/api-response-factory.ts
export function createSuccessResponse<T>(data: T) {
  return {
    status: 200,
    json: () => Promise.resolve({ data }),
    ok: true,
  } as Response;
}

export function createErrorResponse(status: number, error: string, code?: string) {
  return {
    status,
    json: () => Promise.resolve({ error, code }),
    ok: false,
  } as Response;
}
```

---

## 5. Test Doubles

### Types of Doubles

| Type | Purpose | Example |
|---|---|---|
| **Dummy** | Passed but never used | `const dummy = {}` |
| **Stub** | Returns canned responses | `vi.fn().mockResolvedValue(data)` |
| **Spy** | Records calls for verification | `vi.spyOn(obj, "method")` |
| **Mock** | Pre-programmed with expectations | `vi.fn().mockImplementation()` |
| **Fake** | Working but simplified implementation | In-memory database |

### Spy Pattern

```ts
// tests/unit/services/email-service.test.ts
import { vi } from "vitest";

describe("EmailService", () => {
  it("sends welcome email on user creation", async () => {
    const sendSpy = vi.spyOn(emailService, "send").mockResolvedValue();

    await userService.create({ name: "Test", email: "test@example.com", password: "Password123!" });

    expect(sendSpy).toHaveBeenCalledWith(
      "test@example.com",
      "Welcome!",
      expect.any(String)
    );
  });
});
```

### Fake Database

```ts
// tests/fakes/fake-db.ts
export function createFakeDb() {
  const stores = new Map<string, Map<string, any>>();

  return {
    async select(table: string, where?: Record<string, any>) {
      const store = stores.get(table) || new Map();
      let results = Array.from(store.values());
      if (where) {
        results = results.filter(row =>
          Object.entries(where).every(([k, v]) => row[k] === v)
        );
      }
      return results;
    },
    async insert(table: string, values: any) {
      const store = stores.get(table) || new Map();
      const id = crypto.randomUUID();
      store.set(id, { ...values, id });
      return { id };
    },
    async update(table: string, id: string, values: any) {
      const store = stores.get(table) || new Map();
      const existing = store.get(id);
      if (!existing) return null;
      const updated = { ...existing, ...values };
      store.set(id, updated);
      return updated;
    },
    async delete(table: string, id: string) {
      const store = stores.get(table) || new Map();
      return store.delete(id);
    },
    clear() {
      stores.clear();
    },
  };
}
```

---

## Mocking Anti-Patterns

### ❌ Over-Mocking
```ts
// BAD: Mocking everything
vi.mock("@/lib/db");
vi.mock("@/lib/auth");
vi.mock("@/lib/email");

// GOOD: Mock only external dependencies
vi.mock("stripe");
vi.mock("resend");
```

### ❌ Mocking Implementation Details
```ts
// BAD: Testing how it works, not what it does
expect(db.insert).toHaveBeenCalledWith("users", expect.objectContaining({ name: "Test" }));

// GOOD: Testing the outcome
const user = await userService.create({ name: "Test", email: "test@example.com", password: "Password123!" });
expect(user.name).toBe("Test");
```

### ❌ Brittle Mocks
```ts
// BAD: Mock breaks on any implementation change
vi.mocked(db.query).mockResolvedValue([{ id: 1, name: "Test", email: "test@test.com", role: "user", createdAt: new Date() }]);

// GOOD: Factory-based mocks
vi.mocked(db.query).mockResolvedValue([createUser({ id: "1" })]);
```

### ❌ Shared Mock State
```ts
// BAD: Mock state leaks between tests
beforeAll(() => {
  vi.mocked(stripe.customers.create).mockResolvedValue({ id: "cus_123" });
});

// GOOD: Reset mocks per test
beforeEach(() => {
  vi.resetAllMocks();
});
```
