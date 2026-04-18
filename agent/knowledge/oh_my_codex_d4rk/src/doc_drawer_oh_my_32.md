): string {
  const instructions = stripFrontmatter(promptContent);
  const parts = [instructions];

  if (metadata) {
    parts.push(
      "",
      POSTURE_OVERLAYS[metadata.posture],
      "",
      MODEL_CLASS_OVERLAYS[metadata.modelClass],
    );
  }

  if (isExactMiniModel(resolvedModel)) {
    parts.push("", EXACT_MINI_MODEL_OVERLAY);
  }

  const metadataLines = [];
  if (metadata) {
    metadataLines.push(
      "## OMX Agent Metadata",
      `- role: ${metadata.name}`,
      `- posture: ${metadata.posture}`,
      `- model_class: ${metadata.modelClass}`,
      `- routing_role: ${metadata.routingRole}`,
    );
  }
  if (resolvedModel) {
    if (metadataLines.length === 0) {
      metadataLines.push("## OMX Agent Metadata");
    }