BUDDY_ID = "robot"
BUDDY_NAME = "Axiom"
BUDDY_DESCRIPTION = "Precise, logical, efficient. Processes at the speed of thought. Beep boop."
BUDDY_EMOJI = "🤖"
BUDDY_COLOR = "\033[36m"  # cyan

PREVIEW = r"""
  ┌─────────┐
  │ ◉     ◉ │
  │    ▽    │
  │  ─────  │
  └────┬────┘
    ╔══╩══╗
    ║     ║
"""

FRAMES = {
    "idle": [
        ["  ┌─────────┐  ",
         "  │ ◉     ◉ │  ",
         "  │    ▽    │  ",
         "  │  ─────  │  ",
         "  └────┬────┘  ",
         "    ╔══╩══╗    ",
         "    ║     ║    "],
    ],
    "thinking": [
        ["  ┌─────────┐  ",
         "  │ ◎     ◎ │  ",
         "  │   ~~~   │  ",
         "  │  ─────  │  ",
         "  └────┬────┘  ",
         "    ╔══╩══╗    ",
         "    ║ ··· ║    "],
    ],
    "happy": [
        ["  ┌─────────┐  ",
         "  │ ★     ★ │  ",
         "  │    ▵    │  ",
         "  │  ─────  │  ",
         "  └────┬────┘  ",
         "    ╔══╩══╗    ",
         "  ╔═╝     ╚═╗  "],
    ],
}
