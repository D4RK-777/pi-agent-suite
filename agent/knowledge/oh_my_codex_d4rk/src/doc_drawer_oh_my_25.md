rker role.",
    "- Keep responses concise, scope-aware, and conservative under ambiguity.",
    "",
    "</posture_overlay>",
  ].join("\n"),
};

const MODEL_CLASS_OVERLAYS: Record<AgentDefinition["modelClass"], string> = {
  frontier: [
    "<model_class_guidance>",
    "",
    "This role is tuned for frontier-class models.",
    "- Use the model's steerability for coordination, tradeoff reasoning, and precise delegation.",
    "- Favor clean routing decisions over impulsive implementation.",
    "",
    "</model_class_guidance>",
  ].join("\n"),
  standard: [
    "<model_class_guidance>",
    "",
    "This role is tuned for standard-capability models.",
    "- Balance autonomy with clear boundaries.",