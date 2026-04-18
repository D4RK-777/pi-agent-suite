"""Line-by-line brace trace for a TS file. Used to find imbalances."""
import re
import sys

path = sys.argv[1]
src = open(path, encoding='utf-8').read()

# Remove line comments
src = re.sub(r'//[^\n]*', '', src)
# Remove block comments
src = re.sub(r'/\*.*?\*/', '', src, flags=re.DOTALL)
# Remove double-quoted strings
src = re.sub(r'"(?:\\.|[^"\\])*"', '""', src)
# Remove single-quoted strings
src = re.sub(r"'(?:\\.|[^'\\])*'", "''", src)
# Remove template literals
src = re.sub(r'`(?:\\.|[^`\\])*`', '``', src, flags=re.DOTALL)

lines = src.split('\n')
balance = 0
for i, line in enumerate(lines, 1):
    o = line.count('{')
    c = line.count('}')
    if o != c:
        balance += (o - c)
        print(f'L{i:3d}  +{o} -{c}  cum={balance:+d}  | {line.strip()[:80]}')
print(f'\nFinal balance: {balance}')
