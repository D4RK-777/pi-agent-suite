scope: resolveSetupScopeArg(args.slice(1)),
        });
        break;
      case "agents":
        await agentsCommand(args.slice(1));
        break;
      case "agents-init":
        await agentsInitCommand(args.slice(1));
        break;
      case "deepinit":
        await agentsInitCommand(args.slice(1));
        break;
      case "uninstall":
        await uninstall({
          dryRun: options.dryRun,
          keepConfig: flags.has("--keep-config"),
          verbose: options.verbose,
          purge: flags.has("--purge"),
          scope: resolveSetupScopeArg(args.slice(1)),
        });
        break;
      case "doctor": {
        const { doctor } = await import("./doctor.js");
        await doctor(options);
        break;
      }
      case "ask":