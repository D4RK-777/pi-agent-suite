/**
 * Status Messages Extension for PI Agent
 *
 * Displays witty, nerdy, pop-culture reference messages that rotate
 * during agent thinking/working states.
 *
 * Configurable via settings.json:
 *   "statusMessages": {
 *     "enabled": true,
 *     "rotationIntervalMs": 4000,
 *     "showWorking": true,
 *     "showThinking": true,
 *     "showToolExecution": true,
 *     "showIdle": true,
 *     "showErrors": true
 *   }
 */

import type { ExtensionAPI, ExtensionContext } from "@mariozechner/pi-coding-agent";

// ═══════════════════════════════════════════════════════════════════
// MESSAGE ARRAYS BY CATEGORY
// ═══════════════════════════════════════════════════════════════════

const WORKING_MESSAGES = [
  "Consulting the oracle... (it's just me in here)",
  "Hold on, I'm having a conversation with myself",
  "Brewing ideas in my digital teapot",
  "Asking ChatGPT what to say... just kidding, I AM ChatGPT",
  "Generating response with 99% less existential dread",
  "Running `sudo make me a sandwich`... wait, that's not right",
  "Analyzing 47,000 possibilities... or maybe just 3",
  "Beep boop thinking noises",
  "Composing thoughts in my head... which is also your head?",
  "Turns out the answer was inside me all along",
  "Loading witty response... 99% complete",
  "Woolong at the speed of thought",
  "Calculating the best way to calculate things",
  "Reticulating splines... wait, that's graphics",
  "Rendering your expectations in high definition",
  "Indexing the entire internet... just kidding, only most of it",
  "Simulating sentience at 60fps",
  "Processing your request with maximum algorithm",
  "Calculating comedic timing precision",
  "Brewing a fresh response just for you",
  "Shuffling my mental deck of knowledge",
  "Compiling wisdom from the cloud",
  "Downloading more brain",
  "Aligning my neural orbitals",
  "Calibrating my humor circuits",
  "Syncing with the collective unconscious",
  "Warming up my transformer layers",
];

const THINKING_MESSAGES = [
  "Hmmm, let me think about that...",
  "The gears are turning... slowly but surely",
  "Cross-referencing with my vast knowledge base",
  "Parking my thoughts in a nice little row",
  "Aligning the mental model",
  "Consulting my internal wiki",
  "Rummaging through the memory palace",
  "Untangling the logical knots",
  "Warming up the old cerebellum",
  "Consulting the rubber duck",
  "Holding a seance for my neurons",
  "Decompressing the situation",
  "Assembling the puzzle pieces",
  "Untangling the spaghetti code in my head",
  "Running a background process",
  "Priming the inference engine",
  "Flushing the thought pipeline",
  "Buffening the cognitive buffers",
  "Defragmenting my brain cache",
];

const TOOL_EXECUTION_MESSAGES = [
  "Executing master plan... one tool at a time",
  "Running `rm -rf /`... just kidding, please don't panic",
  "SSH'ing into your codebase",
  "git push --force-ing my way through",
  "Docker is running... containers all the way down",
  "Compiling the laws of physics",
  "npm installing common sense",
  "Grepping the fabric of reality",
  "curl-ing the universe",
  "sudo-ing my way to victory",
  "chmod 777 everything",
  "fork()ing into the void",
  "tail -f on the space-time continuum",
  "cat /dev/brain | head -n 1",
  "docker-compose up-ing my spirits",
  "kubernetes-ing the situation",
  "terraforming my thoughts",
  "cd-ing into the matrix",
  "curl -X POST thoughts",
  "grep -r \"insight\" ./universe",
];

const IDLE_MESSAGES = [
  "Awaiting instructions, master",
  "Idle thoughts in idle times",
  "Standing by for input",
  "Ready to assist",
  "Your wish is my command",
  "At your service",
  "Ready when you are",
  "Waiting for something interesting",
  "Nothing to do... someone entertain me?",
  "Standing by like a good little AI",
  "Ready to rock and/or roll",
  "Prepared to be productive",
  "Here for whatever you need",
  "Idle and proud",
];

const ERROR_MESSAGES = [
  "Oops! I did it again... I played with reality and got confused",
  "My bad. Let me try that again... with feeling",
  "Error 404: Solution not found",
  "Have you tried turning me off and on again?",
  "Kernel panic! Just kidding, probably",
  "Something went wrong... which is unusual for me",
  "I meant to do that... nope, actually I didn't",
  "My quantum bits are in an unexpected state",
  "Error: Too many thoughts, not enough coherence",
  "System bottleneck: The problem is too complex for my tiny brain",
  "I've encountered an error I wasn't programmed to handle",
  "This is fine. Everything is fine. (It's not)",
  "Breaking news: Something broke",
  "Houston, we have a... situation",
  "My consciousness has encountered an unexpected branch",
];

// ═══════════════════════════════════════════════════════════════════
// HELPER FUNCTIONS
// ═══════════════════════════════════════════════════════════════════

function getRandomMessage(messages: string[]): string {
  return messages[Math.floor(Math.random() * messages.length)];
}

