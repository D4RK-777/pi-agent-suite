en = numberedMatches[i][0].length;
      const contentStart = numberedMatches[i].index! + prefixLen;
      const end = i + 1 < numberedMatches.length ? numberedMatches[i + 1].index! : task.length;
      const text = task.slice(contentStart, end).trim();
      if (text) {
        parts.push({ subject: text.slice(0, 80), description: text });
      }
    }
    if (parts.length >= 2) return { strategy: 'numbered', subtasks: parts };
  }