t') {
        throw new Error('--keep-policy must be one of: score_improvement, pass_only');
      }
      result.keepPolicy = normalized;
      i++;
    } else if ((arg === '--slug') && next) {
      result.slug = slugifyMissionName(next);
      i++;
    } else if (arg.startsWith('--topic=')) {
      result.topic = arg.slice('--topic='.length);
    } else if (arg.startsWith('--evaluator=')) {
      result.evaluatorCommand = arg.slice('--evaluator='.length);
    } else if (arg.startsWith('--keep-policy=')) {
      const normalized = arg.slice('--keep-policy='.length).trim().toLowerCase();
      if (normalized !== 'pass_only' && normalized !== 'score_improvement') {
        throw new Error('--keep-policy must be one of: score_improvement, pass_only');
      }