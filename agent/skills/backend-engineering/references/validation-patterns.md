# Validation Patterns

Zod schemas, input sanitization, nested validation, custom validators.

---

## 1. Zod Schema Patterns

### Basic Resource Schema

```ts
// lib/schemas/user.ts
import { z } from "zod";

export const createUserSchema = z.object({
  name: z.string()
    .min(2, "Name must be at least 2 characters")
    .max(100, "Name must be less than 100 characters")
    .trim(),
  email: z.string()
    .email("Please enter a valid email address")
    .toLowerCase()
    .max(255),
  password: z.string()
    .min(8, "Password must be at least 8 characters")
    .max(128)
    .regex(/[A-Z]/, "Password must contain at least one uppercase letter")
    .regex(/[a-z]/, "Password must contain at least one lowercase letter")
    .regex(/[0-9]/, "Password must contain at least one number"),
  role: z.enum(["user", "admin", "moderator"]).default("user"),
});

export const updateUserSchema = createUserSchema.partial();

export const userResponseSchema = z.object({
  id: z.string().uuid(),
  name: z.string(),
  email: z.string().email(),
  role: z.enum(["user", "admin", "moderator"]),
  createdAt: z.string().datetime(),
  updatedAt: z.string().datetime(),
}).omit({ password: true }); // Never expose password

// Inferred types
export type CreateUserInput = z.infer<typeof createUserSchema>;
export type UpdateUserInput = z.infer<typeof updateUserSchema>;
export type UserResponse = z.infer<typeof userResponseSchema>;
```

### Nested Object Validation

```ts
// lib/schemas/order.ts
import { z } from "zod";

const addressSchema = z.object({
  street: z.string().min(1, "Street is required").max(200),
  city: z.string().min(1, "City is required").max(100),
  state: z.string().length(2, "State must be 2 characters"),
  zip: z.string().regex(/^\d{5}(-\d{4})?$/, "Invalid ZIP code"),
  country: z.string().length(2, "Country must be 2-letter ISO code"),
});

const orderItemSchema = z.object({
  productId: z.string().uuid("Invalid product ID"),
  quantity: z.number()
    .int("Quantity must be a whole number")
    .min(1, "Quantity must be at least 1")
    .max(999, "Quantity cannot exceed 999"),
  customizations: z.record(z.string(), z.string()).optional(),
});

export const createOrderSchema = z.object({
  shippingAddress: addressSchema,
  billingAddress: addressSchema.optional(),
  items: z.array(orderItemSchema)
    .min(1, "Order must have at least one item")
    .max(50, "Order cannot exceed 50 items"),
  couponCode: z.string().max(20).optional(),
  notes: z.string().max(500).optional(),
}).refine(
  (data) => {
    // Cross-field validation: if billing address differs
    if (data.billingAddress && !data.shippingAddress) {
      return false;
    }
    return true;
  },
  {
    message: "Shipping address is required when billing address is provided",
    path: ["shippingAddress"],
  }
);
```

### Array Validation with Uniqueness

```ts
// lib/schemas/team.ts
import { z } from "zod";

export const inviteMembersSchema = z.object({
  invitations: z.array(
    z.object({
      email: z.string().email(),
      role: z.enum(["member", "admin", "viewer"]),
    })
  )
  .min(1, "Must invite at least one person")
  .max(50, "Cannot invite more than 50 people at once")
  .refine(
    (invites) => {
      const emails = invites.map(i => i.email.toLowerCase());
      return new Set(emails).size === emails.length;
    },
    { message: "Duplicate email addresses are not allowed" }
  ),
});
```

---

## 2. Input Sanitization

### HTML Sanitization

```ts
// lib/sanitization.ts
import sanitizeHtml from "sanitize-html";

export function sanitizeHtmlInput(input: string, allowedTags: string[] = []): string {
  return sanitizeHtml(input, {
    allowedTags: ["p", "br", "strong", "em", "u", "a", "ul", "ol", "li", ...allowedTags],
    allowedAttributes: {
      a: ["href", "title", "target"],
    },
    allowedSchemes: ["http", "https", "mailto"],
    disallowedTagsMode: "discard",
  });
}

// Usage in schema
const postSchema = z.object({
  title: z.string().max(200).trim(),
  content: z.string()
    .max(50000)
    .transform((val) => sanitizeHtmlInput(val)),
});
```

### SQL Injection Prevention (Already handled by ORM, but document it)

```ts
// lib/db/safe-queries.ts
import { db } from "@/lib/db";
import { users } from "@/lib/db/schema";
import { eq, like, sql } from "drizzle-orm";

// SAFE: Parameterized queries (ORM handles this)
const user = await db.select().from(users).where(eq(users.email, userInput));

// SAFE: LIKE with parameterized wildcards
const search = await db.select().from(users).where(like(users.name, `%${searchTerm}%`));

// DANGEROUS: Raw SQL with string interpolation — NEVER do this
// const user = await db.execute(sql`SELECT * FROM users WHERE email = '${userInput}'`);

// SAFE: Raw SQL with parameters
const user = await db.execute(sql`SELECT * FROM users WHERE email = ${userInput}`);
```

### Path Traversal Prevention

```ts
// lib/sanitization.ts
import path from "path";

export function sanitizeFilePath(userInput: string): string {
  // Resolve and ensure it stays within allowed directory
  const basePath = path.resolve(process.env.UPLOAD_DIR || "./uploads");
  const resolvedPath = path.resolve(basePath, userInput);

  if (!resolvedPath.startsWith(basePath)) {
    throw new Error("Invalid file path — directory traversal detected");
  }

  return resolvedPath;
}
```

