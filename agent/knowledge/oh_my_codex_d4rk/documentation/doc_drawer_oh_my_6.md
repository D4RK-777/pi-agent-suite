hrichtigungen, MCP)
    -> .omx/ (Laufzeitzustand, Speicher, Pläne, Protokolle)
```

## Hauptbefehle

```bash
omx                # Codex starten (+ HUD in tmux wenn verfügbar)
omx setup          # Prompts/Skills/Config nach Bereich installieren + Projekt-.omx + bereichsspezifische AGENTS.md
omx doctor         # Installations-/Laufzeitdiagnose
omx doctor --team  # Team/Swarm-Diagnose
omx team ...       # tmux-Team-Worker starten/Status/fortsetzen/herunterfahren
omx status         # Aktive Modi anzeigen
omx cancel         # Aktive Ausführungsmodi abbrechen
omx reasoning <mode> # low|medium|high|xhigh
omx tmux-hook ...  # init|status|validate|test
omx hooks ...      # init|status|validate|test (Plugin-Erweiterungs-Workflow)
omx hud ...        # --watch|--json|--preset
omx help
```