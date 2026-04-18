# Component Testing

React Testing Library patterns, mocking, user event simulation.

---

## 1. Core Pattern

### Setup

```tsx
// tests/helpers/test-utils.tsx
import { render, RenderOptions } from "@testing-library/react";
import { ReactElement } from "react";

// Custom render with providers
const customRender = (
  ui: ReactElement,
  options?: Omit<RenderOptions, "wrapper">
) => render(ui, { ...options });

// Re-export everything
export * from "@testing-library/react";
export { customRender as render };
```

### Testing a Form Component

```tsx
// tests/integration/components/login-form.test.tsx
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { LoginForm } from "@/components/auth/login-form";

describe("LoginForm", () => {
  it("renders email and password fields", () => {
    render(<LoginForm onSubmit={vi.fn()} />);

    expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /sign in/i })).toBeInTheDocument();
  });

  it("shows validation error for invalid email", async () => {
    const user = userEvent.setup();
    render(<LoginForm onSubmit={vi.fn()} />);

    await user.type(screen.getByLabelText(/email/i), "invalid");
    await user.tab(); // Blur the field

    expect(screen.getByText(/valid email/i)).toBeInTheDocument();
  });

  it("calls onSubmit with valid data", async () => {
    const user = userEvent.setup();
    const handleSubmit = vi.fn();
    render(<LoginForm onSubmit={handleSubmit} />);

    await user.type(screen.getByLabelText(/email/i), "test@example.com");
    await user.type(screen.getByLabelText(/password/i), "Password123!");
    await user.click(screen.getByRole("button", { name: /sign in/i }));

    await waitFor(() => {
      expect(handleSubmit).toHaveBeenCalledWith({
        email: "test@example.com",
        password: "Password123!",
      });
    });
  });

  it("shows loading state during submission", async () => {
    const user = userEvent.setup();
    const handleSubmit = vi.fn().mockReturnValue(new Promise(() => {})); // Never resolves
    render(<LoginForm onSubmit={handleSubmit} />);

    await user.type(screen.getByLabelText(/email/i), "test@example.com");
    await user.type(screen.getByLabelText(/password/i), "Password123!");
    await user.click(screen.getByRole("button", { name: /sign in/i }));

    expect(screen.getByRole("button", { name: /signing in/i })).toBeDisabled();
  });

  it("shows error message on submission failure", async () => {
    const user = userEvent.setup();
    const handleSubmit = vi.fn().mockRejectedValue(new Error("Invalid credentials"));
    render(<LoginForm onSubmit={handleSubmit} />);

    await user.type(screen.getByLabelText(/email/i), "test@example.com");
    await user.type(screen.getByLabelText(/password/i), "Password123!");
    await user.click(screen.getByRole("button", { name: /sign in/i }));

    await waitFor(() => {
      expect(screen.getByText(/invalid credentials/i)).toBeInTheDocument();
    });
  });
});
```

---

## 2. Testing Patterns

### Query Priority (in order)

```ts
// 1. getByRole — best, most accessible
screen.getByRole("button", { name: "Submit" });
screen.getByRole("textbox", { name: "Email" });
screen.getByRole("heading", { level: 1 });

// 2. getByLabelText — for form fields
screen.getByLabelText("Email address");

// 3. getByText — for non-interactive elements
screen.getByText("Welcome back!");

// 4. getByTestId — last resort
screen.getByTestId("user-avatar");
```

### Async Patterns

```ts
// waitFor — retry until assertion passes
await waitFor(() => {
  expect(screen.getByText("Success")).toBeInTheDocument();
});

// findBy — built-in waitFor
const successMessage = await screen.findByText("Success");

// within — scoped queries
const modal = screen.getByRole("dialog");
within(modal).getByText("Are you sure?");
```

### Mocking Fetch