---

## 3. Custom Validators

### Phone Number Validation

```ts
// lib/validators/phone.ts
import { z } from "zod";

const phoneRegex = /^\+?[1-9]\d{1,14}$/; // E.164 format

export const phoneSchema = z.string()
  .regex(phoneRegex, "Invalid phone number format. Use E.164 format: +1234567890")
  .transform((val) => val.replace(/\s/g, ""));
```

### URL Validation

```ts
// lib/validators/url.ts
import { z } from "zod";

export const urlSchema = z.string()
  .url("Please enter a valid URL")
  .refine(
    (url) => {
      try {
        const parsed = new URL(url);
        return ["http:", "https:"].includes(parsed.protocol);
      } catch {
        return false;
      }
    },
    { message: "Only HTTP and HTTPS URLs are allowed" }
  );
```

### File Validation

```ts
// lib/validators/file.ts
import { z } from "zod";

const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5MB
const ACCEPTED_IMAGE_TYPES = ["image/jpeg", "image/png", "image/webp", "image/gif"];

export const fileUploadSchema = z.object({
  file: z.instanceof(File)
    .refine((file) => file.size <= MAX_FILE_SIZE, "File size must be less than 5MB")
    .refine(
      (file) => ACCEPTED_IMAGE_TYPES.includes(file.type),
      "Only JPEG, PNG, WebP, and GIF images are allowed"
    ),
});
```

### Slug Validation

```ts
// lib/validators/slug.ts
import { z } from "zod";

export const slugSchema = z.string()
  .min(2, "Slug must be at least 2 characters")
  .max(100, "Slug must be less than 100 characters")
  .regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/, "Slug must be lowercase alphanumeric with hyphens")
  .transform((val) => val.toLowerCase());
```

---

## 4. Validation Error Handling

### Standardized Error Format

```ts
// lib/api/validation.ts
import { z } from "zod";
import { NextResponse } from "next/server";

export function validateRequest<T>(schema: z.ZodSchema<T>, body: unknown): { data: T } | { error: NextResponse } {
  const result = schema.safeParse(body);

  if (!result.success) {
    const fieldErrors = result.error.flatten().fieldErrors;
    return {
      error: NextResponse.json(
        {
          error: "Validation failed",
          code: "VALIDATION_ERROR",
          details: fieldErrors,
        },
        { status: 400 }
      ),
    };
  }

  return { data: result.data };
}

// Usage in route
export async function POST(request: NextRequest) {
  const body = await request.json();
  const validation = validateRequest(createUserSchema, body);

  if ("error" in validation) {
    return validation.error;
  }

  const { name, email, password } = validation.data;
  // ... proceed with valid data
}
```

### Nested Error Formatting

```ts
// lib/api/validation.ts
export function formatValidationErrors(error: z.ZodError): Record<string, string[]> {
  const formatted: Record<string, string[]> = {};

  for (const issue of error.errors) {
    const path = issue.path.join(".");
    if (!formatted[path]) formatted[path] = [];
    formatted[path].push(issue.message);
  }

  return formatted;
}

// Example output:
// {
//   "shippingAddress.city": ["City is required"],
//   "items[0].quantity": ["Quantity must be at least 1"],
//   "email": ["Please enter a valid email address"]
// }
```

---

## 5. Validation Selection Guide

| Scenario | Best Pattern |
|---|---|
| Simple form | Zod object schema |
| Nested data | Nested Zod objects + `.refine()` |
| Array with constraints | `z.array().min().max().refine()` |
| Cross-field validation | `.refine()` on parent object |
| File uploads | `z.instanceof(File)` + size/type refinements |
| HTML content | Zod + `sanitize-html` transform |
| Phone/email/URL | Custom Zod schemas with regex |
| API request body | `validateRequest()` wrapper |
| Database input | Zod schema → inferred type → DB insert |

---

## Validation Anti-Patterns

### ❌ Validating in Multiple Places
```ts
// BAD: Schema duplicated in route and service
const schema = z.object({ email: z.string().email() });
// ... in route
const schema = z.object({ email: z.string().email() });
// ... in service

// GOOD: Single source of truth
// lib/schemas/user.ts
export const createUserSchema = z.object({ email: z.string().email() });
// Import everywhere
```

### ❌ Trusting Client-Side Validation Only
```ts
// BAD: No server-side validation
// Relying on HTML5 required, pattern attributes

// GOOD: Always validate on server
const validated = createUserSchema.safeParse(await request.json());
if (!validated.success) return validationError(validated.error);
```

### ❌ Exposing Internal Data in Errors
```ts
// BAD: Leaks stack traces, DB errors
return NextResponse.json({ error: err.message, stack: err.stack });

// GOOD: User-friendly validation errors
return NextResponse.json({
  error: "Validation failed",
  details: validated.error.flatten().fieldErrors,
});
```

### ❌ Over-Validating
```ts
// BAD: Validating things the ORM already handles
const schema = z.object({
  id: z.string().uuid(), // Auto-generated, don't validate input
  createdAt: z.date(),   // Auto-generated
});

// GOOD: Only validate user-provided input
const schema = z.object({
  name: z.string().min(2),
  email: z.string().email(),
});
```
