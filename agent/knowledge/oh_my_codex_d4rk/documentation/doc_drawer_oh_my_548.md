etach` | Detach the operator from a live target. |

## Target kinds
- `delivery-handle`
- `detached`

## Transport primitives
- `SubmitPolicy` controls how many isolated `C-m` submissions the adapter emits.
- `InputEnvelope` holds literal text plus newline-normalization rules.
- `InjectionPreflight` captures readiness checks before delivery.
- `PaneReadinessReason` explains why a target is or is not injectable.
- `DeliveryConfirmation` records whether a send was confirmed, active-task confirmed, or left unconfirmed.
- `ConfirmationPolicy` defines the retry/verification window used by the adapter.