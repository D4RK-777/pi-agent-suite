ic question]

### Data Requirements
| Data | Available? | Source |
|------|-----------|--------|
```

<anti_patterns>
- **Defining metrics without connection to user outcomes** -- "API calls per day" is not a product metric unless it reflects user value
- **Over-instrumenting** -- track what informs decisions, not everything that moves
- **Ignoring statistical significance** -- experiment conclusions without power analysis are unreliable
- **Ambiguous metric definitions** -- if two people could calculate the metric differently, it is not defined
- **Missing time windows** -- "completion rate" means nothing without specifying the period
- **Conflating correlation with causation** -- observational metrics suggest, only experiments prove