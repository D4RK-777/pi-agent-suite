est is terminal

Successful resume continues from the last kept commit and existing results history.

## Iteration handoff context

Each launched worker session receives a supervisor-written instruction snapshot including:
- current iteration number
- baseline commit
- last kept commit
- last kept score when known
- previous iteration outcome
- bounded recent ledger summary
- keep policy

## Verification targets