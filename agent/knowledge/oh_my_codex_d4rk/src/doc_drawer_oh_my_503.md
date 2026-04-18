e plugin exports/signatures
  omx hooks test       Dispatch synthetic turn-complete event to plugins

Notes:
  - This command is additive. Existing \`omx tmux-hook\` behavior is unchanged.
  - Plugins are enabled by default. Disable with OMX_HOOK_PLUGINS=0.
`;

const SAMPLE_PLUGIN = `export async function onHookEvent(event, sdk) {
  if (event.event !== 'turn-complete') return;

  const current = Number((await sdk.state.read('sample-seen-count')) ?? 0);
  const next = Number.isFinite(current) ? current + 1 : 1;
  await sdk.state.write('sample-seen-count', next);

  await sdk.log.info('sample-plugin observed turn-complete', {
    turn_id: event.turn_id,
    seen_count: next,
  });
}
`;

function hooksDir(cwd = process.cwd()): string {
  return join(cwd, '.omx', 'hooks');
}