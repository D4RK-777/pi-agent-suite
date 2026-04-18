', ${targetLiteral}, 'C-m'], { stdio: 'ignore' }); } catch {}`,
    `}, ${delay});`,
  ].join("");
}

function scheduleDetachedWindowsCodexLaunch(
  sessionName: string,
  commandText: string,
): void {
  const child = spawn(
    process.execPath,
    ["-e", buildDetachedWindowsBootstrapScript(sessionName, commandText)],
    {
      detached: true,
      stdio: "ignore",
      windowsHide: true,
    },
  );
  child.unref();
}