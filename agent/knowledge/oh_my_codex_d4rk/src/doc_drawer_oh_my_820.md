/task-size-detector.js';
import { readApprovedExecutionLaunchHint } from '../planning/artifacts.js';
import { routeTaskToRole } from '../team/role-router.js';
import { allocateTasksToWorkers } from '../team/allocation-policy.js';
import {
  buildFollowupStaffingPlan,
  resolveAvailableAgentTypes,
  type FollowupStaffingPlan,
} from '../team/followup-planner.js';
import {
  TEAM_API_OPERATIONS,
  resolveTeamApiOperation,
  executeTeamApiOperation,
  type TeamApiOperation,
} from '../team/api-interop.js';
import { teamReadConfig as readTeamConfig, teamReadTaskApproval as readTaskApproval } from '../team/team-ops.js';
import { recordLeaderRuntimeActivity } from '../team/leader-activity.js';

type TeamWorkerCli = Exclude<WorkerInfo['worker_cli'], undefined>;