```ts
// tests/helpers/mocks.ts
export function mockFetch(response: unknown, options: { ok?: boolean; status?: number } = {}) {
  return vi.fn().mockResolvedValue({
    ok: options.ok ?? true,
    status: options.status ?? 200,
    json: vi.fn().mockResolvedValue(response),
    text: vi.fn().mockResolvedValue(JSON.stringify(response)),
  });
}

// Usage
beforeEach(() => {
  global.fetch = mockFetch({ users: [{ id: "1", name: "Test" }] });
});
```

### Mocking Next.js Router

```ts
// tests/helpers/mock-router.ts
import { vi } from "vitest";

export function createMockRouter() {
  return {
    push: vi.fn(),
    replace: vi.fn(),
    back: vi.fn(),
    prefetch: vi.fn().mockResolvedValue(undefined),
    pathname: "/",
    query: {},
  };
}

vi.mock("next/navigation", () => ({
  useRouter: () => createMockRouter(),
  usePathname: () => "/",
  useSearchParams: () => new URLSearchParams(),
}));
```

---

## 3. Testing Custom Hooks

```ts
// tests/unit/hooks/use-form.test.ts
import { renderHook, act } from "@testing-library/react";
import { useForm } from "@/hooks/use-form";

describe("useForm", () => {
  it("initializes with default values", () => {
    const { result } = renderHook(() =>
      useForm({ defaultValues: { name: "", email: "" } })
    );

    expect(result.current.values).toEqual({ name: "", email: "" });
    expect(result.current.errors).toEqual({});
  });

  it("updates values on change", () => {
    const { result } = renderHook(() =>
      useForm({ defaultValues: { name: "", email: "" } })
    );

    act(() => {
      result.current.onChange("name", "John");
    });

    expect(result.current.values.name).toBe("John");
  });

  it("validates on submit", () => {
    const { result } = renderHook(() =>
      useForm({
        defaultValues: { email: "" },
        validate: { email: (v) => (v.includes("@") ? null : "Invalid email") },
      })
    );

    act(() => {
      result.current.onSubmit();
    });

    expect(result.current.errors.email).toBe("Invalid email");
  });
});
```

---

## 4. Testing Accessibility

```tsx
// tests/integration/components/modal.test.tsx
import { render, screen } from "@testing-library/react";
import { Modal } from "@/components/ui/modal";

describe("Modal", () => {
  it("has accessible title", () => {
    render(
      <Modal open title="Confirm Action">
        <p>Are you sure?</p>
      </Modal>
    );

    expect(screen.getByRole("dialog", { name: "Confirm Action" })).toBeInTheDocument();
  });

  it("traps focus inside modal", () => {
    render(
      <Modal open title="Test">
        <button>First</button>
        <button>Last</button>
      </Modal>
    );

    const dialog = screen.getByRole("dialog");
    expect(dialog).toHaveFocus();
  });

  it("closes on Escape key", async () => {
    const user = userEvent.setup();
    const onClose = vi.fn();
    render(
      <Modal open title="Test" onClose={onClose}>
        <p>Content</p>
      </Modal>
    );

    await user.keyboard("{Escape}");
    expect(onClose).toHaveBeenCalled();
  });
});
```

---

## Component Testing Anti-Patterns

### ❌ Testing Implementation
```ts
// BAD
expect(component.state.isOpen).toBe(true);

// GOOD
expect(screen.getByRole("dialog")).toBeInTheDocument();
```

### ❌ Testing Third-Party Libraries
```ts
// BAD: Testing React Router behavior
expect(router.push).toHaveBeenCalledWith("/dashboard");

// GOOD: Testing your component's behavior
expect(screen.getByText("Dashboard")).toBeInTheDocument();
```

### ❌ Snapshot Testing Everything
```ts
// BAD: Massive snapshots that nobody reviews
expect(render(<App />)).toMatchSnapshot();

// GOOD: Targeted assertions
expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent("Welcome");
```

### ❌ Ignoring Async Behavior
```ts
// BAD: No waiting for async updates
expect(screen.getByText("Loading")).toBeInTheDocument();

// GOOD: Wait for async state
await waitFor(() => {
  expect(screen.getByText("Loaded")).toBeInTheDocument();
});
```
