c/goal', topic);
      if (!topic) {
        throw new Error('Research topic is required.');
      }

      const evaluatorIntent = await promptWithDefault(io, '\nHow should OMX judge success? Describe it in plain language', topic);
      evaluatorCommand = await promptWithDefault(
        io,
        '\nEvaluator command (leave placeholder to refine further; must output {pass:boolean, score?:number} JSON before launch)',
        evaluatorCommand || `TODO replace with evaluator command for: ${evaluatorIntent}`,
      );

      const keepPolicyInput = await promptWithDefault(io, '\nKeep policy [score_improvement/pass_only]', keepPolicy);
      keepPolicy = keepPolicyInput.trim().toLowerCase() === 'pass_only' ? 'pass_only' : 'score_improvement';