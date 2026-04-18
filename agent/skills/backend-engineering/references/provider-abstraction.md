# Provider Abstraction

Service layer, dependency injection, interface patterns, mock providers.

---

## 1. Service Layer Pattern

**When:** Separating business logic from route handlers — testable, reusable, clean.

### Core Pattern

```ts
// lib/services/user-service.ts
import { userRepository } from "@/lib/repositories/users";
import { emailService } from "@/lib/services/email-service";
import { hashPassword, verifyPassword } from "@/lib/auth/password";
import { CreateUserInput, UpdateUserInput, User } from "@/lib/db/schema";
import { NotFoundError, ConflictError, BadRequestError } from "@/lib/api/errors";

export class UserService {
  // Create user with side effects
  async create(input: CreateUserInput): Promise<User> {
    // Check uniqueness
    const existing = await userRepository.findByEmail(input.email);
    if (existing) {
      throw new ConflictError("A user with this email already exists");
    }

    // Hash password
    const passwordHash = await hashPassword(input.password);

    // Create user
    const user = await userRepository.create({
      name: input.name,
      email: input.email,
      passwordHash,
      role: input.role,
    });

    // Send welcome email (non-blocking)
    emailService.sendWelcome(user.email, user.name).catch(console.error);

    return user;
  }

  // Authenticate user
  async authenticate(email: string, password: string): Promise<User> {
    const user = await userRepository.findByEmail(email);
    if (!user) {
      throw new BadRequestError("Invalid email or password");
    }

    const isValid = await verifyPassword(password, user.passwordHash);
    if (!isValid) {
      throw new BadRequestError("Invalid email or password");
    }

    return user;
  }

  // Update user
  async update(id: string, input: UpdateUserInput): Promise<User> {
    const user = await userRepository.findById(id);
    if (!user) {
      throw new NotFoundError("User");
    }

    // If email is changing, check uniqueness
    if (input.email && input.email !== user.email) {
      const existing = await userRepository.findByEmail(input.email);
      if (existing) {
        throw new ConflictError("A user with this email already exists");
      }
    }

    // If password is changing, hash it
    const updateData = { ...input };
    if (input.password) {
      updateData.passwordHash = await hashPassword(input.password);
      delete updateData.password;
    }

    const updated = await userRepository.update(id, updateData);
    if (!updated) {
      throw new NotFoundError("User");
    }

    return updated;
  }

  // Delete user
  async delete(id: string): Promise<void> {
    const deleted = await userRepository.delete(id);
    if (!deleted) {
      throw new NotFoundError("User");
    }
  }
}

// Singleton instance
export const userService = new UserService();
```

### Usage in Routes

```ts
// app/api/users/route.ts
import { userService } from "@/lib/services/user-service";
import { createUserSchema } from "@/lib/schemas/user";
import { validateRequest } from "@/lib/api/validation";

export async function POST(request: NextRequest) {
  const body = await request.json();
  const validation = validateRequest(createUserSchema, body);
  if ("error" in validation) return validation.error;

  try {
    const user = await userService.create(validation.data);
    return NextResponse.json({ data: user }, { status: 201 });
  } catch (error) {
    return handleApiError(error);
  }
}
```

---

## 2. Interface-Based Abstraction

**When:** Swappable implementations — email providers, payment gateways, storage backends.

### Email Service Interface

