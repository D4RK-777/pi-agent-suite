`| Branches | ${total.branches.pct}% | ${total.branches.covered} / ${total.branches.total} |`,
              `| Statements | ${total.statements.pct}% | ${total.statements.covered} / ${total.statements.total} |`
            ];
            fs.appendFileSync(process.env.GITHUB_STEP_SUMMARY, `${lines.join("\n")}\n`);
          '
      - name: Upload full TypeScript coverage artifact
        uses: actions/upload-artifact@v4
        with:
          name: ts-full-coverage
          path: coverage/ts-full/