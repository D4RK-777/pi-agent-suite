ror.message : String(error),
          },
        }));
        process.exitCode = 1;
        return;
      }
      throw error;
    }
    const envelope = await executeTeamApiOperation(parsedApi.operation, parsedApi.input, cwd);
    if (parsedApi.json) {
      console.log(JSON.stringify({
        ...jsonBase,
        command: `omx team api ${parsedApi.operation}`,
        ...envelope,
      }));
      if (!envelope.ok) process.exitCode = 1;
      return;
    }
    if (envelope.ok) {
      console.log(`ok operation=${envelope.operation}`);
      console.log(JSON.stringify(envelope.data, null, 2));
      return;
    }
    console.error(`error operation=${envelope.operation} code=${envelope.error.code}: ${envelope.error.message}`);
    process.exitCode = 1;
    return;
  }