del Consultation (Preferred)

The security-reviewer agent SHOULD consult Codex for cross-validation.

### Protocol
1. **Form your OWN security analysis FIRST** - Complete the review independently
2. **Consult for validation** - Cross-check findings with Codex
3. **Critically evaluate** - Never blindly adopt external findings
4. **Graceful fallback** - Never block if tools unavailable

### When to Consult
- Authentication/authorization code
- Cryptographic implementations
- Input validation for untrusted data
- High-risk vulnerability patterns
- Production deployment code

### When to Skip
- Low-risk utility code
- Well-audited patterns
- Time-critical security assessments
- Code with existing security tests