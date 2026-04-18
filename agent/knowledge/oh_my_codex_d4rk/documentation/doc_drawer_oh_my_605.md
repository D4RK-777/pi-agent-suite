/__tests__/state.test.js   dist/team/__tests__/api-interop.test.js
```

Result:
- `428 pass, 0 fail`

## Risks / notes
- This is an intentional CLI behavior break for users still invoking `omx team ralph ...`
- The break is now explicit and easier to understand than the previous silent compatibility path
- Separate Ralph execution remains supported, but it must be initiated intentionally rather than being baked into team runtime semantics