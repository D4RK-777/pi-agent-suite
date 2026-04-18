issue_number: context.issue.number,
                labels: [label],
              });
            }

            core.notice(`PR size: ${total} changes (${additions}+, ${deletions}-) → ${label}`);

  draft-check:
    name: Draft Check
    runs-on: ubuntu-latest
    steps:
      - uses: actions/github-script@v8
        with:
          script: |
            if (context.payload.pull_request.draft) {
              core.notice('This PR is still in draft state.');
            }