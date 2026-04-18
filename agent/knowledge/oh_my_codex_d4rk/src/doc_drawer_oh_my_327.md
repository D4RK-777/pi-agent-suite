take.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

export interface InitAutoresearchOptions {
  topic: string;
  evaluatorCommand: string;
  keepPolicy: AutoresearchKeepPolicy;
  slug: string;
  repoRoot: string;
}

export interface InitAutoresearchResult {
  missionDir: string;
  slug: string;
}

export interface AutoresearchQuestionIO {
  question(prompt: string): Promise<string>;
  close(): void;
}

function shellQuote(s: string): string {
  return "'" + s.replace(/'/g, "'\\''") + "'";
}