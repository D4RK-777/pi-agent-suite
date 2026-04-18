# Form Patterns

Concrete, production-ready patterns for every form scenario you'll encounter.

Use these as starting points. Adapt to your project's validation library, styling approach, and component system.

---

## 1. Simple Form

**When:** Login, contact, newsletter signup — single section, straightforward validation.

### Core Pattern (React Hook Form + Zod)

```tsx
// components/forms/simple-form.tsx
"use client";

import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import { useState } from "react";

// Define schema with Zod — this is your single source of truth
const formSchema = z.object({
  email: z.string().email("Please enter a valid email address"),
  name: z.string().min(2, "Name must be at least 2 characters"),
  message: z.string().min(10, "Message must be at least 10 characters"),
});

type FormValues = z.infer<typeof formSchema>;

interface SimpleFormProps {
  onSubmit: (data: FormValues) => Promise<void>;
  defaultValues?: Partial<FormValues>;
}

export function SimpleForm({ onSubmit, defaultValues }: SimpleFormProps) {
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitError, setSubmitError] = useState<string | null>(null);
  const [submitSuccess, setSubmitSuccess] = useState(false);

  const {
    register,
    handleSubmit,
    formState: { errors, isDirty, isValid },
    reset,
  } = useForm<FormValues>({
    resolver: zodResolver(formSchema),
    defaultValues: defaultValues || {
      email: "",
      name: "",
      message: "",
    },
    mode: "onBlur", // Validate on blur, not on every keystroke
  });

  const onSubmitForm = async (data: FormValues) => {
    setIsSubmitting(true);
    setSubmitError(null);
    setSubmitSuccess(false);

    try {
      await onSubmit(data);
      setSubmitSuccess(true);
      reset();
    } catch (error) {
      setSubmitError(error instanceof Error ? error.message : "Something went wrong");
    } finally {
      setIsSubmitting(false);
    }
  };

  if (submitSuccess) {
    return (
      <div className="rounded-lg border border-green-200 bg-green-50 p-6 text-center">
        <p className="font-medium text-green-800">Message sent successfully!</p>
        <button
          className="mt-3 text-sm text-green-700 underline hover:text-green-900"
          onClick={() => setSubmitSuccess(false)}
        >
          Send another message
        </button>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit(onSubmitForm)} className="space-y-4" noValidate>
      {/* Name Field */}
      <div>
        <label htmlFor="name" className="block text-sm font-medium mb-1">
          Name <span className="text-destructive">*</span>
        </label>
        <input
          id="name"
          type="text"
          {...register("name")}
          className={`w-full rounded-md border px-3 py-2 text-sm transition-colors ${
            errors.name
              ? "border-destructive focus:ring-destructive"
              : "border-input focus:ring-primary"
          } focus:outline-none focus:ring-2`}
          aria-invalid={!!errors.name}
          aria-describedby={errors.name ? "name-error" : undefined}
        />
        {errors.name && (
          <p id="name-error" className="mt-1 text-xs text-destructive" role="alert">
            {errors.name.message}
          </p>
        )}
      </div>

      {/* Email Field */}
      <div>
        <label htmlFor="email" className="block text-sm font-medium mb-1">
          Email <span className="text-destructive">*</span>
        </label>
        <input
          id="email"
          type="email"
          {...register("email")}
          className={`w-full rounded-md border px-3 py-2 text-sm transition-colors ${
            errors.email
              ? "border-destructive focus:ring-destructive"
              : "border-input focus:ring-primary"
          } focus:outline-none focus:ring-2`}
          aria-invalid={!!errors.email}
          aria-describedby={errors.email ? "email-error" : undefined}
        />
        {errors.email && (
          <p id="email-error" className="mt-1 text-xs text-destructive" role="alert">
            {errors.email.message}
          </p>
        )}
      </div>

      {/* Message Field */}
      <div>
        <label htmlFor="message" className="block text-sm font-medium mb-1">
          Message <span className="text-destructive">*</span>
        </label>
        <textarea
          id="message"
          rows={4}
          {...register("message")}
          className={`w-full rounded-md border px-3 py-2 text-sm transition-colors resize-none ${
            errors.message
              ? "border-destructive focus:ring-destructive"
              : "border-input focus:ring-primary"
          } focus:outline-none focus:ring-2`}
          aria-invalid={!!errors.message}
          aria-describedby={errors.message ? "message-error" : undefined}
        />
        {errors.message && (
          <p id="message-error" className="mt-1 text-xs text-destructive" role="alert">
            {errors.message.message}
          </p>
        )}
      </div>

      {/* Submit Error */}
      {submitError && (
        <div className="rounded-md border border-destructive/50 bg-destructive/10 p-3 text-sm text-destructive" role="alert">
          {submitError}
        </div>
      )}

      {/* Submit Button */}
      <button
        type="submit"
        disabled={isSubmitting || !isDirty || !isValid}
        className="w-full rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground transition-colors disabled:opacity-50"
      >
        {isSubmitting ? (
          <span className="flex items-center justify-center gap-2">
            <span className="h-4 w-4 animate-spin rounded-full border-2 border-current border-t-transparent" />
            Sending...
          </span>
        ) : (
          "Send Message"
        )}
      </button>
    </form>
  );
}
```

