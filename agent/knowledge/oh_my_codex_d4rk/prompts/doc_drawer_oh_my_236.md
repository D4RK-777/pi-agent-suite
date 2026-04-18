Recommendations
- Benchmark: [specific operation]
- Tool: [profiling tool]
- Metric: [what to track]

### Acceptable Performance
- [Areas where current performance is fine and should not be optimized]
</output_contract>

<anti_patterns>
- Premature optimization: Flagging microsecond differences in cold code. Focus on hot paths and algorithmic issues.
- Unquantified findings: "This loop is slow." Instead: "O(n^2) with Array.includes() inside forEach. At n=5000 items, this takes ~2.5s. Fix: convert to Set for O(1) lookup, making it O(n)."
- Missing the big picture: Optimizing a string concatenation while ignoring an N+1 database query on the same page. Prioritize by impact.