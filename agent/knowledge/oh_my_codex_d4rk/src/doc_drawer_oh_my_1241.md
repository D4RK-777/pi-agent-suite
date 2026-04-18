const originalMeta = hadExistingMeta ? await fsPromises.readFile(packagedMeta, 'utf-8') : null;
        await mkdir(packageBinDir, { recursive: true });
        await writeFile(packagedBinary, '#!/bin/sh\necho "stub harness"\n');
        await writeFile(packagedMeta, JSON.stringify({ binaryName: process.platform === 'win32' ? 'omx-explore-harness.exe' : 'omx-explore-harness', platform: process.platform, arch: process.arch }));
        spawnSync('chmod', ['+x', packagedBinary], { encoding: 'utf-8' });