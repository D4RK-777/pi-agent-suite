ion/__tests__/explore-harness-release-workflow.test.js \
            dist/compat/__tests__/*.test.js

  coverage-team-critical:
    name: Coverage Gate (Team Critical)
    runs-on: ubuntu-latest
    needs: [typecheck]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v6
        with:
          node-version: 20
          cache: npm
      - run: npm ci
      - name: Run team/state coverage gate
        run: npm run coverage:team-critical
      - name: Add coverage summary to job summary
        run: |
          node -e '
            const fs = require("node:fs");
            const summary = JSON.parse(fs.readFileSync("coverage/team/coverage-summary.json", "utf8"));
            const total = summary.total;
            const lines = [