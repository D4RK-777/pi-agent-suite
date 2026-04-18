romptUpdate } from "./update.js";
import { maybePromptGithubStar } from "./star-prompt.js";
import {
  generateOverlay,
  removeSessionModelInstructionsFile,
  resolveSessionOrchestrationMode,
  sessionModelInstructionsPath,
  writeSessionModelInstructionsFile,
} from "../hooks/agents-overlay.js";
import {
  readSessionState,
  writeSessionStart,
  writeSessionEnd,
  resetSessionMetrics,
} from "../hooks/session.js";
import {
  buildClientAttachedReconcileHookName,
  buildReconcileHudResizeArgs,
  buildRegisterClientAttachedReconcileArgs,
  buildRegisterResizeHookArgs,
  buildResizeHookName,
  buildResizeHookTarget,
  buildScheduleDelayedHudResizeArgs,
  buildUnregisterClientAttachedReconcileArgs,
  buildUnregisterResizeHookArgs,
  enableMouseScrolling,
  isNativeWindows,