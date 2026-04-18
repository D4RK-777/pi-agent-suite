"""Strip strings/comments/templates from a TS file, then count code-level braces."""
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
# Remove template literals (naive: does not handle nested ${})
src = re.sub(r'`(?:\\.|[^`\\])*`', '``', src, flags=re.DOTALL)

opens = src.count('{')
closes = src.count('}')
print(f"{path}: {{={opens} }}={closes} diff={opens - closes}")