### Key Decisions

- **Zod schema is the source of truth** — types are inferred, not manually written.
- **`mode: "onBlur"`** — validates on blur, not every keystroke. Less annoying UX.
- **`noValidate`** on form — disables native HTML validation, lets React Hook Form handle it.
- **Error IDs** — `aria-describedby` links errors to fields for screen readers.
- **Submit states** — loading spinner, success message, error banner. All three are mandatory.

---

## 2. Complex Form with Dependent Fields

**When:** Job applications, multi-field configurations, conditional sections.

### Core Pattern

```tsx
// components/forms/complex-form.tsx
"use client";

import { useForm, useWatch, Controller } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import { useState } from "react";

// Schema with refinements for conditional validation
const formSchema = z.object({
  accountType: z.enum(["personal", "business"]),
  companyName: z.string().min(1, "Company name is required").optional(),
  companySize: z.enum(["1-10", "11-50", "51-200", "200+"]).optional(),
  email: z.string().email("Valid email required"),
  phone: z.string().optional(),
  notifyByEmail: z.boolean().default(true),
  notifyBySms: z.boolean().default(false),
  // Conditional: phone required if SMS notifications enabled
}).refine(
  (data) => {
    if (data.notifyBySms && !data.phone) return false;
    return true;
  },
  { message: "Phone number is required when SMS notifications are enabled", path: ["phone"] }
).refine(
  (data) => {
    if (data.accountType === "business" && !data.companyName) return false;
    return true;
  },
  { message: "Company name is required for business accounts", path: ["companyName"] }
);

type FormValues = z.infer<typeof formSchema>;

export function ComplexForm({ onSubmit }: { onSubmit: (data: FormValues) => Promise<void> }) {
  const [isSubmitting, setIsSubmitting] = useState(false);

  const {
    register,
    handleSubmit,
    control,
    formState: { errors },
  } = useForm<FormValues>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      accountType: "personal",
      companyName: "",
      companySize: "1-10",
      email: "",
      phone: "",
      notifyByEmail: true,
      notifyBySms: false,
    },
    mode: "onBlur",
  });

  // Watch values for conditional rendering
  const accountType = useWatch({ control, name: "accountType" });
  const notifyBySms = useWatch({ control, name: "notifyBySms" });

  const isBusiness = accountType === "business";

  return (
    <form onSubmit={handleSubmit(async (data) => {
      setIsSubmitting(true);
      try { await onSubmit(data); }
      finally { setIsSubmitting(false); }
    })} className="space-y-6" noValidate>

      {/* Account Type — controls conditional fields */}
      <fieldset className="space-y-3">
        <legend className="text-sm font-medium">Account Type</legend>
        <div className="flex gap-4">
          {(["personal", "business"] as const).map((type) => (
            <label key={type} className="flex items-center gap-2 cursor-pointer">
              <input
                type="radio"
                value={type}
                {...register("accountType")}
                className="h-4 w-4"
              />
              <span className="text-sm capitalize">{type}</span>
            </label>
          ))}
        </div>
        {errors.accountType && (
          <p className="text-xs text-destructive">{errors.accountType.message}</p>
        )}
      </fieldset>

      {/* Conditional: Business fields */}
      {isBusiness && (
        <div className="space-y-4 rounded-lg border p-4 bg-muted/30">
          <h3 className="text-sm font-medium">Business Details</h3>

          <div>
            <label htmlFor="companyName" className="block text-sm font-medium mb-1">
              Company Name <span className="text-destructive">*</span>
            </label>
            <input
              id="companyName"
              {...register("companyName")}
              className="w-full rounded-md border px-3 py-2 text-sm"
              aria-invalid={!!errors.companyName}
            />
            {errors.companyName && (
              <p className="mt-1 text-xs text-destructive">{errors.companyName.message}</p>
            )}
          </div>

          <div>
            <label htmlFor="companySize" className="block text-sm font-medium mb-1">
              Company Size
            </label>
            <select
              id="companySize"
              {...register("companySize")}
              className="w-full rounded-md border px-3 py-2 text-sm"
            >
              <option value="1-10">1-10 employees</option>
              <option value="11-50">11-50 employees</option>
              <option value="51-200">51-200 employees</option>
              <option value="200+">200+ employees</option>
            </select>
          </div>
        </div>
      )}

      {/* Contact */}
      <div className="space-y-4">
        <h3 className="text-sm font-medium">Contact Information</h3>

        <div>
          <label htmlFor="email" className="block text-sm font-medium mb-1">
            Email <span className="text-destructive">*</span>
          </label>
          <input
            id="email"
            type="email"
            {...register("email")}
            className="w-full rounded-md border px-3 py-2 text-sm"
            aria-invalid={!!errors.email}
          />
          {errors.email && (
            <p className="mt-1 text-xs text-destructive">{errors.email.message}</p>
          )}
        </div>

        <div>
          <label htmlFor="phone" className="block text-sm font-medium mb-1">
            Phone {notifyBySms && <span className="text-destructive">*</span>}
          </label>
          <input
            id="phone"
            type="tel"
            {...register("phone")}
            className="w-full rounded-md border px-3 py-2 text-sm"
            aria-invalid={!!errors.phone}
          />
          {errors.phone && (
            <p className="mt-1 text-xs text-destructive">{errors.phone.message}</p>
          )}
        </div>
      </div>

      {/* Notification Preferences */}
      <fieldset className="space-y-3">
        <legend className="text-sm font-medium">Notifications</legend>
        <label className="flex items-center gap-2">
          <Controller
            name="notifyByEmail"
            control={control}
            render={({ field }) => (
              <input
                type="checkbox"
                checked={field.value}
                onChange={(e) => field.onChange(e.target.checked)}
                className="h-4 w-4"
              />
            )}
          />
          <span className="text-sm">Email notifications</span>
        </label>
        <label className="flex items-center gap-2">
          <Controller
            name="notifyBySms"
            control={control}
            render={({ field }) => (
              <input
                type="checkbox"
                checked={field.value}
                onChange={(e) => field.onChange(e.target.checked)}
                className="h-4 w-4"
              />
            )}
          />
          <span className="text-sm">SMS notifications</span>
        </label>
      </fieldset>

      <button
        type="submit"
        disabled={isSubmitting}
        className="w-full rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground disabled:opacity-50"
      >
        {isSubmitting ? "Saving..." : "Create Account"}
      </button>
    </form>
  );
}
```

