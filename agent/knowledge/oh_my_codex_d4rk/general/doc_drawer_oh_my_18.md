Rust
        uses: dtolnay/rust-toolchain@stable
      - run: npm ci
      - run: npm run build:full

  ci-status:
    name: CI Status
    if: always()
    runs-on: ubuntu-latest
    needs: [rustfmt, clippy, lint, typecheck, test, coverage-team-critical, coverage-ts-full, coverage-rust, ralph-persistence-gate, build]
    steps:
      - name: Check required job results
        run: |
          if [[ "${{ needs.rustfmt.result }}" != "success" ]] ||
             [[ "${{ needs.clippy.result }}" != "success" ]] ||
             [[ "${{ needs.lint.result }}" != "success" ]] ||
             [[ "${{ needs.typecheck.result }}" != "success" ]] ||
             [[ "${{ needs.test.result }}" != "success" ]] ||
             [[ "${{ needs.coverage-team-critical.result }}" != "success" ]] ||