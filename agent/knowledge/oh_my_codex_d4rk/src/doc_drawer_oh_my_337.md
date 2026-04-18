t') {
        throw new Error('--keep-policy must be one of: score_improvement, pass_only');
      }
      result.keepPolicy = normalized;
    } else if (arg.startsWith('--slug=')) {
      result.slug = slugifyMissionName(arg.slice('--slug='.length));
    } else if (arg.startsWith('--')) {
      throw new Error(`Unknown init flag: ${arg.split('=')[0]}`);
    }
  }
  return result;
}

export async function runAutoresearchNoviceBridge(
  repoRoot: string,
  seedInputs: AutoresearchSeedInputs = {},
  io: AutoresearchQuestionIO = createQuestionIO(),
): Promise<InitAutoresearchResult> {
  if (!process.stdin.isTTY) {
    throw new Error('Guided setup requires an interactive terminal. Use <mission-dir> or init --topic/--evaluator/--keep-policy/--slug for non-interactive use.');
  }