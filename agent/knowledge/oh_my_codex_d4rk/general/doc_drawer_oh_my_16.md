build
      - name: Run Ralph persistence verification matrix
        run: |
          node --test \
            dist/cli/__tests__/session-scoped-runtime.test.js \
            dist/mcp/__tests__/trace-server.test.js \
            dist/hud/__tests__/state.test.js \
            dist/mcp/__tests__/state-server-ralph-phase.test.js \
            dist/ralph/__tests__/persistence.test.js \
            dist/verification/__tests__/ralph-persistence-gate.test.js