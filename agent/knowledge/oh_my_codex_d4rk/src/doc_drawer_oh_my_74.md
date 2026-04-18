, missionDir) || basename(missionDir);
  const missionSlug = slugifyMissionName(missionRelativeDir);

  return {
    missionDir,
    repoRoot,
    missionFile,
    sandboxFile,
    missionRelativeDir,
    missionContent,
    sandboxContent,
    sandbox,
    missionSlug,
  };
}