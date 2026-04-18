ncrease header nav spacing"
  ]
}
```

## Pass 5 — Iterate

Fix highest-impact issues and re-verify.

1. **Prioritize fixes** by impact: layout > interactions > spacing > typography > colors.
2. **Apply targeted edits**: Fix only the issues listed in `priority_fixes`. Do not refactor working code.
3. **Re-verify**: Repeat Pass 4.
4. **Loop**: Continue until `overall_verdict` is `pass` OR max **5 iterations** reached.
5. **Final report**: Summarize what was successfully cloned, any remaining differences, and elements that could not be replicated.

</Steps>

<Output_Contract>
After each verification pass, emit a **composite web-clone verdict** JSON: