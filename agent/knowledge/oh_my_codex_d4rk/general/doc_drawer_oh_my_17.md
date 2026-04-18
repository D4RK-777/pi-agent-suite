tests__/persistence.test.js \
            dist/verification/__tests__/ralph-persistence-gate.test.js

  build:
    name: Build (Full Source Build)
    runs-on: ubuntu-latest
    needs: [rustfmt, clippy, lint, typecheck, test, ralph-persistence-gate]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v6
        with:
          node-version: 20
          cache: npm
      - name: Setup Rust
        uses: dtolnay/rust-toolchain@stable
      - run: npm ci
      - run: npm run build:full