### Key Decisions

- **Conditional rendering** via `useWatch` — fields appear/disappear based on other values.
- **Conditional validation** via `.refine()` — Zod validates cross-field dependencies.
- **`Controller` for checkboxes** — React Hook Form needs `Controller` for non-standard inputs.
- **Grouped sections** — `<fieldset>` and `<legend>` for accessibility.
- **Visual grouping** — conditional fields are in a bordered box so the user sees they're related.

---

## 3. Multi-Step Wizard

**When:** Onboarding flows, multi-page applications, checkout processes.

### Core Pattern

```tsx
// components/forms/wizard.tsx
"use client";

import { useState, useCallback } from "react";
import { useForm, useWatch } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";

// Each step has its own schema
const stepSchemas = {
  1: z.object({
    name: z.string().min(2, "Name is required"),
    email: z.string().email("Valid email required"),
  }),
  2: z.object({
    company: z.string().min(1, "Company is required"),
    role: z.string().min(1, "Role is required"),
  }),
  3: z.object({
    plan: z.enum(["free", "pro", "enterprise"]),
    billing: z.enum(["monthly", "yearly"]),
  }),
};

// Combined schema for final submission
const fullSchema = z.object({
  ...stepSchemas[1].shape,
  ...stepSchemas[2].shape,
  ...stepSchemas[3].shape,
});

type FormValues = z.infer<typeof fullSchema>;

const TOTAL_STEPS = 3;

interface WizardProps {
  onComplete: (data: FormValues) => Promise<void>;
}

export function Wizard({ onComplete }: WizardProps) {
  const [currentStep, setCurrentStep] = useState(1);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const {
    register,
    handleSubmit,
    trigger,
    control,
    formState: { errors },
  } = useForm<FormValues>({
    resolver: zodResolver(fullSchema),
    defaultValues: {
      name: "",
      email: "",
      company: "",
      role: "",
      plan: "free",
      billing: "monthly",
    },
    mode: "onBlur",
  });

  const validateStep = useCallback(async () => {
    const stepSchema = stepSchemas[currentStep as keyof typeof stepSchemas];
    const stepFields = Object.keys(stepSchema.shape) as (keyof FormValues)[];
    return trigger(stepFields);
  }, [currentStep, trigger]);

  const nextStep = async () => {
    const isValid = await validateStep();
    if (isValid) {
      setCurrentStep((prev) => Math.min(prev + 1, TOTAL_STEPS));
    }
  };

  const prevStep = () => {
    setCurrentStep((prev) => Math.max(prev - 1, 1));
  };

  const onSubmit = async (data: FormValues) => {
    if (currentStep < TOTAL_STEPS) {
      await nextStep();
      return;
    }

    setIsSubmitting(true);
    try {
      await onComplete(data);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="mx-auto max-w-lg">
      {/* Progress Indicator */}
      <div className="mb-8">
        <div className="flex items-center justify-between mb-2">
          {Array.from({ length: TOTAL_STEPS }, (_, i) => i + 1).map((step) => (
            <div
              key={step}
              className={`flex items-center justify-center w-8 h-8 rounded-full text-sm font-medium transition-colors ${
                step < currentStep
                  ? "bg-primary text-primary-foreground"
                  : step === currentStep
                  ? "bg-primary/20 text-primary"
                  : "bg-muted text-muted-foreground"
              }`}
            >
              {step < currentStep ? "✓" : step}
            </div>
          ))}
        </div>
        <div className="h-1 bg-muted rounded-full overflow-hidden">
          <div
            className="h-full bg-primary transition-all duration-300"
            style={{ width: `${(currentStep / TOTAL_STEPS) * 100}%` }}
          />
        </div>
        <p className="mt-2 text-sm text-muted-foreground text-center">
          Step {currentStep} of {TOTAL_STEPS}
        </p>
      </div>

      {/* Form */}
      <form onSubmit={handleSubmit(onSubmit)} noValidate>
        {currentStep === 1 && (
          <div className="space-y-4">
            <h2 className="text-lg font-semibold">Personal Information</h2>
            <div>
              <label htmlFor="name" className="block text-sm font-medium mb-1">Name</label>
              <input id="name" {...register("name")} className="w-full rounded-md border px-3 py-2 text-sm" />
              {errors.name && <p className="text-xs text-destructive mt-1">{errors.name.message}</p>}
            </div>
            <div>
              <label htmlFor="email" className="block text-sm font-medium mb-1">Email</label>
              <input id="email" type="email" {...register("email")} className="w-full rounded-md border px-3 py-2 text-sm" />
              {errors.email && <p className="text-xs text-destructive mt-1">{errors.email.message}</p>}
            </div>
          </div>
        )}

        {currentStep === 2 && (
          <div className="space-y-4">
            <h2 className="text-lg font-semibold">Work Details</h2>
            <div>
              <label htmlFor="company" className="block text-sm font-medium mb-1">Company</label>
              <input id="company" {...register("company")} className="w-full rounded-md border px-3 py-2 text-sm" />
              {errors.company && <p className="text-xs text-destructive mt-1">{errors.company.message}</p>}
            </div>
            <div>
              <label htmlFor="role" className="block text-sm font-medium mb-1">Role</label>
              <input id="role" {...register("role")} className="w-full rounded-md border px-3 py-2 text-sm" />
              {errors.role && <p className="text-xs text-destructive mt-1">{errors.role.message}</p>}
            </div>
          </div>
        )}

        {currentStep === 3 && (
          <div className="space-y-4">
            <h2 className="text-lg font-semibold">Choose Your Plan</h2>
            <div className="space-y-2">
              {(["free", "pro", "enterprise"] as const).map((plan) => (
                <label key={plan} className="flex items-center gap-3 p-3 rounded-md border cursor-pointer hover:bg-muted/50">
                  <input type="radio" value={plan} {...register("plan")} className="h-4 w-4" />
                  <span className="text-sm capitalize font-medium">{plan}</span>
                </label>
              ))}
            </div>
            <div className="flex gap-4">
              {(["monthly", "yearly"] as const).map((billing) => (
                <label key={billing} className="flex-1 flex items-center justify-center gap-2 p-3 rounded-md border cursor-pointer hover:bg-muted/50">
                  <input type="radio" value={billing} {...register("billing")} className="h-4 w-4" />
                  <span className="text-sm capitalize">{billing}</span>
                </label>
              ))}
            </div>
          </div>
        )}

        {/* Navigation */}
        <div className="mt-6 flex items-center justify-between">
          <button
            type="button"
            onClick={prevStep}
            disabled={currentStep === 1}
            className="text-sm text-muted-foreground hover:text-foreground disabled:opacity-50 disabled:cursor-not-allowed"
          >
            ← Back
          </button>
          <button
            type="submit"
            disabled={isSubmitting}
            className="rounded-md bg-primary px-6 py-2 text-sm font-medium text-primary-foreground disabled:opacity-50"
          >
            {isSubmitting
              ? "Submitting..."
              : currentStep === TOTAL_STEPS
              ? "Complete"
              : "Continue →"}
          </button>
        </div>
      </form>
    </div>
  );
}
```

