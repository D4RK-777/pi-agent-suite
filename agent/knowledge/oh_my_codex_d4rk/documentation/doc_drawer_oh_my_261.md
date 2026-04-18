# Migration Guide: post-v0.4.4 mainline changes

This guide covers migration from **v0.4.4** to the current mainline changes merged after it (including PR #137 and follow-up fixes).

## Who is affected

You are affected if you:

- invoke removed prompts or skills from old notes/scripts,
- depend on pre-consolidation catalog names,
- use `omx setup` and need predictable install scope behavior,
- run `omx team`/tmux workflows and want the latest reliability fixes,
- use notifier output and need verbosity control.

## What changed (high level)