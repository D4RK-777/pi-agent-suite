export type CatalogSkillCategory = 'execution' | 'planning' | 'shortcut' | 'utility';
export type CatalogAgentCategory = 'build' | 'review' | 'domain' | 'product' | 'coordination';
export type CatalogEntryStatus = 'active' | 'alias' | 'merged' | 'deprecated' | 'internal';

export interface CatalogSkillEntry {
  name: string;
  category: CatalogSkillCategory;
  status: CatalogEntryStatus;
  canonical?: string;
  core?: boolean;
  internalRequired?: boolean;
}

export interface CatalogAgentEntry {
  name: string;
  category: CatalogAgentCategory;
  status: CatalogEntryStatus;
  canonical?: string;
}

export interface CatalogManifest {
  schemaVersion: number;
  catalogVersion: string;
  skills: CatalogSkillEntry[];
  agents: CatalogAgentEntry[];
}