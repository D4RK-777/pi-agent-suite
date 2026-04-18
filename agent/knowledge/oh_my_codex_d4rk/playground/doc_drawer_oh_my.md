# Autoresearch Research Showcase

This folder collects **small, reproducible research-style demos** used to showcase `omx autoresearch` on harder optimization problems.

Design goals:
- deterministic or seed-controlled evaluations
- small code footprint
- no large datasets checked into git
- no heavyweight runtime artifacts committed
- evaluator-driven keep/discard loops that are easy to inspect under `.omx/logs/autoresearch/`

## Layout

- `playground/*` — demo code and benchmark logic
- `missions/*` — autoresearch mission contracts used by the showcase
- `scripts/eval-*` — focused evaluator entrypoints
- `scripts/run-autoresearch-showcase.sh` — convenience launcher for the bundled showcase missions