verage-summary.json", "utf8"));
            const total = summary.total;
            const lines = [
              "## Team/State Coverage Summary",
              "",
              "| Metric | Pct | Covered / Total |",
              "|---|---:|---:|",
              `| Lines | ${total.lines.pct}% | ${total.lines.covered} / ${total.lines.total} |`,
              `| Functions | ${total.functions.pct}% | ${total.functions.covered} / ${total.functions.total} |`,
              `| Branches | ${total.branches.pct}% | ${total.branches.covered} / ${total.branches.total} |`,
              `| Statements | ${total.statements.pct}% | ${total.statements.covered} / ${total.statements.total} |`
            ];
            fs.appendFileSync(process.env.GITHUB_STEP_SUMMARY, `${lines.join("\n")}\n`);