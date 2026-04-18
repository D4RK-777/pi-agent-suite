ct_clis)) {
    if (workerCli) {
      console.log(`inspect_cli_${target}: ${workerCli}`);
    }
  }
  for (const [target, role] of Object.entries(paneStatus.recommended_inspect_roles)) {
    if (role) {
      console.log(`inspect_role_${target}: ${role}`);
    }
  }
  for (const [target, index] of Object.entries(paneStatus.recommended_inspect_indexes)) {
    if (typeof index === 'number') {
      console.log(`inspect_index_${target}: ${index}`);
    }
  }
  for (const [target, alive] of Object.entries(paneStatus.recommended_inspect_alive)) {
    if (typeof alive === 'boolean') {
      console.log(`inspect_alive_${target}: ${alive}`);
    }
  }
  for (const [target, turnCount] of Object.entries(paneStatus.recommended_inspect_turn_counts)) {
    if (typeof turnCount === 'number') {