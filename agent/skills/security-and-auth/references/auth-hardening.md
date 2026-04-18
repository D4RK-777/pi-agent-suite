# Auth Hardening

Rate limiting, brute force protection, session fixation, token expiry.

---

## 1. Brute Force Protection

### Account Lockout Pattern

```ts
// lib/auth/lockout.ts
import { db } from "@/lib/db";
import { loginAttempts } from "@/lib/db/schema";
import { eq, and, gt, sql } from "drizzle-orm";

const MAX_ATTEMPTS = 5;
const LOCKOUT_DURATION_MS = 15 * 60 * 1000; // 15 minutes

export async function checkLockout(email: string): Promise<{ locked: boolean; remainingAttempts: number; unlockAt?: Date }> {
  const [attempt] = await db
    .select()
    .from(loginAttempts)
    .where(eq(loginAttempts.email, email.toLowerCase()))
    .limit(1);

  if (!attempt) {
    return { locked: false, remainingAttempts: MAX_ATTEMPTS };
  }

  const isLocked = attempt.count >= MAX_ATTEMPTS &&
    Date.now() - attempt.lastAttempt.getTime() < LOCKOUT_DURATION_MS;

  if (isLocked) {
    const unlockAt = new Date(attempt.lastAttempt.getTime() + LOCKOUT_DURATION_MS);
    return { locked: true, remainingAttempts: 0, unlockAt };
  }

  // Reset if lockout period has passed
  if (Date.now() - attempt.lastAttempt.getTime() >= LOCKOUT_DURATION_MS) {
    await db.delete(loginAttempts).where(eq(loginAttempts.email, email.toLowerCase()));
    return { locked: false, remainingAttempts: MAX_ATTEMPTS };
  }

  return {
    locked: false,
    remainingAttempts: MAX_ATTEMPTS - attempt.count,
  };
}

export async function recordFailedAttempt(email: string): Promise<void> {
  await db
    .insert(loginAttempts)
    .values({
      email: email.toLowerCase(),
      count: 1,
      lastAttempt: new Date(),
    })
    .onConflictDoUpdate({
      target: loginAttempts.email,
      set: {
        count: sql`${loginAttempts.count} + 1`,
        lastAttempt: new Date(),
      },
    });
}

export async function resetAttempts(email: string): Promise<void> {
  await db.delete(loginAttempts).where(eq(loginAttempts.email, email.toLowerCase()));
}
```

### Usage in Login Route

```ts
// app/api/auth/login/route.ts
export async function POST(request: NextRequest) {
  const { email, password } = await request.json();

  // Check lockout
  const lockout = await checkLockout(email);
  if (lockout.locked) {
    return NextResponse.json(
      {
        error: `Too many failed attempts. Try again after ${lockout.unlockAt?.toLocaleTimeString()}`,
        code: "ACCOUNT_LOCKED",
        unlockAt: lockout.unlockAt,
      },
      { status: 429 }
    );
  }

  // Attempt login
  try {
    const user = await userService.authenticate(email, password);
    await resetAttempts(email); // Reset on success
    // ... create session
    return NextResponse.json({ data: { token } });
  } catch {
    await recordFailedAttempt(email);
    const remaining = lockout.remainingAttempts - 1;
    return NextResponse.json(
      {
        error: "Invalid email or password",
        remainingAttempts: Math.max(0, remaining),
      },
      { status: 401 }
    );
  }
}
```

---

## 2. Session Fixation Protection

### The Attack
```
1. Attacker visits site, gets session ID: abc123
2. Attacker sends link to victim: https://site.com/login?session=abc123
3. Victim logs in, now abc123 is an authenticated session
4. Attacker uses abc123 to access victim's account
```

