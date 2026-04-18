<p>
              Route workers per pane with <code>OMX_TEAM_WORKER_CLI_MAP</code> (for example:
              <code>codex,codex,claude,claude</code>) so one <code>$team</code> run can use both CLIs.
            </p>
          </article>
          <article class="card">
            <h3>Claude-team leader nudges</h3>
            <p>
              Added a leader-side all-workers-idle fallback so notifications still fire even when worker-side Codex hooks are unavailable.
            </p>
          </article>
          <article class="card">
            <h3>Safer trigger retries</h3>
            <p>
              Team trigger fallback now gates adaptive resend behind a ready prompt and no-active-task check, with safer clear-line resend behavior.
            </p>
          </article>