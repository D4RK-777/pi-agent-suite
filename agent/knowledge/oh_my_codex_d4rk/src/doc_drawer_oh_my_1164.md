;
      await writeFile(join(missionDir, 'mission.md'), '# Mission\nSplit pane launch.\n', 'utf-8');
      await writeFile(
        join(missionDir, 'sandbox.md'),
        '---\nevaluator:\n  command: node scripts/eval.js\n  format: json\n  keep_policy: pass_only\n---\nStay inside the mission boundary.\n',
        'utf-8',
      );
      await writeFile(join(repo, 'scripts', 'eval.js'), "process.stdout.write(JSON.stringify({ pass: true }));\n", 'utf-8');
      execFileSync('git', ['add', '.'], { cwd: repo, stdio: 'ignore' });
      execFileSync('git', ['commit', '-m', 'add autoresearch mission'], { cwd: repo, stdio: 'ignore' });