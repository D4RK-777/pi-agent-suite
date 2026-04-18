tool (omx) for setup, diagnostics, and management
 * - Notification hooks for workflow tracking
 */

export { setup } from './cli/setup.js';
export { doctor } from './cli/doctor.js';
export { version } from './cli/version.js';
export { mergeConfig } from './config/generator.js';
export { AGENT_DEFINITIONS, type AgentDefinition } from './agents/definitions.js';
export { generateAgentToml, installNativeAgentConfigs } from './agents/native-config.js';
export { hudCommand } from './hud/index.js';