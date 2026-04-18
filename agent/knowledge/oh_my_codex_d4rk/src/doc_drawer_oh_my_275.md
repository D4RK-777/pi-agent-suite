ion isManagedAgentsInitFile(content: string): boolean {
  return content.includes(MANAGED_MARKER);
}

function extractManualSection(
  existingContent: string | undefined,
  fallbackBody: string,
): string {
  if (!existingContent) return fallbackBody.trim();
  const start = existingContent.indexOf(MANUAL_START);
  const end = existingContent.indexOf(MANUAL_END);
  if (start === -1 || end === -1 || end < start) return fallbackBody.trim();
  return (
    existingContent.slice(start + MANUAL_START.length, end).trim() ||
    fallbackBody.trim()
  );
}

function wrapManagedContent(body: string, manualBody: string): string {
  return `${MANAGED_MARKER}\n${body.trimEnd()}\n\n${MANUAL_START}\n${manualBody.trim()}\n${MANUAL_END}\n`;
}