### The Fix
```ts
// lib/auth/session.ts
import { SignJWT } from "jose";

export async function createSession(userId: string, role: string): Promise<string> {
  // Generate a NEW session ID — never reuse the pre-login session
  const jti = crypto.randomUUID(); // Fresh session ID

  return new SignJWT({ userId, role })
    .setProtectedHeader({ alg: "HS256" })
    .setJti(jti) // Unique session identifier
    .setIssuedAt()
    .setExpirationTime("7d")
    .setSubject(userId)
    .sign(new TextEncoder().encode(env.JWT_SECRET));
}

// On login — ALWAYS regenerate session
export async function login(email: string, password: string) {
  const user = await userService.authenticate(email, password);
  const token = await createSession(user.id, user.role);
  await resetAttempts(email);
  return token; // New session, not the pre-login one
}
```

### Session Invalidation on Password Change

```ts
// lib/auth/session.ts
export async function invalidateAllSessions(userId: string): Promise<void> {
  // Add a "session version" to the user record
  await db
    .update(users)
    .set({ sessionVersion: sql`${users.sessionVersion} + 1` })
    .where(eq(users.id, userId));
}

// In JWT verification
export async function verifyToken(token: string) {
  const { payload } = await jwtVerify(token, secret);
  const user = await userRepository.findById(payload.sub);

  // Check session version
  if (user.sessionVersion !== payload.sessionVersion) {
    throw new Error("Session invalidated");
  }

  return payload;
}

// On password change
async function changePassword(userId: string, newPassword: string) {
  await userRepository.update(userId, { passwordHash: await hashPassword(newPassword) });
  await invalidateAllSessions(userId); // All other devices logged out
}
```

---

## 3. Token Expiry and Refresh

### Access + Refresh Token Pattern

```ts
// lib/auth/tokens.ts
import { SignJWT, jwtVerify } from "jose";

const ACCESS_TOKEN_EXPIRY = "15m";  // Short-lived
const REFRESH_TOKEN_EXPIRY = "7d";   // Longer-lived

export async function createTokenPair(userId: string, role: string) {
  const secret = new TextEncoder().encode(env.JWT_SECRET);

  // Access token — short-lived, used for API requests
  const accessToken = await new SignJWT({ userId, role })
    .setProtectedHeader({ alg: "HS256" })
    .setSubject(userId)
    .setIssuedAt()
    .setExpirationTime(ACCESS_TOKEN_EXPIRY)
    .setJti(crypto.randomUUID())
    .sign(secret);

  // Refresh token — longer-lived, used only to get new access tokens
  const refreshToken = await new SignJWT({ userId })
    .setProtectedHeader({ alg: "HS256" })
    .setSubject(userId)
    .setIssuedAt()
    .setExpirationTime(REFRESH_TOKEN_EXPIRY)
    .setJti(crypto.randomUUID())
    .sign(secret);

  // Store refresh token hash in DB
  await db.insert(refreshTokens).values({
    userId,
    tokenHash: hashToken(refreshToken),
    expiresAt: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000),
  });

  return { accessToken, refreshToken };
}

export async function refreshAccessToken(refreshToken: string) {
  const secret = new TextEncoder().encode(env.JWT_SECRET);

  // Verify refresh token
  const { payload } = await jwtVerify(refreshToken, secret);

  // Check if it's in the database (not revoked)
  const [stored] = await db
    .select()
    .from(refreshTokens)
    .where(and(
      eq(refreshTokens.userId, payload.sub),
      eq(refreshTokens.tokenHash, hashToken(refreshToken))
    ))
    .limit(1);

  if (!stored) {
    throw new Error("Refresh token revoked");
  }

  // Rotate: delete old, create new
  await db.delete(refreshTokens).where(eq(refreshTokens.id, stored.id));

  const user = await userRepository.findById(payload.sub);
  if (!user) throw new Error("User not found");

  return createTokenPair(user.id, user.role);
}

function hashToken(token: string): string {
  return require("crypto").createHash("sha256").update(token).digest("hex");
}
```

### Token Expiry Handling (Client-Side)

