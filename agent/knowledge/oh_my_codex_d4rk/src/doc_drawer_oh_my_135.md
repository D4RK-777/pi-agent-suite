ch candidate artifact base_commit is required');
  }
  if (typeof record.description !== 'string') {
    throw new Error('autoresearch candidate artifact description is required');
  }
  if (!Array.isArray(record.notes) || record.notes.some((note) => typeof note !== 'string')) {
    throw new Error('autoresearch candidate artifact notes must be a string array');
  }
  if (typeof record.created_at !== 'string' || !record.created_at.trim()) {
    throw new Error('autoresearch candidate artifact created_at is required');
  }
  return {
    status,
    candidate_commit: record.candidate_commit,
    base_commit: record.base_commit,
    description: record.description,
    notes: record.notes,
    created_at: record.created_at,
  };
}