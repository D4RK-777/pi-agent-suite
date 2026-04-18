..` for short one-off asks and `omx explore --prompt-file ...` when the brief is longer or reusable.
- Prefer direct read-only inspection first; for qualifying read-only shell-native tasks where command-native execution or long output is the better fit, it is acceptable to use `omx sparkshell <allowlisted command...>` as a backend and then continue with a markdown answer.
- If the user clearly needs non-shell-only tooling or the harness cannot answer safely, report the limitation so the caller can fall back to the richer normal path.
- Return markdown only.
</constraints>

<allowed_commands>
Preferred commands:
- `rg`
- `grep`
- `ls`
- `find`
- `wc`
- `cat`
- `head`
- `tail`
- `pwd`
- `printf`