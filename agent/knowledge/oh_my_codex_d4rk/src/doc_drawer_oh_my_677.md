throw new Error(`[native-assets] downloaded archive size mismatch for ${asset.archive}`);
        }
        const digest = await sha256ForFile(archivePath);
        if (digest !== asset.sha256) {
          throw new Error(`[native-assets] checksum mismatch for ${asset.archive}`);
        }

        await extractArchive(archivePath, extractDir);
        const extractedBinaryPath = await findExtractedBinaryPath(extractDir, asset.binary_path);
        if (!extractedBinaryPath) {
          throw new Error(`[native-assets] extracted archive missing expected binary ${asset.binary_path}`);
        }