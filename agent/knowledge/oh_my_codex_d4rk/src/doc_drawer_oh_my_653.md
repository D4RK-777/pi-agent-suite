packageRoot?: string;
  env?: NodeJS.ProcessEnv;
  platform?: NodeJS.Platform;
  arch?: string;
}

export interface NativeBinaryCandidateOptions {
  linuxLibcPreference?: readonly NativeLibc[];
}

export interface ResolveLinuxNativeLibcPreferenceOptions {
  env?: NodeJS.ProcessEnv;
  detectedRuntime?: NativeLibc;
}

const NATIVE_AUTO_FETCH_ENV = 'OMX_NATIVE_AUTO_FETCH';
const NATIVE_MANIFEST_URL_ENV = 'OMX_NATIVE_MANIFEST_URL';
const NATIVE_RELEASE_BASE_URL_ENV = 'OMX_NATIVE_RELEASE_BASE_URL';
const NATIVE_CACHE_DIR_ENV = 'OMX_NATIVE_CACHE_DIR';
export const EXPLORE_BIN_ENV = 'OMX_EXPLORE_BIN';
export const SPARKSHELL_BIN_ENV = 'OMX_SPARKSHELL_BIN';

function packageJsonPath(packageRoot = getPackageRoot()): string {
  return join(packageRoot, 'package.json');
}