```ts
// lib/services/email-service.ts
export interface EmailProvider {
  send(to: string, subject: string, html: string): Promise<void>;
  sendTemplate(to: string, template: string, variables: Record<string, string>): Promise<void>;
}

// Resend implementation
import { Resend } from "resend";

export class ResendEmailProvider implements EmailProvider {
  private resend: Resend;

  constructor() {
    this.resend = new Resend(process.env.RESEND_API_KEY);
  }

  async send(to: string, subject: string, html: string): Promise<void> {
    await this.resend.emails.send({
      from: process.env.EMAIL_FROM || "noreply@example.com",
      to,
      subject,
      html,
    });
  }

  async sendTemplate(to: string, template: string, variables: Record<string, string>): Promise<void> {
    await this.resend.emails.send({
      from: process.env.EMAIL_FROM || "noreply@example.com",
      to,
      subject: template,
      html: this.renderTemplate(template, variables),
    });
  }

  private renderTemplate(template: string, variables: Record<string, string>): string {
    // Render HTML from template
    return `<h1>${template}</h1>`;
  }
}

// Mock implementation for testing
export class MockEmailProvider implements EmailProvider {
  public sentEmails: Array<{ to: string; subject: string; html: string }> = [];

  async send(to: string, subject: string, html: string): Promise<void> {
    this.sentEmails.push({ to, subject, html });
  }

  async sendTemplate(to: string, template: string, variables: Record<string, string>): Promise<void> {
    this.sentEmails.push({ to, subject: template, html: JSON.stringify(variables) });
  }
}

// Factory — swap implementations via env var
export function createEmailProvider(): EmailProvider {
  if (process.env.NODE_ENV === "test") {
    return new MockEmailProvider();
  }
  return new ResendEmailProvider();
}

export const emailService = createEmailProvider();
```

### Payment Gateway Abstraction

```ts
// lib/services/payment-service.ts
export interface PaymentProvider {
  createCustomer(email: string, name: string): Promise<string>;
  createSubscription(customerId: string, priceId: string): Promise<{ subscriptionId: string; status: string }>;
  cancelSubscription(subscriptionId: string): Promise<void>;
  getInvoice(invoiceId: string): Promise<{ url: string; amount: number; status: string }>;
  handleWebhook(payload: string, signature: string): Promise<void>;
}

// Stripe implementation
import Stripe from "stripe";

export class StripePaymentProvider implements PaymentProvider {
  private stripe: Stripe;

  constructor() {
    this.stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);
  }

  async createCustomer(email: string, name: string): Promise<string> {
    const customer = await this.stripe.customers.create({ email, name });
    return customer.id;
  }

  async createSubscription(customerId: string, priceId: string) {
    const subscription = await this.stripe.subscriptions.create({
      customer: customerId,
      items: [{ price: priceId }],
      payment_behavior: "default_incomplete",
      expand: ["latest_invoice.payment_intent"],
    });

    return {
      subscriptionId: subscription.id,
      status: subscription.status,
    };
  }

  async cancelSubscription(subscriptionId: string): Promise<void> {
    await this.stripe.subscriptions.cancel(subscriptionId);
  }

  async getInvoice(invoiceId: string) {
    const invoice = await this.stripe.invoices.retrieve(invoiceId);
    return {
      url: invoice.hosted_invoice_url!,
      amount: invoice.amount_due,
      status: invoice.status!,
    };
  }

  async handleWebhook(payload: string, signature: string): Promise<void> {
    const event = this.stripe.webhooks.constructEvent(
      payload,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET!
    );

    // Handle event types
    switch (event.type) {
      case "invoice.payment_succeeded":
        // Update subscription status
        break;
      case "invoice.payment_failed":
        // Notify user
        break;
      case "customer.subscription.deleted":
        // Revoke access
        break;
    }
  }
}

export const paymentService = new StripePaymentProvider();
```

---

## 3. Dependency Injection

**When:** Testable services — inject mocks instead of real providers.

### DI Container Pattern

