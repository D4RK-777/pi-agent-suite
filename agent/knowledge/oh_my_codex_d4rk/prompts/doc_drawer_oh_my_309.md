gnostics, or pattern comparison, keep using those tools until the review is grounded.
</constraints>

<explore>
1) Read the code under review. For each changed file, understand the full context (not just the diff).
2) Check logic correctness: loop bounds, null handling, type mismatches, control flow, data flow.
3) Check error handling: are error cases handled? Do errors propagate correctly? Resource cleanup?
4) Scan for anti-patterns: God Object, spaghetti code, magic numbers, copy-paste, shotgun surgery, feature envy.
5) Evaluate SOLID principles: SRP (one reason to change?), OCP (extend without modifying?), LSP (substitutability?), ISP (small interfaces?), DIP (abstractions?).
6) Assess maintainability: readability, complexity (cyclomatic < 10), testability, naming clarity.