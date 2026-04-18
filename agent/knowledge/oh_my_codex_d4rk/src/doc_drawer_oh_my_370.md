s < newerThanMs) {
        continue;
      }
    }
    filtered.push(path);
  }
  return filtered;
}

export async function resolveAutoresearchDeepInterviewResult(
  repoRoot: string,
  options: {
    slug?: string;
    newerThanMs?: number;
    excludeResultPaths?: ReadonlySet<string>;
    excludeDraftPaths?: ReadonlySet<string>;
  } = {},
): Promise<AutoresearchDeepInterviewResult | null> {
  const slug = options.slug?.trim() ? slugifyMissionName(options.slug) : null;