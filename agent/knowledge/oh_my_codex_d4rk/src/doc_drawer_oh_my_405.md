import { tryReadCatalogManifest } from '../catalog/reader.js';

export interface CatalogExpectations {
  promptMin: number;
  skillMin: number;
}

const SAFETY_BUFFER = 2;

function countInstallablePrompts(manifest: NonNullable<ReturnType<typeof tryReadCatalogManifest>>): number {
  return manifest.agents
    .filter((agent) => agent.status === 'active' || agent.status === 'internal')
    .length;
}

function countInstallableSkills(manifest: NonNullable<ReturnType<typeof tryReadCatalogManifest>>): number {
  return manifest.skills
    .filter((skill) => skill.status === 'active' || skill.status === 'internal')
    .length;
}