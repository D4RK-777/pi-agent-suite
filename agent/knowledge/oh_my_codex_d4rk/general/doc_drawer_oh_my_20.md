cho "  typecheck: ${{ needs.typecheck.result }}"
            echo "  test: ${{ needs.test.result }}"
            echo "  coverage-team-critical: ${{ needs.coverage-team-critical.result }}"
            echo "  coverage-ts-full: ${{ needs.coverage-ts-full.result }}"
            echo "  coverage-rust: ${{ needs.coverage-rust.result }}"
            echo "  ralph-persistence-gate: ${{ needs.ralph-persistence-gate.result }}"
            echo "  build: ${{ needs.build.result }}"
            exit 1
          fi
          echo "All required CI checks passed"