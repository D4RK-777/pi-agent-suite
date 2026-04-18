-autoresearch-showcase.sh --list

# run one showcase
./scripts/run-autoresearch-showcase.sh bayesopt

# run several showcases back-to-back
./scripts/run-autoresearch-showcase.sh omx-self ml-tabular bayesopt
```

See `playground/README.md` for the mission index, completed-result summaries, and repository-hygiene guidance.

## Demo Script Reference

### `scripts/demo-team-e2e.sh`

The bundled E2E demo script provides a complete, automated test of the tmux claude workers demo with comprehensive coverage of all major features.

#### Script Features