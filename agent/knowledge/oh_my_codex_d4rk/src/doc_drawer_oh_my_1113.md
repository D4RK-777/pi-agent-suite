nore' });
  execFileSync('git', ['commit', '-m', 'init'], { cwd, stdio: 'ignore' });
  return cwd;
}

function withMockedTty<T>(fn: () => Promise<T>): Promise<T> {
  const descriptor = Object.getOwnPropertyDescriptor(process.stdin, 'isTTY');
  Object.defineProperty(process.stdin, 'isTTY', { configurable: true, value: true });
  return fn().finally(() => {
    if (descriptor) {
      Object.defineProperty(process.stdin, 'isTTY', descriptor);
    } else {
      Object.defineProperty(process.stdin, 'isTTY', { configurable: true, value: false });
    }
  });
}

function makeFakeIo(answers: string[]): AutoresearchQuestionIO {
  const queue = [...answers];
  return {
    async question(): Promise<string> {
      return queue.shift() ?? '';
    },
    close(): void {},
  };
}