components: rustfmt
      - name: Check Rust formatting
        run: cargo fmt --all --check

  clippy:
    name: Rust Clippy
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Rust
        uses: dtolnay/rust-toolchain@stable
        with:
          components: clippy
      - name: Run clippy
        run: cargo clippy --workspace --all-targets -- -D warnings

  lint:
    name: Lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v6
        with:
          node-version: 20
          cache: npm
      - run: npm ci
      - run: npm run lint