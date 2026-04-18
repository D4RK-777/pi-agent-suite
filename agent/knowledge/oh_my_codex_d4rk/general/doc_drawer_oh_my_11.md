summary to job summary
        run: |
          node -e '
            const fs = require("node:fs");
            const summary = JSON.parse(fs.readFileSync("coverage/ts-full/coverage-summary.json", "utf8"));
            const total = summary.total;
            const lines = [
              "## Full TypeScript Coverage Summary",
              "",
              "| Metric | Pct | Covered / Total |",
              "|---|---:|---:|",
              `| Lines | ${total.lines.pct}% | ${total.lines.covered} / ${total.lines.total} |`,
              `| Functions | ${total.functions.pct}% | ${total.functions.covered} / ${total.functions.total} |`,
              `| Branches | ${total.branches.pct}% | ${total.branches.covered} / ${total.branches.total} |`,