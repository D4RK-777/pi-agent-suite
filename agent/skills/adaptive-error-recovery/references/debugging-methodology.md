# Debugging Methodology

Scientific method for debugging, hypothesis testing, isolation techniques.

---

## 1. The Debugging Process

### Step 1: Reproduce

```
Before anything else, reproduce the issue consistently.

Questions to answer:
- What exact steps trigger the bug?
- Does it happen every time or intermittently?
- What environment (browser, OS, user role)?
- What data triggers it?

If you can't reproduce it, you can't fix it.
```

### Step 2: Isolate

```
Narrow down the cause to the smallest possible scope.

Techniques:
- Binary search: Comment out half the code, does it still happen?
- Input reduction: What's the minimal input that triggers it?
- Dependency removal: Does it happen without the database? Without the API call?
- Environment simplification: Does it happen in a fresh install?

Goal: Reduce "it's broken somewhere in 10,000 lines" to "it's broken in these 20 lines"
```

### Step 3: Hypothesize

```
Form a specific, testable hypothesis about the cause.

Good hypothesis: "The error occurs because the user object is null when the API returns 404"
Bad hypothesis: "Something is wrong with the authentication"

A good hypothesis predicts:
- What you'll see if you're right
- What you'll see if you're wrong
- How to test it
```

### Step 4: Test

```
Test your hypothesis with the smallest possible change.

DO:
- Add a console.log to check the value
- Add a guard clause to see if it prevents the error
- Mock the API response to test the edge case

DON'T:
- Rewrite the whole component
- Change multiple things at once
- Guess and check randomly
```

### Step 5: Fix

```
Once you've confirmed the hypothesis, implement the fix.

Rules:
- Change ONE thing at a time
- Test after each change
- If the fix doesn't work, revert and form a new hypothesis
```

### Step 6: Verify

```
Confirm the fix works AND doesn't break anything else.

- Reproduce the original issue — it should be gone
- Run the test suite — nothing should break
- Test related functionality — no regressions
- Test edge cases — did you fix the class of bug, not just this instance?
```

---

## 2. Common Bug Patterns

### Off-by-One Errors

```ts
// BAD: Loop runs one too many or too few
for (let i = 0; i <= items.length; i++) { // Should be <
  console.log(items[i]); // Last iteration: undefined
}

// How to spot: Check loop boundaries, especially <=, >=, -1, +1
```

### Race Conditions

```tsx
// BAD: Async state update can arrive out of order
function Search({ query }: { query: string }) {
  const [results, setResults] = useState([]);

  useEffect(() => {
    fetchResults(query).then(setResults);
  }, [query]);

  // If user types "a" then "ab" quickly,
  // the "a" response might arrive AFTER "ab", overwriting it
}

// GOOD: Abort previous request
function Search({ query }: { query: string }) {
  const [results, setResults] = useState([]);

  useEffect(() => {
    const controller = new AbortController();
    fetchResults(query, { signal: controller.signal }).then(setResults);
    return () => controller.abort();
  }, [query]);
}
```

### Stale Closures

```tsx
// BAD: count is captured at render time, always 0
function Counter() {
  const [count, setCount] = useState(0);

  const handleClick = useCallback(() => {
    console.log(count); // Always 0!
    setCount(count + 1); // Always sets to 1
  }, []); // Empty deps = stale closure

  return <button onClick={handleClick}>Count: {count}</button>;
}

// GOOD: Functional update
function Counter() {
  const [count, setCount] = useState(0);

  const handleClick = useCallback(() => {
    setCount((prev) => prev + 1); // Always uses latest
  }, []);

  return <button onClick={handleClick}>Count: {count}</button>;
}
```

### Memory Leaks

```tsx
// BAD: Event listener never removed
function Component() {
  useEffect(() => {
    window.addEventListener("resize", handleResize);
    // Missing cleanup
  }, []);
}

// GOOD: Cleanup on unmount
function Component() {
  useEffect(() => {
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);
}
```

### Hydration Mismatches (Next.js)

```tsx
// BAD: Different content on server vs client
function Component() {
  const [isClient, setIsClient] = useState(false);
  // Server: isClient = false
  // Client: isClient = false (initial), then true (after render)
  // Mismatch!

  useEffect(() => setIsClient(true), []);
  return <div>{isClient ? "Client" : "Server"}</div>;
}

// GOOD: Consistent initial render
function Component() {
  const [isClient, setIsClient] = useState(false);
  useEffect(() => setIsClient(true), []);

  if (!isClient) return null; // Or show loading
  return <div>Client</div>;
}
```

---

## 3. Debugging Tools

### Browser DevTools

```
Elements: Inspect DOM, check styles, edit live
Console: Run JS, check errors, log values
Network: Check requests, responses, timing
Performance: Record and analyze runtime performance
Memory: Take heap snapshots, find leaks
Application: Check storage, cookies, service workers
Sources: Set breakpoints, step through code
```

### Node.js Debugging

```bash
# Start with inspector
node --inspect dist/index.js

# Connect Chrome DevTools
# Open chrome://inspect → click your process

# Or use ndb for better experience
npx ndb dist/index.js
```

### React DevTools

```
Components: Inspect component tree, props, state, hooks
Profiler: Record renders, identify unnecessary re-renders
Highlight updates: See what re-renders on each interaction
```

### Logging Strategy

```ts
// Good: Structured, searchable
logger.error({
  message: "Failed to process order",
  orderId: order.id,
  userId: order.userId,
  error: err.message,
  stack: err.stack,
  traceId,
});

// Bad: Unstructured, hard to search
console.error("Order failed:", err);
```

---

## 4. Isolation Techniques

### Binary Search Debugging

```
1. Comment out half the code
2. Does the bug still happen?
   - YES: Bug is in the remaining half
   - NO: Bug is in the commented half
3. Repeat with the suspect half
4. Continue until you've isolated to < 10 lines
```

### Minimal Reproduction

```
Create the smallest possible example that triggers the bug.

Start with:
- A fresh project
- Only the dependencies needed
- Only the code that triggers the bug

If the bug doesn't happen in the minimal example,
the cause is in something you left out.
```

### A/B Comparison

```
Compare working vs broken:
- Working page vs broken page
- Working user vs broken user
- Working environment vs broken environment
- Working version vs broken version (git bisect)

The difference is the cause.
```

---

## Debugging Anti-Patterns

### ❌ Random Changes
```
BAD: "Let me try changing this... and this... and this..."
GOOD: "My hypothesis is X. If I change Y, I expect Z."
```

### ❌ Debugging in Production
```
BAD: Adding console.log and deploying to see what happens
GOOD: Reproducing in staging with structured logging
```

### ❌ Fixing Symptoms
```
BAD: Adding a null check where the error occurs
GOOD: Finding why the value is null in the first place
```

### ❌ Not Reverting
```
BAD: Keeping a failed fix and adding more code on top
GOOD: Reverting to last known good state, starting fresh
```
