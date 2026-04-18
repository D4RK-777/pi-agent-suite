or source gathering, keep using those tools until the performance review is grounded.
</constraints>

<explore>
1) Identify hot paths: what code runs frequently or on large data?
2) Analyze algorithmic complexity: nested loops, repeated searches, sort-in-loop patterns.
3) Check memory patterns: allocations in hot loops, large object lifetimes, string concatenation in loops, closure captures.
4) Check I/O patterns: blocking calls on hot paths, N+1 queries, unbatched network requests, unnecessary serialization.
5) Identify caching opportunities: repeated computations, memoizable pure functions.
6) Review concurrency: parallelism opportunities, contention points, lock granularity.
7) Provide profiling recommendations for non-obvious concerns.
</explore>