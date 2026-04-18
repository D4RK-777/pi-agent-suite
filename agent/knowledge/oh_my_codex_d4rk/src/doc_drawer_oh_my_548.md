case "session":
        await sessionCommand(args.slice(1));
        break;
      case "ralph":
        await ralphCommand(args.slice(1));
        break;
      case "version":
        version();
        break;
      case "hud":
        await hudCommand(args.slice(1));
        break;
      case "tmux-hook":
        await tmuxHookCommand(args.slice(1));
        break;
      case "hooks":
        await hooksCommand(args.slice(1));
        break;
      case "status":
        await showStatus();
        break;
      case "cancel":
        await cancelModes();
        break;
      case "reasoning":
        await reasoningCommand(args.slice(1));
        break;
      case "help":
      case "--help":
      case "-h":
        console.log(HELP);
        break;
      default:
        if (