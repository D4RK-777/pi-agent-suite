# Secrets Patterns

Use this file when secret findings need fast interpretation before escalating into deeper security
work.

## Strong Secret Signals

- cloud access keys
- PATs and CI tokens
- webhook secrets
- private keys
- database URLs with embedded credentials
- plaintext passwords or API keys in committed files

## Common False Positives

- placeholder examples
- environment-variable reads
- docs showing fake sample keys
- commented-out examples

## Rule

Treat secret findings as high priority until proved otherwise.

If a value looks real and could still be active, rotate first and clean the repo second.
