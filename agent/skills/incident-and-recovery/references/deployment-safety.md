# Deployment Safety

Blue-green, canary, feature flags, rollback procedures, migration safety.

---

## 1. Blue-Green Deployment

### When to Use
- Zero-downtime deployments required
- Quick rollback capability needed
- Production-critical services

### Pattern

```
┌─────────────────────────────────────────────────────┐
│                    Load Balancer                     │
│                  (points to Blue)                    │
└──────────────┬──────────────────┬───────────────────┘
               │                  │
    ┌──────────▼──────┐  ┌────────▼────────┐
    │   Blue (Live)   │  │  Green (New)    │
    │   v2.4.0        │  │  v2.4.1         │
    │   Running       │  │  Deployed       │
    └─────────────────┘  └─────────────────┘
```

### Deployment Steps

```bash
# Step 1: Deploy new version to green environment
kubectl apply -f deployment-green.yaml

# Step 2: Run health checks against green
curl -s https://green.yourapp.com/api/health | jq

# Step 3: Run smoke tests
npm run test:smoke -- --base-url=https://green.yourapp.com

# Step 4: Switch traffic to green
kubectl patch service api -p '{"spec":{"selector":{"version":"green"}}}'

# Step 5: Monitor for 5 minutes
# Watch error rates, latency, business metrics

# Step 6: If healthy, decommission blue
# If unhealthy, switch back to blue (instant rollback)
kubectl patch service api -p '{"spec":{"selector":{"version":"blue"}}}'
```

### Rollback Procedure

```bash
# Instant rollback — just switch traffic back
kubectl patch service api -p '{"spec":{"selector":{"version":"blue"}}}'

# No data migration needed — both versions share the same database
# Ensure database schema is backward-compatible
```

---

## 2. Canary Deployment

### When to Use
- Risk mitigation for major changes
- A/B testing new features
- Gradual rollout confidence

### Pattern

```
Traffic Split:
  90% → v2.4.0 (stable)
  10% → v2.4.1 (canary)

Monitor for 15 minutes:
  - Error rate comparison
  - Latency comparison
  - Business metrics comparison

If canary is healthy:
  50% → v2.4.1
  Monitor 15 minutes

If still healthy:
  100% → v2.4.1
  Decommission v2.4.0
```

### Kubernetes Canary

```yaml
# canary-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-canary
spec:
  replicas: 1  # Small number for canary
  selector:
    matchLabels:
      app: api
      track: canary
  template:
    metadata:
      labels:
        app: api
        track: canary
    spec:
      containers:
      - name: api
        image: yourapp:v2.4.1
---
# Service routes 10% to canary
apiVersion: v1
kind: Service
metadata:
  name: api
spec:
  selector:
    app: api
  ports:
  - port: 80
    targetPort: 3000
```

### Istio Traffic Split

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: api
spec:
  hosts:
  - api
  http:
  - route:
    - destination:
        host: api
        subset: stable
      weight: 90
    - destination:
        host: api
        subset: canary
      weight: 10
```

---

## 3. Feature Flags

### When to Use
- Deploy code without enabling feature
- Gradual feature rollout
- Kill switch for problematic features

### Core Pattern

```ts
// lib/feature-flags.ts
interface FeatureFlags {
  newCheckout: boolean;
  darkMode: boolean;
  betaSearch: boolean;
  maintenanceMode: boolean;
}

// Default flags (can be overridden by environment)
const defaultFlags: FeatureFlags = {
  newCheckout: false,
  darkMode: false,
  betaSearch: false,
  maintenanceMode: false,
};

// Environment overrides
const envFlags: Partial<FeatureFlags> = {
  newCheckout: process.env.FF_NEW_CHECKOUT === "true",
  maintenanceMode: process.env.FF_MAINTENANCE === "true",
};

export function getFeatureFlags(): FeatureFlags {
  return { ...defaultFlags, ...envFlags };
}

export function isFeatureEnabled(flag: keyof FeatureFlags): boolean {
  return getFeatureFlags()[flag];
}
```

### Usage in Code

```tsx
// components/checkout.tsx
import { isFeatureEnabled } from "@/lib/feature-flags";

