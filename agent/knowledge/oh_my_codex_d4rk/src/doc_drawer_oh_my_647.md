string;
        scope: "root" | "session";
        state: Record<string, unknown>;
      }
    >();

    for (const ref of refs) {
      const content = await readFile(ref.path, "utf-8");
      let parsedState: Record<string, unknown>;
      try {
        parsedState = JSON.parse(content) as Record<string, unknown>;
      } catch (err) {
        process.stderr.write(`[cli/index] operation failed: ${err}\n`);
        continue;
      }
      states.set(ref.mode, {
        path: ref.path,
        scope: ref.scope,
        state: parsedState,
      });
    }

    const changed = new Set<string>();
    const reported = new Set<string>();