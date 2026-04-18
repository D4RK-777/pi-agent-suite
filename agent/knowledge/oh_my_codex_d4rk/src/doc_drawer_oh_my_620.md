iteral = JSON.stringify(`${sessionName}:0.0`);
  const commandLiteral = JSON.stringify(commandText);

  return [
    "const { execFileSync } = require('child_process');",
    `setTimeout(() => {`,
    `try { execFileSync('tmux', ['send-keys', '-t', ${targetLiteral}, '-l', '--', ${commandLiteral}], { stdio: 'ignore' }); } catch {}`,
    `try { execFileSync('tmux', ['send-keys', '-t', ${targetLiteral}, 'C-m'], { stdio: 'ignore' }); } catch {}`,
    `}, ${delay});`,
  ].join("");
}