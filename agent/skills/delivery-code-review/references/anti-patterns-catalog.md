# Anti-Patterns Catalog

Common code smells with examples and fixes.

---

## 1. Frontend Anti-Patterns

### Prop Drilling
```tsx
// BAD: Passing through 4 levels
<App user={user} theme={theme}>
  <Layout user={user} theme={theme}>
    <Sidebar user={user} theme={theme}>
      <UserMenu user={user} theme={theme} />
    </Sidebar>
  </Layout>
</App>

// GOOD: Context or composition
<ThemeProvider>
  <AuthProvider>
    <App />
  </AuthProvider>
</ThemeProvider>
```

### God Component
```tsx
// BAD: 500-line component doing everything
function Dashboard() {
  // Fetches data
  // Handles auth
  // Renders charts
  // Manages filters
  // Handles exports
  // ... 200 more lines
}

// GOOD: Split by responsibility
function Dashboard() {
  return (
    <>
      <DashboardHeader />
      <DashboardFilters />
      <DashboardCharts />
      <DashboardExport />
    </>
  );
}
```

### useEffect for Everything
```tsx
// BAD: useEffect for derived state
const [fullName, setFullName] = useState("");
useEffect(() => {
  setFullName(`${firstName} ${lastName}`);
}, [firstName, lastName]);

// GOOD: Derive directly
const fullName = `${firstName} ${lastName}`;
```

### Missing Error Boundary
```tsx
// BAD: One error crashes the whole app
function App() {
  return (
    <Router>
      <Page />
    </Router>
  );
}

// GOOD: Error boundary isolates failures
function App() {
  return (
    <ErrorBoundary fallback={<ErrorPage />}>
      <Router>
        <Page />
      </Router>
    </ErrorBoundary>
  );
}
```

---

## 2. Backend Anti-Patterns

### Fat Controller
```ts
// BAD: Route handler does everything
export async function POST(request: NextRequest) {
  const body = await request.json();
  // Validate
  // Check auth
  // Query database
  // Send email
  // Update cache
  // Log analytics
  // Return response
}

// GOOD: Delegate to services
export async function POST(request: NextRequest) {
  const validation = validateRequest(createUserSchema, await request.json());
  if ("error" in validation) return validation.error;
  const user = await userService.create(validation.data);
  return NextResponse.json({ data: user }, { status: 201 });
}
```

### Silent Failure
```ts
// BAD: Error swallowed
try {
  await sendEmail(user.email, "Welcome");
} catch (e) {
  // Nothing
}

// GOOD: Log and handle
try {
  await sendEmail(user.email, "Welcome");
} catch (e) {
  logger.warn({ message: "Failed to send welcome email", userId: user.id, error: String(e) });
  // Non-critical — continue
}
```

### Raw SQL
```ts
// BAD: String interpolation
const user = await db.execute(sql`SELECT * FROM users WHERE email = '${email}'`);

// GOOD: Parameterized
const user = await db.select().from(users).where(eq(users.email, email)).limit(1);
```

---

## 3. Security Anti-Patterns

### Verbose Error Messages
```ts
// BAD: Leaks internals
return NextResponse.json({
  error: err.message,
  stack: err.stack,
  query: sqlQuery,
});

// GOOD: User-friendly
return NextResponse.json({
  error: "An unexpected error occurred",
  code: "INTERNAL_ERROR",
  traceId,
});
```

### Inconsistent Auth
```ts
// BAD: Some routes check auth, some don't
export async function GET() { /* no auth check */ }
export async function POST() { const user = await auth(); /* ... */ }

// GOOD: Middleware enforces consistently
// middleware.ts checks all /api/* routes
```

### Trusting Client Data
```tsx
// BAD: Client-side only check
if (user.role !== "admin") return <Forbidden />;
// Admin page renders anyway

// GOOD: Server-side check
export async function GET() {
  const user = await requireAdmin();
  // ...
}
```

---

## 4. Performance Anti-Patterns

### Unbounded Rendering
```tsx
// BAD: Renders 10,000 DOM nodes
{items.map(item => <Item key={item.id} {...item} />)}

// GOOD: Virtualize
<VirtualList items={items} itemHeight={40} renderItem={(item) => <Item {...item} />} />
```

### Unnecessary Re-renders
```tsx
// BAD: New object reference every render
function Parent() {
  return <Child config={{ theme: "dark", lang: "en" }} />;
}

// GOOD: Stable reference
const config = useMemo(() => ({ theme: "dark", lang: "en" }), []);
function Parent() {
  return <Child config={config} />;
}
```

### Blocking Main Thread
```ts
// BAD: Synchronous heavy computation
function processData(data: largeData[]) {
  return data.map(expensiveTransform); // Blocks UI
}

// GOOD: Web Worker or chunking
const worker = new Worker("./process-worker.ts");
worker.postMessage(data);
```

---

## 5. Testing Anti-Patterns

### Testing Implementation
```ts
// BAD
expect(component.state.isOpen).toBe(true);

// GOOD
expect(screen.getByRole("dialog")).toBeInTheDocument();
```

### Shared Test State
```ts
// BAD: Tests depend on order
it("creates user", () => {});
it("updates that user", () => {});

// GOOD: Independent tests
it("creates and updates user", () => {
  // Create, then update in same test
});
```

### Flaky Timeouts
```ts
// BAD: Arbitrary timeout
await new Promise(r => setTimeout(r, 1000));

// GOOD: Wait for condition
await waitFor(() => {
  expect(screen.getByText("Loaded")).toBeInTheDocument();
});
```

---

## Anti-Pattern Quick Reference

| Pattern | Smell | Fix |
|---|---|---|
| God Component | > 200 lines | Split by responsibility |
| Prop Drilling | > 2 levels | Context or composition |
| useEffect for Derived State | State from state | Compute directly |
| Fat Controller | Route handler > 20 lines | Delegate to services |
| Silent Failure | Empty catch block | Log or rethrow |
| Raw SQL | String interpolation | Parameterized queries |
| Verbose Errors | Stack traces in response | Generic message + trace ID |
| Unbounded Rendering | No pagination/virtualization | Virtualize or paginate |
| Testing Implementation | Checking state/refs | Checking behavior |
| Flaky Timeouts | setTimeout in tests | waitFor/assertion |