### Key Decisions

- **Per-step validation** — only validate the current step's fields, not the whole form.
- **Progress indicator** — shows completed (✓), current (highlighted), and upcoming (muted) steps.
- **Back button** — always allow going back without losing data.
- **State persists** — `useForm` keeps all values across steps, no manual state management needed.
- **Final submission** — only happens on the last step.

---

## 4. File Upload

**When:** Profile pictures, document uploads, image galleries.

### Core Pattern

```tsx
// components/forms/file-upload.tsx
"use client";

import { useState, useCallback, useRef } from "react";
import { cn } from "@/lib/utils";

interface FileUploadProps {
  accept?: string;
  maxSize?: number; // in MB
  multiple?: boolean;
  onFilesChange: (files: File[]) => void;
  label?: string;
  error?: string;
}

export function FileUpload({
  accept = "image/*",
  maxSize = 5,
  multiple = false,
  onFilesChange,
  label = "Upload files",
  error,
}: FileUploadProps) {
  const [dragActive, setDragActive] = useState(false);
  const [previews, setPreviews] = useState<{ file: File; url: string }[]>([]);
  const [uploadError, setUploadError] = useState<string | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const validateFile = useCallback(
    (file: File): string | null => {
      if (file.size > maxSize * 1024 * 1024) {
        return `${file.name} is too large. Maximum size is ${maxSize}MB.`;
      }
      if (accept !== "*/*" && !file.type.match(accept.replace("*", ".*"))) {
        return `${file.name} is not an accepted file type.`;
      }
      return null;
    },
    [accept, maxSize]
  );

  const handleFiles = useCallback(
    (files: FileList | File[]) => {
      setUploadError(null);
      const fileArray = Array.from(files);
      const errors: string[] = [];

      const validFiles: File[] = [];
      for (const file of fileArray) {
        const err = validateFile(file);
        if (err) errors.push(err);
        else validFiles.push(file);
      }

      if (errors.length > 0) {
        setUploadError(errors[0]);
      }

      // Create previews for images
      const newPreviews = validFiles
        .filter((f) => f.type.startsWith("image/"))
        .map((f) => ({ file: f, url: URL.createObjectURL(f) }));

      setPreviews((prev) => [...prev, ...newPreviews]);
      onFilesChange(validFiles);
    },
    [validateFile, onFilesChange]
  );

  const handleDrag = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(e.type === "dragenter" || e.type === "dragover");
  }, []);

  const handleDrop = useCallback(
    (e: React.DragEvent) => {
      e.preventDefault();
      e.stopPropagation();
      setDragActive(false);
      if (e.dataTransfer.files) handleFiles(e.dataTransfer.files);
    },
    [handleFiles]
  );

  const removeFile = useCallback(
    (index: number) => {
      setPreviews((prev) => {
        URL.revokeObjectURL(prev[index].url);
        const next = [...prev];
        next.splice(index, 1);
        onFilesChange(next.map((p) => p.file));
        return next;
      });
    },
    [onFilesChange]
  );

  return (
    <div className="space-y-3">
      <label className="block text-sm font-medium">{label}</label>

      {/* Drop Zone */}
      <div
        className={cn(
          "relative flex flex-col items-center justify-center rounded-lg border-2 border-dashed p-8 text-center transition-colors cursor-pointer",
          dragActive
            ? "border-primary bg-primary/5"
            : "border-input hover:border-primary/50",
          error && "border-destructive"
        )}
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
        onClick={() => inputRef.current?.click()}
        role="button"
        tabIndex={0}
        onKeyDown={(e) => e.key === "Enter" && inputRef.current?.click()}
      >
        <input
          ref={inputRef}
          type="file"
          accept={accept}
          multiple={multiple}
          className="hidden"
          onChange={(e) => e.target.files && handleFiles(e.target.files)}
        />
        <div className="text-3xl mb-2">📁</div>
        <p className="text-sm text-muted-foreground">
          Drag and drop files here, or{" "}
          <span className="text-primary underline">browse</span>
        </p>
        <p className="mt-1 text-xs text-muted-foreground">
          {accept.replace("*/*", "any")} • Max {maxSize}MB
        </p>
      </div>

      {/* Error */}
      {(error || uploadError) && (
        <p className="text-xs text-destructive" role="alert">
          {error || uploadError}
        </p>
      )}

      {/* Previews */}
      {previews.length > 0 && (
        <div className="flex flex-wrap gap-3">
          {previews.map((preview, index) => (
            <div key={index} className="relative group">
              <img
                src={preview.url}
                alt={preview.file.name}
                className="h-20 w-20 rounded-md object-cover border"
              />
              <button
                className="absolute -top-2 -right-2 h-5 w-5 rounded-full bg-destructive text-destructive-foreground text-xs flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity"
                onClick={(e) => {
                  e.stopPropagation();
                  removeFile(index);
                }}
                aria-label={`Remove ${preview.file.name}`}
              >
                ✕
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
```

