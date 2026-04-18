import { existsSync } from 'fs';
import { mkdir, readFile, writeFile } from 'fs/promises';
import { join } from 'path';
import { pathToFileURL } from 'url';
import { buildHookEvent } from '../hooks/extensibility/events.js';
import { dispatchHookEvent } from '../hooks/extensibility/dispatcher.js';
import { discoverHookPlugins, isHookPluginsEnabled } from '../hooks/extensibility/loader.js';
import type { HookPluginDescriptor } from '../hooks/extensibility/types.js';

const HELP = `
Usage:
  omx hooks init       Create .omx/hooks/sample-plugin.mjs scaffold
  omx hooks status     Show plugin directory + discovered plugins
  omx hooks validate   Validate plugin exports/signatures
  omx hooks test       Dispatch synthetic turn-complete event to plugins