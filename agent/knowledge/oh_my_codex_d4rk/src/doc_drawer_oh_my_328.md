: void;
}

function shellQuote(s: string): string {
  return "'" + s.replace(/'/g, "'\\''") + "'";
}

function createQuestionIO(): AutoresearchQuestionIO {
  const rl = createInterface({ input: process.stdin, output: process.stdout });
  return {
    question(prompt: string) {
      return rl.question(prompt);
    },
    close() {
      rl.close();
    },
  };
}

async function promptWithDefault(io: AutoresearchQuestionIO, prompt: string, currentValue?: string): Promise<string> {
  const suffix = currentValue?.trim() ? ` [${currentValue.trim()}]` : '';
  const answer = await io.question(`${prompt}${suffix}\n> `);
  return answer.trim() || currentValue?.trim() || '';
}