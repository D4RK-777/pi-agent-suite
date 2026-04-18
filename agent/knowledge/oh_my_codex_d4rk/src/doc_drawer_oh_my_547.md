await import("./doctor.js");
        await doctor(options);
        break;
      }
      case "ask":
        await askCommand(args.slice(1));
        break;
      case "cleanup":
        await cleanupCommand(args.slice(1));
        break;
      case "autoresearch":
        await autoresearchCommand(args.slice(1));
        break;
      case "explore":
        await exploreCommand(args.slice(1));
        break;
      case "exec":
        await execWithOverlay(launchArgs);
        break;
      case "sparkshell":
        await sparkshellCommand(args.slice(1));
        break;
      case "team":
        await teamCommand(args.slice(1), options);
        break;
      case "session":
        await sessionCommand(args.slice(1));
        break;
      case "ralph":