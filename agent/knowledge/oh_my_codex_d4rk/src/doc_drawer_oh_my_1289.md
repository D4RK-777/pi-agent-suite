-codex.git' },
      }));
      await mkdir(join(wd, 'crates', 'omx-explore'), { recursive: true });
      await writeFile(join(wd, 'crates', 'omx-explore', 'Cargo.toml'), '[package]\nname=\"omx-explore-harness\"\nversion=\"0.8.15\"\n');
      const binaryPath = join(stagingDir, packagedExploreHarnessBinaryName());
      await writeFile(binaryPath, '#!/bin/sh\necho hydrated-explore\n');
      await chmod(binaryPath, 0o755);