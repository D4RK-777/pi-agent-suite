r, backgroundColor: cs.backgroundColor,
           border: cs.border, borderRadius: cs.borderRadius,
           flexDirection: cs.flexDirection, justifyContent: cs.justifyContent,
           alignItems: cs.alignItems, gap: cs.gap,
           gridTemplateColumns: cs.gridTemplateColumns,
         },
         text: el.childNodes.length === 1 && el.childNodes[0].nodeType === 3
           ? el.textContent?.trim().slice(0, 100) : undefined,
         children: [...el.children].map(c => walk(c, depth + 1)).filter(Boolean),
       };
     };
     return walk(document.body);
   })()
   ```
6. **Interactive elements**: `browser_evaluate` to catalog all interactable elements. **COPY THIS SCRIPT EXACTLY — do not modify it**:
   ```javascript
   (() => {
     const results = [];