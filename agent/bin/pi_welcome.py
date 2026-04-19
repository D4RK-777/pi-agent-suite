#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, os, shutil, sys
from pathlib import Path
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
RESET=chr(27)+'[0m'; BOLD=chr(27)+'[1m'; DIM=chr(27)+'[2m'
CYAN=chr(27)+'[36m'; GREEN=chr(27)+'[32m'; YELLOW=chr(27)+'[33m'
MAGENTA=chr(27)+'[35m'; WHITE=chr(27)+'[97m'
ORANGE=chr(27)+'[38;5;208m'; RED_C=chr(27)+'[31m'
def c(col,txt): return f"{col}{txt}{RESET}"
def clear(): print(chr(27)+"[2J"+chr(27)+"[H",end="",flush=True)
BUDDIES=[
  {"id":"alien","name":"Cosmo","emoji":"👽","color":ORANGE,"desc":"Wise, calm, thinks deeply. A trusted guide from beyond the stars.","prev":["  ▓▓▓▓▓▓▓▓▓  ","  ████████  ","  ██ █ ███  ","  ████████  "]},
  {"id":"robot","name":"Axiom","emoji":"🤖","color":CYAN,"desc":"Precise, logical, efficient. Processes at the speed of thought.","prev":["  ┌─────────┐  ","  │ ◉     ◉ │  ","  │    ▽    │  ","  └────┬────┘  "]},
  {"id":"wizard","name":"Merlin","emoji":"🧙","color":MAGENTA,"desc":"Ancient wisdom, modern power. Conjures solutions from arcane knowledge.","prev":["      /\      ","     /★★\     ","   | ◕  ◕ |   ","   └──────┘   "]},
  {"id":"ghost","name":"Phantom","emoji":"👻","color":WHITE,"desc":"Mysterious and swift. Glides through codebases leaving no trace.","prev":["  ╭────────╮  ","  │ ◠    ◠ │  ","  │   ▿    │  ","  ╰────────╯  "]},
  {"id":"dragon","name":"Ember","emoji":"🐉","color":RED_C,"desc":"Fierce, powerful, loyal. Burns through bugs with fiery precision.","prev":["  >\  ██████  ","  >)  █◉  ◉█  ","  >/  ██████  ","      ██████  "]},
]
THEMES=[
  {"id":"cyberpunk-neon","name":"Cyberpunk Neon","emoji":"⚡ ","sw":chr(27)+"[38;5;51m","desc":"Neon glows on a dark cityscape. Pure cyberpunk."},
  {"id":"nordic-frost","name":"Nordic Frost","emoji":"❄️  ","sw":chr(27)+"[38;5;87m","desc":"Aurora borealis over frozen fjords. Cool and crisp."},
  {"id":"forest-spirit","name":"Forest Spirit","emoji":"🌿","sw":chr(27)+"[38;5;106m","desc":"Deep woods and ancient moss. Grounded and alive."},
  {"id":"ocean-depth","name":"Ocean Depth","emoji":"🌊","sw":chr(27)+"[38;5;38m","desc":"Bioluminescent deep-sea blues. Calm, vast, mysterious."},
  {"id":"sunset-glow","name":"Sunset Glow","emoji":"🌅","sw":chr(27)+"[38;5;209m","desc":"Warm coral and gold as the day ends. Energetic and vivid."},
  {"id":"warm-amber","name":"Warm Amber","emoji":"🍂","sw":chr(27)+"[38;5;214m","desc":"Cozy amber and warm browns. Like coding by a fireplace."},
  {"id":"claude-warm","name":"Claude Warm","emoji":"🧡","sw":chr(27)+"[38;5;208m","desc":"The classic Claude palette. Orange, red, pink, purple."},
]
PI_HOME=Path(os.environ.get("PI_AGENT_HOME",Path.home()/".pi"))
PREFS=PI_HOME/"preferences.json"
def load_prefs():
    try: return json.loads(PREFS.read_text()) if PREFS.exists() else {}
    except: return {}
def save_prefs(p):
    PI_HOME.mkdir(parents=True,exist_ok=True); PREFS.write_text(json.dumps(p,indent=2))
def pal(color,n=4): return "  ".join(f"{color}██{RESET}" for _ in range(n))
def header():
    print(); print(c(CYAN+BOLD,"═"*60))
    print(c(CYAN+BOLD,"  🧠  Pi Agent Suite — Welcome!"))
    print(c(CYAN+BOLD,"═"*60)); print()
    print(c(DIM,"  Personalise your setup. Two quick choices."))
    print(c(DIM,"  Re-run anytime: python ~/.pi/agent/bin/pi_welcome.py")); print()