### Key Decisions

- **Drag and drop** — with visual feedback on drag over.
- **File validation** — size and type checks before accepting.
- **Image previews** — `URL.createObjectURL` for instant previews.
- **Cleanup** — `URL.revokeObjectURL` when removing files to prevent memory leaks.
- **Keyboard accessible** — click or Enter to browse.

---

## 5. Inline Editing

**When:** Click-to-edit fields in tables, profiles, settings.

### Core Pattern

```tsx
// components/forms/inline-edit.tsx
"use client";

import { useState, useRef, useEffect, ReactNode } from "react";

interface InlineEditProps {
  value: string;
  onSave: (value: string) => Promise<void>;
  placeholder?: string;
  type?: "text" | "textarea";
  validate?: (value: string) => string | null;
  renderDisplay?: (value: string) => ReactNode;
}

export function InlineEdit({
  value: initialValue,
  onSave,
  placeholder = "Click to edit",
  type = "text",
  validate,
  renderDisplay,
}: InlineEditProps) {
  const [isEditing, setIsEditing] = useState(false);
  const [value, setValue] = useState(initialValue);
  const [error, setError] = useState<string | null>(null);
  const [isSaving, setIsSaving] = useState(false);
  const inputRef = useRef<HTMLInputElement | HTMLTextAreaElement>(null);

  useEffect(() => {
    if (isEditing) {
      inputRef.current?.focus();
    }
  }, [isEditing]);

  const handleSave = async () => {
    const validationError = validate?.(value);
    if (validationError) {
      setError(validationError);
      return;
    }

    setIsSaving(true);
    try {
      await onSave(value);
      setIsEditing(false);
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to save");
    } finally {
      setIsSaving(false);
    }
  };

  const handleCancel = () => {
    setValue(initialValue);
    setIsEditing(false);
    setError(null);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && type === "text") {
      handleSave();
    }
    if (e.key === "Escape") {
      handleCancel();
    }
  };

  if (isEditing) {
    return (
      <div className="space-y-1">
        {type === "textarea" ? (
          <textarea
            ref={inputRef as React.RefObject<HTMLTextAreaElement>}
            value={value}
            onChange={(e) => setValue(e.target.value)}
            onKeyDown={handleKeyDown}
            className="w-full rounded-md border px-3 py-2 text-sm"
            rows={3}
          />
        ) : (
          <input
            ref={inputRef as React.RefObject<HTMLInputElement>}
            type="text"
            value={value}
            onChange={(e) => setValue(e.target.value)}
            onKeyDown={handleKeyDown}
            className="w-full rounded-md border px-3 py-2 text-sm"
          />
        )}
        {error && <p className="text-xs text-destructive">{error}</p>}
        <div className="flex gap-2">
          <button
            onClick={handleSave}
            disabled={isSaving}
            className="text-xs text-primary hover:underline disabled:opacity-50"
          >
            {isSaving ? "Saving..." : "Save"}
          </button>
          <button
            onClick={handleCancel}
            className="text-xs text-muted-foreground hover:text-foreground"
          >
            Cancel
          </button>
        </div>
      </div>
    );
  }

  return (
    <div
      className="group cursor-pointer rounded-md px-2 py-1 -mx-2 hover:bg-muted transition-colors"
      onClick={() => setIsEditing(true)}
      role="button"
      tabIndex={0}
      onKeyDown={(e) => e.key === "Enter" && setIsEditing(true)}
    >
      {renderDisplay ? (
        renderDisplay(initialValue)
      ) : initialValue ? (
        <span className="text-sm">{initialValue}</span>
      ) : (
        <span className="text-sm text-muted-foreground italic">{placeholder}</span>
      )}
    </div>
  );
}
```

