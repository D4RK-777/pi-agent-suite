import type { ExtensionAPI, ExtensionContext } from "@mariozechner/pi-coding-agent";

export default function (pi: ExtensionAPI) {
  let savedCtx: ExtensionContext | null = null;
  let currentAnimation: AnimationController | null = null;

  function setWidget(lines: string[]) {
    if (!savedCtx) return;
    savedCtx.ui.setWidget("byte", lines);
  }

  function setAnimatedWidget(name: string, frames: string[][]) {
    if (!savedCtx) return;
    if (currentAnimation) {
      currentAnimation.stop();
    }
    currentAnimation = new AnimationController(savedCtx, name, frames);
    currentAnimation.start();
  }

  // ═══════════════════════════════════════════════════════════════════
  // ANIMATION CONTROLLER
  // ═══════════════════════════════════════════════════════════════════

  class AnimationController {
    private ctx: ExtensionContext;
    private name: string;
    private frames: string[][];
    private currentFrame: number = 0;
    private intervalId: ReturnType<typeof setInterval> | null = null;
    private speed: number;

    constructor(ctx: ExtensionContext, name: string, frames: string[][], speed: number = 500) {
      this.ctx = ctx;
      this.name = name;
      this.frames = frames;
      this.speed = speed;
    }

    start() {
      if (this.frames.length <= 1) {
        this.ctx.ui.setWidget(this.name, this.frames[0]);
        return;
      }
      this.tick();
      this.intervalId = setInterval(() => this.tick(), this.speed);
    }

    stop() {
      if (this.intervalId) {
        clearInterval(this.intervalId);
        this.intervalId = null;
      }
    }

    private tick() {
      this.ctx.ui.setWidget(this.name, this.frames[this.currentFrame]);
      this.currentFrame = (this.currentFrame + 1) % this.frames.length;
    }
  }

  // ═══════════════════════════════════════════════════════════════════
  // ALIEN BUDDY PIXEL ART - Enhanced with expressions
  // ═══════════════════════════════════════════════════════════════════

  // Helper to create frames with subtle vertical offset (floating effect)
  function withFloatOffset(frames: string[][], offset: number = 1): string[][] {
    return frames.map(frame => {
      const result = [...frame];
      if (offset > 0) {
        result.unshift('');
        result.pop();
      } else {
        result.push('');
        result.shift();
      }
      return result;
    });
  }

  // ═══════════════════════════════════════════════════════════════════
  // PIXEL BUDDY v2 — twin antennae, fatter body, dotted blink, colored
  //
  // 7 rows × 11 chars wide:
  //   '  █     █  '  ← antenna TIPS (green)
  //   '  █▄   ▄█  '  ← antenna bases with inward flare (green)
  //   '  ███████  '  ← head top (white)
  //   '  ██ █ ██  '  ← eyes: 2 body | eye | center divider | eye | 2 body
  //   '  ███████  '  ← under-eye body row 1 (gray, fatter section)
  //   ' ▄███████▄ '  ← under-eye body row 2 + arms (gray)
  //   '  █ █ █ █  '  ← 4 stubby legs (gray)
  //
  // Pure block chars only: █ ▀ ▄ ▒ ▓ and space.
  // Blink uses ▒ (dotted) instead of █ so eyes stay distinct from body.
  // ANSI colors: antennae green, head white, body gray, eyes cyan.
  // ═══════════════════════════════════════════════════════════════════

  // Color codes applied per-line. Mid-line color changes via concatenation.
  const A = '\x1b[92m';   // bright green — antennae
  const H = '\x1b[37m';   // white — head top
  const B = '\x1b[90m';   // dark gray — body (under-eye fat section)
  const E = '\x1b[96m';   // bright cyan — eyes (when blinking/expressive)
  const S = '\x1b[93m';   // yellow — sparkles (success)
  const X = '\x1b[91m';   // red — error body
  const R = '\x1b[0m';    // reset

  const line = (code: string, body: string) => code + body + R;

  // Eye-row builder: lets us color just the eye chars differently from the head.
  // body='head block char' for sides (default █), eye='eye char' (default space).
  const eyeRow = (eye: string, eyeColor: string = H) =>
    H + '  ██' + R + eyeColor + eye + H + '█' + eyeColor + eye + H + '██  ' + R;

  // ─── IDLE (subtle blink: eyes become ▒ dotted, not solid ─ so they stay distinct from body) ───
  const IDLE_FRAMES = [
    [
      line(A, '  █     █  '),
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow(' '),
      line(B, '  ███████  '),
      line(B, ' ▄███████▄ '),
      line(B, '  █ █ █ █  '),
    ],
    [
      line(A, '  █     █  '),
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow('▒', E),              // blink: ▒ dotted eyes in cyan
      line(B, '  ███████  '),
      line(B, ' ▄███████▄ '),
      line(B, '  █ █ █ █  '),
    ],
  ];

  // ─── THINKING (eyes dart up then down) ───
  const THINKING_FRAMES = [
    [
      line(A, '  █     █  '),
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow('▀', E),              // eyes looking up
      line(B, '  ███████  '),
      line(B, ' ▄███████▄ '),
      line(B, '  █ █ █ █  '),
    ],
    [
      line(A, '  █     █  '),
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow('▄', E),              // eyes looking down
      line(B, '  ███████  '),
      line(B, ' ▄███████▄ '),
      line(B, '  █ █ █ █  '),
    ],
  ];

  // ─── HAPPY (squint eyes) ───
  const HAPPY_FRAMES = [
    [
      line(A, '  █     █  '),
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow('▄', E),
      line(B, '  ███████  '),
      line(B, ' ▄███████▄ '),
      line(B, '  █ █ █ █  '),
    ],
  ];

  // ─── ERROR (closed ▒ eyes, red-tinted body) ───
  const ERROR_FRAMES = [
    [
      line(A, '  █     █  '),
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow('▒', X),              // red dotted eyes
      line(X, '  ▒▒▒▒▒▒▒  '),
      line(X, ' ▄▒▒▒▒▒▒▒▄ '),
      line(X, '  █ █ █ █  '),
    ],
  ];

  // ─── TYPING (arms wave) ───
  const TYPING_FRAMES = [
    [
      line(A, '  █     █  '),
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow(' '),
      line(B, '  ███████  '),
      line(B, '▄█████████▄'),       // arms extended
      line(B, '  █ █ █ █  '),
    ],
    [
      line(A, '  █     █  '),
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow(' '),
      line(B, '  ███████  '),
      line(B, '  ▄█████▄  '),       // arms tucked
      line(B, '  █ █ █ █  '),
    ],
    [
      line(A, '  █     █  '),
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow(' '),
      line(B, '  ███████  '),
      line(B, ' ▄███████▄ '),       // arms neutral
      line(B, '  █ █ █ █  '),
    ],
  ];

  // ─── EXCITED (happy eyes, jumping — legs tuck) ───
  const EXCITED_FRAMES = [
    [
      line(A, '  █     █  '),
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow('▄', E),
      line(B, '  ███████  '),
      line(B, ' ▄███████▄ '),
      line(B, '  █ █ █ █  '),
    ],
    [
      line(A, '  █     █  '),
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow('▄', E),
      line(B, '  ███████  '),
      line(B, ' ▄███████▄ '),
      line(B, '   █████   '),       // legs tucked mid-jump
    ],
  ];

  // ─── SLEEPY (closed eyes + floating Z dot) ───
  const SLEEPY_FRAMES = [
    [
      line(A, '  █     █  '),
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow('▒', E),
      line(B, '  ███████  '),
      line(B, ' ▄███████▄ '),
      line(B, '  █ █ █ █  '),
    ],
    [
      line(A, '  █') + S + '  ▀  ' + A + '█  ' + R,   // Z dot floats between antennae
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow('▒', E),
      line(B, '  ███████  '),
      line(B, ' ▄███████▄ '),
      line(B, '  █ █ █ █  '),
    ],
  ];

  // ─── SURPRISED (antennae perk up taller, eyes widen with ▀ arches) ───
  const SURPRISED_FRAMES = [
    [
      line(A, ' ▄█     █▄ '),        // raised antennae
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      line(H, '  █') + E + '▀ █ ▀' + H + '█  ' + R,   // ▀ eyebrows
      line(B, '  ███████  '),
      line(B, ' ▄███████▄ '),
      line(B, '  █ █ █ █  '),
    ],
  ];

  // ─── CONFUSED (antenna tilts right, one eye droops) ───
  const CONFUSED_FRAMES = [
    [
      line(A, '   █    █  '),        // left antenna shifted right
      line(A, '   █▄  ▄█  '),
      line(H, '  ███████  '),
      line(H, '  ██') + E + ' █▄' + H + '██  ' + R,   // right eye droopy
      line(B, '  ███████  '),
      line(B, ' ▄███████▄ '),
      line(B, '  █ █ █ █  '),
    ],
  ];

  // ─── WORKING (busy hatched body in yellow/orange) ───
  const WORKING_FRAMES = [
    [
      line(A, '  █     █  '),
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow(' '),
      line(S, '  ▒▒▒▒▒▒▒  '),       // yellow hatch = working
      line(S, ' ▄▒▒▒▒▒▒▒▄ '),
      line(B, '  █ █ █ █  '),
    ],
    [
      line(A, '  █     █  '),
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow(' '),
      line(S, '  ▓▓▓▓▓▓▓  '),       // darker hatch
      line(S, ' ▄▓▓▓▓▓▓▓▄ '),
      line(B, '  █ █ █ █  '),
    ],
  ];

  // ─── SUCCESS (green antennae + yellow sparkles + happy eyes) ───
  const SUCCESS_FRAMES = [
    [
      line(S, '▀ ') + A + '█     █' + S + ' ▀' + R,   // sparkles at corners
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow('▄', E),
      line(B, '  ███████  '),
      line(B, ' ▄███████▄ '),
      line(S, '▀ ') + B + '█ █ █ █' + S + ' ▀' + R,   // sparkles around legs
    ],
    [
      line(A, '  █     █  '),
      line(S, '▀ ') + A + '█▄   ▄█' + S + ' ▀' + R,
      line(H, '  ███████  '),
      eyeRow('▄', E),
      line(B, '  ███████  '),
      line(S, '▀') + B + '▄███████▄' + S + '▀' + R,
      line(B, '  █ █ █ █  '),
    ],
  ];

  // ─── WAITING (subtle pulsing body) ───
  const WAITING_FRAMES = [
    [
      line(A, '  █     █  '),
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow(' '),
      line(B, '  ███████  '),
      line(B, ' ▄███████▄ '),
      line(B, '  █ █ █ █  '),
    ],
    [
      line(A, '  █     █  '),
      line(A, '  █▄   ▄█  '),
      line(H, '  ███████  '),
      eyeRow(' '),
      line(B, '  ▒▒▒▒▒▒▒  '),       // subtle body pulse
      line(B, ' ▄▒▒▒▒▒▒▒▄ '),
      line(B, '  █ █ █ █  '),
    ],
  ];

  // ═══════════════════════════════════════════════════════════════════
  // EXPORTED STATE API (for external control)
  // ═══════════════════════════════════════════════════════════════════

  const alienStates = {
    idle: { frames: IDLE_FRAMES, speed: 3000 },
    thinking: { frames: THINKING_FRAMES, speed: 800 },
    happy: { frames: HAPPY_FRAMES, speed: 600 },
    error: { frames: ERROR_FRAMES, speed: 0 },
    typing: { frames: TYPING_FRAMES, speed: 400 },
    excited: { frames: EXCITED_FRAMES, speed: 200 },
    sleepy: { frames: SLEEPY_FRAMES, speed: 2000 },
    surprised: { frames: SURPRISED_FRAMES, speed: 500 },
    confused: { frames: CONFUSED_FRAMES, speed: 600 },
    working: { frames: WORKING_FRAMES, speed: 300 },
    success: { frames: SUCCESS_FRAMES, speed: 500 },
    waiting: { frames: WAITING_FRAMES, speed: 1000 },
  };

  // Public API to set a specific state
  function setAlienState(stateName: keyof typeof alienStates) {
    if (!savedCtx) return;
    const state = alienStates[stateName];
    if (!state) return;

    if (currentAnimation) {
      currentAnimation.stop();
    }

    if (state.frames.length === 1) {
      savedCtx.ui.setWidget("byte", state.frames[0]);
    } else {
      currentAnimation = new AnimationController(savedCtx, "byte", state.frames, state.speed);
      currentAnimation.start();
    }
  }

  // ─────────────────────────────────────────────────────────────────
  // EVENT HANDLERS
  // ─────────────────────────────────────────────────────────────────

  pi.on("session_start", async (_e, ctx) => {
    savedCtx = ctx;
    setAlienState("idle");
  });

  pi.on("agent_start", async (_e, ctx) => {
    savedCtx = ctx;
    setAlienState("thinking");
  });

  pi.on("tool_execution_start", async (_e, ctx) => {
    savedCtx = ctx;
    setAlienState("typing");
  });

  pi.on("tool_execution_end", async (e, ctx) => {
    savedCtx = ctx;
    if (e.isError) {
      setAlienState("error");
    } else {
      setAlienState("happy");
    }
  });

  pi.on("agent_end", async (_e, ctx) => {
    savedCtx = ctx;
    setAlienState("success");
  });

  pi.on("error", async (_e, ctx) => {
    savedCtx = ctx;
    setAlienState("error");
  });

  pi.on("session_end", async () => {
    if (currentAnimation) {
      currentAnimation.stop();
      currentAnimation = null;
    }
    savedCtx = null;
  });

  // ─────────────────────────────────────────────────────────────────
  // DEBUG: Expose alienStates for testing (remove in production)
  // ─────────────────────────────────────────────────────────────────

  (pi as any).alienStates = alienStates;
  (pi as any).setAlienState = setAlienState;
}
