writeHead(404);
          res.end('missing');
        });
        srv.listen(0, '127.0.0.1', () => {
          const address = srv.address();
          if (!address || typeof address === 'string') throw new Error('bad address');
          resolve({
            baseUrl: `http://127.0.0.1:${address.port}`,
            close: () => new Promise<void>((done, reject) => srv.close((err: Error | undefined) => err ? reject(err) : done())),
          });
        });
      });