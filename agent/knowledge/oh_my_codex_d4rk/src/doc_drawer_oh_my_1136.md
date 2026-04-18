',
          '',
          '',
          '',
          '',
          'launch',
        ]),
      ));

      const draftContent = await readFile(join(repo, '.omx', 'specs', 'deep-interview-autoresearch-seeded-topic.md'), 'utf-8');
      assert.equal(result.slug, 'seeded-topic');
      assert.match(draftContent, /- topic: Seeded topic/);
      assert.match(draftContent, /- evaluator: node scripts\/eval\.js/);
      assert.match(draftContent, /Launch-ready: yes/);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });
});