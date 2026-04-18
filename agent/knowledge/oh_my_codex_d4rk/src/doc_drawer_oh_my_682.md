ion"
  omx ralph --model gpt-5 "Refactor state hydration"
  omx ralph -- --task-with-leading-dash
`;

const VALUE_TAKING_FLAGS = new Set(['--model', '--provider', '--config', '-c', '-i', '--images-dir']);
const RALPH_OMX_FLAGS = new Set(['--prd', '--no-deslop']);
const RALPH_APPEND_ENV = 'OMX_RALPH_APPEND_INSTRUCTIONS_FILE';

export function extractRalphTaskDescription(args: readonly string[], fallbackTask?: string): string {
  const words: string[] = [];
  let i = 0;
  while (i < args.length) {
    const token = args[i];
    if (token === '--') {
      for (let j = i + 1; j < args.length; j++) words.push(args[j]);
      break;
    }
    if (token.startsWith('--') && token.includes('=')) { i++; continue; }