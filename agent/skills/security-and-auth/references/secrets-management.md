# Secrets Management

Environment variables, secret rotation, key management, .gitignore patterns.

---

## 1. Environment Variable Patterns

### Core Setup

```ts
// lib/env.ts — Single source of truth for all env vars
import { z } from "zod";

const envSchema = z.object({
  NODE_ENV: z.enum(["development", "test", "production"]).default("development"),
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32, "JWT_SECRET must be at least 32 characters"),
  RESEND_API_KEY: z.string().optional(),
  STRIPE_SECRET_KEY: z.string().optional(),
  STRIPE_WEBHOOK_SECRET: z.string().optional(),
  UPSTASH_REDIS_REST_URL: z.string().url().optional(),
  UPSTASH_REDIS_REST_TOKEN: z.string().optional(),
  EMAIL_FROM: z.string().email().default("noreply@example.com"),
  ALLOWED_ORIGINS: z.string().default("http://localhost:3000"),
});

// Validate at startup
export const env = envSchema.parse(process.env);

// Usage
import { env } from "@/lib/env";
const db = new Pool({ connectionString: env.DATABASE_URL });
```

### Type-Safe Access

```ts
// BAD: process.env.DATABASE_URL — could be undefined
const db = new Pool({ connectionString: process.env.DATABASE_URL });

// GOOD: Validated at startup, guaranteed to exist
import { env } from "@/lib/env";
const db = new Pool({ connectionString: env.DATABASE_URL });
```

---

## 2. .gitignore Patterns

```gitignore
# Secrets
.env
.env.local
.env.*.local
!.env.example

# Keys
*.pem
*.key
*.p12
*.jks

# Credentials
.aws/credentials
.gcloud/credentials.json
.kube/config

# IDE secrets
.vscode/settings.json
.idea/workspace.xml

# OS files
.DS_Store
Thumbs.db

# Build output
.next/
out/
dist/

# Logs
*.log
npm-debug.log*

# Database
*.db
*.sqlite
*.sqlite3
```

### .env.example Template

```env
# .env.example — Safe to commit, no real values
NODE_ENV=development
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
JWT_SECRET=your-secret-key-at-least-32-characters-long
RESEND_API_KEY=re_xxxxxxxxxxxxx
STRIPE_SECRET_KEY=sk_test_xxxxxxxxxxxxx
STRIPE_WEBHOOK_SECRET=whsec_xxxxxxxxxxxxx
EMAIL_FROM=noreply@example.com
ALLOWED_ORIGINS=http://localhost:3000
```

---

## 3. Secret Rotation

### Database Credentials

```ts
// lib/db/rotation.ts
import { Pool } from "pg";

let pool: Pool | null = null;

export function getDbPool(): Pool {
  if (!pool) {
    pool = new Pool({
      connectionString: env.DATABASE_URL,
      // Auto-reconnect on credential expiry
      max: 20,
      idleTimeoutMillis: 30000,
      connectionTimeoutMillis: 2000,
    });

    // Handle credential expiry
    pool.on("error", (err) => {
      if (err.message.includes("password authentication failed")) {
        console.error("Database credentials expired — restarting pool");
        pool?.end();
        pool = null;
      }
    });
  }

  return pool;
}
```

### JWT Secret Rotation

```ts
// lib/auth/jwt.ts
import { SignJWT, jwtVerify } from "jose";

// Support multiple secrets during rotation
const secrets = [
  env.JWT_SECRET,           // Current
  env.JWT_SECRET_PREVIOUS, // Previous (still valid for verification)
].filter(Boolean);

export async function createToken(payload: Record<string, unknown>): Promise<string> {
  const secret = new TextEncoder().encode(secrets[0]);
  return new SignJWT(payload)
    .setProtectedHeader({ alg: "HS256" })
    .setExpirationTime("7d")
    .sign(secret);
}

export async function verifyToken(token: string): Promise<Record<string, unknown>> {
  // Try each secret until one works
  for (const secret of secrets) {
    try {
      const { payload } = await jwtVerify(
        token,
        new TextEncoder().encode(secret)
      );
      return payload;
    } catch {
      // Try next secret
    }
  }
  throw new Error("Invalid token");
}
```

### API Key Rotation Pattern

```ts
// lib/services/email-service.ts
import { Resend } from "resend";

// Support multiple API keys for rotation
const apiKeys = [
  env.RESEND_API_KEY,
  env.RESEND_API_KEY_PREVIOUS,
].filter(Boolean);

let currentKeyIndex = 0;

export function getResendClient(): Resend {
  return new Resend(apiKeys[currentKeyIndex]);
}

// Rotate to next key
export function rotateApiKey(): void {
  currentKeyIndex = (currentKeyIndex + 1) % apiKeys.length;
  console.log(`Rotated to API key index ${currentKeyIndex}`);
}
```

