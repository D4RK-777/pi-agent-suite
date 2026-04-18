---
name: tdd
description: Test-Driven Development enforcement skill - write tests first, always
---

# TDD Mode

[TDD MODE ACTIVATED]

## The Iron Law

**NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST**

Write code before test? DELETE IT. Start over. No exceptions.

## Red-Green-Refactor Cycle

### 1. RED: Write Failing Test
- Write test for the NEXT piece of functionality
- Run test - MUST FAIL
- If it passes, your test is wrong

### 2. GREEN: Minimal Implementation
- Write ONLY enough code to pass the test
- No extras. No "while I'm here."
- Run test - MUST PASS

### 3. REFACTOR: Clean Up
- Improve code quality
- Run tests after EVERY change
- Must stay green

### 4. REPEAT
- Next failing test
- Continue cycle

## Enforcement Rules