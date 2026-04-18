(!hasBypass) {
        normalized.push(arg);
        hasBypass = true;
      }
      continue;
    }

    if (arg === HIGH_REASONING_FLAG) {
      reasoningMode = "high";
      continue;
    }

    if (arg === XHIGH_REASONING_FLAG) {
      reasoningMode = "xhigh";
      continue;
    }

    if (arg === SPARK_FLAG) {
      // Spark model is injected into worker env only (not the leader). Consume flag.
      continue;
    }

    if (arg === MADMAX_SPARK_FLAG) {
      // Bypass applies to leader; spark model goes to workers only. Consume flag.
      wantsBypass = true;
      continue;
    }

    normalized.push(arg);
  }

  if (wantsBypass && !hasBypass) {
    normalized.push(CODEX_BYPASS_FLAG);
  }