|| args.includes('--help') || args.includes('-h')) {
    console.log(AGENTS_USAGE);
    return;
  }

  const subcommand = args[0];
  const scope = parseScopeArg(args.slice(1));
  const force = args.includes('--force');

  switch (subcommand) {
    case 'list': {
      const agents = await listNativeAgents(process.cwd(), scope);
      printAgentsTable(agents);
      return;
    }
    case 'add': {
      const name = args[1];
      assert.ok(name, 'Usage: omx agents add <name>');
      const path = await addNativeAgent(name, { cwd: process.cwd(), scope, force });
      console.log(`Created native agent: ${path}`);
      return;
    }
    case 'edit': {
      const name = args[1];
      assert.ok(name, 'Usage: omx agents edit <name>');