---

## 6. Search / Filter Form

**When:** Product filters, data table search, multi-field filtering.

### Core Pattern

```tsx
// components/forms/search-filter.tsx
"use client";

import { useState, useEffect, useCallback } from "react";
import { useSearchParams, useRouter, usePathname } from "next/navigation";

interface FilterOption {
  label: string;
  value: string;
}

interface SearchFilterProps {
  searchPlaceholder?: string;
  categories?: FilterOption[];
  statuses?: FilterOption[];
  debounceMs?: number;
}

export function SearchFilter({
  searchPlaceholder = "Search...",
  categories,
  statuses,
  debounceMs = 300,
}: SearchFilterProps) {
  const searchParams = useSearchParams();
  const router = useRouter();
  const pathname = usePathname();

  const [search, setSearch] = useState(searchParams.get("q") || "");

  // Debounced search
  useEffect(() => {
    const timer = setTimeout(() => {
      const params = new URLSearchParams(searchParams);
      if (search) params.set("q", search);
      else params.delete("q");
      router.replace(`${pathname}?${params.toString()}`);
    }, debounceMs);

    return () => clearTimeout(timer);
  }, [search, debounceMs, router, pathname, searchParams]);

  const updateFilter = useCallback(
    (key: string, value: string | null) => {
      const params = new URLSearchParams(searchParams);
      if (value) params.set(key, value);
      else params.delete(key);
      router.replace(`${pathname}?${params.toString()}`);
    },
    [router, pathname, searchParams]
  );

  const clearAll = () => {
    setSearch("");
    router.replace(pathname);
  };

  const hasFilters = search || searchParams.get("category") || searchParams.get("status");

  return (
    <div className="space-y-4">
      {/* Search Input */}
      <div className="relative">
        <span className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground">🔍</span>
        <input
          type="search"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder={searchPlaceholder}
          className="w-full rounded-md border pl-10 pr-10 py-2 text-sm"
        />
        {search && (
          <button
            className="absolute right-3 top-1/2 -translate-y-1/2 text-muted-foreground hover:text-foreground"
            onClick={() => setSearch("")}
            aria-label="Clear search"
          >
            ✕
          </button>
        )}
      </div>

      {/* Filters */}
      <div className="flex flex-wrap gap-3">
        {categories && (
          <select
            value={searchParams.get("category") || ""}
            onChange={(e) => updateFilter("category", e.target.value || null)}
            className="rounded-md border px-3 py-2 text-sm"
          >
            <option value="">All categories</option>
            {categories.map((c) => (
              <option key={c.value} value={c.value}>{c.label}</option>
            ))}
          </select>
        )}

        {statuses && (
          <select
            value={searchParams.get("status") || ""}
            onChange={(e) => updateFilter("status", e.target.value || null)}
            className="rounded-md border px-3 py-2 text-sm"
          >
            <option value="">All statuses</option>
            {statuses.map((s) => (
              <option key={s.value} value={s.value}>{s.label}</option>
            ))}
          </select>
        )}

        {hasFilters && (
          <button
            onClick={clearAll}
            className="text-sm text-muted-foreground hover:text-foreground underline"
          >
            Clear all
          </button>
        )}
      </div>
    </div>
  );
}
```

