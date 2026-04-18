name: CI

on:
  push:
    branches: [main, dev, experimental/dev]
  pull_request:
    branches: [main, dev, experimental/dev]

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true

jobs:
  rustfmt:
    name: Rust Format
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Rust
        uses: dtolnay/rust-toolchain@stable
        with:
          components: rustfmt
      - name: Check Rust formatting
        run: cargo fmt --all --check