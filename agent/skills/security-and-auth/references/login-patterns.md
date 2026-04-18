# Login Patterns

Email/password, magic links, social OAuth, MFA flows.

---

## 1. Email/Password Login

### Core Pattern

```ts
// app/api/auth/login/route.ts
import { z } from "zod";
import { userService } from "@/lib/services/user-service";
import { createTokenPair } from "@/lib/auth/tokens";
import { checkLockout, recordFailedAttempt, resetAttempts } from "@/lib/auth/lockout";

const loginSchema = z.object({
  email: z.string().email(),
  password: z.string(),
});

export async function POST(request: NextRequest) {
  const body = await request.json();
  const validated = loginSchema.safeParse(body);
  if (!validated.success) {
    return validationError(validated.error.flatten().fieldErrors);
  }

  const { email, password } = validated.data;

  // Check account lockout
  const lockout = await checkLockout(email);
  if (lockout.locked) {
    return NextResponse.json(
      { error: "Account locked. Try again later.", code: "ACCOUNT_LOCKED", unlockAt: lockout.unlockAt },
      { status: 429 }
    );
  }

  try {
    const user = await userService.authenticate(email, password);
    await resetAttempts(email);

    const { accessToken, refreshToken } = await createTokenPair(user.id, user.role);

    return NextResponse.json(
      {
        data: {
          user: { id: user.id, name: user.name, email: user.email, role: user.role },
          accessToken,
          refreshToken,
        },
      },
      {
        status: 200,
        headers: {
          "Set-Cookie": [
            `refreshToken=${refreshToken}; HttpOnly; Secure; SameSite=Strict; Path=/; Max-Age=604800`,
          ].join(", "),
        },
      }
    );
  } catch {
    await recordFailedAttempt(email);
    return NextResponse.json(
      { error: "Invalid email or password", code: "INVALID_CREDENTIALS" },
      { status: 401 }
    );
  }
}
```

### Login Form Component

```tsx
// components/auth/login-form.tsx
"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export function LoginForm() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setIsLoading(true);

    try {
      const res = await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      const data = await res.json();

      if (!res.ok) {
        setError(data.error);
        return;
      }

      // Store access token
      localStorage.setItem("accessToken", data.data.accessToken);
      router.push("/dashboard");
    } catch {
      setError("Network error. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 max-w-sm mx-auto">
      <h2 className="text-xl font-semibold">Sign In</h2>

      {error && (
        <div className="rounded-md border border-destructive/50 bg-destructive/10 p-3 text-sm text-destructive" role="alert">
          {error}
        </div>
      )}

      <div>
        <label htmlFor="email" className="block text-sm font-medium mb-1">Email</label>
        <input
          id="email"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full rounded-md border px-3 py-2 text-sm"
          required
          autoComplete="email"
        />
      </div>

      <div>
        <label htmlFor="password" className="block text-sm font-medium mb-1">Password</label>
        <input
          id="password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full rounded-md border px-3 py-2 text-sm"
          required
          autoComplete="current-password"
        />
      </div>

      <button
        type="submit"
        disabled={isLoading}
        className="w-full rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground disabled:opacity-50"
      >
        {isLoading ? "Signing in..." : "Sign In"}
      </button>

      <div className="text-center text-sm">
        <a href="/forgot-password" className="text-primary hover:underline">
          Forgot your password?
        </a>
      </div>
    </form>
  );
}
```

---

## 2. Magic Link Login

**When:** Passwordless login — simpler UX, no password to forget.

### Core Pattern

```ts
// app/api/auth/magic-link/route.ts
import { randomBytes } from "crypto";
import { db } from "@/lib/db";
import { magicLinks, users } from "@/lib/db/schema";
import { eq } from "drizzle-orm";
import { rateLimit } from "@/lib/rate-limiter";

const MAGIC_LINK_EXPIRY_MS = 15 * 60 * 1000; // 15 minutes

export async function POST(request: NextRequest) {
  const { email } = await request.json();
  if (!email) return badRequest("Email is required");

  // Rate limit magic link requests
  const ip = request.ip || "unknown";
  const limit = rateLimit(`magic-link:${ip}`, { windowMs: 60 * 60 * 1000, maxRequests: 3 });
  if (!limit.allowed) return rateLimited(limit.resetAt);

  const user = await userRepository.findByEmail(email);
  if (!user) {
    // Don't reveal if email exists
    return NextResponse.json({ message: "If an account exists, you'll receive an email" });
  }

  // Generate secure token
  const token = randomBytes(32).toString("hex");
  const expiresAt = new Date(Date.now() + MAGIC_LINK_EXPIRY_MS);

  // Store token hash
  const tokenHash = require("crypto").createHash("sha256").update(token).digest("hex");
  await db.insert(magicLinks).values({
    userId: user.id,
    tokenHash,
    expiresAt,
    used: false,
  });

  // Send magic link
  const loginUrl = `${env.APP_URL}/auth/magic-link?token=${token}`;
  await emailService.sendTemplate(user.email, "magic-link", { loginUrl });

  return NextResponse.json({ message: "If an account exists, you'll receive an email" });
}

// Verify magic link
// app/api/auth/magic-link/verify/route.ts
export async function POST(request: NextRequest) {
  const { token } = await request.json();
  const tokenHash = require("crypto").createHash("sha256").update(token).digest("hex");

  const [magicLink] = await db
    .select()
    .from(magicLinks)
    .where(and(
      eq(magicLinks.tokenHash, tokenHash),
      eq(magicLinks.used, false),
      gt(magicLinks.expiresAt, new Date()),
    ))
    .limit(1);

  if (!magicLink) {
    return badRequest("Invalid or expired login link");
  }

  // Mark as used (single-use)
  await db.update(magicLinks).set({ used: true }).where(eq(magicLinks.id, magicLink.id));

  // Create session
  const user = await userRepository.findById(magicLink.userId);
  const { accessToken, refreshToken } = await createTokenPair(user!.id, user!.role);

  return NextResponse.json({ data: { accessToken, refreshToken } });
}
```

