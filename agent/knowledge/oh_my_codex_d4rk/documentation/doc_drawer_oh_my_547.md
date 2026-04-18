# OMX ↔ mux canonical operation space

This document defines the mux boundary owned by OMX core semantics.

## Canonical operations

| Operation | Purpose |
|---|---|
| `resolve-target` | Convert a logical delivery target into an adapter-specific endpoint. |
| `send-input` | Forward literal input to a resolved target. |
| `capture-tail` | Read a bounded tail of adapter output. |
| `inspect-liveness` | Check whether a target is still alive. |
| `attach` | Attach the operator to a live target. |
| `detach` | Detach the operator from a live target. |

## Target kinds
- `delivery-handle`
- `detached`