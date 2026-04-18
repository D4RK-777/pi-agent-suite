rovides the `--prd` flag, initialize a Product Requirements Document before starting the ralph loop.

### Detecting PRD Mode
Check if `{{PROMPT}}` contains `--prd` or `--PRD`.

### Detecting `--no-deslop`
Check if `{{PROMPT}}` contains `--no-deslop`.
If `--no-deslop` is present, skip the deslop pass entirely after Step 7 and continue using the latest successful pre-deslop verification evidence.

### Visual Reference Flags (Optional)
Ralph execution supports visual reference flags for screenshot tasks:
- Repeatable image inputs: `-i <image-path>` (can be used multiple times)
- Image directory input: `--images-dir <directory>`

Example:
`ralph -i refs/hn.png -i refs/hn-item.png --images-dir ./screenshots "match HackerNews layout"`