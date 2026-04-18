nDir,
    repoRoot: repo,
    missionFile,
    sandboxFile,
    missionRelativeDir: 'missions/demo',
    missionContent,
    sandboxContent,
    sandbox: {
      frontmatter: { evaluator: { command: 'node scripts/eval.js', format: 'json', ...(keepPolicy ? { keep_policy: keepPolicy } : {}) } },
      evaluator: { command: 'node scripts/eval.js', format: 'json', ...(keepPolicy ? { keep_policy: keepPolicy } : {}) },
      body: 'Stay inside the mission boundary.',
    },
    missionSlug: 'missions-demo',
  };
}