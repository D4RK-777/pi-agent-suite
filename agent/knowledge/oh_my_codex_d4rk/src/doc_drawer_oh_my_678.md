w Error(`[native-assets] extracted archive missing expected binary ${asset.binary_path}`);
        }

        await mkdir(dirname(cachedBinaryPath), { recursive: true });
        await copyFile(extractedBinaryPath, cachedBinaryPath);
        if (platform !== 'win32') chmodSync(cachedBinaryPath, 0o755);
        return cachedBinaryPath;
      } catch (error) {
        if (index < assets.length - 1 && isUnavailableArchiveError(error)) {
          await rm(archivePath, { force: true });
          await rm(extractDir, { recursive: true, force: true });
          continue;
        }
        throw error;
      }
    }
    return undefined;
  } finally {
    await rm(tempRoot, { recursive: true, force: true });
  }
}