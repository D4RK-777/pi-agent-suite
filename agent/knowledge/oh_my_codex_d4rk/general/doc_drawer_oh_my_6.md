cache: npm
      - run: npm ci
      - run: npx tsc --noEmit
      - run: npm run check:no-unused

  test:
    name: Test (Node ${{ matrix.node-version }} / ${{ matrix.lane }})
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        include:
          - node-version: 20
            lane: full
          - node-version: 22
            lane: smoke
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v6
        with:
          node-version: ${{ matrix.node-version }}
          cache: npm
      - run: npm ci
      - name: Run full suite
        if: matrix.lane == 'full'
        run: npm test
      - name: Run cross-rebase smoke command
        if: matrix.lane == 'smoke'
        run: npm run test:team:cross-rebase-smoke