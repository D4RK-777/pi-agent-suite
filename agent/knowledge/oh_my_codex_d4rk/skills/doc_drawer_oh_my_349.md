NT=$(find "$HOME/.codex/skills" -name "*.md" 2>/dev/null | wc -l)
  echo "Total skills: $USER_COUNT"

  if [ $USER_COUNT -gt 0 ]; then
    echo ""
    echo "Skills found:"
    find "$HOME/.codex/skills" -name "*.md" -type f -exec sh -c '
      FILE="$1"
      NAME=$(grep -m1 "^name:" "$FILE" 2>/dev/null | sed "s/name: //")
      DESC=$(grep -m1 "^description:" "$FILE" 2>/dev/null | sed "s/description: //")
      MODIFIED=$(stat -c "%y" "$FILE" 2>/dev/null || stat -f "%Sm" "$FILE" 2>/dev/null)
      echo "  - $NAME"
      [ -n "$DESC" ] && echo "    Description: $DESC"
      echo "    Modified: $MODIFIED"
      echo ""
    ' sh {} \;
  fi
else
  echo "Directory not found"
fi