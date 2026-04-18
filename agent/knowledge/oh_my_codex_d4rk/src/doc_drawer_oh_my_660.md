'/lib64', '/usr/lib', '/usr/local/lib'];
const MUSL_LOADER_PATTERN = /^ld-musl-.*\.so(?:\.\d+)*$/i;

function inferRuntimeLibcFromText(text: string | undefined): NativeLibc | undefined {
  const normalized = String(text || '').toLowerCase();
  if (!normalized) return undefined;
  if (normalized.includes('musl')) return 'musl';
  if (normalized.includes('glibc') || normalized.includes('gnu libc')) return 'glibc';
  return undefined;
}

export function resolveLinuxNativeLibcPreference(
  options: ResolveLinuxNativeLibcPreferenceOptions = {},
): NativeLibc[] {
  const { env = process.env, detectedRuntime } = options;
  const runtime = detectedRuntime ?? detectLinuxRuntimeLibc(env);
  if (runtime === 'musl') return ['musl'];
  return ['musl', 'glibc'];
}