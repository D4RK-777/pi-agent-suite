# Test Strategy

Testing pyramid, what to test, what to skip, risk-based prioritization.

---

## 1. Testing Pyramid

### The Pyramid

```
        ┌─────────┐
        │  E2E    │  ← Few tests, full user flows
       ┌┴─────────┴┐
       │Integration│  ← Medium tests, component + API
      ┌┴───────────┴┐
      │    Unit     │  ← Many tests, isolated logic
     └───────────────┘
```

### Distribution

| Layer | Count | Speed | Confidence | Cost |
|---|---|---|---|---|
| Unit | 70% | < 1ms each | Low (isolated) | Low |
| Integration | 20% | 10-100ms each | Medium | Medium |
| E2E | 10% | 1-10s each | High (realistic) | High |

### What Goes Where

| What to Test | Layer | Why |
|---|---|---|
| Pure functions, utilities | Unit | Fast, deterministic |
| Component rendering | Integration | Real DOM behavior |
| API endpoints | Integration | Request/response contracts |
| Database queries | Integration | Real data behavior |
| Critical user flows | E2E | End-to-end confidence |
| Authentication flows | E2E | Security-critical paths |

---

## 2. Risk-Based Prioritization

### Test Priority Matrix

| Impact ↓ / Likelihood → | High | Medium | Low |
|---|---|---|---|
| **High** | P0 — Test first | P1 — Test soon | P1 — Test soon |
| **Medium** | P1 — Test soon | P2 — Test later | P3 — Optional |
| **Low** | P2 — Test later | P3 — Optional | Skip |

### P0 Tests (Must Have)

- Authentication and authorization
- Payment processing
- Data deletion
- Core business logic
- Security-critical paths

### P1 Tests (Should Have)

- API request/response contracts
- Form validation
- Error handling paths
- Database migrations
- Component rendering

### P2 Tests (Nice to Have)

- Edge cases in pure functions
- UI state transitions
- Performance characteristics
- Browser compatibility

### P3 Tests (Optional)

- Third-party library behavior
- CSS styling details
- Animation timing
- Browser-specific quirks

---

## 3. What NOT to Test

### Skip These

| What | Why | Alternative |
|---|---|---|
| Third-party libraries | They test themselves | Trust their test suite |
| Getters/setters | No logic | Test the behavior that uses them |
| Framework code | React/Next.js test themselves | Test your code |
| Generated code | Deterministic | Test the generator |
| Constants/config | No behavior | Validate config at startup |
| Private methods | Implementation detail | Test the public interface |

### Anti-Pattern: Testing Implementation

```ts
// BAD: Testing internal implementation
test("component sets state.foo to bar", () => {
  render(<Component />);
  expect(component.state.foo).toBe("bar");
});

// GOOD: Testing behavior
test("component shows error message on invalid input", () => {
  render(<Component />);
  fireEvent.change(input, { target: { value: "invalid" } });
  expect(screen.getByText("Invalid input")).toBeInTheDocument();
});
```

---

## 4. Test Organization

### Structure

```
tests/
├── unit/
│   ├── lib/
│   │   ├── auth.test.ts
│   │   └── validation.test.ts
│   └── services/
│       └── user-service.test.ts
├── integration/
│   ├── api/
│   │   └── users.test.ts
│   └── components/
│       └── login-form.test.tsx
├── e2e/
│   └── login-flow.spec.ts
├── fixtures/
│   └── users.json
└── helpers/
    └── test-utils.tsx
```

### Naming Convention

```ts
// Describe the behavior, not the implementation
describe("UserService", () => {
  describe("create", () => {
    it("creates a user with valid input", () => {});
    it("rejects duplicate email", () => {});
    it("hashes the password before saving", () => {});
  });
});

// BAD: Testing implementation details
describe("UserService.create", () => {
  it("calls userRepository.insert", () => {});
  it("sets createdAt to new Date()", () => {});
});
```

---

## 5. Test Selection Guide

| Scenario | Best Approach |
|---|---|
| Pure function | Unit test |
| Component rendering | Integration test (RTL) |
| API endpoint | Integration test (supertest) |
| Database query | Integration test (test DB) |
| User flow | E2E test (Playwright) |
| Performance | Benchmark test |
| Security | Security test (OWASP ZAP) |
| Accessibility | a11y test (axe-core) |

---

## Test Strategy Anti-Patterns

### ❌ 100% Coverage Goal
```
BAD: "We need 100% code coverage"
GOOD: "We need 100% coverage of P0 paths"
```

### ❌ Testing Everything
```
BAD: Test every getter, setter, and utility
GOOD: Test behavior that matters to users
```

### ❌ Brittle Tests
```ts
// BAD: Breaks on any implementation change
expect(component).toHaveProperty("state.users.length", 3);

// GOOD: Tests behavior, not implementation
expect(screen.getAllByRole("listitem")).toHaveLength(3);
```

### ❌ No Test Data Strategy
```ts
// BAD: Hardcoded test data
const user = { id: "1", name: "Test User", email: "test@test.com" };

// GOOD: Factory pattern
const user = createTestUser({ role: "admin" });
```
