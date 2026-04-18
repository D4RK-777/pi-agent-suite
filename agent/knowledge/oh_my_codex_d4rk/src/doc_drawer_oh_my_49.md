"standard",
      routingRole: "executor",
      tools: "analysis",
      category: "build",
    };

    const prompt = "Instruction line";
    const exactMiniToml = generateAgentToml(agent, prompt, {
      env: { OMX_DEFAULT_STANDARD_MODEL: "gpt-5.4-mini" } as NodeJS.ProcessEnv,
    });
    const frontierToml = generateAgentToml(agent, prompt, {
      env: { OMX_DEFAULT_STANDARD_MODEL: "gpt-5.4" } as NodeJS.ProcessEnv,
    });
    const tunedToml = generateAgentToml(agent, prompt, {
      env: { OMX_DEFAULT_STANDARD_MODEL: "gpt-5.4-mini-tuned" } as NodeJS.ProcessEnv,
    });