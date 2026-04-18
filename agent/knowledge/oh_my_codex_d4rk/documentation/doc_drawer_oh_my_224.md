SS_DEFAULT_SYSTEM_PROMPT=0 omx
OMX_MODEL_INSTRUCTIONS_FILE=/path/to/instructions.md omx</code></pre>

      <h2>Troubleshooting</h2>
      <table>
        <thead><tr><th>Issue</th><th>What to check</th></tr></thead>
        <tbody>
          <tr><td><code>omx</code> command not found</td><td>Re-run global install and ensure npm global bin is in PATH.</td></tr>
          <tr><td>Prompts not available</td><td>Confirm files exist in <code>~/.codex/prompts/</code> and re-run <code>omx setup</code>.</td></tr>
          <tr><td>Skills not loading</td><td>Verify <code>~/.codex/skills/*/SKILL.md</code> files were installed.</td></tr>
          <tr><td>Doctor reports config issues</td><td>Run <code>omx doctor</code> and apply the suggested fixes.</td></tr>
        </tbody>
      </table>