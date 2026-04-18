ne shared skill root/,
      );
      assert.doesNotMatch(res.stdout, /\[!!\] Legacy skill roots:/);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });
});