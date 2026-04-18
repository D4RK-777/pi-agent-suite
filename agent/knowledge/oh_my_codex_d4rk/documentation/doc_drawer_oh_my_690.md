val.
   - Terminal success sets `active=false`, `current_phase=complete`, and writes `completed_at`.

4. **Cancellation semantics**
   - Cancellation is treated as lifecycle terminalization, not silent deletion.
   - Linked cleanup is expected (`ralph` + linked execution mode cleanup via cancel workflow).

## Audit notes

- This baseline is commit-pinned. Any parity update MUST reference a new commit SHA and hash.
- The parity mapping for each rule is tracked in `docs/reference/ralph-parity-matrix.md`.