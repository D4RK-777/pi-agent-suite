ntAttachedReconcileArgs,
  buildUnregisterResizeHookArgs,
  enableMouseScrolling,
  isNativeWindows,
  isTmuxAvailable,
} from "../team/tmux-session.js";
import { getPackageRoot } from "../utils/package.js";
import { codexConfigPath } from "../utils/paths.js";
import { repairConfigIfNeeded } from "../config/generator.js";
import { HUD_TMUX_HEIGHT_LINES } from "../hud/constants.js";
import {
  classifySpawnError,
  spawnPlatformCommandSync,
} from "../utils/platform-command.js";
import { buildHookEvent } from "../hooks/extensibility/events.js";
import { dispatchHookEvent } from "../hooks/extensibility/dispatcher.js";
import {
  collectInheritableTeamWorkerArgs as collectInheritableTeamWorkerArgsShared,
  resolveTeamWorkerLaunchArgs,
  resolveTeamLowComplexityDefaultModel,