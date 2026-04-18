dFile(archivePath);
      const checksum = createHash('sha256').update(archiveBuffer).digest('hex');

      const server = await new Promise<{ baseUrl: string; close: () => Promise<void> }>((resolve) => {
        const srv = createServer(async (req, res) => {
          const url = new URL(req.url || '/', 'http://127.0.0.1');
          const filePath = join(assetRoot, url.pathname.replace(/^\//, ''));
          try {
            res.writeHead(200);
            res.end(await readFile(filePath));
          } catch {
            res.writeHead(404);
            res.end('missing');
          }
        });
        srv.listen(0, '127.0.0.1', () => {
          const address = srv.address();
          if (!address || typeof address === 'string') throw new Error('bad address');
          resolve({