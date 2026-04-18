nt>

<Context_Budget>
Pass 1 extraction can produce very large data. Apply these limits proactively:

- **DOM tree**: If the serialized JSON exceeds ~30KB, reduce `depth` parameter from 8 to 4 and re-extract. Focus on top-level structure.
- **Accessibility snapshot**: If it exceeds ~20KB, this is normal for complex pages. Summarize key landmarks rather than keeping the full tree.
- **Interactive elements**: Cap at 50 elements. If more exist, keep only visible ones (`isVisible: true`).
- **Total extraction context**: Aim for under 60KB combined. If exceeded, prioritize: screenshot > accessibility snapshot > interactive elements > DOM styles.