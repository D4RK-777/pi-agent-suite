verbose },
    );
  }
  console.log(`  Config refresh complete (${scopeDirs.codexConfigFile}).\n`);

  // Step 5.5: Verify team CLI interop surface is available.
  console.log("[5.5/8] Verifying Team CLI API interop...");
  const teamToolsCheck = await verifyTeamCliApiInterop(pkgRoot);
  if (teamToolsCheck.ok) {
    console.log("  omx team api command detected (CLI-first interop ready)");
  } else {
    console.log(`  WARNING: ${teamToolsCheck.message}`);
    console.log("  Run `npm run build` and then re-run `omx setup`.");
  }
  console.log();