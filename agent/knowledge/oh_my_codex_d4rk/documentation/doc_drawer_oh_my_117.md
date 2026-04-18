NTS.md`, quando sobrescrito) com o `./AGENTS.md` do projeto e depois adicionam o overlay de runtime.
- Arquivos `AGENTS.md` existentes nunca são sobrescritos silenciosamente: em TTY interativo o setup pergunta antes de substituir; em modo não interativo a substituição é ignorada, a menos que você use `--force` (verificações de segurança de sessões ativas continuam valendo).
- Atualizações do `config.toml` (para ambos os escopos):
  - `notify = ["node", "..."]`
  - `model_reasoning_effort = "high"`
  - `developer_instructions = "..."`
  - `[features] multi_agent = true, child_agents_md = true`
  - Entradas de servidores MCP (`omx_state`, `omx_memory`, `omx_code_intel`, `omx_trace`)
  - `[tui] status_line`
- `AGENTS.md` específico do escopo