import assert from 'node:assert/strict';
import { describe, it } from 'node:test';
import {
  AGENT_DEFINITIONS,
  getAgent,
  getAgentNames,
  getAgentsByCategory,
  type AgentDefinition,
} from '../definitions.js';

describe('agents/definitions', () => {
  it('returns known agents and undefined for unknown names', () => {
    assert.equal(getAgent('executor'), AGENT_DEFINITIONS.executor);
    assert.equal(getAgent('does-not-exist'), undefined);
  });

  it('keeps key/name contract aligned', () => {
    const names = getAgentNames();
    assert.ok(names.length > 20, 'expected non-trivial agent catalog');