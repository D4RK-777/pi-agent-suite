echo '```'
            echo ''
            echo '### omx-sparkshell'
            echo '```text'
            cat coverage/rust/omx-sparkshell-summary.txt
            echo '```'
          } >> "$GITHUB_STEP_SUMMARY"
      - name: Upload Rust coverage artifact
        uses: actions/upload-artifact@v4
        with:
          name: rust-coverage
          path: coverage/rust/

  ralph-persistence-gate:
    name: Ralph Persistence Gate
    runs-on: ubuntu-latest
    needs: [typecheck]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v6
        with:
          node-version: 20
          cache: npm
      - run: npm ci
      - run: npm run build
      - name: Run Ralph persistence verification matrix
        run: |
          node --test \