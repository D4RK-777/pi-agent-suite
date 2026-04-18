lete

## Evidence strength hierarchy

Treat evidence as ranked, not flat. From strongest to weakest:

1. **Controlled reproductions / direct experiments / uniquely discriminating artifacts**
2. **Primary source artifacts with tight provenance** (trace events, logs, metrics, configs, git history, file:line behavior)
3. **Multiple independent sources converging on the same explanation**
4. **Single-source code-path or behavioral inference**
5. **Weak circumstantial clues** (timing, naming, stack order, resemblance to prior bugs)
6. **Intuition / analogy / speculation**

Explicitly down-rank hypotheses that depend mostly on lower tiers when stronger contradictory evidence exists.

## Strong falsification rules

Every serious investigation must try to falsify its own favorite explanation.