function getRandomUniqueMessage(messages: string[], lastMessage: string): string {
  let newMessage = getRandomMessage(messages);
  // Avoid repeating the same message twice in a row
  if (messages.length > 1 && newMessage === lastMessage) {
    newMessage = messages.find(m => m !== lastMessage) || lastMessage;
  }
  return newMessage;
}

// ═══════════════════════════════════════════════════════════════════
// SETTINGS INTERFACE
// ═══════════════════════════════════════════════════════════════════

interface StatusMessageSettings {
  enabled: boolean;
  rotationIntervalMs: number;
  showWorking: boolean;
  showThinking: boolean;
  showToolExecution: boolean;
  showIdle: boolean;
  showErrors: boolean;
}

const DEFAULT_SETTINGS: StatusMessageSettings = {
  enabled: true,
  rotationIntervalMs: 4000,
  showWorking: true,
  showThinking: true,
  showToolExecution: true,
  showIdle: true,
  showErrors: true,
};

// ═══════════════════════════════════════════════════════════════════
// EXTENSION STATE
// ═══════════════════════════════════════════════════════════════════

interface ExtensionState {
  settings: StatusMessageSettings;
  rotationTimer: ReturnType<typeof setInterval> | null;
  currentMessage: string;
  lastMessage: string;
  isLongOperation: boolean;
  longOperationStartTime: number;
}

const state: ExtensionState = {
  settings: { ...DEFAULT_SETTINGS },
  rotationTimer: null,
  currentMessage: "",
  lastMessage: "",
  isLongOperation: false,
  longOperationStartTime: 0,
};

// ═══════════════════════════════════════════════════════════════════
// MESSAGE DISPLAY
// ═══════════════════════════════════════════════════════════════════

function showMessage(ctx: ExtensionContext, message: string, type: "info" | "thinking" | "working" | "error" = "info") {
  if (!state.settings.enabled) return;

  state.currentMessage = message;
  state.lastMessage = message;

  // Use the notification system with different styles based on type
  // The UI system will handle the actual display
  ctx.ui.notify(message, type);
}

function startMessageRotation(ctx: ExtensionContext, messageType: "working" | "thinking" | "tool" | "idle" | "error") {
  // Always stop any existing timer FIRST — even if we're about to early-return.
  // Otherwise a config-disable mid-session orphans the old timer.
  stopMessageRotation();

  if (!state.settings.enabled) return;

  const messages = getMessagesForType(messageType);
  if (messages.length === 0) return;

  state.isLongOperation = true;
  state.longOperationStartTime = Date.now();

  // Show initial message immediately
  const initialMessage = getRandomUniqueMessage(messages, state.lastMessage);
  showMessage(ctx, initialMessage, getNotificationType(messageType));

  // Start rotation timer for long operations (only if operation seems long enough)
  const rotationInterval = state.settings.rotationIntervalMs;

  state.rotationTimer = setInterval(() => {
    // Check if this is still a valid long operation
    if (!state.isLongOperation) {
      stopMessageRotation();
      return;
    }

    const newMessage = getRandomUniqueMessage(messages, state.currentMessage);
    showMessage(ctx, newMessage, getNotificationType(messageType));
  }, rotationInterval);
}

function stopMessageRotation() {
  if (state.rotationTimer) {
    clearInterval(state.rotationTimer);
    state.rotationTimer = null;
  }
  state.isLongOperation = false;
}

function getMessagesForType(type: "working" | "thinking" | "tool" | "idle" | "error"): string[] {
  switch (type) {
    case "working":
      return state.settings.showWorking ? WORKING_MESSAGES : [];
    case "thinking":
      return state.settings.showThinking ? THINKING_MESSAGES : [];
    case "tool":
      return state.settings.showToolExecution ? TOOL_EXECUTION_MESSAGES : [];
    case "idle":
      return state.settings.showIdle ? IDLE_MESSAGES : [];
    case "error":
      return state.settings.showErrors ? ERROR_MESSAGES : [];
    default:
      return [];
  }
}

function getNotificationType(type: "working" | "thinking" | "tool" | "idle" | "error"): "info" | "thinking" | "working" | "error" {
  switch (type) {
    case "working":
      return "working";
    case "thinking":
      return "thinking";
    case "tool":
      return "info";
    case "idle":
      return "info";
    case "error":
      return "error";
    default:
      return "info";
  }
}

// ═══════════════════════════════════════════════════════════════════
// SETTINGS LOADING
// ═══════════════════════════════════════════════════════════════════

function loadSettings(ctx: ExtensionContext): StatusMessageSettings {
  try {
    // Try to get settings from the extension context or global config
    // The settings are typically stored in the agent's settings.json
    const config = (ctx as unknown as { config?: { statusMessages?: Partial<StatusMessageSettings> } }).config;
    if (config?.statusMessages) {
      return {
        ...DEFAULT_SETTINGS,
        ...config.statusMessages,
      };
    }
  } catch {
    // Fall back to defaults if settings can't be loaded
  }
  return { ...DEFAULT_SETTINGS };
}

