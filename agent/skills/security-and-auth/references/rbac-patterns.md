# RBAC Patterns

Role hierarchies, permission checks, policy-based access, resource-level permissions.

---

## 1. Role-Based Access Control

### Core Role Definitions

```ts
// lib/auth/roles.ts
export const ROLES = {
  SUPER_ADMIN: "super_admin",
  ADMIN: "admin",
  MODERATOR: "moderator",
  USER: "user",
} as const;

export type Role = (typeof ROLES)[keyof typeof ROLES];

// Role hierarchy — higher roles inherit lower role permissions
export const ROLE_HIERARCHY: Record<Role, number> = {
  [ROLES.SUPER_ADMIN]: 100,
  [ROLES.ADMIN]: 80,
  [ROLES.MODERATOR]: 60,
  [ROLES.USER]: 10,
};

export function hasMinimumRole(userRole: Role, requiredRole: Role): boolean {
  return ROLE_HIERARCHY[userRole] >= ROLE_HIERARCHY[requiredRole];
}
```

### Permission Matrix

```ts
// lib/auth/permissions.ts
import { Role, ROLES } from "./roles";

export const PERMISSIONS = {
  // User management
  USER_READ: "user:read",
  USER_WRITE: "user:write",
  USER_DELETE: "user:delete",
  // Content
  CONTENT_READ: "content:read",
  CONTENT_WRITE: "content:write",
  CONTENT_DELETE: "content:delete",
  CONTENT_PUBLISH: "content:publish",
  // Settings
  SETTINGS_READ: "settings:read",
  SETTINGS_WRITE: "settings:write",
  // Billing
  BILLING_READ: "billing:read",
  BILLING_WRITE: "billing:write",
} as const;

export type Permission = (typeof PERMISSIONS)[keyof typeof PERMISSIONS];

// Role → Permission mapping
export const ROLE_PERMISSIONS: Record<Role, Permission[]> = {
  [ROLES.SUPER_ADMIN]: Object.values(PERMISSIONS), // All permissions
  [ROLES.ADMIN]: [
    PERMISSIONS.USER_READ, PERMISSIONS.USER_WRITE,
    PERMISSIONS.CONTENT_READ, PERMISSIONS.CONTENT_WRITE, PERMISSIONS.CONTENT_DELETE, PERMISSIONS.CONTENT_PUBLISH,
    PERMISSIONS.SETTINGS_READ, PERMISSIONS.SETTINGS_WRITE,
    PERMISSIONS.BILLING_READ, PERMISSIONS.BILLING_WRITE,
  ],
  [ROLES.MODERATOR]: [
    PERMISSIONS.USER_READ,
    PERMISSIONS.CONTENT_READ, PERMISSIONS.CONTENT_WRITE, PERMISSIONS.CONTENT_DELETE,
    PERMISSIONS.SETTINGS_READ,
  ],
  [ROLES.USER]: [
    PERMISSIONS.USER_READ,
    PERMISSIONS.CONTENT_READ, PERMISSIONS.CONTENT_WRITE,
  ],
};

export function hasPermission(userRole: Role, permission: Permission): boolean {
  return ROLE_PERMISSIONS[userRole]?.includes(permission) ?? false;
}

export function hasAnyPermission(userRole: Role, permissions: Permission[]): boolean {
  return permissions.some((p) => hasPermission(userRole, p));
}

export function hasAllPermissions(userRole: Role, permissions: Permission[]): boolean {
  return permissions.every((p) => hasPermission(userRole, p));
}
```

### Permission Check Middleware

```ts
// lib/auth/permission-check.ts
import { NextResponse } from "next/server";
import { Permission, hasPermission } from "./permissions";
import { getCurrentUser } from "./helpers";

export async function requirePermission(permission: Permission) {
  const user = await getCurrentUser();
  if (!user) throw new Error("Unauthorized");

  if (!hasPermission(user.role as any, permission)) {
    throw new Error("Forbidden");
  }

  return user;
}

// Usage in route handler
export async function GET() {
  try {
    await requirePermission(PERMISSIONS.USER_READ);
    // ... authorized logic
  } catch (error) {
    if (error.message === "Unauthorized") return unauthorized();
    if (error.message === "Forbidden") return forbidden();
    throw error;
  }
}
```

---

## 2. Resource-Level Permissions

### Ownership-Based Access

```ts
// lib/auth/resource-permission.ts
import { db } from "@/lib/db";
import { documents } from "@/lib/db/schema";
import { eq, and } from "drizzle-orm";
import { getCurrentUser } from "./helpers";
import { hasPermission, PERMISSIONS } from "./permissions";

export async function canAccessDocument(documentId: string, action: "read" | "write" | "delete") {
  const user = await getCurrentUser();
  if (!user) return false;

  // Admins can access all documents
  if (hasPermission(user.role as any, PERMISSIONS.CONTENT_READ)) {
    return true;
  }

  // Users can only access their own documents
  const [doc] = await db
    .select()
    .from(documents)
    .where(and(eq(documents.id, documentId), eq(documents.ownerId, user.id)))
    .limit(1);

  return !!doc;
}

// Usage in route
export async function PATCH(request: NextRequest, { params }: { params: { id: string } }) {
  const { id } = await params;

  if (!(await canAccessDocument(id, "write"))) {
    return forbidden("You don't have permission to edit this document");
  }

  // ... edit logic
}
```

### Team-Based Permissions

