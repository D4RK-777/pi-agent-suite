">Français</a></li>
        <li><a href="./openclaw-integration.it.md">Italiano</a></li>
      </ul>

      <h2>Architecture</h2>
      <pre><code>User
  -> Codex CLI
     -> AGENTS.md (orchestration brain)
     -> ~/.codex/prompts/*.md (installable active/internal agent prompt catalog)
     -> ~/.codex/skills/*/SKILL.md (skill catalog)
     -> ~/.codex/config.toml (features, notify, MCP)
     -> .omx/ (runtime state, memory, plans, logs)</code></pre>
    </main>

    <footer>
      <div class="container">
        <span class="muted">GitHub: <a href="https://github.com/Yeachan-Heo/oh-my-codex">Yeachan-Heo/oh-my-codex</a></span>
      </div>
    </footer>
  </body>
</html>