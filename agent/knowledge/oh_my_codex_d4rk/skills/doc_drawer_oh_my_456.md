- Dropdowns/modals → show/hide toggle with transitions
   - Accordions/tabs → state-based visibility

4. **Extract design tokens**: Identify recurring values:
   - Color palette (primary, secondary, background, text colors)
   - Font stack (families, size scale, weight scale)
   - Spacing scale (padding/margin patterns)
   - Border radius values

5. **Define file structure**:
   ```
   {output_dir}/
   ├── index.html          (or App.tsx / App.vue)
   ├── styles/
   │   ├── globals.css      (reset + tokens)
   │   └── components.css   (or scoped styles)
   ├── scripts/
   │   └── interactions.js  (toggle, modal, dropdown logic)
   └── assets/              (placeholder images)
   ```
   Adapt to `tech_stack` if specified (React components, Vue SFCs, etc.).

## Pass 3 — Generate Clone