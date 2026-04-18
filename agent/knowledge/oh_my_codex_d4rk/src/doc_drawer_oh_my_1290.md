t writeFile(binaryPath, '#!/bin/sh\necho hydrated-explore\n');
      await chmod(binaryPath, 0o755);

      const archivePath = join(assetRoot, 'omx-explore-harness-x86_64-unknown-linux-musl.tar.gz');
      const archive = spawnSync('tar', ['-czf', archivePath, '-C', stagingDir, packagedExploreHarnessBinaryName()], { encoding: 'utf-8' });
      assert.equal(archive.status, 0, archive.stderr || archive.stdout);
      const archiveBuffer = await readFile(archivePath);
      const checksum = createHash('sha256').update(archiveBuffer).digest('hex');