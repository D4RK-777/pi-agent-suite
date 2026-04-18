n: number;
  catalogVersion: string;
  skills: CatalogSkillEntry[];
  agents: CatalogAgentEntry[];
}

const SKILL_CATEGORIES = new Set<CatalogSkillCategory>(['execution', 'planning', 'shortcut', 'utility']);
const AGENT_CATEGORIES = new Set<CatalogAgentCategory>(['build', 'review', 'domain', 'product', 'coordination']);
const ENTRY_STATUSES = new Set<CatalogEntryStatus>(['active', 'alias', 'merged', 'deprecated', 'internal']);
const REQUIRED_CORE_SKILLS = new Set(['ralplan', 'team', 'ralph', 'ultrawork', 'autopilot']);

function isObject(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}