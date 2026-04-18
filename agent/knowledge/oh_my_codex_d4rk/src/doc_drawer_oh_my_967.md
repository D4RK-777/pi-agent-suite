t });
      }
    }
    if (parts.length >= 2) return { strategy: 'numbered', subtasks: parts };
  }

  const bulletParts = task
    .split(/\r?\n+/)
    .map((line) => line.trim())
    .map((line) => line.match(BULLET_LINE_PATTERN)?.[1]?.trim() ?? '')
    .filter((line) => line.length > 0);
  if (bulletParts.length >= 2) {
    return {
      strategy: 'bulleted',
      subtasks: bulletParts.map((part) => ({ subject: part.slice(0, 80), description: part })),
    };
  }

  const strongParts = task.split(/;\s+/).map(s => s.trim()).filter(s => s.length > 0);
  if (strongParts.length >= 2) {
    return {
      strategy: 'conjunction',
      subtasks: strongParts.map((part) => ({ subject: part.slice(0, 80), description: part })),
    };
  }