#!/usr/bin/env python3
"""
👽 ALIEN BUDDY — Animated Version!

Features:
- Moving tentacles when working
- Eye size changes per mood
- Typing animation

Usage: python buddy-animated.py [mood] [loops]
"""

import sys
import time

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ORANGE = '\033[38;5;208m'
GRAY = '\033[90m'
RESET = '\033[0m'
GREEN = '\033[32m'
RED = '\033[91m'
BLUE = '\033[34m'

# Animation frames for each mood
FRAMES = {
    'idle': [
        # Normal idle - steady
        [
            f'  {ORANGE}▓▓▓▓▓▓▓{RESET}  ',
            f'  {ORANGE}████████{RESET}  ',
            f'  {ORANGE}██ █ ███{RESET}  ',
            f'  {ORANGE}████████{RESET}  ',
            f' {ORANGE}▓▓▓▓▓▓▓▓▓{RESET} ',
            f' {ORANGE}▓{RESET}       {ORANGE}▓{RESET} ',
            f'{ORANGE}▓{RESET}         {ORANGE}▓{RESET}',
        ],
    ],
    
    'thinking': [
        # Big eye - thinking deeply
        [
            f' {ORANGE}▓▓▓▓▓▓▓▓{RESET} ',
            f' {ORANGE}██████████{RESET} ',
            f' {ORANGE}██ ████ ███{RESET} ',
            f' {ORANGE}██████████{RESET} ',
            f'{ORANGE}▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f' {ORANGE}▓{RESET}       {ORANGE}▓{RESET} ',
            f'{ORANGE}▓{RESET}         {ORANGE}▓{RESET}',
        ],
    ],
    
    'working': [
        # Frame 1 - left tentacle up (typing)
        [
            f'{ORANGE}▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f'{ORANGE}████████████{RESET} ',
            f'{ORANGE}███ █ █ ███{RESET} ',
            f'{ORANGE}████████████{RESET} ',
            f'{ORANGE}▓▓▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f' {ORANGE}▓{RESET}       {ORANGE}▓{RESET} ',
            f' {ORANGE}▓{RESET}       {ORANGE}▓{RESET} ',
        ],
        # Frame 2 - right tentacle up (typing)
        [
            f'{ORANGE}▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f'{ORANGE}████████████{RESET} ',
            f'{ORANGE}███ █ █ ███{RESET} ',
            f'{ORANGE}████████████{RESET} ',
            f'{ORANGE}▓▓▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f'         {ORANGE}▓{RESET} ',
            f'         {ORANGE}▓{RESET} ',
        ],
        # Frame 3 - both down (pause)
        [
            f'{ORANGE}▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f'{ORANGE}████████████{RESET} ',
            f'{ORANGE}███ █ █ ███{RESET} ',
            f'{ORANGE}████████████{RESET} ',
            f'{ORANGE}▓▓▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f'  {ORANGE}▓▓▓▓▓▓▓▓{RESET}  ',
            f'  {ORANGE}▓▓▓▓▓▓▓▓{RESET}  ',
        ],
    ],
    
    'typing': [
        # Fast typing animation - multiple frames
        # Strike left
        [
            f'{ORANGE}▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f'{ORANGE}████████████{RESET} ',
            f'{ORANGE}██ █ █ █ ███{RESET} ',
            f'{ORANGE}████████████{RESET} ',
            f'{ORANGE}▓▓▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f'       {ORANGE}▓{RESET}   ',
            f'      {ORANGE}▓{RESET}    ',
        ],
        # Return
        [
            f'{ORANGE}▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f'{ORANGE}████████████{RESET} ',
            f'{ORANGE}██ █ █ █ ███{RESET} ',
            f'{ORANGE}████████████{RESET} ',
            f'{ORANGE}▓▓▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f'    {ORANGE}▓{RESET}     ',
            f'   {ORANGE}▓{RESET}      ',
        ],
        # Strike right
        [
            f'{ORANGE}▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f'{ORANGE}████████████{RESET} ',
            f'{ORANGE}██ █ █ █ ███{RESET} ',
            f'{ORANGE}████████████{RESET} ',
            f'{ORANGE}▓▓▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f'   {ORANGE}▓{RESET}     ',
            f'    {ORANGE}▓{RESET}      ',
        ],
        # Return center
        [
            f'{ORANGE}▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f'{ORANGE}████████████{RESET} ',
            f'{ORANGE}██ █ █ █ ███{RESET} ',
            f'{ORANGE}████████████{RESET} ',
            f'{ORANGE}▓▓▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f'  {ORANGE}▓▓▓▓▓▓▓▓{RESET}  ',
            f'  {ORANGE}▓▓▓▓▓▓▓▓{RESET}  ',
        ],
    ],
    
    'happy': [
        # Happy with medium eyes
        [
            f'  {ORANGE}▓▓▓▓▓▓▓{RESET}  ',
            f'  {ORANGE}████████{RESET}  ',
            f'  {ORANGE}██ █ █ █{RESET}  ',
            f'  {ORANGE}████████{RESET}  ',
            f' {ORANGE}▓▓▓▓▓▓▓▓▓{RESET} ',
            f' {ORANGE}▓{RESET}       {ORANGE}▓{RESET} ',
            f'{ORANGE}▓{RESET}         {ORANGE}▓{RESET}',
        ],
        # Winking
        [
            f'  {ORANGE}▓▓▓▓▓▓▓{RESET}  ',
            f'  {ORANGE}████████{RESET}  ',
            f'  {ORANGE}██ ████{RESET}  ',
            f'  {ORANGE}████████{RESET}  ',
            f' {ORANGE}▓▓▓▓▓▓▓▓▓{RESET} ',
            f' {ORANGE}▓{RESET}       {ORANGE}▓{RESET} ',
            f'{ORANGE}▓{RESET}         {ORANGE}▓{RESET}',
        ],
    ],
    
    'celebrating': [
        # Big excited eyes + jumping
        [
            f' {ORANGE}▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f' {ORANGE}████████████{RESET} ',
            f' {ORANGE}███ █ █ ███{RESET} ',
            f' {ORANGE}████████████{RESET} ',
            f'{ORANGE}▓▓▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f' {ORANGE}▓{RESET}         {ORANGE}▓{RESET} ',
            f'{ORANGE}▓{RESET}           {ORANGE}▓{RESET}',
        ],
        # Jump up
        [
            f'  {ORANGE}▓▓▓▓▓▓▓▓▓{RESET}  ',
            f'  {ORANGE}████████████{RESET}  ',
            f'  {ORANGE}███ █ █ ███{RESET}  ',
            f'  {ORANGE}████████████{RESET}  ',
            f' {ORANGE}▓▓▓▓▓▓▓▓▓▓▓▓{RESET} ',
            f'{ORANGE}▓{RESET}           {ORANGE}▓{RESET}',
            f'              ',
        ],
    ],
    
    'sad': [
        # Droopy sad face
        [
            f'  {ORANGE}▓▓▓▓▓▓▓{RESET}  ',
            f'  {ORANGE}████████{RESET}  ',
            f'  {ORANGE}██ █ ███{RESET}  ',
            f'  {ORANGE}████████{RESET}  ',
            f' {ORANGE}▓▓▓▓▓▓▓▓▓{RESET} ',
            f' {ORANGE}▓{RESET}       {ORANGE}▓{RESET} ',
            f'{GRAY}░░       ░░{RESET}',
        ],
        # Crying
        [
            f'  {ORANGE}▓▓▓▓▓▓▓{RESET}  ',
            f'  {ORANGE}████████{RESET}  ',
            f'  {ORANGE}██ █ ███{RESET}  ',
            f'  {ORANGE}████████{RESET}  ',
            f' {ORANGE}▓▓▓▓▓▓▓▓▓{RESET} ',
            f' {ORANGE}▓{RESET}       {ORANGE}▓{RESET} ',
            f'{GRAY}░░  ▓▓  ░░{RESET}',
        ],
    ],
    
    'error': [
        # X eyes
        [
            f'  {ORANGE}▓▓▓▓▓▓▓{RESET}  ',
            f'  {ORANGE}████████{RESET}  ',
            f'  {ORANGE}██ █ ███{RESET}  ',
            f'  {ORANGE}████████{RESET}  ',
            f' {ORANGE}▓▓▓▓▓▓▓▓▓{RESET} ',
            f' {ORANGE}▓{RESET}       {ORANGE}▓{RESET} ',
            f'{ORANGE}▓{RESET}  {RED}███{RESET}  {ORANGE}▓{RESET}',
        ],
    ],
    
    'sleeping': [
        # Closed eyes (horizontal line), zzz
        [
            f'  {ORANGE}▓▓▓▓▓▓▓{RESET}  ',
            f'  {ORANGE}████████{RESET}  ',
            f'  {ORANGE}██ ████ ███{RESET}  ',
            f'  {ORANGE}████████{RESET}  ',
            f' {ORANGE}▓▓▓▓▓▓▓▓▓{RESET} ',
            f' {ORANGE}▓{RESET}       {ORANGE}▓{RESET} ',
            f'{ORANGE}▓{RESET}   {BLUE}z{RESET}   {ORANGE}▓{RESET}',
        ],
        # Deep sleep
        [
            f'  {ORANGE}▓▓▓▓▓▓▓{RESET}  ',
            f'  {ORANGE}████████{RESET}  ',
            f'  {ORANGE}██ ████ ███{RESET}  ',
            f'  {ORANGE}████████{RESET}  ',
            f' {ORANGE}▓▓▓▓▓▓▓▓▓{RESET} ',
            f' {ORANGE}▓{RESET}       {ORANGE}▓{RESET} ',
            f'{ORANGE}▓{RESET}  {BLUE}ZZ{RESET}  {ORANGE}▓{RESET}',
        ],
    ],
}


