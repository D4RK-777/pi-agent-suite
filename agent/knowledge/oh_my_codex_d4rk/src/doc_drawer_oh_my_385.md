ructionsFile;
    } else {
      delete process.env[AUTORESEARCH_APPEND_INSTRUCTIONS_ENV];
    }
  }

  const result = await resolveAutoresearchDeepInterviewResult(repoRoot, {
    excludeResultPaths: existingResultPaths,
    excludeDraftPaths: existingDraftPaths,
  });
  if (!result) {
    throw new Error('autoresearch deep-interview did not produce .omx/specs launch artifacts.');
  }
  if (!result.launchReady) {
    throw new Error(
      `autoresearch deep-interview exited without a launch-ready result. ${result.blockedReasons.join(' ') || 'Refine the interview result and retry.'}`,
    );
  }
  return materializeAutoresearchDeepInterviewResult(result);
}