elClass,
          routingRole: agent.routingRole,
        }
      : null,
    resolvedModel,
  );
}

/**
 * Strip YAML frontmatter (between --- markers) from markdown content.
 */
export function stripFrontmatter(content: string): string {
  const match = content.match(/^---\r?\n[\s\S]*?\r?\n---\r?\n?/);
  if (match) {
    return content.slice(match[0].length).trim();
  }
  return content.trim();
}

/**
 * Escape content for TOML triple-quoted strings.
 * TOML """ strings only need to escape sequences of 3+ consecutive quotes.
 */
function escapeTomlMultiline(s: string): string {
  return s.replace(/"{3,}/g, (match) => match.split("").join("\\"));
}

function escapeTomlBasicString(s: string): string {
  return s.replace(/\\/g, "\\\\").replace(/"/g, '\\"');
}