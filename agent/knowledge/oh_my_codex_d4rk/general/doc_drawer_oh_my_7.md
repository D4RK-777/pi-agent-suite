e smoke command
        if: matrix.lane == 'smoke'
        run: npm run test:team:cross-rebase-smoke
      - name: Run remaining smoke suite
        if: matrix.lane == 'smoke'
        run: |
          node --test \
            dist/cli/__tests__/packaged-script-resolution.test.js \
            dist/cli/__tests__/package-bin-contract.test.js \
            dist/cli/__tests__/explore.test.js \
            dist/cli/__tests__/sparkshell-cli.test.js \
            dist/hooks/__tests__/explore-routing.test.js \
            dist/hooks/__tests__/explore-sparkshell-guidance-contract.test.js \
            dist/scripts/__tests__/smoke-packed-install.test.js \
            dist/verification/__tests__/explore-harness-release-workflow.test.js \
            dist/compat/__tests__/*.test.js