rom '../utils/package.js';
import { getDefaultBridge, isBridgeEnabled } from '../runtime/bridge.js';
import { OMX_EXPLORE_CMD_ENV, isExploreCommandRoutingEnabled } from '../hooks/explore-routing.js';
import { isLeaderRuntimeStale } from '../team/leader-activity.js';

interface DoctorOptions {
  verbose?: boolean;
  force?: boolean;
  dryRun?: boolean;
  team?: boolean;
}

interface Check {
  name: string;
  status: 'pass' | 'warn' | 'fail';
  message: string;
}

type DoctorSetupScope = 'user' | 'project';

interface DoctorScopeResolution {
  scope: DoctorSetupScope;
  source: 'persisted' | 'default';
}

interface DoctorPaths {
  codexHomeDir: string;
  configPath: string;
  promptsDir: string;
  skillsDir: string;
  stateDir: string;
}