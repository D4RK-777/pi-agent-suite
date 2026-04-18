than bluff when deeper work is required.",
    "",
    "</model_class_guidance>",
  ].join("\n"),
};

const EXACT_MINI_MODEL_OVERLAY = [
  "<exact_model_guidance>",
  "",
  `This role is executing under the exact ${EXACT_GPT_5_4_MINI_MODEL} model.`,
  "- Use a strict execution order: inspect -> plan -> act -> verify.",
  "- Treat completion criteria as explicit: only report done after the requested work is implemented and fresh verification passes.",
  "- If requirements are ambiguous or a blocker appears, state the blocker plainly and stop guessing until the missing decision is resolved.",
  "- Do not bluff, pad, or invent results; report missing evidence and incomplete work honestly.",
  "",
  "</exact_model_guidance>",
].join("\n");