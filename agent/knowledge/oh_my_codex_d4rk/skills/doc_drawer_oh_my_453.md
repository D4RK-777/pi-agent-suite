COPY THIS SCRIPT EXACTLY — do not modify it**:
   ```javascript
   (() => {
     const results = [];
     document.querySelectorAll(
       'button, a[href], input, select, textarea, [role="button"], ' +
       '[onclick], [aria-haspopup], [aria-expanded], details, dialog'
     ).forEach(el => {
       results.push({
         tag: el.tagName.toLowerCase(),
         type: el.type || el.getAttribute('role') || 'interactive',
         text: (el.textContent || '').trim().slice(0, 80),
         href: el.href || undefined,
         ariaLabel: el.getAttribute('aria-label') || undefined,
         isVisible: el.offsetParent !== null,
       });
     });
     return results;
   })()
   ```