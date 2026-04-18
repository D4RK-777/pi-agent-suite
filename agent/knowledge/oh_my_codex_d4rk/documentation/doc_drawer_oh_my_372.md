sts__/prompt-guidance-scenarios.test.js \
  dist/hooks/__tests__/prompt-guidance-catalog.test.js
```

If you touch the exact-model `gpt-5.4-mini` composition seam, also run:

```bash
node --test \
  dist/agents/__tests__/native-config.test.js \
  dist/team/__tests__/runtime.test.js \
  dist/team/__tests__/scaling.test.js \
  dist/team/__tests__/worker-bootstrap.test.js
```

For broader prompt or skill changes, prefer the full suite:

```bash
npm test
```

## References

- Implementation issue: [#608](https://github.com/Yeachan-Heo/oh-my-codex/issues/608)
- Documentation issue: [#615](https://github.com/Yeachan-Heo/oh-my-codex/issues/615)
- Rollout summary: `docs/release-notes-0.8.6.md:24-47`
- Guidance schema: `docs/guidance-schema.md`