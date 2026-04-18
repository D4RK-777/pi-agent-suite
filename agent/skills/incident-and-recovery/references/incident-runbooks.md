# Incident Runbooks

Concrete, step-by-step procedures for common production incidents.

---

## 1. Database Outage

**Symptoms:** API errors, timeouts, "connection refused" logs, health check failures.

### Immediate Response (0-5 minutes)

```bash
# Step 1: Verify the outage
curl -s https://yourapp.com/api/health | jq

# Step 2: Check database connectivity
pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER

# Step 3: Check connection pool
# If using PgBouncer:
echo "SHOW POOLS;" | psql -h $PGBOUNCER_HOST -p $PGBOUNCER_PORT -U pgbouncer

# Step 4: Check database server status
systemctl status postgresql
journalctl -u postgresql --since "5 minutes ago" --no-pager
```

### Diagnosis (5-15 minutes)

```bash
# Check for long-running queries
SELECT pid, now() - pg_stat_activity.query_start AS duration, query, state
FROM pg_stat_activity
WHERE (now() - pg_stat_activity.query_start) > interval '5 minutes'
  AND state != 'idle';

# Check for lock contention
SELECT blocked_locks.pid AS blocked_pid,
       blocking_locks.pid AS blocking_pid,
       blocked_activity.query AS blocked_query,
       blocking_activity.query AS blocking_query
FROM pg_catalog.pg_locks blocked_locks
JOIN pg_catalog.pg_stat_activity blocked_activity ON blocked_activity.pid = blocked_locks.pid
JOIN pg_catalog.pg_locks blocking_locks ON blocking_locks.locktype = blocked_locks.locktype
JOIN pg_catalog.pg_stat_activity blocking_activity ON blocking_activity.pid = blocking_locks.pid
WHERE NOT blocked_locks.granted;

# Check disk space
df -h /var/lib/postgresql/data

# Check memory usage
free -h
```

### Resolution

| Cause | Fix |
|---|---|
| Long-running query | `SELECT pg_cancel_backend(pid);` |
| Connection pool exhausted | Increase pool size or kill idle connections |
| Disk full | Archive old data, expand volume |
| Deadlock | Kill blocking transaction, investigate root cause |
| Server crash | Restart PostgreSQL, check WAL logs |

### Recovery Verification

```bash
# Verify database is accepting connections
pg_isready -h $DB_HOST

# Verify API health
curl -s https://yourapp.com/api/health | jq

# Check error rates have dropped
# In monitoring dashboard: verify 5xx rate < 1%
```

### Post-Incident

1. Document root cause in incident report
2. Add monitoring alert if gap was detected
3. Update runbook if new diagnosis step was needed
4. Schedule follow-up if structural fix is needed

---

## 2. API Failure (5xx Errors)

**Symptoms:** Spike in 500/502/503 errors, user reports of broken features.

### Immediate Response

```bash
# Step 1: Check error rate
# In monitoring: check 5xx rate over last 15 minutes

# Step 2: Check recent deployments
git log --oneline -10
# Or check deployment dashboard

# Step 3: Check application logs
kubectl logs -l app=api --tail=100 | grep -i "error\|exception\|fatal"

# Step 4: Check resource usage
kubectl top pods -l app=api
```

### Diagnosis

```bash
# Check for OOM kills
kubectl get events --sort-by='.lastTimestamp' | grep -i "oom\|killed"

# Check for crash loops
kubectl get pods -l app=api

# Check recent config changes
kubectl describe deployment api | grep -A5 "Conditions"

# Check dependency health
curl -s https://yourapp.com/api/health | jq '.dependencies'
```

### Resolution

| Cause | Fix |
|---|---|
| Bad deployment | `kubectl rollout undo deployment/api` |
| OOM | Increase memory limit, investigate memory leak |
| Dependency failure | Check downstream service, enable circuit breaker |
| Config error | Revert config change, validate config schema |
| Traffic spike | Scale up, enable rate limiting |

### Rollback Procedure

```bash
# Kubernetes rollback
kubectl rollout undo deployment/api

# Verify rollback
kubectl rollout status deployment/api

# Monitor error rate for 5 minutes
# Confirm 5xx rate returns to baseline
```

---

## 3. Memory Leak

**Symptoms:** Gradual memory increase, eventual OOM kills, slowing response times.

### Diagnosis

