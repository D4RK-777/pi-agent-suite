3:executor "execute the approved plan in parallel"</code> based on execution style.</li>
      </ol>

      <h2>Prompt Instruction Source</h2>
      <p>OMX layers project instructions by default (extends Codex behavior, does not replace/bypass Codex core system policies):</p>
      <pre><code>-c model_instructions_file="&lt;cwd&gt;/AGENTS.md"</code></pre>
      <p>Override behavior when needed:</p>
      <pre><code>OMX_BYPASS_DEFAULT_SYSTEM_PROMPT=0 omx
OMX_MODEL_INSTRUCTIONS_FILE=/path/to/instructions.md omx</code></pre>