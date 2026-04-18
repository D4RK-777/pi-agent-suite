eDraftArtifactContent(draftContent, repoRoot, draftArtifactPath);
      }
    }
    return null;
  }

  const resultPaths = await filterRecentPaths(
    await listAutoresearchDeepInterviewResultPaths(repoRoot),
    options.newerThanMs,
    options.excludeResultPaths,
  );
  const resultEntries = await Promise.all(resultPaths.map(async (path) => ({ path, metadata: await stat(path) })));
  const newestResultPath = resultEntries.sort((left, right) => right.metadata.mtimeMs - left.metadata.mtimeMs)[0]?.path;
  if (newestResultPath) {
    return readPersistedResult(newestResultPath);
  }