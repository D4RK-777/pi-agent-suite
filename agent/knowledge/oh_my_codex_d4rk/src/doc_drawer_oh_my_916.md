if (workerPanePairs.length > 0) {
    console.log(`worker_panes: ${workerPanePairs.join(' ')}`);
  }

  if (paneStatus.sparkshell_hint) {
    console.log('sparkshell_hint: omx sparkshell --tmux-pane <pane-id> --tail-lines 400');
  }

  if (paneStatus.recommended_inspect_targets.length > 0) {
    console.log(`recommended_inspect_targets: ${paneStatus.recommended_inspect_targets.join(' ')}`);
  }
  for (const [target, reason] of Object.entries(paneStatus.recommended_inspect_reasons)) {
    console.log(`inspect_reason_${target}: ${reason}`);
  }
  for (const [target, workerCli] of Object.entries(paneStatus.recommended_inspect_clis)) {
    if (workerCli) {
      console.log(`inspect_cli_${target}: ${workerCli}`);
    }
  }