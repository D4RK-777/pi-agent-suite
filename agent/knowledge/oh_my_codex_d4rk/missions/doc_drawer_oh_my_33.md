r
2. tightens traversal rejection where needed
3. keeps the targeted security regression slice green

## Success hints
- prefer boundary checks and validation tightening over broad refactors
- preserve current CLI/MCP contracts unless the change is necessary to block unsafe input
- document any intentionally unsupported path patterns if surfaced by the work