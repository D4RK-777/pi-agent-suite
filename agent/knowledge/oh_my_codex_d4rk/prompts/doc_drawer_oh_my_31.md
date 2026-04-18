tus":"approved","reviewer":"leader-fixed","decision_reason":"demo approval","required":true}' --json
omx team api cleanup --input '{"team_name":"e2e-team-demo"}' --json
```

### 7.4 Verification expectations

```bash
# Envelope checks (schema_version + operation + ok)
omx team api get-summary --input '{"team_name":"e2e-team-demo"}' --json | jq -e '.schema_version == "1.0" and .operation == "get-summary" and (.ok == true or .ok == false)'

# Team lifecycle checks
omx team status "e2e-team-demo"
omx team shutdown "e2e-team-demo"
```