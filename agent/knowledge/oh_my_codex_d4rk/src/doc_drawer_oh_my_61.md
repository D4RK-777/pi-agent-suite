or block.';
const EVALUATOR_COMMAND_ERROR = 'sandbox.md frontmatter evaluator.command is required.';
const EVALUATOR_FORMAT_REQUIRED_ERROR = 'sandbox.md frontmatter evaluator.format is required and must be json in autoresearch v1.';
const EVALUATOR_FORMAT_JSON_ERROR = 'sandbox.md frontmatter evaluator.format must be json in autoresearch v1.';

function contractError(message: string): Error {
  return new Error(message);
}