---

## 3. Social OAuth

### Google OAuth Flow

```ts
// app/api/auth/google/route.ts
import { google } from "googleapis";

const oauth2Client = new google.auth.OAuth2(
  process.env.GOOGLE_CLIENT_ID,
  process.env.GOOGLE_CLIENT_SECRET,
  `${env.APP_URL}/api/auth/google/callback`
);

// Step 1: Redirect to Google
export async function GET() {
  const url = oauth2Client.generateAuthUrl({
    access_type: "offline",
    scope: ["email", "profile"],
    prompt: "consent",
  });

  return NextResponse.redirect(url);
}

// Step 2: Handle callback
// app/api/auth/google/callback/route.ts
export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const code = searchParams.get("code");

  if (!code) return badRequest("No authorization code");

  // Exchange code for tokens
  const { tokens } = await oauth2Client.getToken(code);
  oauth2Client.setCredentials(tokens);

  // Get user info from Google
  const oauth2 = google.oauth2({ version: "v2", auth: oauth2Client });
  const { data: googleUser } = await oauth2.userinfo.get();

  // Find or create user
  let user = await userRepository.findByEmail(googleUser.email!);
  if (!user) {
    user = await userRepository.create({
      name: googleUser.name!,
      email: googleUser.email!,
      passwordHash: "", // No password for OAuth users
      role: "user",
    });
  }

  // Create session
  const { accessToken, refreshToken } = await createTokenPair(user.id, user.role);

  return NextResponse.redirect(`${env.APP_URL}/dashboard?token=${accessToken}`);
}
```

### OAuth Button Component

```tsx
// components/auth/oauth-buttons.tsx
function GoogleLoginButton() {
  return (
    <a
      href="/api/auth/google"
      className="flex items-center justify-center gap-2 w-full rounded-md border px-4 py-2 text-sm hover:bg-muted"
    >
      <GoogleIcon />
      Continue with Google
    </a>
  );
}
```

---

## 4. Multi-Factor Authentication (MFA)

### TOTP Setup

```ts
// lib/auth/mfa.ts
import { authenticator } from "otplib";
import { toDataURL } from "qrcode";

export async function generateMFASecret(userId: string): Promise<{ secret: string; qrCode: string }> {
  const secret = authenticator.generateSecret();
  const user = await userRepository.findById(userId);

  const otpauth = authenticator.keyuri(user!.email, "MyApp", secret);
  const qrCode = await toDataURL(otpauth);

  // Store secret (not yet enabled)
  await db.update(users).set({ mfaSecret: secret, mfaEnabled: false }).where(eq(users.id, userId));

  return { secret, qrCode };
}

export async function verifyMFAToken(userId: string, token: string): Promise<boolean> {
  const user = await userRepository.findById(userId);
  if (!user?.mfaSecret) return false;

  return authenticator.verify({ token, secret: user.mfaSecret });
}

export async function enableMFA(userId: string, token: string): Promise<boolean> {
  const isValid = await verifyMFAToken(userId, token);
  if (!isValid) return false;

  await db.update(users).set({ mfaEnabled: true }).where(eq(users.id, userId));
  return true;
}
```

### MFA Login Flow

```ts
// app/api/auth/login/route.ts (updated)
export async function POST(request: NextRequest) {
  // ... existing login logic ...

  const user = await userService.authenticate(email, password);

  // Check if MFA is enabled
  if (user.mfaEnabled) {
    return NextResponse.json({
      data: { requiresMFA: true, userId: user.id },
    });
  }

  // No MFA — return tokens
  const { accessToken, refreshToken } = await createTokenPair(user.id, user.role);
  return NextResponse.json({ data: { accessToken, refreshToken } });
}

// MFA verification endpoint
// app/api/auth/mfa/verify/route.ts
export async function POST(request: NextRequest) {
  const { userId, token } = await request.json();
  const isValid = await verifyMFAToken(userId, token);

  if (!isValid) {
    return badRequest("Invalid verification code");
  }

  const user = await userRepository.findById(userId);
  const { accessToken, refreshToken } = await createTokenPair(user!.id, user!.role);

  return NextResponse.json({ data: { accessToken, refreshToken } });
}
```

---

## Login Selection Guide

| Method | Security | UX | Best For |
|---|---|---|---|
| Email/Password | Medium | Medium | General purpose |
| Email/Password + MFA | High | Medium-High | Sensitive apps |
| Magic Link | High | High | Low-friction apps |
| Social OAuth | High | Very High | Consumer apps |
| Passkeys | Very High | High | Modern apps |

---

## Login Anti-Patterns

### ❌ Verbose Error Messages
```ts
// BAD: Reveals if email exists
if (!user) return badRequest("No account found with this email");
if (!isValid) return badRequest("Incorrect password");

// GOOD: Generic message
return badRequest("Invalid email or password");
```

### ❌ No Rate Limiting
```ts
// BAD: Unlimited login attempts
export async function POST(request: NextRequest) {
  // ... login logic with no rate limit
}

// GOOD: Rate limited
const limit = rateLimit(`login:${ip}`, { windowMs: 900000, maxRequests: 5 });
if (!limit.allowed) return rateLimited(limit.resetAt);
```

### ❌ Storing Passwords in Plaintext
```ts
// BAD
const user = await db.insert(users).values({ password: input.password });

// GOOD
const user = await db.insert(users).values({ passwordHash: await hashPassword(input.password) });
```
