d = `${shellQuote(process.execPath)} ${shellQuote(omxPath)} autoresearch ${shellQuote(missionDir)}`;

  execFileSync('tmux', ['new-session', '-d', '-s', sessionName, cmd], { stdio: 'ignore',
      windowsHide: true,
    });

  console.log(`\nAutoresearch launched in background tmux session.`);
  console.log(`  Session:  ${sessionName}`);
  console.log(`  Mission:  ${missionDir}`);
  console.log(`  Attach:   tmux attach -t ${sessionName}`);
}