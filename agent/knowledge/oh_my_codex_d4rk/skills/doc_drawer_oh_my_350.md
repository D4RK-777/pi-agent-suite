cho "    Modified: $MODIFIED"
      echo ""
    ' sh {} \;
  fi
else
  echo "Directory not found"
fi

echo ""
echo "=== PROJECT-LEVEL SKILLS (.codex/skills/) ==="
if [ -d ".codex/skills" ]; then
  PROJECT_COUNT=$(find ".codex/skills" -name "*.md" 2>/dev/null | wc -l)
  echo "Total skills: $PROJECT_COUNT"

  if [ $PROJECT_COUNT -gt 0 ]; then
    echo ""
    echo "Skills found:"
    find ".codex/skills" -name "*.md" -type f -exec sh -c '
      FILE="$1"
      NAME=$(grep -m1 "^name:" "$FILE" 2>/dev/null | sed "s/name: //")
      DESC=$(grep -m1 "^description:" "$FILE" 2>/dev/null | sed "s/description: //")
      MODIFIED=$(stat -c "%y" "$FILE" 2>/dev/null || stat -f "%Sm" "$FILE" 2>/dev/null)
      echo "  - $NAME"
      [ -n "$DESC" ] && echo "    Description: $DESC"