δικά ανθεκτικό συντονισμό tmux/worktree, όχι ως τον προεπιλεγμένο τρόπο για να ξεκινήσετε με το OMX.

```bash
omx team 3:executor "fix the failing tests with verification"
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

### Setup, doctor και HUD

Αυτές είναι λειτουργίες διαχείρισης/υποστήριξης:
- `omx setup` εγκαθιστά prompts, skills, ρυθμίσεις και scaffolding AGENTS
- `omx doctor` επαληθεύει την εγκατάσταση όταν κάτι φαίνεται λάθος
- `omx hud --watch` είναι λειτουργία παρακολούθησης/κατάστασης, όχι η κύρια ροή εργασίας του χρήστη

### Explore και sparkshell

- `omx explore --prompt "..."` είναι για αναζήτηση μόνο ανάγνωσης στο repository
- `omx sparkshell <command>` είναι για επιθεώρηση απευθείας από το shell και στοχευμένη επαλήθευση