```bash
# Step 1: Confirm memory trend
# In monitoring: check memory usage over last 24 hours

# Step 2: Check for OOM kills
dmesg | grep -i "out of memory\|oom\|killed process"

# Step 3: Profile memory (Node.js)
# Send SIGUSR2 to trigger heap dump
kill -USR2 <pid>

# Step 4: Analyze heap dump
# Use clinic.js or node --inspect
```

### Common Causes

| Pattern | Fix |
|---|---|
| Unclosed event listeners | Add `.removeListener()` or use `.once()` |
| Growing caches without TTL | Add max size and eviction policy |
| Global variable accumulation | Move to scoped state, add cleanup |
| Unclosed database connections | Use connection pool, ensure `.end()` in finally |
| Large object retention | Stream instead of loading full result |

### Immediate Mitigation

```bash
# Restart pods to free memory (temporary)
kubectl rollout restart deployment/api

# Set memory limits to force recycling
kubectl set resources deployment/api -c=api --limits=memory=512Mi
```

### Permanent Fix

1. Identify leak source via heap comparison
2. Fix the retention pattern
3. Add memory usage alert at 80% of limit
4. Add load test to catch regression

---

## 4. Cascading Failure

**Symptoms:** One service failure triggers failures in dependent services.

### Immediate Response

```bash
# Step 1: Identify the root service
# In monitoring: check which service failed first

# Step 2: Check circuit breaker status
# If using circuit breakers, check which are open

# Step 3: Enable fallbacks
# Enable cached/stale responses where available

# Step 4: Isolate the failing service
# Remove from load balancer or enable maintenance mode
```

### Resolution

| Scenario | Fix |
|---|---|
| Downstream service down | Enable circuit breaker, return cached data |
| Database overload | Enable read replicas, reduce query rate |
| Traffic amplification | Add rate limiting, enable request coalescing |
| Retry storm | Add jitter to retries, cap retry count |

### Prevention

1. Circuit breakers on all external dependencies
2. Timeout on all outbound requests (max 5 seconds)
3. Retry with exponential backoff + jitter
4. Graceful degradation (cached data > error)
5. Bulkhead pattern (separate thread pools per dependency)

---

## 5. Security Incident

**Symptoms:** Unauthorized access detected, suspicious activity, data breach alert.

### Immediate Response (0-15 minutes)

```bash
# Step 1: Confirm the incident
# Verify it's not a false positive

# Step 2: Contain the breach
# Revoke compromised credentials
# Block suspicious IPs
# Enable enhanced logging

# Step 3: Assess scope
# What data was accessed?
# How many users affected?
# When did it start?
```

### Containment

```bash
# Revoke compromised tokens
UPDATE sessions SET revoked_at = NOW() WHERE user_id = '<compromised_user>';

# Block suspicious IPs
# In firewall/WAF:
# Add IP to blocklist

# Rotate compromised secrets
# In secrets manager: rotate API keys, DB passwords
```

### Resolution

| Incident Type | Fix |
|---|---|
| Stolen credentials | Force password reset, revoke sessions, enable MFA |
| API key leak | Rotate key, audit usage, update allowlists |
| SQL injection | Patch vulnerability, audit all queries, add WAF rule |
| XSS attack | Patch vulnerability, add CSP headers, audit user input |
| Unauthorized access | Review permissions, fix RBAC, audit access logs |

### Post-Incident

1. Document timeline and impact
2. Notify affected users if required by law
3. Patch the vulnerability
4. Add monitoring for similar patterns
5. Review and update security runbook

---

## Incident Response Checklist

For EVERY incident:

- [ ] Acknowledge the alert within 5 minutes
- [ ] Assess severity (P1-P4)
- [ ] Communicate status to team
- [ ] Follow the relevant runbook
- [ ] Document actions taken with timestamps
- [ ] Verify recovery (monitoring confirms fix)
- [ ] Write post-incident report within 24 hours
- [ ] Schedule follow-up for structural fixes
- [ ] Update runbook if new learnings

---

## Severity Classification

| Severity | Response Time | Impact | Example |
|---|---|---|---|
| P1 (Critical) | 5 minutes | Complete outage, data loss | Database down, security breach |
| P2 (High) | 15 minutes | Major feature broken | API returning 500s |
| P3 (Medium) | 1 hour | Partial degradation | Slow responses, non-critical feature down |
| P4 (Low) | Next business day | Minor issue, workaround exists | UI glitch, typo |
