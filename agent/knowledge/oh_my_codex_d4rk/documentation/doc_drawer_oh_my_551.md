) |
| `Attach` | `tmux attach-session -t <target>` |
| `Detach` | `tmux detach-client -t <target>` |

Target handles use the format `session_name:window_index.pane_index` (e.g. `"omx:0.1"`). `MuxTarget::Detached` is rejected for all operations that require a real pane.