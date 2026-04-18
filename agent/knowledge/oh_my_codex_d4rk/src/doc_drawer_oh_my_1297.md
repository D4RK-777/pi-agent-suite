ose();
      }
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });
});

describe('buildExploreHarnessArgs', () => {
  it('includes cwd, prompt, prompt contract, and constrained model settings', () => {
    const args = buildExploreHarnessArgs('find auth', '/repo', {
      OMX_EXPLORE_SPARK_MODEL: 'spark-model',
    } as NodeJS.ProcessEnv, '/pkg');
    assert.deepEqual(args, [
      '--cwd',
      '/repo',
      '--prompt',
      'find auth',
      '--prompt-file',
      '/pkg/prompts/explore-harness.md',
      '--model-spark',
      'spark-model',
      '--model-fallback',
      'gpt-5.4',
    ]);
  });
});