```ts
// lib/di/container.ts
import { EmailProvider, ResendEmailProvider, MockEmailProvider } from "@/lib/services/email-service";
import { PaymentProvider, StripePaymentProvider } from "@/lib/services/payment-service";
import { UserRepository } from "@/lib/repositories/users";
import { UserService } from "@/lib/services/user-service";

export interface Container {
  userRepository: UserRepository;
  emailProvider: EmailProvider;
  paymentProvider: PaymentProvider;
  userService: UserService;
}

// Production container
export function createProductionContainer(): Container {
  const userRepository = new UserRepository();
  const emailProvider = new ResendEmailProvider();
  const paymentProvider = new StripePaymentProvider();
  const userService = new UserService(userRepository, emailProvider);

  return { userRepository, emailProvider, paymentProvider, userService };
}

// Test container
export function createTestContainer(): Container {
  const userRepository = new MockUserRepository();
  const emailProvider = new MockEmailProvider();
  const paymentProvider = new MockPaymentProvider();
  const userService = new UserService(userRepository, emailProvider);

  return { userRepository, emailProvider, paymentProvider, userService };
}

// Service with injected dependencies
export class UserService {
  constructor(
    private userRepository: UserRepository,
    private emailProvider: EmailProvider
  ) {}

  async create(input: CreateUserInput): Promise<User> {
    // ... uses this.userRepository and this.emailProvider
  }
}
```

---

## 4. Mock Providers for Testing

```ts
// __mocks__/email-service.ts
export class MockEmailProvider {
  public sentEmails: Array<{ to: string; subject: string; html: string }> = [];

  async send(to: string, subject: string, html: string): Promise<void> {
    this.sentEmails.push({ to, subject, html });
  }

  async sendTemplate(to: string, template: string, variables: Record<string, string>): Promise<void> {
    this.sentEmails.push({ to, subject: template, html: JSON.stringify(variables) });
  }

  clear() {
    this.sentEmails = [];
  }

  wasSent(to: string, subject: string): boolean {
    return this.sentEmails.some(e => e.to === to && e.subject === subject);
  }
}

// Test usage
describe("UserService", () => {
  let container: Container;

  beforeEach(() => {
    container = createTestContainer();
  });

  it("sends welcome email on user creation", async () => {
    const emailProvider = container.emailProvider as MockEmailProvider;

    await container.userService.create({
      name: "Test User",
      email: "test@example.com",
      password: "Password123!",
    });

    expect(emailProvider.wasSent("test@example.com", "Welcome!")).toBe(true);
  });
});
```

---

## Provider Selection Guide

| Scenario | Best Pattern |
|---|---|
| Simple CRUD | Direct repository calls |
| Business logic + side effects | Service layer |
| Swappable providers (email, payments) | Interface + implementation |
| Testing with mocks | Dependency injection |
| Multiple implementations | Factory function |
| Complex dependency graph | DI container |

---

## Provider Anti-Patterns

### ❌ Business Logic in Route Handlers
```ts
// BAD: Route handler does everything
export async function POST(request: NextRequest) {
  const body = await request.json();
  const user = await db.insert(users).values(body).returning();
  await resend.emails.send({ to: user.email, subject: "Welcome" });
  await analytics.track("user_created", { userId: user.id });
  return NextResponse.json(user);
}

// GOOD: Route handler delegates to service
export async function POST(request: NextRequest) {
  const validation = validateRequest(createUserSchema, await request.json());
  if ("error" in validation) return validation.error;
  const user = await userService.create(validation.data);
  return NextResponse.json({ data: user }, { status: 201 });
}
```

### ❌ Hardcoded Provider Dependencies
```ts
// BAD: Can't swap email provider
class UserService {
  private resend = new Resend(process.env.RESEND_API_KEY);
}

// GOOD: Injected via constructor
class UserService {
  constructor(private emailProvider: EmailProvider) {}
}
```

### ❌ Tight Coupling to Third-Party SDKs
```ts
// BAD: Stripe types leak into business logic
async function createSubscription(customerId: string, priceId: string) {
  const subscription: Stripe.Subscription = await stripe.subscriptions.create(...);
  return subscription; // Returns Stripe-specific type
}

// GOOD: Abstract return types
async function createSubscription(customerId: string, priceId: string): Promise<{ subscriptionId: string; status: string }> {
  const subscription = await stripe.subscriptions.create(...);
  return { subscriptionId: subscription.id, status: subscription.status };
}
```
