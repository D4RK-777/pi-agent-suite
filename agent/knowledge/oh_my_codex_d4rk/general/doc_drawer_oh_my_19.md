" != "success" ]] ||
             [[ "${{ needs.coverage-team-critical.result }}" != "success" ]] ||
             [[ "${{ needs.coverage-ts-full.result }}" != "success" ]] ||
             [[ "${{ needs.coverage-rust.result }}" != "success" ]] ||
             [[ "${{ needs.ralph-persistence-gate.result }}" != "success" ]] ||
             [[ "${{ needs.build.result }}" != "success" ]]; then
            echo "::error::One or more required CI jobs failed"
            echo "  rustfmt: ${{ needs.rustfmt.result }}"
            echo "  clippy: ${{ needs.clippy.result }}"
            echo "  lint: ${{ needs.lint.result }}"
            echo "  typecheck: ${{ needs.typecheck.result }}"
            echo "  test: ${{ needs.test.result }}"