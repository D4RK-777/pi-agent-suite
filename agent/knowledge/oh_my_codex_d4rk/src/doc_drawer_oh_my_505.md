nt, sdk)`' };
    }
    return { valid: true };
  } catch (error) {
    return {
      valid: false,
      reason: error instanceof Error ? error.message : 'failed to import plugin',
    };
  }
}

export async function hooksCommand(args: string[]): Promise<void> {
  const subcommand = args[0] || 'status';
  switch (subcommand) {
    case 'init':
      await initHooks();
      return;
    case 'status':
      await statusHooks();
      return;
    case 'validate':
      await validateHooks();
      return;
    case 'test':
      await testHooks();
      return;
    case 'help':
    case '--help':
    case '-h':
      console.log(HELP);
      return;
    default:
      throw new Error(`Unknown hooks subcommand: ${subcommand}`);
  }
}