',
          'node scripts/eval.js',
          'pass_only',
          'ux-eval',
          'launch',
        ]),
      ));

      const draftContent = await readFile(join(repo, '.omx', 'specs', 'deep-interview-autoresearch-ux-eval.md'), 'utf-8');
      const resultContent = await readFile(join(repo, '.omx', 'specs', 'autoresearch-ux-eval', 'result.json'), 'utf-8');
      const missionContent = await readFile(join(result.missionDir, 'mission.md'), 'utf-8');
      const sandboxContent = await readFile(join(result.missionDir, 'sandbox.md'), 'utf-8');