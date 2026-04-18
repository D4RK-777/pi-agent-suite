uildTeamExecutionPlan(task, workerCount, agentType, explicitAgentType, explicitWorkerCount).tasks;
}

const ACTIONABLE_TASK_PREFIX = /^(?:add|analy(?:se|ze)|audit|benchmark|build|clean(?:\s+up)?|create|debug|design|document|draft|fix|implement|improve|investigate|migrate|optimi(?:s|z)e|profile|refactor|repair|research|review|ship|summari(?:s|z)e|test|update|validate|verify|write)\b/i;
const TASK_LABEL_PREFIX = /^(?:task|step|phase|part)\s+[\w-]+(?:\s+[\w-]+)?$/i;
const ANALYSIS_TASK_PREFIX = /^(?:analy(?:se|ze)|audit|assess|evaluate|explore|investigate|research|review|study|summari(?:s|z)e)\b/i;
const ANALYSIS_DELIVERABLE_SIGNAL = /\b(?:actionable recommendations?|evidence(?: pointers?)?|findings?|issue|operator|report|root cause|summary|user impact|write-?up)\b/i;