```ts
// lib/auth/team-permission.ts
import { db } from "@/lib/db";
import { teamMembers, teams } from "@/lib/db/schema";
import { eq, and } from "drizzle-orm";

export const TEAM_ROLES = {
  OWNER: "owner",
  ADMIN: "admin",
  EDITOR: "editor",
  VIEWER: "viewer",
} as const;

export async function getTeamRole(userId: string, teamId: string): Promise<string | null> {
  const [member] = await db
    .select({ role: teamMembers.role })
    .from(teamMembers)
    .where(and(eq(teamMembers.userId, userId), eq(teamMembers.teamId, teamId)))
    .limit(1);

  return member?.role || null;
}

export async function canAccessTeamResource(
  userId: string,
  teamId: string,
  requiredRole: string
): Promise<boolean> {
  const role = await getTeamRole(userId, teamId);
  if (!role) return false;

  const roleHierarchy = { owner: 100, admin: 80, editor: 60, viewer: 10 };
  return roleHierarchy[role as keyof typeof roleHierarchy] >= roleHierarchy[requiredRole as keyof typeof roleHierarchy];
}
```

---

## 3. Policy-Based Access Control (ABAC)

### When RBAC Isn't Enough

```ts
// lib/auth/policies.ts
import { getCurrentUser } from "./helpers";

interface PolicyContext {
  user: { id: string; role: string };
  resource: Record<string, unknown>;
  action: string;
  time?: Date;
  ip?: string;
}

type PolicyCheck = (ctx: PolicyContext) => boolean | Promise<boolean>;

// Policy: Users can only edit their own resources during business hours
export const ownResourceBusinessHours: PolicyCheck = async (ctx) => {
  if (ctx.resource.ownerId !== ctx.user.id) return false;
  const hour = (ctx.time || new Date()).getHours();
  return hour >= 8 && hour <= 18;
};

// Policy: Admins can edit anything except super admin resources
export const adminExceptSuperAdmin: PolicyCheck = async (ctx) => {
  if (ctx.user.role !== "admin") return false;
  if (ctx.resource.ownerRole === "super_admin") return false;
  return true;
};

// Policy engine
export async function evaluatePolicy(
  policies: PolicyCheck[],
  context: PolicyContext
): Promise<boolean> {
  // All policies must pass
  for (const policy of policies) {
    if (!(await policy(context))) return false;
  }
  return true;
}

// Usage
export async function PATCH(request: NextRequest, { params }: { params: { id: string } }) {
  const user = await getCurrentUser();
  if (!user) return unauthorized();

  const resource = await getResource(params.id);
  if (!resource) return notFound("Resource");

  const allowed = await evaluatePolicy(
    [ownResourceBusinessHours, adminExceptSuperAdmin],
    {
      user,
      resource,
      action: "update",
      time: new Date(),
      ip: request.ip || undefined,
    }
  );

  if (!allowed) return forbidden("You don't have permission to perform this action");

  // ... update logic
}
```

---

## 4. Permission Checks in Practice

### Route-Level Checks

```ts
// app/api/users/route.ts
export async function GET() {
  await requirePermission(PERMISSIONS.USER_READ);
  const users = await userRepository.list({});
  return NextResponse.json({ data: users });
}

export async function POST(request: NextRequest) {
  await requirePermission(PERMISSIONS.USER_WRITE);
  // ... create user
}

export async function DELETE(request: NextRequest, { params }: { params: { id: string } }) {
  await requirePermission(PERMISSIONS.USER_DELETE);
  // ... delete user
}
```

### Component-Level Checks (Frontend)

```tsx
// components/auth/permission-guard.tsx
"use client";

import { useAuth } from "@/hooks/use-auth";
import { hasPermission, Permission } from "@/lib/auth/permissions";

export function PermissionGuard({
  permission,
  children,
  fallback = null,
}: {
  permission: Permission;
  children: React.ReactNode;
  fallback?: React.ReactNode;
}) {
  const { user } = useAuth();
  if (!user) return null;

  if (!hasPermission(user.role as any, permission)) {
    return <>{fallback}</>;
  }

  return <>{children}</>;
}

// Usage
<PermissionGuard permission={PERMISSIONS.USER_DELETE} fallback={<span>View only</span>}>
  <button onClick={() => deleteUser(userId)}>Delete User</button>
</PermissionGuard>
```

---

## RBAC Selection Guide

| Scenario | Best Approach |
|---|---|
| Simple roles (user/admin) | Role hierarchy + permission matrix |
| Resource ownership | Ownership checks + role fallback |
| Team-based access | Team roles + resource permissions |
| Time/location-based rules | Policy-based access (ABAC) |
| Dynamic permissions | Database-driven permission table |
| Multi-tenant | Tenant isolation + role within tenant |

---

## RBAC Anti-Patterns

### ❌ Hardcoded Role Checks
```ts
// BAD: Scattered role checks
if (user.role !== "admin") return forbidden();
if (user.role === "user") return forbidden();

// GOOD: Permission-based checks
await requirePermission(PERMISSIONS.USER_WRITE);
```

### ❌ No Resource Ownership Check
```ts
// BAD: Any admin can delete any user
export async function DELETE(request, { params }) {
  await requirePermission(PERMISSIONS.USER_DELETE);
  await userRepository.delete(params.id);
}

// GOOD: Check ownership or role
export async function DELETE(request, { params }) {
  const user = await getCurrentUser();
  const target = await userRepository.findById(params.id);

  // Can delete if admin OR if deleting own account
  const isAdmin = hasPermission(user.role, PERMISSIONS.USER_DELETE);
  const isOwn = target?.id === user.id;

  if (!isAdmin && !isOwn) return forbidden();
  await userRepository.delete(params.id);
}
```

### ❌ Role Creep
```ts
// BAD: Adding special-case logic to role checks
if (user.role === "admin" || user.id === "special-user-id") {
  // Backdoor access
}

// GOOD: Create a proper role or permission
// Add "super_moderator" role with needed permissions
```
