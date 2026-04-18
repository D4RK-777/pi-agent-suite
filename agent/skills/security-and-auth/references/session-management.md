# Session Management

JWT vs sessions, refresh tokens, session invalidation, concurrent sessions.

---

## 1. JWT Sessions

### When to Use JWT
- Stateless authentication (no server-side session store)
- Microservices (token can be verified by any service)
- Mobile apps (no cookie support)
- Short-lived tokens (15 min access tokens)

### JWT Structure

```ts
// lib/auth/jwt.ts
import { SignJWT, jwtVerify, type JWTPayload } from "jose";

const ACCESS_TOKEN_EXPIRY = "15m";
const REFRESH_TOKEN_EXPIRY = "7d";

interface TokenPayload extends JWTPayload {
  userId: string;
  role: string;
  sessionVersion?: number;
}

export async function createAccessToken(payload: TokenPayload): Promise<string> {
  return new SignJWT(payload)
    .setProtectedHeader({ alg: "HS256" })
    .setIssuedAt()
    .setExpirationTime(ACCESS_TOKEN_EXPIRY)
    .setJti(crypto.randomUUID())
    .sign(new TextEncoder().encode(env.JWT_SECRET));
}

export async function createRefreshToken(userId: string): Promise<string> {
  return new SignJWT({ userId })
    .setProtectedHeader({ alg: "HS256" })
    .setIssuedAt()
    .setExpirationTime(REFRESH_TOKEN_EXPIRY)
    .setJti(crypto.randomUUID())
    .sign(new TextEncoder().encode(env.JWT_SECRET));
}

export async function verifyAccessToken(token: string): Promise<TokenPayload> {
  const { payload } = await jwtVerify(token, new TextEncoder().encode(env.JWT_SECRET));
  return payload as TokenPayload;
}
```

### Auth Middleware (JWT Verification)

```ts
// middleware.ts
import { verifyAccessToken } from "@/lib/auth/jwt";

export async function middleware(request: NextRequest) {
  const authHeader = request.headers.get("authorization");
  const token = authHeader?.startsWith("Bearer ") ? authHeader.slice(7) : null;

  if (!token) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  try {
    const payload = await verifyAccessToken(token);
    const requestHeaders = new Headers(request.headers);
    requestHeaders.set("x-user-id", payload.userId);
    requestHeaders.set("x-user-role", payload.role);
    return NextResponse.next({ request: { headers: requestHeaders } });
  } catch {
    return NextResponse.json({ error: "Invalid or expired token" }, { status: 401 });
  }
}
```

---

## 2. Database Sessions

### When to Use DB Sessions
- Need to invalidate sessions server-side
- Track active sessions per user
- Enforce concurrent session limits
- Audit login activity

### Session Table

```ts
// drizzle/migrations/0001_create_sessions.ts
import { pgTable, text, timestamp, uuid, varchar } from "drizzle-orm/pg-core";

export const sessions = pgTable("sessions", {
  id: uuid("id").defaultRandom().primaryKey(),
  userId: uuid("user_id").notNull().references(() => users.id),
  tokenHash: text("token_hash").notNull(),
  userAgent: text("user_agent"),
  ip: text("ip"),
  expiresAt: timestamp("expires_at").notNull(),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  revokedAt: timestamp("revoked_at"),
});
```

### Session Manager

```ts
// lib/auth/session-manager.ts
import { db } from "@/lib/db";
import { sessions } from "@/lib/db/schema";
import { eq, and, gt, desc, count } from "drizzle-orm";
import { randomBytes } from "crypto";

const MAX_CONCURRENT_SESSIONS = 5;
const SESSION_EXPIRY_DAYS = 30;

export async function createSession(
  userId: string,
  userAgent?: string,
  ip?: string
): Promise<{ sessionToken: string; expiresAt: Date }> {
  // Check concurrent session limit
  const [{ activeSessions }] = await db
    .select({ activeSessions: count() })
    .from(sessions)
    .where(and(
      eq(sessions.userId, userId),
      gt(sessions.expiresAt, new Date()),
    ));

  if (activeSessions >= MAX_CONCURRENT_SESSIONS) {
    // Revoke oldest session
    const [oldest] = await db
      .select()
      .from(sessions)
      .where(and(
        eq(sessions.userId, userId),
        gt(sessions.expiresAt, new Date()),
      ))
      .orderBy(sessions.createdAt)
      .limit(1);

    if (oldest) {
      await db.update(sessions).set({ revokedAt: new Date() }).where(eq(sessions.id, oldest.id));
    }
  }

  // Generate session token
  const sessionToken = randomBytes(48).toString("hex");
  const tokenHash = require("crypto").createHash("sha256").update(sessionToken).digest("hex");
  const expiresAt = new Date(Date.now() + SESSION_EXPIRY_DAYS * 24 * 60 * 60 * 1000);

  await db.insert(sessions).values({
    userId,
    tokenHash,
    userAgent: userAgent || null,
    ip: ip || null,
    expiresAt,
  });

  return { sessionToken, expiresAt };
}

export async function verifySession(token: string): Promise<{ userId: string } | null> {
  const tokenHash = require("crypto").createHash("sha256").update(token).digest("hex");

  const [session] = await db
    .select()
    .from(sessions)
    .where(and(
      eq(sessions.tokenHash, tokenHash),
      gt(sessions.expiresAt, new Date()),
    ))
    .limit(1);

  if (!session || session.revokedAt) return null;

  return { userId: session.userId };
}

export async function revokeSession(token: string): Promise<void> {
  const tokenHash = require("crypto").createHash("sha256").update(token).digest("hex");
  await db.update(sessions).set({ revokedAt: new Date() }).where(eq(sessions.tokenHash, tokenHash));
}

export async function revokeAllUserSessions(userId: string): Promise<void> {
  await db
    .update(sessions)
    .set({ revokedAt: new Date() })
    .where(and(
      eq(sessions.userId, userId),
      gt(sessions.expiresAt, new Date()),
    ));
}

export async function getUserSessions(userId: string) {
  return db
    .select({
      id: sessions.id,
      userAgent: sessions.userAgent,
      ip: sessions.ip,
      createdAt: sessions.createdAt,
      expiresAt: sessions.expiresAt,
    })
    .from(sessions)
    .where(and(
      eq(sessions.userId, userId),
      gt(sessions.expiresAt, new Date()),
    ))
    .orderBy(desc(sessions.createdAt));
}
```