```ts
// lib/api/client.ts
let accessToken: string | null = null;
let refreshToken: string | null = null;

async function apiCall(url: string, options: RequestInit) {
  let response = await fetch(url, {
    ...options,
    headers: { ...options.headers, Authorization: `Bearer ${accessToken}` },
  });

  // If access token expired, try refresh
  if (response.status === 401 && refreshToken) {
    const { accessToken: newAccess, refreshToken: newRefresh } =
      await fetch("/api/auth/refresh", {
        method: "POST",
        body: JSON.stringify({ refreshToken }),
      }).then(r => r.json());

    accessToken = newAccess;
    refreshToken = newRefresh;

    // Retry original request
    response = await fetch(url, {
      ...options,
      headers: { ...options.headers, Authorization: `Bearer ${accessToken}` },
    });
  }

  return response;
}
```

---

## 4. Password Policy

```ts
// lib/auth/password.ts
import { hash, verify } from "argon2";

export async function hashPassword(password: string): Promise<string> {
  return hash(password, {
    memoryCost: 19456,    // 19 MB
    timeCost: 2,          // 2 iterations
    parallelism: 1,
  });
}

export async function verifyPassword(password: string, hash: string): Promise<boolean> {
  return verify(hash, password);
}

// Password strength validation
export function validatePasswordStrength(password: string): string[] {
  const issues: string[] = [];

  if (password.length < 8) issues.push("At least 8 characters");
  if (password.length > 128) issues.push("Maximum 128 characters");
  if (!/[A-Z]/.test(password)) issues.push("At least one uppercase letter");
  if (!/[a-z]/.test(password)) issues.push("At least one lowercase letter");
  if (!/[0-9]/.test(password)) issues.push("At least one number");
  if (!/[!@#$%^&*(),.?":{}|<>]/.test(password)) issues.push("At least one special character");

  // Check against common passwords
  const commonPasswords = ["password", "12345678", "qwerty123", "admin123"];
  if (commonPasswords.includes(password.toLowerCase())) {
    issues.push("Password is too common");
  }

  return issues;
}
```

---

## 5. Account Recovery Security

### Secure Password Reset

```ts
// lib/auth/reset.ts
import { randomBytes } from "crypto";

export async function requestPasswordReset(email: string): Promise<void> {
  const user = await userRepository.findByEmail(email);
  if (!user) return; // Don't reveal if email exists

  // Generate secure token
  const token = randomBytes(32).toString("hex");
  const expiresAt = new Date(Date.now() + 60 * 60 * 1000); // 1 hour

  // Store hash, not the token itself
  const tokenHash = require("crypto").createHash("sha256").update(token).digest("hex");

  await db.insert(resetTokens).values({
    userId: user.id,
    tokenHash,
    expiresAt,
  });

  // Send email with token (not the hash)
  const resetUrl = `${env.APP_URL}/reset-password?token=${token}`;
  await emailService.sendTemplate(user.email, "password-reset", { resetUrl });
}

export async function resetPassword(token: string, newPassword: string): Promise<boolean> {
  const tokenHash = require("crypto").createHash("sha256").update(token).digest("hex");

  const [resetToken] = await db
    .select()
    .from(resetTokens)
    .where(and(
      eq(resetTokens.tokenHash, tokenHash),
      gt(resetTokens.expiresAt, new Date()),
    ))
    .limit(1);

  if (!resetToken) return false;

  // Update password
  await userRepository.update(resetToken.userId, {
    passwordHash: await hashPassword(newPassword),
  });

  // Invalidate all sessions and reset tokens
  await invalidateAllSessions(resetToken.userId);
  await db.delete(resetTokens).where(eq(resetTokens.userId, resetToken.userId));

  return true;
}
```

---

## Auth Hardening Checklist

For every auth implementation, verify:

- [ ] Rate limiting on login endpoints (max 5 attempts per 15 min)
- [ ] Account lockout after repeated failures
- [ ] Session regeneration on login (no session fixation)
- [ ] Short access token expiry (15 min)
- [ ] Refresh token rotation and revocation
- [ ] All sessions invalidated on password change
- [ ] Password reset tokens are single-use, time-limited
- [ ] Password reset doesn't reveal if email exists
- [ ] Argon2/bcrypt for password hashing (never MD5/SHA1)
- [ ] Password strength validation on creation
- [ ] HTTPS enforced for all auth endpoints
- [ ] SameSite=Strict on auth cookies
- [ ] HttpOnly on auth cookies (not accessible via JS)