---

## 4. Key Management

### Encryption at Rest

```ts
// lib/crypto.ts
import { createCipheriv, createDecipheriv, randomBytes } from "crypto";

const ALGORITHM = "aes-256-gcm";
const KEY = Buffer.from(env.ENCRYPTION_KEY, "hex"); // 32 bytes
const IV_LENGTH = 16;
const AUTH_TAG_LENGTH = 16;

export function encrypt(plaintext: string): string {
  const iv = randomBytes(IV_LENGTH);
  const cipher = createCipheriv(ALGORITHM, KEY, iv);

  let encrypted = cipher.update(plaintext, "utf8", "hex");
  encrypted += cipher.final("hex");
  const authTag = cipher.getAuthTag().toString("hex");

  // IV + auth tag + ciphertext
  return `${iv.toString("hex")}:${authTag}:${encrypted}`;
}

export function decrypt(ciphertext: string): string {
  const [ivHex, authTagHex, encrypted] = ciphertext.split(":");
  const iv = Buffer.from(ivHex, "hex");
  const authTag = Buffer.from(authTagHex, "hex");

  const decipher = createDecipheriv(ALGORITHM, KEY, iv);
  decipher.setAuthTag(authTag);

  let decrypted = decipher.update(encrypted, "hex", "utf8");
  decrypted += decipher.final("utf8");

  return decrypted;
}
```

### Usage for Sensitive Data

```ts
// lib/repositories/users.ts
import { encrypt, decrypt } from "@/lib/crypto";

export async function createApiKey(userId: string): Promise<string> {
  const rawKey = randomBytes(32).toString("hex");
  const encrypted = encrypt(rawKey);

  await db.insert(apiKeys).values({
    userId,
    encryptedKey: encrypted,
    createdAt: new Date(),
  });

  return rawKey; // Return raw key to user once — never store it plaintext
}

export async function verifyApiKey(key: string): Promise<boolean> {
  // Hash the input and compare with stored hash
  const hashedKey = hashApiKey(key);
  const [apiKey] = await db
    .select()
    .from(apiKeys)
    .where(eq(apiKeys.hashedKey, hashedKey))
    .limit(1);
  return !!apiKey;
}
```

---

## 5. Git Secret Scanning

### Pre-Commit Hook

```json
// package.json
{
  "scripts": {
    "prepare": "husky install",
    "lint:secrets": "detect-secrets scan .env"
  }
}
```

### Common Secret Patterns to Block

```regex
# .gitleaks.toml
[[rules]]
id = "generic-api-key"
regex = '''(?i)(?:api[_-]?key|secret|token|password|auth)["\s:=]+["']?[A-Za-z0-9_\-]{20,}["']?'''

[[rules]]
id = "aws-access-key"
regex = '''AKIA[0-9A-Z]{16}'''

[[rules]]
id = "private-key"
regex = '''-----BEGIN (?:RSA |EC |DSA )?PRIVATE KEY-----'''

[[rules]]
id = "database-url"
regex = '''(?:postgres|mysql|mongodb)://[^\s]+:[^\s]+@'''
```

---

## Secrets Anti-Patterns

### ❌ Hardcoded Secrets
```ts
// BAD: Secret in source code
const API_KEY = "sk-1234567890abcdef";
const DB_PASSWORD = "supersecret";

// GOOD: Environment variables
const API_KEY = env.STRIPE_SECRET_KEY;
const DB_PASSWORD = env.DATABASE_URL; // Parsed from connection string
```

### ❌ Committing .env Files
```bash
# BAD: .env in git
git add .env
git commit -m "Add config"

# GOOD: Only .env.example
git add .env.example
git commit -m "Add env template"
```

### ❌ Logging Secrets
```ts
// BAD: Secrets in logs
console.log("Connecting to DB:", process.env.DATABASE_URL);
console.log("API response:", { headers: { Authorization: token } });

// GOOD: Redacted logs
console.log("Connecting to DB:", env.DATABASE_URL?.replace(/:[^@]+@/, ":***@"));
console.log("API response:", { status: response.status });
```

### ❌ Secrets in Client Code
```tsx
// BAD: Secret exposed to browser
const stripe = Stripe("sk_live_xxxxx"); // Server-side key!

// GOOD: Public key only
const stripe = Stripe("pk_live_xxxxx"); // Client-safe public key
```

---

## Secrets Selection Guide

| Secret Type | Storage | Rotation |
|---|---|---|
| Database URL | Environment variable | Via hosting platform |
| JWT Secret | Environment variable | Dual-secret rotation |
| API Keys | Environment variable | Key versioning |
| Encryption Keys | Environment variable (hex) | Re-encrypt data |
| OAuth Secrets | Environment variable | Via provider |
| TLS Certificates | Hosting platform | Auto-renew (Let's Encrypt) |
