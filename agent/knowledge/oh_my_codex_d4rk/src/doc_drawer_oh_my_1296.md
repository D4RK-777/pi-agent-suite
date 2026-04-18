.close((err: Error | undefined) => err ? reject(err) : done())),
          });
        });
      });

      try {
        await assert.rejects(
          () => resolveExploreHarnessCommandWithHydration(wd, {
            OMX_NATIVE_MANIFEST_URL: `${server.baseUrl}/native-release-manifest.json`,
            OMX_NATIVE_CACHE_DIR: join(wd, 'cache'),
          } as NodeJS.ProcessEnv),
          /no compatible native harness is available/,
        );
      } finally {
        await server.close();
      }
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });
});