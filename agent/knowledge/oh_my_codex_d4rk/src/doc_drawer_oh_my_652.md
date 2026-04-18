NativeProduct = 'omx-explore-harness' | 'omx-sparkshell';
export type NativeLibc = 'musl' | 'glibc';

export interface NativeReleaseAsset {
  product: NativeProduct;
  version: string;
  platform: NodeJS.Platform;
  arch: string;
  target?: string;
  libc?: NativeLibc;
  archive: string;
  binary: string;
  binary_path: string;
  sha256: string;
  size?: number;
  download_url: string;
}

export interface NativeReleaseManifest {
  manifest_version?: number;
  version: string;
  tag?: string;
  generated_at?: string;
  assets: NativeReleaseAsset[];
}

export interface HydrateNativeBinaryOptions {
  packageRoot?: string;
  env?: NodeJS.ProcessEnv;
  platform?: NodeJS.Platform;
  arch?: string;
}