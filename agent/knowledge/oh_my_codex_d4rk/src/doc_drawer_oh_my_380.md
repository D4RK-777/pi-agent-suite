un prefers interview|autoresearch split-pane launch inside tmux, with foreground fallback on failure
  - --resume loads the authoritative per-run manifest and continues from the last kept commit
`;

const AUTORESEARCH_APPEND_INSTRUCTIONS_ENV = 'OMX_AUTORESEARCH_APPEND_INSTRUCTIONS_FILE';
const AUTORESEARCH_MAX_CONSECUTIVE_NOOPS = 3;

function buildAutoresearchDeepInterviewAppendix(): string {
  return [
    '<autoresearch_deep_interview_mode>',
    'You are in OMX autoresearch intake mode.',
    'Run the deep-interview skill in autoresearch mode and clarify the research mission before launch.',
    'Do not start tmux, do not launch `omx autoresearch`, and do not bypass the user confirmation boundary.',