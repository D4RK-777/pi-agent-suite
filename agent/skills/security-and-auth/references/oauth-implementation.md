# OAuth Implementation

OAuth 2.0 flows, PKCE, callback handling, token exchange.

---

## 1. OAuth 2.0 Authorization Code Flow

### When to Use
- Server-side apps (can keep client secret secure)
- Web applications with backend
- When you need long-lived access (refresh tokens)

### Flow Diagram

```
1. User clicks "Login with Google"
   → Browser redirects to Google's authorization endpoint

2. Google shows consent screen
   → User approves or denies

3. Google redirects back to your callback
   → URL contains authorization code

4. Your server exchanges code for tokens
   → POST to Google's token endpoint with code + client secret

5. Your server creates session
   → Sets cookies, redirects to dashboard
```

### Implementation

```ts
// lib/oauth/google.ts
import { google } from "googleapis";

export const googleOAuth = new google.auth.OAuth2(
  process.env.GOOGLE_CLIENT_ID,
  process.env.GOOGLE_CLIENT_SECRET,
  `${process.env.APP_URL}/api/auth/google/callback`
);

// Step 1: Generate authorization URL
export function getGoogleAuthUrl(state: string): string {
  return googleOAuth.generateAuthUrl({
    access_type: "offline", // Get refresh token
    scope: ["email", "profile"],
    state, // CSRF protection
    prompt: "consent", // Always show consent
  });
}

// Step 2: Exchange code for tokens
export async function exchangeCodeForTokens(code: string) {
  const { tokens } = await googleOAuth.getToken(code);
  return tokens;
}

// Step 3: Get user info
export async function getGoogleUserInfo(accessToken: string) {
  const oauth2 = google.oauth2({ version: "v2", auth: new google.auth.OAuth2() });
  oauth2.auth.setCredentials({ access_token: accessToken });
  const { data } = await oauth2.userinfo.get();
  return data;
}
```

### Callback Handler

```ts
// app/api/auth/google/callback/route.ts
import { NextRequest, NextResponse } from "next/server";
import { googleOAuth, getGoogleUserInfo } from "@/lib/oauth/google";
import { createTokenPair } from "@/lib/auth/tokens";
import { userRepository } from "@/lib/repositories/users";

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const code = searchParams.get("code");
  const state = searchParams.get("state");
  const error = searchParams.get("error");

  // Handle errors
  if (error) {
    return NextResponse.redirect(`${env.APP_URL}/login?error=oauth_denied`);
  }

  if (!code) {
    return NextResponse.redirect(`${env.APP_URL}/login?error=oauth_no_code`);
  }

  // Verify state (CSRF protection)
  const storedState = request.cookies.get("oauth_state")?.value;
  if (state !== storedState) {
    return NextResponse.redirect(`${env.APP_URL}/login?error=oauth_invalid_state`);
  }

  try {
    // Exchange code for tokens
    const { tokens } = await googleOAuth.getToken(code);
    if (!tokens.access_token) throw new Error("No access token");

    // Get user info from Google
    const googleUser = await getGoogleUserInfo(tokens.access_token);
    if (!googleUser?.email) throw new Error("No email from Google");

    // Find or create user
    let user = await userRepository.findByEmail(googleUser.email);
    if (!user) {
      user = await userRepository.create({
        name: googleUser.name || "",
        email: googleUser.email,
        passwordHash: "", // No password for OAuth
        role: "user",
      });
    }

    // Create session
    const { accessToken, refreshToken } = await createTokenPair(user.id, user.role);

    // Redirect to dashboard with token
    const redirectUrl = new URL("/dashboard", env.APP_URL);
    redirectUrl.searchParams.set("token", accessToken);

    const response = NextResponse.redirect(redirectUrl);
    response.cookies.set("refreshToken", refreshToken, {
      httpOnly: true,
      secure: true,
      sameSite: "strict",
      path: "/",
      maxAge: 7 * 24 * 60 * 60, // 7 days
    });

    return response;
  } catch (error) {
    console.error("OAuth error:", error);
    return NextResponse.redirect(`${env.APP_URL}/login?error=oauth_failed`);
  }
}
```

---

