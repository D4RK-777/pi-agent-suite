gs[j]);
      break;
    }
    if (token.startsWith('--') && token.includes('=')) { i++; continue; }
    if (token.startsWith('-') && VALUE_TAKING_FLAGS.has(token)) { i += 2; continue; }
    if (token.startsWith('-')) { i++; continue; }
    words.push(token);
    i++;
  }
  return words.join(' ') || fallbackTask || 'ralph-cli-launch';
}

function buildRalphApprovedContextLines(approvedHint: ApprovedExecutionLaunchHint | null): string[] {
  if (!approvedHint) return [];
  const lines = [
    'Approved planning handoff context:',
    `- approved plan: ${approvedHint.sourcePath}`,
  ];
  if (approvedHint.testSpecPaths.length > 0) {
    lines.push(`- test specs: ${approvedHint.testSpecPaths.join(', ')}`);
  }
  if (approvedHint.deepInterviewSpecPaths.length > 0) {