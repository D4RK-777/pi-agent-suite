ore !== undefined ? { score: parsed.score } : {}),
        exit_code: result.status,
        stdout,
        stderr,
      };
    } catch (error) {
      record = {
        command: contract.sandbox.evaluator.command,
        ran_at,
        status: 'error',
        exit_code: result.status,
        stdout,
        stderr,
        parse_error: error instanceof Error ? error.message : String(error),
      };
    }
  }