/ Ignore malformed persisted scope and fall back to user prompts.
  }

  return codexPromptsDir();
}

async function resolveAgentPromptContent(
  role: string,
  promptsDir: string,
): Promise<string> {
  const normalizedRole = role.trim().toLowerCase();
  if (!SAFE_ROLE_PATTERN.test(normalizedRole)) {
    throw new Error(`[ask] invalid --agent-prompt role "${role}". Expected lowercase role names like "executor" or "test-engineer".`);
  }

  if (!existsSync(promptsDir)) {
    throw new Error(`[ask] prompts directory not found: ${promptsDir}. Run "omx setup" to install prompts.`);
  }