---

## 3. Refresh Token Rotation

### The Pattern

```
Access Token (15 min) → API requests
Refresh Token (7 days) → Get new access tokens
  ↓
On each refresh:
  1. Verify refresh token
  2. Delete old refresh token
  3. Create new access + refresh token pair
  4. If refresh token was already used → REVOKE ALL SESSIONS (compromise detected)
```

### Implementation

```ts
// lib/auth/refresh.ts
import { db } from "@/lib/db";
import { refreshTokens, users } from "@/lib/db/schema";
import { eq, and, gt } from "drizzle-orm";
import { createTokenPair } from "./tokens";

export async function refreshAccessToken(oldRefreshToken: string) {
  const tokenHash = hashToken(oldRefreshToken);

  // Find the refresh token
  const [storedToken] = await db
    .select()
    .from(refreshTokens)
    .where(and(
      eq(refreshTokens.tokenHash, tokenHash),
      gt(refreshTokens.expiresAt, new Date()),
    ))
    .limit(1);

  if (!storedToken) {
    // Token not found — could be expired or already used
    throw new Error("Invalid refresh token");
  }

  // Check if it's already been used (reuse detection)
  if (storedToken.usedAt) {
    // COMPROMISE DETECTED — revoke all sessions for this user
    await revokeAllUserSessions(storedToken.userId);
    throw new Error("Session compromised —all sessions revoked");
  }

  // Mark old token as used
  await db
    .update(refreshTokens)
    .set({ usedAt: new Date() })
    .where(eq(refreshTokens.id, storedToken.id));

  // Create new token pair
  const user = await userRepository.findById(storedToken.userId);
  if (!user) throw new Error("User not found");

  return createTokenPair(user.id, user.role);
}

function hashToken(token: string): string {
  return require("crypto").createHash("sha256").update(token).digest("hex");
}
```

---

## 4. Session Invalidation

### Triggers for Invalidation

```ts
// lib/auth/session-invalidation.ts

// Password change — invalidate all other sessions
export async function onPasswordChange(userId: string) {
  await db
    .update(sessions)
    .set({ revokedAt: new Date() })
    .where(and(
      eq(sessions.userId, userId),
      // Keep current session alive (identified by request)
    ));
}

// Role change — invalidate all sessions
export async function onRoleChange(userId: string) {
  await revokeAllUserSessions(userId);
}

// Suspicious activity — invalidate all sessions
export async function onSuspiciousActivity(userId: string) {
  await revokeAllUserSessions(userId);
  await emailService.sendTemplate(
    (await userRepository.findById(userId))!.email,
    "security-alert",
    { action: "All sessions have been revoked due to suspicious activity" }
  );
}

// Session expiry — cleanup expired sessions
export async function cleanupExpiredSessions() {
  await db
    .delete(sessions)
    .where(lt(sessions.expiresAt, new Date()));
}

// Run cleanup daily
// cron job → cleanupExpiredSessions()
```

---

## Session Selection Guide

| Scenario | Best Approach | Why |
|---|---|---|
| Stateless API | JWT only | No server state, fast verification |
| Need session tracking | DB sessions | Can revoke, audit, limit concurrent |
| Mobile app | JWT + refresh tokens | No cookies, token-based |
| High security | DB sessions + rotation | Full control, compromise detection |
| Microservices | JWT | Verifiable by any service |
| Admin panel | DB sessions + IP binding | Strict control, audit trail |

---

## Session Anti-Patterns

### ❌ Never-Expiring Tokens
```ts
// BAD: Token never expires
.setExpirationTime("100y")

// GOOD: Short expiry with refresh
.setExpirationTime("15m")
```

### ❌ No Session Invalidation
```ts
// BAD: Can't log out user from other devices
// No revoke mechanism

// GOOD: Can invalidate any session
await revokeAllUserSessions(userId);
```

### ❌ Storing Sensitive Data in JWT
```ts
// BAD: PII in token (visible to anyone who decodes it)
{ userId, email, name, role, ssn, creditCard }

// GOOD: Only non-sensitive identifiers
{ userId, role, sessionVersion }
```

### ❌ No Concurrent Session Limit
```ts
// BAD: User can have 1000 active sessions
// No check on session count

// GOOD: Limit concurrent sessions
if (activeSessions >= MAX_CONCURRENT_SESSIONS) {
  // Revoke oldest
}
```
