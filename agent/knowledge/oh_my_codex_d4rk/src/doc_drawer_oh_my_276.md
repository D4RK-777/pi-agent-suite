`${MANAGED_MARKER}\n${body.trimEnd()}\n\n${MANUAL_START}\n${manualBody.trim()}\n${MANUAL_END}\n`;
}

export function applyProjectScopePathRewritesToAgentsTemplate(
  content: string,
): string {
  return content.replaceAll("~/.codex", "./.codex");
}

async function readProjectRootTemplate(): Promise<string> {
  const pkgRoot = getPackageRoot();
  const templatePath = join(pkgRoot, "templates", "AGENTS.md");
  return readFile(templatePath, "utf-8");
}