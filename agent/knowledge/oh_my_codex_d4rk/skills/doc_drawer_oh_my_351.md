m" "$FILE" 2>/dev/null)
      echo "  - $NAME"
      [ -n "$DESC" ] && echo "    Description: $DESC"
      echo "    Modified: $MODIFIED"
      echo ""
    ' sh {} \;
  fi
else
  echo "Directory not found"
fi

# Summary
TOTAL=$((USER_COUNT + PROJECT_COUNT))
echo "=== SUMMARY ==="
echo "Total skills across all directories: $TOTAL"
```

#### Step 3: Quick Actions Menu

After scanning, use the AskUserQuestion tool to offer these options:

**Question:** "What would you like to do with your local skills?"