}
    } catch {
      // Ignore unreadable loader directories.
    }
  }

  return undefined;
}

export function inferNativeAssetLibc(asset: Pick<NativeReleaseAsset, 'archive' | 'target' | 'libc'>): NativeLibc | undefined {
  if (asset.libc === 'musl' || asset.libc === 'glibc') return asset.libc;
  const hint = [asset.target, asset.archive].filter(Boolean).join(' ').toLowerCase();
  if (hint.includes('musl')) return 'musl';
  if (hint.includes('linux-gnu') || hint.includes('glibc')) return 'glibc';
  return undefined;
}