];
            fs.appendFileSync(process.env.GITHUB_STEP_SUMMARY, `${lines.join("\n")}\n`);
          '
      - name: Upload team coverage artifact
        uses: actions/upload-artifact@v4
        with:
          name: team-critical-coverage
          path: coverage/team/

  coverage-ts-full:
    name: Coverage Report (TypeScript Full)
    runs-on: ubuntu-latest
    needs: [typecheck]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v6
        with:
          node-version: 20
          cache: npm
      - run: npm ci
      - name: Run full TypeScript coverage report
        run: npm run coverage:ts:full
      - name: Add TypeScript coverage summary to job summary
        run: |
          node -e '
            const fs = require("node:fs");