idence(?: pointers?)?|findings?|issue|operator|report|root cause|summary|user impact|write-?up)\b/i;
const CONTEXTUAL_DECOMPOSITION_CLAUSE = /\b(?:focusing on|focus on|including|covers?|covering|with|while|without|ensuring|suitable for|root cause|user impact|evidence pointers|actionable recommendations)\b/i;
const BULLET_LINE_PATTERN = /^(?:[-*•]|(?:\[\s?[xX]?\]))\s+(.+)$/;
const FILE_REFERENCE_PATTERN = /(?:^|[\s`'"])([A-Za-z0-9_./-]+\.[A-Za-z0-9]+)(?=$|[\s`'",;:])/g;
const CODE_SYMBOL_PATTERN = /[`'][A-Za-z_][A-Za-z0-9_.-]*[`']/g;
const PARALLELIZATION_SIGNAL = /\b(?:acceptance criteria|cross[\s-]cutting|independent|in parallel|separately|verification|verify|tests?|docs?|documentation|benchmarks?|migration|rollout)\b/i;