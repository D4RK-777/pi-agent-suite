isVisible: el.offsetParent !== null,
       });
     });
     return results;
   })()
   ```
7. **Network patterns** (optional): `browser_network_requests` — note XHR/fetch calls for reference. Do not attempt to replicate backends.

Keep all extraction results in working memory for Pass 2.

## Pass 2 — Build Plan

Analyze extraction results and decompose into a component plan.

1. **Identify page regions**: From DOM tree + accessibility snapshot, identify major sections:
   - Navigation bar / header
   - Hero / banner section
   - Main content area(s)
   - Sidebar (if present)
   - Footer
   - Overlay elements (modals, drawers)