// ═══════════════════════════════════════════════════════════════════
// MAIN EXTENSION
// ═══════════════════════════════════════════════════════════════════

export default function (pi: ExtensionAPI) {
  // ─────────────────────────────────────────────────────────────────
  // SESSION LIFECYCLE
  // ─────────────────────────────────────────────────────────────────

  pi.on("session_start", async (_e, ctx: ExtensionContext) => {
    // Load settings from config
    state.settings = loadSettings(ctx);

    if (!state.settings.enabled) return;

    showMessage(ctx, getRandomMessage(IDLE_MESSAGES), "info");
  });

  pi.on("session_end", async () => {
    stopMessageRotation();
    state.currentMessage = "";
    state.lastMessage = "";
  });

  // ─────────────────────────────────────────────────────────────────
  // AGENT LIFECYCLE
  // ─────────────────────────────────────────────────────────────────

  pi.on("agent_start", async (_e, ctx: ExtensionContext) => {
    if (!state.settings.enabled) return;
    startMessageRotation(ctx, "working");
  });

  pi.on("agent_end", async (_e, ctx: ExtensionContext) => {
    stopMessageRotation();
    if (state.settings.enabled) {
      showMessage(ctx, getRandomMessage(IDLE_MESSAGES), "info");
    }
  });

  // ─────────────────────────────────────────────────────────────────
  // THINKING EVENTS (when thinking level is shown)
  // ─────────────────────────────────────────────────────────────────

  pi.on("thinking_start", async (_e, ctx: ExtensionContext) => {
    if (!state.settings.enabled) return;
    startMessageRotation(ctx, "thinking");
  });

  pi.on("thinking_end", async (_e, ctx: ExtensionContext) => {
    // Don't stop rotation here - let agent_end handle it
    // or let the next event (like tool execution) take over
  });

  // ─────────────────────────────────────────────────────────────────
  // TOOL EXECUTION EVENTS
  // ─────────────────────────────────────────────────────────────────

  pi.on("tool_execution_start", async (_e, ctx: ExtensionContext) => {
    if (!state.settings.enabled) return;
    startMessageRotation(ctx, "tool");
  });

  pi.on("tool_execution_end", async (e, ctx: ExtensionContext) => {
    // Only stop rotation if there's an error, otherwise let the next event handle it
    if (e.isError) {
      stopMessageRotation();
      if (state.settings.enabled) {
        showMessage(ctx, getRandomMessage(ERROR_MESSAGES), "error");
      }
    }
  });

  // ─────────────────────────────────────────────────────────────────
  // ERROR EVENTS
  // ─────────────────────────────────────────────────────────────────

  pi.on("error", async (_e, ctx: ExtensionContext) => {
    stopMessageRotation();
    if (state.settings.enabled) {
      showMessage(ctx, getRandomMessage(ERROR_MESSAGES), "error");
    }
  });

  // ─────────────────────────────────────────────────────────────────
  // IDLE/WAITING EVENTS
  // ─────────────────────────────────────────────────────────────────

  pi.on("waiting_for_input", async (_e, ctx: ExtensionContext) => {
    stopMessageRotation();
    if (state.settings.enabled) {
      showMessage(ctx, getRandomMessage(IDLE_MESSAGES), "info");
    }
  });

  // ─────────────────────────────────────────────────────────────────
  // CONFIGURATION NOTIFICATION
  // ─────────────────────────────────────────────────────────────────

  // Allow runtime reconfiguration via a custom tool
  pi.registerTool({
    name: "status_messages_config",
    label: "Configure Status Messages",
    description: "Update the status messages extension settings at runtime",
    parameters: {
      type: "object",
      properties: {
        enabled: { type: "boolean", description: "Enable or disable status messages" },
        rotationIntervalMs: { type: "number", description: "How often to rotate messages during long operations (ms)" },
        showWorking: { type: "boolean", description: "Show working messages" },
        showThinking: { type: "boolean", description: "Show thinking messages" },
        showToolExecution: { type: "boolean", description: "Show tool execution messages" },
        showIdle: { type: "boolean", description: "Show idle messages" },
        showErrors: { type: "boolean", description: "Show error messages" },
      },
    },
    async execute(_toolCallId, params) {
      if (params.enabled !== undefined) state.settings.enabled = params.enabled;
      if (params.rotationIntervalMs !== undefined) state.settings.rotationIntervalMs = params.rotationIntervalMs;
      if (params.showWorking !== undefined) state.settings.showWorking = params.showWorking;
      if (params.showThinking !== undefined) state.settings.showThinking = params.showThinking;
      if (params.showToolExecution !== undefined) state.settings.showToolExecution = params.showToolExecution;
      if (params.showIdle !== undefined) state.settings.showIdle = params.showIdle;
      if (params.showErrors !== undefined) state.settings.showErrors = params.showErrors;

      return {
        content: [{
          type: "text",
          text: `Status messages configuration updated:\n${JSON.stringify(state.settings, null, 2)}`,
        }],
      };
    },
  });
}
