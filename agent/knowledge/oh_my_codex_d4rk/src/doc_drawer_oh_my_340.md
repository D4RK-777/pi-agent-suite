epPolicy = keepPolicyInput.trim().toLowerCase() === 'pass_only' ? 'pass_only' : 'score_improvement';

      slug = await promptWithDefault(io, '\nMission slug', slug || slugifyMissionName(topic));
      slug = slugifyMissionName(slug);

      const deepInterview = await writeAutoresearchDeepInterviewArtifacts({
        repoRoot,
        topic,
        evaluatorCommand,
        keepPolicy,
        slug,
        seedInputs,
      });

      console.log(`\nDraft saved: ${deepInterview.draftArtifactPath}`);
      console.log(`Launch readiness: ${deepInterview.launchReady ? 'ready' : deepInterview.blockedReasons.join(' ')}`);

      const action = await promptAction(io, deepInterview.launchReady);
      if (action === 'refine') {
        continue;
      }