def clear_screen():
    """Clear terminal"""
    print('\033[2J\033[H', end='')


def print_at_center(lines):
    """Print lines centered"""
    for line in lines:
        print(line)


def animate(mood='idle', loops=5, delay=0.3):
    """Animate the buddy"""
    frames = FRAMES.get(mood, FRAMES['idle'])
    
    for _ in range(loops):
        for i, frame in enumerate(frames):
            clear_screen()
            print_at_center(frame)
            time.sleep(delay if mood != 'typing' else 0.15)


def main():
    import argparse
    parser = argparse.ArgumentParser(description='👽 Alien Buddy - Animated!')
    parser.add_argument('mood', nargs='?', default='idle',
                        choices=['idle', 'thinking', 'working', 'typing', 'happy', 'celebrating', 'sad', 'error', 'sleeping'],
                        help='Mood to display')
    parser.add_argument('-l', '--loops', type=int, default=10,
                        help='Number of animation loops')
    parser.add_argument('-d', '--delay', type=float, default=0.4,
                        help='Delay between frames (seconds)')
    args = parser.parse_args()
    
    print(f'👽 Alien Buddy - {args.mood} mode (Ctrl+C to stop)')
    print()
    
    try:
        animate(args.mood, loops=args.loops, delay=args.delay)
    except KeyboardInterrupt:
        print()
        print('👋 Bye!')


if __name__ == '__main__':
    main()
