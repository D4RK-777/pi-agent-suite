.tar.gz',
            binary: 'omx-explore-harness',
            binary_path: 'omx-explore-harness',
            sha256: checksum,
            size: archiveBuffer.length,
            download_url: `${server.baseUrl}/omx-explore-harness-x86_64-unknown-linux-musl.tar.gz`,
          }],
        }, null, 2));

        const resolved = await resolveExploreHarnessCommandWithHydration(wd, {
          OMX_NATIVE_MANIFEST_URL: `${server.baseUrl}/native-release-manifest.json`,
          OMX_NATIVE_CACHE_DIR: cacheDir,
        } as NodeJS.ProcessEnv);
        assert.notEqual(resolved.command, 'cargo');
        assert.match(resolved.command, /cache/);
      } finally {
        await server.close();
      }
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });