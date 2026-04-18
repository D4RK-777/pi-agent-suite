ase "--help":
      case "-h":
        console.log(HELP);
        break;
      default:
        if (
          firstArg &&
          firstArg.startsWith("-") &&
          !knownCommands.has(firstArg)
        ) {
          await launchWithHud(args);
          break;
        }
        console.error(`Unknown command: ${command}`);
        console.log(HELP);
        process.exit(1);
    }
  } catch (err) {
    console.error(`Error: ${err instanceof Error ? err.message : err}`);
    process.exit(1);
  }
}