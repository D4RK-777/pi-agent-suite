y: ${seedInputs.keepPolicy || '(none)'}`,
    `- slug: ${seedInputs.slug?.trim() || '(none)'}`,
  ];

  return [
    '$deep-interview --autoresearch',
    'Run the deep-interview skill in autoresearch mode for `omx autoresearch`.',
    'Guide the user through research topic definition, evaluator readiness, keep policy, and slug/session naming.',
    'Do not launch tmux or run `omx autoresearch` yourself.',
    'When the user confirms launch and the evaluator is concrete, write/update these canonical artifacts under `.omx/specs/`:',
    '- `deep-interview-autoresearch-{slug}.md`',
    '- `autoresearch-{slug}/mission.md`',
    '- `autoresearch-{slug}/sandbox.md`',
    '- `autoresearch-{slug}/result.json`',