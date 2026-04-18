ry.name);
      if (entry.isDirectory()) {
        pending.push(fullPath);
        continue;
      }
      const relative = fullPath.slice(rootDir.length + 1).replaceAll('\\', '/');
      if (relative === normalizedNeedle || relative.endsWith(`/${normalizedNeedle}`)) {
        return fullPath;
      }
    }
  }

  return undefined;
}

export async function hydrateNativeBinary(
  product: NativeProduct,
  options: HydrateNativeBinaryOptions = {},
): Promise<string | undefined> {
  const {
    packageRoot = getPackageRoot(),
    env = process.env,
    platform = process.platform,
    arch = process.arch,
  } = options;