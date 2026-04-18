nded_inspect_commands.entries()) {
    console.log(`inspect_priority_${index + 1}: ${command}`);
  }
  for (const [index, item] of paneStatus.recommended_inspect_items.entries()) {
    const panePart = item.pane_id ? ` pane=${item.pane_id}` : '';
    const cliPart = item.worker_cli ? ` cli=${item.worker_cli}` : '';
    const rolePart = item.role ? ` role=${item.role}` : '';
    const indexPart = typeof item.index === 'number' ? ` index=${item.index}` : '';
    const alivePart = typeof item.alive === 'boolean' ? ` alive=${item.alive}` : '';
    const turnCountPart = typeof item.turn_count === 'number' ? ` turn_count=${item.turn_count}` : '';
    const turnsWithoutProgressPart = typeof item.turns_without_progress === 'number'
      ? ` turns_without_progress=${item.turns_without_progress}`