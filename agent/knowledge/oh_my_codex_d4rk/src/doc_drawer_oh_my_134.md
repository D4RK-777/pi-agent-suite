isArray(parsed)) {
    throw new Error('autoresearch candidate artifact must be a JSON object');
  }
  const record = parsed as Record<string, unknown>;
  const status = record.status;
  if (status !== 'candidate' && status !== 'noop' && status !== 'abort' && status !== 'interrupted') {
    throw new Error('autoresearch candidate artifact status must be candidate|noop|abort|interrupted');
  }
  if (record.candidate_commit !== null && typeof record.candidate_commit !== 'string') {
    throw new Error('autoresearch candidate artifact candidate_commit must be string|null');
  }
  if (typeof record.base_commit !== 'string' || !record.base_commit.trim()) {
    throw new Error('autoresearch candidate artifact base_commit is required');
  }
  if (typeof record.description !== 'string') {