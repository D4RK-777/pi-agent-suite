summary.txt
          cargo llvm-cov --workspace --lcov --output-path coverage/rust/omx-explore.lcov

          cargo llvm-cov --manifest-path crates/omx-sparkshell/Cargo.toml --summary-only | tee coverage/rust/omx-sparkshell-summary.txt
          cargo llvm-cov --manifest-path crates/omx-sparkshell/Cargo.toml --lcov --output-path coverage/rust/omx-sparkshell.lcov
      - name: Add Rust coverage summary to job summary
        shell: bash
        run: |
          {
            echo '## Rust Coverage Summary'
            echo ''
            echo '### omx-explore'
            echo '```text'
            cat coverage/rust/omx-explore-summary.txt
            echo '```'
            echo ''
            echo '### omx-sparkshell'
            echo '```text'