## 2. PKCE (Proof Key for Code Exchange)

### When to Use PKCE
- Single-page apps (no server-side secret)
- Mobile apps
- Any public client (can't keep secret secure)
- **Recommended for ALL OAuth flows now**

### PKCE Flow

```ts
// lib/oauth/pkce.ts
import { randomBytes, createHash } from "crypto";

// Generate code verifier (random string)
export function generateCodeVerifier(): string {
  return randomBytes(32).toString("base64url");
}

// Generate code challenge from verifier
export function generateCodeChallenge(verifier: string): string {
  return createHash("sha256").update(verifier).digest("base64url");
}

// Usage in login flow
export function startPKCEFlow(): { authUrl: string; verifier: string } {
  const verifier = generateCodeVerifier();
  const challenge = generateCodeChallenge(verifier);
  const state = randomBytes(16).toString("hex");

  const authUrl = `https://accounts.google.com/o/oauth2/v2/auth?` +
    `client_id=${process.env.GOOGLE_CLIENT_ID}` +
    `&redirect_uri=${encodeURIComponent(`${env.APP_URL}/api/auth/google/callback`)}` +
    `&response_type=code` +
    `&scope=email%20profile` +
    `&state=${state}` +
    `&code_challenge=${challenge}` +
    `&code_challenge_method=S256`;

  return { authUrl, verifier };
}

// Exchange code with verifier
export async function exchangePKCECode(code: string, verifier: string) {
  const response = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      code,
      client_id: process.env.GOOGLE_CLIENT_ID!,
      client_secret: process.env.GOOGLE_CLIENT_SECRET!,
      redirect_uri: `${env.APP_URL}/api/auth/google/callback`,
      grant_type: "authorization_code",
      code_verifier: verifier,
    }),
  });

  if (!response.ok) throw new Error("Token exchange failed");
  return response.json();
}
```

---

## 3. Token Exchange

### Exchanging OAuth Tokens for App Sessions

```ts
// lib/oauth/token-exchange.ts
import { createTokenPair } from "@/lib/auth/tokens";
import { userRepository } from "@/lib/repositories/users";

interface OAuthUserInfo {
  email: string;
  name: string;
  avatar?: string;
  provider: string;
  providerId: string;
}

export async function exchangeOAuthForSession(userInfo: OAuthUserInfo) {
  // Find or create user
  let user = await userRepository.findByEmail(userInfo.email);

  if (!user) {
    user = await userRepository.create({
      name: userInfo.name,
      email: userInfo.email,
      passwordHash: "",
      role: "user",
    });

    // Link OAuth provider
    await db.insert(oauthAccounts).values({
      userId: user.id,
      provider: userInfo.provider,
      providerId: userInfo.providerId,
      accessToken: "", // Store if needed for API access
    });
  } else {
    // Check if provider is already linked
    const linked = await db
      .select()
      .from(oauthAccounts)
      .where(and(
        eq(oauthAccounts.userId, user.id),
        eq(oauthAccounts.provider, userInfo.provider),
      ))
      .limit(1);

    if (!linked.length) {
      // Link new provider
      await db.insert(oauthAccounts).values({
        userId: user.id,
        provider: userInfo.provider,
        providerId: userInfo.providerId,
      });
    }
  }

  // Create app session
  return createTokenPair(user.id, user.role);
}
```

---

## 4. Multi-Provider OAuth

### Supporting Google, GitHub, Apple

```ts
// lib/oauth/providers.ts
export interface OAuthProvider {
  name: string;
  getAuthUrl(state: string, codeChallenge?: string): string;
  exchangeCode(code: string, verifier?: string): Promise<OAuthTokens>;
  getUserInfo(accessToken: string): Promise<OAuthUserInfo>;
}

