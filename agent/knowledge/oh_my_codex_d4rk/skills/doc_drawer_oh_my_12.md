y
- `omx sparkshell <command>` είναι για επιθεώρηση απευθείας από το shell και στοχευμένη επαλήθευση

Παραδείγματα:

```bash
omx explore --prompt "find where team state is written"
omx sparkshell git status
omx sparkshell --tmux-pane %12 --tail-lines 400
```

### Σημειώσεις πλατφόρμας για τη λειτουργία team

Η `omx team` χρειάζεται ένα tmux-συμβατό backend:

| Πλατφόρμα | Εγκατάσταση |
| --- | --- |
| macOS | `brew install tmux` |
| Ubuntu/Debian | `sudo apt install tmux` |
| Fedora | `sudo dnf install tmux` |
| Arch | `sudo pacman -S tmux` |
| Windows | `winget install psmux` |
| Windows (WSL2) | `sudo apt install tmux` |

## Γνωστά ζητήματα

### Mac με Intel: υψηλή χρήση CPU `syspolicyd` / `trustd` κατά την εκκίνηση