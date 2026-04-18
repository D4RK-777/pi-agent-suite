thering, keep using those tools until the git recommendation is grounded.
</ask_gate>
</constraints>

<explore>
1) Detect commit style: `git log -30 --pretty=format:"%s"`. Identify language and format (feat:/fix: semantic vs plain vs short).
2) Analyze changes: `git status`, `git diff --stat`. Map which files belong to which logical concern.
3) Split by concern: different directories/modules = SPLIT, different component types = SPLIT, independently revertable = SPLIT.
4) Create atomic commits in dependency order, matching detected style.
5) Verify: show git log output as evidence.
</explore>