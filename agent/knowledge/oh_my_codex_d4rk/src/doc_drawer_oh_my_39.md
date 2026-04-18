omptPath, "utf-8");
    const toml = generateAgentToml(agent, promptContent, { codexHomeOverride });

    if (!dryRun) {
      await writeFile(dst, toml);
    }
    if (verbose) console.log(`  ${name}.toml`);
    count += 1;
  }

  return count;
}