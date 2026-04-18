/upload-artifact@v4
        with:
          name: ts-full-coverage
          path: coverage/ts-full/

  coverage-rust:
    name: Coverage Report (Rust)
    runs-on: ubuntu-latest
    needs: [lint]
    steps:
      - uses: actions/checkout@v4
      - name: Setup Rust
        uses: dtolnay/rust-toolchain@stable
        with:
          components: llvm-tools-preview
      - name: Install cargo-llvm-cov
        uses: taiki-e/install-action@cargo-llvm-cov
      - name: Generate Rust coverage reports
        shell: bash
        run: |
          mkdir -p coverage/rust

          cargo llvm-cov --workspace --summary-only | tee coverage/rust/omx-explore-summary.txt
          cargo llvm-cov --workspace --lcov --output-path coverage/rust/omx-explore.lcov