# oh-my-codex v0.8.3

Released: **2026-03-06**

This is a **focused hotfix release** for the Gemini team-worker path shipped in the `0.8.2` dev release line.

---

## TL;DR

- Fixes Gemini worker startup in team prompt mode by launching workers with `--approval-mode yolo -i "<initial inbox prompt>"` instead of depending on stdin for the first instruction (`#585`).
- Prevents non-Gemini default models such as `gpt-5.3-codex-spark` from being passed through to Gemini workers unless the configured model is explicitly a Gemini model (`#585`).
- Adds targeted runtime and tmux-session regression coverage for the Gemini prompt-launch path (`#585`).
- Includes a small test-only hardening for the notify-fallback watcher so full-suite release validation remains stable under load.

---