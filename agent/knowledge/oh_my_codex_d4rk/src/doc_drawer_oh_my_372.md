data.mtimeMs >= options.newerThanMs) {
        return readPersistedResult(resultPath);
      }
    }

    const draftArtifactPath = buildDraftArtifactPath(repoRoot, slug);
    if (existsSync(draftArtifactPath)) {
      const metadata = await stat(draftArtifactPath).catch(() => null);
      if (!metadata || options.newerThanMs == null || metadata.mtimeMs >= options.newerThanMs) {
        const draftContent = await readFile(draftArtifactPath, 'utf-8');
        return parseDraftArtifactContent(draftContent, repoRoot, draftArtifactPath);
      }
    }
    return null;
  }