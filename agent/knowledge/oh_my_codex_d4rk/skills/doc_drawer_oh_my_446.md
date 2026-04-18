<State_Management>
Persist extraction and progress data so the pipeline can resume if interrupted.

- **After Pass 1 completes**: Write extraction summary to `.omx/state/{scope}/web-clone-extraction.json` containing:
  - `target_url`, `extracted_at` timestamp
  - `screenshot_path` (path to `target-full.png`)
  - `landmark_count` (number of nav, main, footer, form elements)
  - `interactive_count` (number of detected interactive elements)
  - `extraction_size_kb` (approximate size of DOM extraction data)
- **After each Pass 4 verification**: Append the composite verdict to `.omx/state/{scope}/web-clone-verdicts.json`.