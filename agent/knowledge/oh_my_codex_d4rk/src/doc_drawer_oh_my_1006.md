'string' || marker.trim() === '') {
    throw new Error('`marker` must be a non-empty string');
  }

  if (parsed.dry_run !== true && parsed.dry_run !== false) {
    throw new Error('`dry_run` must be boolean');
  }
  if (parsed.log_level !== 'error' && parsed.log_level !== 'info' && parsed.log_level !== 'debug') {
    throw new Error('`log_level` must be one of: error, info, debug');
  }
  if (parsed.skip_if_scrolling !== undefined && parsed.skip_if_scrolling !== true && parsed.skip_if_scrolling !== false) {
    throw new Error('`skip_if_scrolling` must be boolean');
  }