export function CheckoutPage() {
  if (isFeatureEnabled("newCheckout")) {
    return <NewCheckout />;
  }
  return <LegacyCheckout />;
}
```

### Database-Driven Feature Flags

```ts
// lib/feature-flags-db.ts
import { db } from "@/lib/db";
import { featureFlags } from "@/lib/db/schema";
import { eq } from "drizzle-orm";

export async function isFeatureEnabledForUser(
  flag: string,
  userId: string
): Promise<boolean> {
  const [flagConfig] = await db
    .select()
    .from(featureFlags)
    .where(eq(featureFlags.name, flag))
    .limit(1);

  if (!flagConfig) return false;

  // Percentage-based rollout
  if (flagConfig.rolloutPercentage < 100) {
    const hash = require("crypto")
      .createHash("md5")
      .update(`${userId}-${flag}`)
      .digest("hex");
    const bucket = parseInt(hash.slice(0, 8), 16) % 100;
    return bucket < flagConfig.rolloutPercentage;
  }

  return flagConfig.enabled;
}
```

### Feature Flag Lifecycle

```
1. Create flag (default: false)
2. Deploy code with flag check
3. Enable for internal users (1%)
4. Monitor metrics
5. Gradually increase rollout (10% → 50% → 100%)
6. Once stable, remove flag and old code path
7. Clean up flag from database
```

---

## 4. Rollback Procedures

### Application Rollback

```bash
# Kubernetes
kubectl rollout undo deployment/api
kubectl rollout status deployment/api

# Verify rollback
curl -s https://yourapp.com/api/health | jq
curl -s https://yourapp.com/api/version | jq

# Monitor for 15 minutes
# Confirm error rates return to baseline
```

### Database Migration Rollback

```ts
// drizzle/migrations/0005_add_column.ts
import { pgTable, text } from "drizzle-orm/pg-core";
import { users } from "../schema";

export async function up() {
  // Add new column (nullable, safe)
  await db.execute(sql`ALTER TABLE users ADD COLUMN new_field TEXT`);
}

export async function down() {
  // Remove column (safe because it was nullable)
  await db.execute(sql`ALTER TABLE users DROP COLUMN new_field`);
}
```

### Migration Safety Rules

1. **Never remove columns in production** — deprecate first, remove in next release
2. **Never change column types** — add new column, migrate data, swap
3. **Always make migrations backward-compatible** — old code must work with new schema
4. **Test rollback in staging** — before running in production
5. **Have a rollback plan** — before running any migration

---

## 5. Deployment Checklist

### Pre-Deployment

- [ ] All tests passing
- [ ] Code review approved
- [ ] Database migrations tested in staging
- [ ] Feature flags configured
- [ ] Rollback plan documented
- [ ] Monitoring alerts verified
- [ ] Team notified of deployment window

### During Deployment

- [ ] Deploy to staging first
- [ ] Run smoke tests against staging
- [ ] Deploy to production (canary or blue-green)
- [ ] Monitor error rates for 5 minutes
- [ ] Monitor business metrics for 15 minutes
- [ ] Confirm deployment successful

### Post-Deployment

- [ ] Error rates at baseline
- [ ] Latency at baseline
- [ ] Business metrics normal
- [ ] No new error log patterns
- [ ] Team notified of completion
- [ ] Deployment documented

---

## Deployment Anti-Patterns

### ❌ Friday Deployments
```
BAD: Deploying at 5pm on Friday
GOOD: Deploy Tuesday-Thursday, 10am-2pm
```

### ❌ No Rollback Plan
```
BAD: "We'll fix it if it breaks"
GOOD: "If error rate > 5%, rollback within 2 minutes"
```

### ❌ Database + Code Coupling
```
BAD: Code requires new column, column requires new code
GOOD: Column added first (backward-compatible), then code deployed
```

### ❌ Big Bang Deployments
```
BAD: Deploy everything at once
GOOD: Deploy incrementally with feature flags
```
