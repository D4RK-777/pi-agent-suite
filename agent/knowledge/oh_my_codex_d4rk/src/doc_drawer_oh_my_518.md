eritableTeamWorkerArgsShared,
  resolveTeamWorkerLaunchArgs,
  resolveTeamLowComplexityDefaultModel,
} from "../team/model-contract.js";
import {
  parseWorktreeMode,
  planWorktreeTarget,
  ensureWorktree,
} from "../team/worktree.js";
import {
  OMX_NOTIFY_TEMP_CONTRACT_ENV,
  parseNotifyTempContractFromArgs,
  serializeNotifyTempContract,
  type NotifyTempContract,
  type ParseNotifyTempContractResult,
} from "../notifications/temp-contract.js";

export function resolveNotifyFallbackWatcherScript(pkgRoot = getPackageRoot()): string {
  return join(pkgRoot, "dist", "scripts", "notify-fallback-watcher.js");
}

export function resolveHookDerivedWatcherScript(pkgRoot = getPackageRoot()): string {
  return join(pkgRoot, "dist", "scripts", "hook-derived-watcher.js");
}