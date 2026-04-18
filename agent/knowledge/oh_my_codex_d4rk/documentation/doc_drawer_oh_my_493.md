his keeps npm installs simple for users while still shipping verified cross-platform native helpers.

### Native release assets are now first-class

`0.9.0` also upgrades OMX's release shape so the new native surfaces are publishable and consumable across platforms.

This release:
- unifies cross-platform native publishing for `omx-explore-harness` and `omx-sparkshell`
- generates a native release manifest with per-target metadata and checksums
- adds packed-install smoke verification to the release workflow
- validates `build:full` directly in CI
- keeps runtime fallback order explicit across env overrides, hydrated cache, packaged artifacts, and repo-local builds