if (!address || typeof address === 'string') throw new Error('bad address');
          resolve({
            baseUrl: `http://127.0.0.1:${address.port}`,
            close: () => new Promise<void>((done, reject) => srv.close((err: Error | undefined) => err ? reject(err) : done())),
          });
        });
      });

      try {
        await writeFile(join(assetRoot, 'native-release-manifest.json'), JSON.stringify({
          version: '0.8.15',
          assets: [{
            product: 'omx-explore-harness',
            version: '0.8.15',
            platform: 'linux',
            arch: 'x64',
            archive: 'omx-explore-harness-x86_64-unknown-linux-musl.tar.gz',
            binary: 'omx-explore-harness',
            binary_path: 'omx-explore-harness',