def buddy_grid():
    print(c(BOLD,"  ┌─ CHOOSE YOUR BUDDY ─────────────────────────────────┐")); print()
    for i,b in enumerate(BUDDIES):
        print(f"  {c(YELLOW+BOLD,f'[{i+1}]')}  {b['emoji']}  {c(b['color']+BOLD,b['name'])}")
        print(f"       {c(DIM,b['desc'])}")
        for ln in b["prev"]: print(f"       {c(b['color'],ln)}")
        print()
    print(c(BOLD,"  └───────────────────────────────────────────────────────┘"))
def theme_grid():
    print(); print(c(BOLD,"  ┌─ CHOOSE YOUR THEME ──────────────────────────────────┐")); print()
    for i,t in enumerate(THEMES):
        print(f"  {c(YELLOW+BOLD,f'[{i+1}]')}  {t['emoji']}  {c(t['sw']+BOLD,t['name'])}   {pal(t['sw'])}")
        print(f"       {c(DIM,t['desc'])}"); print()
    print(c(BOLD,"  └───────────────────────────────────────────────────────┘"))
def pick(label,mx,default=1):
    while True:
        try:
            raw=input(c(CYAN+BOLD,f"  Choose {label} [1-{mx}] (default {default}): ")).strip()
            if not raw: return default-1
            n=int(raw)
            if 1<=n<=mx: return n-1
            print(c(RED_C,f"  Number between 1 and {mx} please."))
        except (ValueError,EOFError): print(c(RED_C,"  Enter a valid number."))
        except KeyboardInterrupt: print(); return default-1
def load_buddy_mod(bid):
    bf=PI_HOME/"agent"/"buddies"/bid/"buddy.py"
    if not bf.exists(): return None
    spec=importlib.util.spec_from_file_location(f"buddy_{bid}",bf)
    if not spec or not spec.loader: return None
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
def confirm(buddy,theme):
    clear(); print()
    print(c(CYAN+BOLD,"═"*60)); print(c(GREEN+BOLD,"  ✓  Saved!")); print(c(CYAN+BOLD,"═"*60)); print()
    print(f"  {buddy['emoji']}  Buddy:  {c(buddy['color']+BOLD,buddy['name'])}")
    print(f"         {c(DIM,buddy['desc'])}"); print()
    mod=load_buddy_mod(buddy["id"])
    if mod:
        frames=getattr(mod,"FRAMES",{}); col=getattr(mod,"BUDDY_COLOR",buddy["color"])
        frame=(frames.get("happy") or frames.get("idle") or [[]])[0]
        for ln in frame: print(f"  {col}{ln}{RESET}")
        print()
    print(f"  {theme['emoji']}  Theme:  {c(theme['sw']+BOLD,theme['name'])}")
    print(f"         {c(DIM,theme['desc'])}"); print(f"         {pal(theme['sw'])}"); print()
    print(c(DIM,"  "+"─"*56)); print(); print(c(BOLD,"  Next steps:")); print()
    print(f"  1.  {c(YELLOW,'mempalace mine ~/your-project')}  {c(DIM,'— mine your codebase')}")
    print(f"  2.  {c(YELLOW,'edit ~/.pi/env.sh')}  {c(DIM,'— set MINIMAX_API_KEY')}")
    print(f"  3.  {c(DIM,'Open Claude Code — hooks fire automatically')}")
    print(f"  4.  {c(YELLOW,'bash installer/verify.sh')}  {c(DIM,'— confirm install')}")
    print(); print(c(CYAN+BOLD,"═"*60)); print(c(GREEN+BOLD,"  Happy coding!  🚀")); print(c(CYAN+BOLD,"═"*60)); print()
def main():
    clear(); header(); buddy_grid(); b=BUDDIES[pick("your buddy",len(BUDDIES))]
    clear(); header(); theme_grid(); t=THEMES[pick("your theme",len(THEMES))]
    p=load_prefs(); p.update({"buddy":b["id"],"buddy_name":b["name"],"theme":t["id"]}); save_prefs(p)
    src=PI_HOME/"agent"/"themes"/f"{t['id']}.json"; dst=PI_HOME/"active-theme.json"
    if src.exists(): shutil.copy2(src,dst)
    confirm(b,t)
if __name__=="__main__":
    main()
