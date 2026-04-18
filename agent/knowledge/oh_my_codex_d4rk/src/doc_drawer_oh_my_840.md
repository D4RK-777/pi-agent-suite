M_API_OPERATION_OPTIONAL_FIELDS[operation] ?? [];
  const sampleInput: Record<string, unknown> = {};

  for (const field of requiredFields) {
    sampleInput[field] = sampleValueForTeamApiField(field);
  }
  const sampleInputJson = JSON.stringify(sampleInput);
  const required = requiredFields.length > 0
    ? requiredFields.map((field) => `  - ${field}`).join('\n')
    : '  (none)';
  const optional = optionalFields.length > 0
    ? `\nOptional input fields:\n${optionalFields.map((field) => `  - ${field}`).join('\n')}\n`
    : '\n';
  const note = TEAM_API_OPERATION_NOTES[operation]
    ? `\nNote:\n  ${TEAM_API_OPERATION_NOTES[operation]}\n`
    : '';

  return `
Usage: omx team api ${operation} --input <json> [--json]