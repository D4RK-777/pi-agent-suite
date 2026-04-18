# Refactoring Catalog

Behavior-preserving transformations with before/after examples.

---

## 1. Extract Function

**When:** A code block has a clear purpose that can be named.

### Before
```tsx
function UserCard({ user }: { user: User }) {
  return (
    <div className="card">
      <img src={user.avatar} alt={user.name} />
      <h2>{user.name}</h2>
      <p>{user.email}</p>
      <p>Joined {new Date(user.createdAt).toLocaleDateString()}</p>
      {user.role === "admin" && <Badge>Admin</Badge>}
      {user.status === "inactive" && <Badge>Inactive</Badge>}
    </div>
  );
}
```

### After
```tsx
function UserCard({ user }: { user: User }) {
  return (
    <div className="card">
      <UserAvatar src={user.avatar} name={user.name} />
      <UserInfo user={user} />
      <UserBadges user={user} />
    </div>
  );
}

function UserBadges({ user }: { user: User }) {
  const badges = [];
  if (user.role === "admin") badges.push(<Badge key="admin">Admin</Badge>);
  if (user.status === "inactive") badges.push(<Badge key="inactive">Inactive</Badge>);
  return <>{badges}</>;
}
```

---

## 2. Decompose Conditional

**When:** A complex conditional is hard to read.

### Before
```ts
if (user.role === "admin" && user.status === "active" && !user.isLocked) {
  // Grant access
}
```

### After
```ts
const hasAccess = user.role === "admin" && user.status === "active" && !user.isLocked;
if (hasAccess) {
  // Grant access
}

// Or even better:
if (user.canAccess("admin-panel")) {
  // Grant access
}
```

---

## 3. Replace Conditional with Polymorphism

**When:** Switch/if-else chains based on type.

### Before
```ts
function calculateShipping(order: Order): number {
  switch (order.shippingMethod) {
    case "standard": return 5.99;
    case "express": return 12.99;
    case "overnight": return 24.99;
    case "free": return 0;
    default: throw new Error(`Unknown method: ${order.shippingMethod}`);
  }
}
```

### After
```ts
interface ShippingMethod {
  calculateCost(order: Order): number;
}

const shippingMethods: Record<string, ShippingMethod> = {
  standard: { calculateCost: () => 5.99 },
  express: { calculateCost: () => 12.99 },
  overnight: { calculateCost: () => 24.99 },
  free: { calculateCost: () => 0 },
};

function calculateShipping(order: Order): number {
  const method = shippingMethods[order.shippingMethod];
  if (!method) throw new Error(`Unknown method: ${order.shippingMethod}`);
  return method.calculateCost(order);
}
```

---

## 4. Consolidate Duplicate Logic

**When:** Same code appears in multiple places.

### Before
```tsx
function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch("/api/users")
      .then(r => r.json())
      .then(data => { setUsers(data); setError(null); })
      .catch(e => setError(e.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <Spinner />;
  if (error) return <ErrorMessage error={error} />;
  return <table>{/* ... */}</table>;
}

function ProductList() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch("/api/products")
      .then(r => r.json())
      .then(data => { setProducts(data); setError(null); })
      .catch(e => setError(e.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <Spinner />;
  if (error) return <ErrorMessage error={error} />;
  return <table>{/* ... */}</table>;
}
```

### After
```tsx
// hooks/use-api-data.ts
function useApiData<T>(url: string) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(url)
      .then(r => r.json())
      .then(data => { setData(data); setError(null); })
      .catch(e => setError(e.message))
      .finally(() => setLoading(false));
  }, [url]);

  return { data, loading, error };
}

// Usage
function UserList() {
  const { data: users, loading, error } = useApiData<User[]>("/api/users");
  if (loading) return <Spinner />;
  if (error) return <ErrorMessage error={error} />;
  return <table>{/* render users */}</table>;
}

function ProductList() {
  const { data: products, loading, error } = useApiData<Product[]>("/api/products");
  if (loading) return <Spinner />;
  if (error) return <ErrorMessage error={error} />;
  return <table>{/* render products */}</table>;
}
```

---

## 5. Introduce Parameter Object

**When:** A function has many parameters.

### Before
```ts
function createOrder(
  userId: string,
  items: OrderItem[],
  shippingAddress: Address,
  billingAddress: Address,
  paymentMethod: string,
  couponCode?: string,
  notes?: string
) {
  // ...
}
```

### After
```ts
interface CreateOrderInput {
  userId: string;
  items: OrderItem[];
  shippingAddress: Address;
  billingAddress?: Address;
  paymentMethod: string;
  couponCode?: string;
  notes?: string;
}

function createOrder(input: CreateOrderInput) {
  const { userId, items, shippingAddress, billingAddress = shippingAddress, paymentMethod, couponCode, notes } = input;
  // ...
}
```

---

## 6. Replace Magic Numbers with Named Constants

### Before
```ts
if (user.age >= 18 && user.age <= 65) {
  if (order.total > 10000) {
    discount = 0.15;
  }
}
```

### After
```ts
const MIN_ADULT_AGE = 18;
const MAX_SENIOR_AGE = 65;
const FREE_SHIPPING_THRESHOLD = 10000; // cents
const BULK_DISCOUNT_RATE = 0.15;

if (user.age >= MIN_ADULT_AGE && user.age <= MAX_SENIOR_AGE) {
  if (order.total > FREE_SHIPPING_THRESHOLD) {
    discount = BULK_DISCOUNT_RATE;
  }
}
```

---

## 7. Split Loop

### Before
```ts
function processEmployees(employees: Employee[]) {
  let totalSalary = 0;
  let totalBonus = 0;

  for (const emp of employees) {
    if (emp.isManager) {
      totalSalary += emp.salary * 1.2;
      totalBonus += emp.bonus * 1.5;
    } else {
      totalSalary += emp.salary;
      totalBonus += emp.bonus;
    }
  }

  return { totalSalary, totalBonus };
}
```

### After
```ts
function calculateSalary(employees: Employee[]): number {
  return employees.reduce((sum, emp) => {
    return sum + (emp.isManager ? emp.salary * 1.2 : emp.salary);
  }, 0);
}

function calculateBonus(employees: Employee[]): number {
  return employees.reduce((sum, emp) => {
    return sum + (emp.isManager ? emp.bonus * 1.5 : emp.bonus);
  }, 0);
}
```

---

## Refactoring Safety Rules

1. **Tests first** — ensure behavior is captured before changing code
2. **Small steps** — one refactoring at a time, test after each
3. **Commit often** — each successful refactoring is a commit
4. **Don't change behavior** — if tests fail, you made a mistake
5. **Use IDE tools** — rename, extract, move — let the IDE handle references
6. **Review the diff** — make sure only structure changed, not behavior

---

## Refactoring Anti-Patterns

### ❌ Big Bang Refactoring
```
BAD: Rewriting the whole module at once
GOOD: One small extraction at a time, with tests between each
```

### ❌ Refactoring Without Tests
```
BAD: Changing code with no safety net
GOOD: Write characterization tests first, then refactor
```

### ❌ Refactoring + Feature Change
```
BAD: "I'll refactor and add the new feature at the same time"
GOOD: Refactor first (tests pass), then add feature (tests pass)
```

### ❌ Endless Refactoring
```
BAD: "Just one more improvement..."
GOOD: Set a timebox, ship when time is up
```
