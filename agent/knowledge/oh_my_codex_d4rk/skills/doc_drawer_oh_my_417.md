t to verify]
     Service: [how to start]
     Test cases: [specific scenarios to verify]")
     ```

2. **CHECK RESULT**: Did the goal pass?
   - **YES** → Exit with success message
   - **NO** → Continue to step 3

3. **ARCHITECT DIAGNOSIS**: Spawn architect to analyze failure
   ```
   delegate(role="architect", tier="THOROUGH", task="DIAGNOSE FAILURE:
   Goal: [goal type]
   Output: [test/build output]
   Provide root cause and specific fix recommendations.")
   ```

4. **FIX ISSUES**: Apply architect's recommendations
   ```
   delegate(role="executor", tier="STANDARD", task="FIX:
   Issue: [architect diagnosis]
   Files: [affected files]
   Apply the fix precisely as recommended.")
   ```

5. **REPEAT**: Go back to step 1

## Exit Conditions