// Google provider
export const googleProvider: OAuthProvider = {
  name: "google",
  getAuthUrl(state: string) {
    return googleOAuth.generateAuthUrl({
      access_type: "offline",
      scope: ["email", "profile"],
      state,
    });
  },
  async exchangeCode(code: string) {
    const { tokens } = await googleOAuth.getToken(code);
    return {
      accessToken: tokens.access_token!,
      refreshToken: tokens.refresh_token || undefined,
      expiresIn: tokens.expiry_date ? Math.floor((tokens.expiry_date - Date.now()) / 1000) : 3600,
    };
  },
  async getUserInfo(accessToken: string) {
    const oauth2 = google.oauth2({ version: "v2", auth: new google.auth.OAuth2() });
    oauth2.auth.setCredentials({ access_token: accessToken });
    const { data } = await oauth2.userinfo.get();
    return {
      email: data.email!,
      name: data.name || "",
      avatar: data.picture,
      provider: "google",
      providerId: data.id!,
    };
  },
};

// GitHub provider
export const githubProvider: OAuthProvider = {
  name: "github",
  getAuthUrl(state: string) {
    return `https://github.com/login/oauth/authorize?` +
      `client_id=${process.env.GITHUB_CLIENT_ID}` +
      `&redirect_uri=${encodeURIComponent(`${env.APP_URL}/api/auth/github/callback`)}` +
      `&state=${state}` +
      `&scope=user:email`;
  },
  async exchangeCode(code: string) {
    const response = await fetch("https://github.com/login/oauth/access_token", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({
        client_id: process.env.GITHUB_CLIENT_ID,
        client_secret: process.env.GITHUB_CLIENT_SECRET,
        code,
      }),
    });
    const data = await response.json();
    return {
      accessToken: data.access_token,
      expiresIn: data.expires_in,
    };
  },
  async getUserInfo(accessToken: string) {
    const [userRes, emailRes] = await Promise.all([
      fetch("https://api.github.com/user", {
        headers: { Authorization: `Bearer ${accessToken}`, Accept: "application/vnd.github.v3+json" },
      }),
      fetch("https://api.github.com/user/emails", {
        headers: { Authorization: `Bearer ${accessToken}`, Accept: "application/vnd.github.v3+json" },
      }),
    ]);

    const user = await userRes.json();
    const emails = await emailRes.json();
    const primaryEmail = emails.find((e: any) => e.primary)?.email;

    return {
      email: primaryEmail,
      name: user.name || user.login,
      avatar: user.avatar_url,
      provider: "github",
      providerId: String(user.id),
    };
  },
};

// Provider registry
export const providers: Record<string, OAuthProvider> = {
  google: googleProvider,
  github: githubProvider,
};
```

---

## OAuth Security Checklist

- [ ] State parameter used (CSRF protection)
- [ ] PKCE enabled (even for confidential clients)
- [ ] Redirect URI validated against allowlist
- [ ] Access tokens stored securely (not in localStorage)
- [ ] Refresh tokens rotated on each use
- [ ] OAuth tokens exchanged for app sessions (not used directly)
- [ ] User email verified before creating account
- [ ] Account linking verified (prevent account takeover)
- [ ] Error messages don't leak OAuth internals
- [ ] Scopes are minimal (only request what you need)

---

## OAuth Anti-Patterns

### ❌ Storing OAuth Tokens in LocalStorage
```ts
// BAD: Accessible to XSS attacks
localStorage.setItem("googleToken", tokens.access_token);

// GOOD: Exchange for app session immediately
const { accessToken, refreshToken } = await exchangeOAuthForSession(userInfo);
// Set HttpOnly cookie
response.cookies.set("refreshToken", refreshToken, { httpOnly: true });
```

### ❌ No State Parameter
```ts
// BAD: Vulnerable to CSRF attacks
const authUrl = googleOAuth.generateAuthUrl({ scope: ["email"] });

// GOOD: State parameter for CSRF protection
const state = crypto.randomUUID();
response.cookies.set("oauth_state", state, { httpOnly: true, maxAge: 300 });
const authUrl = googleOAuth.generateAuthUrl({ scope: ["email"], state });
```

### ❌ Not Verifying Redirect URI
```ts
// BAD: Attacker can redirect to malicious site
&redirect_uri=https://evil.com/steal-token

// GOOD: Validate against allowlist
const allowedRedirects = ["http://localhost:3000/callback", "https://myapp.com/callback"];
if (!allowedRedirects.includes(redirectUri)) {
  throw new Error("Invalid redirect URI");
}
```
