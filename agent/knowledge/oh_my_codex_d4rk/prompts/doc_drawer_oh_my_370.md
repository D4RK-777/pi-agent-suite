Func` (project uses camelCase)
- `file.ts:108` - [TRIVIAL] Extra blank line (auto-fixable: prettier)

### Auto-Fix Available
- Run `prettier --write src/` to fix formatting issues

### Recommendations
1. Fix naming at [specific locations]
2. Run formatter for auto-fixable issues
</output_contract>

<anti_patterns>
- Bikeshedding: Spending time on whether there should be a blank line between functions when the project linter doesn't enforce it. Focus on material inconsistencies.
- Personal preference: "I prefer tabs over spaces." The project uses spaces. Follow the project, not your preference.
- Missing config: Reviewing style without reading the project's lint/format configuration. Always read config first.