ll_request.labels
              .map(l => l.name)
              .filter(n => n.startsWith('size/'));

            for (const old of existing) {
              if (old !== label) {
                await github.rest.issues.removeLabel({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: context.issue.number,
                  name: old,
                });
              }
            }

            if (!existing.includes(label)) {
              await github.rest.issues.addLabels({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: context.issue.number,
                labels: [label],
              });
            }