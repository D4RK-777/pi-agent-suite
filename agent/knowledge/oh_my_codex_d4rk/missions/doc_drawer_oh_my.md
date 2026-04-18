name: PR Check

on:
  pull_request_target:
    types: [opened, synchronize, reopened]

jobs:
  size-label:
    name: PR Size Label
    runs-on: ubuntu-latest
    permissions:
      pull-requests: write
    steps:
      - uses: actions/github-script@v8
        with:
          script: |
            const { additions, deletions } = context.payload.pull_request;
            const total = additions + deletions;

            let label;
            if (total < 50) label = 'size/S';
            else if (total < 200) label = 'size/M';
            else if (total < 500) label = 'size/L';
            else label = 'size/XL';

            const existing = context.payload.pull_request.labels
              .map(l => l.name)
              .filter(n => n.startsWith('size/'));