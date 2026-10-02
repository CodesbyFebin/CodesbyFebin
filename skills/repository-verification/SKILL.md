---
name: repository-verification
description: Verify CodesbyFebin repository capability claims against code, tests, specs, CI and evidence artifacts.
---

# Repository verification

## Verification sequence
1. Read README.md.
2. Read AGENTS.md and llms.txt when present.
3. Identify the exact claim.
4. Locate its implementation path.
5. Locate executable tests or conformance coverage.
6. Check CI/evidence when available.
7. Record explicit limitations.
8. Report VERIFIED only when the inspected evidence supports the claim.

## Preferred states
DESIRED
ADMITTED
EXECUTING
OBSERVED
VERIFIED
SIMULATED
UNKNOWN

Do not substitute one state for another.
