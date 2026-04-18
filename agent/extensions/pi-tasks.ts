/**
 * pi_tasks — In-Session Task Tracker (TodoWrite equivalent)
 *
 * Matches Claude Code's TodoWrite flow: the model rewrites the whole list each
 * time, with three statuses (pending, in_progress, completed). Simpler than
 * CRUD, and the model already knows the pattern.
 *
 * Persisted per-session under ~/.pi/sessions/tasks/<sessionId>.json so the
 * list survives a /resume. Cleared on demand via pi_tasks_clear.
 *
 * Injected on before_agent_start as a compact <pi-tasks> block so the model
 * always sees the current state without needing to re-query.
 */

import type { ExtensionAPI, BeforeAgentStartEvent, BeforeAgentStartEventResult } from "@mariozechner/pi-coding-agent";
import { Type } from "@sinclair/typebox";
import { mkdir, readFile, writeFile } from "fs/promises";
import { homedir } from "os";
import { join } from "path";

const TASKS_DIR = join(homedir(), ".pi", "sessions", "tasks");

type Status = "pending" | "in_progress" | "completed";
interface Task {
  id: string;
  subject: string;
  status: Status;
  activeForm?: string;
}

async function ensureDir() {
  await mkdir(TASKS_DIR, { recursive: true });
}

function fileFor(sessionId: string) {
  return join(TASKS_DIR, `${sessionId}.json`);
}

async function loadTasks(sessionId: string): Promise<Task[]> {
  try {
    const raw = await readFile(fileFor(sessionId), "utf8");
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

async function saveTasks(sessionId: string, tasks: Task[]) {
  await ensureDir();
  await writeFile(fileFor(sessionId), JSON.stringify(tasks, null, 2), "utf8");
}

function renderTasks(tasks: Task[]): string {
  if (!tasks.length) return "";
  const lines = tasks.map((t) => {
    const marker = t.status === "completed" ? "[x]" : t.status === "in_progress" ? "[~]" : "[ ]";
    const active = t.status === "in_progress" && t.activeForm ? ` — ${t.activeForm}` : "";
    return `${marker} ${t.id}. ${t.subject}${active}`;
  });
  return [
    "<pi-tasks>",
    "Current session task list (status: [ ] pending, [~] in_progress, [x] completed).",
    "Call pi_tasks to replace the list, or pi_tasks_update to change a single task's status.",
    "",
    lines.join("\n"),
    "</pi-tasks>",
  ].join("\n");
}

function inProgressCount(tasks: Task[]): number {
  return tasks.filter((t) => t.status === "in_progress").length;
}

export default function (pi: ExtensionAPI) {
  // Cache per session so injection is sync.
  const cache = new Map<string, Task[]>();

  async function refresh(sessionId: string) {
    cache.set(sessionId, await loadTasks(sessionId));
  }

  pi.on("session_start", async (_event, ctx) => {
    await refresh(ctx.sessionManager.getSessionId());
  });

  pi.on("before_agent_start", (_event: BeforeAgentStartEvent, ctx): BeforeAgentStartEventResult | void => {
    const sessionId = ctx.sessionManager.getSessionId();
    const tasks = cache.get(sessionId) || [];
    const block = renderTasks(tasks);
    if (!block) return;
    return { systemPrompt: block };
  });

  // Full-list replacement. Model rewrites the whole list — matches Claude's TodoWrite.
  pi.registerTool({
    name: "pi_tasks",
    label: "pi tasks",
    description:
      "Replace the session task list. Use for multi-step work. Follow the discipline: " +
      "exactly ONE task should be in_progress at a time; mark completed immediately after finishing; " +
      "never batch completions.",
    promptGuidelines: [
      "Use pi_tasks for any task that requires 3+ distinct steps or when the user gives a list.",
      "Exactly ONE task in_progress at a time. Mark completed the moment you finish — never batch.",
      "Skip pi_tasks for trivial or single-step work; the overhead isn't worth it.",
      "Use pi_tasks_update to flip one task's status rather than rewriting the whole list.",
    ],
    parameters: Type.Object({
      tasks: Type.Array(
        Type.Object({
          subject: Type.String({ description: "Imperative title, e.g. 'Fix auth bug in login flow'." }),
          status: Type.Union([Type.Literal("pending"), Type.Literal("in_progress"), Type.Literal("completed")]),
          activeForm: Type.Optional(Type.String({ description: "Present-continuous form shown while in_progress, e.g. 'Fixing auth bug'." })),
        }),
      ),
    }),
    async execute(_toolCallId, params, _signal, _onUpdate, ctx) {
      const sessionId = ctx.sessionManager.getSessionId();
      const withIds: Task[] = params.tasks.map((t, i) => ({
        id: String(i + 1),
        subject: t.subject,
        status: t.status,
        activeForm: t.activeForm,
      }));

      await saveTasks(sessionId, withIds);
      cache.set(sessionId, withIds);

      const n = withIds.length;
      const done = withIds.filter((t) => t.status === "completed").length;
      const ip = inProgressCount(withIds);
      let warning = "";
      if (ip > 1) {
        warning = `\n⚠ ${ip} tasks in_progress — discipline says exactly one at a time.`;
      }

      return {
        content: [
          {
            type: "text",
            text: `Task list updated (${n} tasks, ${done} completed, ${ip} in progress).${warning}\n\n${renderTasks(withIds)}`,
          },
        ],
        details: { count: n, completed: done, in_progress: ip },
      };
    },
  });

  // Cheap single-task status update so the model doesn't rewrite the list to flip one flag.
  pi.registerTool({
    name: "pi_tasks_update",
    label: "pi tasks update",
    description: "Update a single task's status by id. Preferred over rewriting the whole list for one flag flip.",
    parameters: Type.Object({
      id: Type.String({ description: "Task id as shown in <pi-tasks>." }),
      status: Type.Union([Type.Literal("pending"), Type.Literal("in_progress"), Type.Literal("completed")]),
    }),
    async execute(_toolCallId, params, _signal, _onUpdate, ctx) {
      const sessionId = ctx.sessionManager.getSessionId();
      const tasks = cache.get(sessionId) || (await loadTasks(sessionId));
      const t = tasks.find((x) => x.id === params.id);
      if (!t) {
        return {
          content: [{ type: "text", text: `No task with id ${params.id}. Use pi_tasks to create or replace the list.` }],
          details: { updated: false },
        };
      }
      t.status = params.status;
      await saveTasks(sessionId, tasks);
      cache.set(sessionId, tasks);
      return {
        content: [{ type: "text", text: `Task ${params.id} → ${params.status}\n\n${renderTasks(tasks)}` }],
        details: { updated: true, id: params.id, status: params.status },
      };
    },
  });

  pi.registerTool({
    name: "pi_tasks_clear",
    label: "pi tasks clear",
    description: "Clear the current session's task list. Use when starting fresh unrelated work.",
    parameters: Type.Object({}),
    async execute(_toolCallId, _params, _signal, _onUpdate, ctx) {
      const sessionId = ctx.sessionManager.getSessionId();
      await saveTasks(sessionId, []);
      cache.set(sessionId, []);
      return { content: [{ type: "text", text: "Task list cleared." }], details: { cleared: true } };
    },
  });
}
