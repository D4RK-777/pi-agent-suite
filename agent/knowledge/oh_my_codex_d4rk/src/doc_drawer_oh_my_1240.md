xplore-harness');
        const packagedMeta = join(packageBinDir, 'omx-explore-harness.meta.json');
        const hadExistingBinary = existsSync(packagedBinary);
        const hadExistingMeta = existsSync(packagedMeta);

        await mkdir(codexDir, { recursive: true });
        await mkdir(fakeBin, { recursive: true });
        await writeFile(join(fakeBin, 'codex'), '#!/bin/sh\necho "codex test"\n');
        spawnSync('chmod', ['+x', join(fakeBin, 'codex')], { encoding: 'utf-8' });
        const fsPromises = await import('node:fs/promises');
        const originalBinary = hadExistingBinary ? await fsPromises.readFile(packagedBinary) : null;
        const originalMeta = hadExistingMeta ? await fsPromises.readFile(packagedMeta, 'utf-8') : null;