### Key Decisions

- **URL state** — filters are in the URL, so sharing/bookmarking works.
- **Debounced search** — 300ms delay prevents API spam.
- **Clear all** — one button to reset everything.
- **Server-compatible** — uses `useSearchParams` so it works with Next.js App Router.

---

## Form Design Unification Rules

When you receive a messy form or need to unify existing forms:

### 1. Single Source of Truth
- **Zod schema** defines validation, types, and error messages.
- Never duplicate validation logic between frontend and schema.
- Error messages come from Zod, not hardcoded in the UI.

### 2. Consistent Error Display
- Errors always appear below the field.
- Errors always use `text-destructive` color.
- Errors always have `role="alert"` for screen readers.
- Fields with errors get `border-destructive` and `aria-invalid`.

### 3. Consistent Loading States
- Submit button shows spinner + "Saving..." text.
- Button is `disabled` during submission.
- No other loading indicators needed for simple forms.

### 4. Consistent Success States
- Show a success message, don't just silently reset.
- Offer to "do it again" (send another, create another).
- Clear the form on success unless the user might want to reference it.

### 5. Accessibility Checklist
- Every input has a `<label>` with matching `htmlFor`/`id`.
- Required fields marked with `*` and `aria-required`.
- Error messages linked with `aria-describedby`.
- Keyboard navigation works (Tab order, Enter to submit, Escape to cancel).
- Focus moves to first field on mount, to error on submit failure.
