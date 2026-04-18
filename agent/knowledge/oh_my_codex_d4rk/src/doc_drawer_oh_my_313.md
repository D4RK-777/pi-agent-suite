case 'edit': {
      const name = args[1];
      assert.ok(name, 'Usage: omx agents edit <name>');
      const path = await editNativeAgent(name, { cwd: process.cwd(), scope });
      console.log(`Edited native agent: ${path}`);
      return;
    }
    case 'remove': {
      const name = args[1];
      assert.ok(name, 'Usage: omx agents remove <name>');
      const path = await removeNativeAgent(name, { cwd: process.cwd(), scope, force });
      console.log(`Removed native agent: ${path}`);
      return;
    }
    default:
      throw new Error(`unknown agents subcommand: ${subcommand}`);
  }
}