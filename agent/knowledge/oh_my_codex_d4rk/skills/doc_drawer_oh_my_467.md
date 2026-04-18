iterations**: Report the current state as best-effort. List the unresolved differences for the user.
- **Extraction data too large for context**: Truncate deep DOM branches (depth > 6). Focus on top-level structure and defer nested details to iteration fixes.
</Error_Handling>

<Example>
**User**: "Clone https://news.ycombinator.com"

**Pass 1**: Navigate to HN. Extract: table-based layout, orange (#ff6600) nav bar, story list with links + points + comments, footer. Screenshot saved.

**Pass 2**: Regions: nav bar (logo + links), story table (30 rows × title + meta), footer. Tokens: orange #ff6600, gray #828282, Verdana font, 10pt base. Interaction map: story links (external), comment links, "more" pagination.