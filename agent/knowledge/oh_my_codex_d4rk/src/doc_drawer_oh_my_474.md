atus: 'warn',
      message: `not found in ${userAgentsMd} (run omx setup --scope user)`,
    };
  }

  const projectAgentsMd = join(process.cwd(), 'AGENTS.md');
  if (existsSync(projectAgentsMd)) {
    return { name: 'AGENTS.md', status: 'pass', message: 'found in project root' };
  }
  return {
    name: 'AGENTS.md',
    status: 'warn',
    message: 'not found in project root (run omx agents-init . or omx setup --scope project)',
  };
}