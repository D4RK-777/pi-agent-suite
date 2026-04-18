sage: stderr !== '' ? `probe failed - ${stderr}` : `probe failed with exit ${result.status}`,
  };
}

function checkNodeVersion(): Check {
  const major = parseInt(process.versions.node.split('.')[0] ?? '0', 10);
  if (isNaN(major)) {
    return { name: 'Node.js', status: 'fail', message: `v${process.versions.node} (unable to parse major version)` };
  }
  if (major >= 20) {
    return { name: 'Node.js', status: 'pass', message: `v${process.versions.node}` };
  }
  return { name: 'Node.js', status: 'fail', message: `v${process.versions.node} (need >= 20)` };
}