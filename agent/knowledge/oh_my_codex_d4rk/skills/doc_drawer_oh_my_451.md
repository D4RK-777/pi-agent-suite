PT EXACTLY — do not modify it**:
   ```javascript
   (() => {
     const walk = (el, depth = 0) => {
       if (depth > 8 || !el.tagName) return null;
       const cs = window.getComputedStyle(el);
       return {
         tag: el.tagName.toLowerCase(),
         id: el.id || undefined,
         classes: [...el.classList].slice(0, 5),
         styles: {
           display: cs.display, position: cs.position,
           width: cs.width, height: cs.height,
           padding: cs.padding, margin: cs.margin,
           fontSize: cs.fontSize, fontFamily: cs.fontFamily,
           fontWeight: cs.fontWeight, lineHeight: cs.lineHeight,
           color: cs.color, backgroundColor: cs.backgroundColor,
           border: cs.border, borderRadius: cs.borderRadius,