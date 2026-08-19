# PolicyForge

[![Live policy suite](https://img.shields.io/badge/Live%20suite-GitHub%20Pages-6366f1?style=flat-square&logo=github)](https://dedsec-terminal.github.io/PolicyForge/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

**PolicyForge** is a portfolio-grade information-security governance suite for the fictional fintech organisation **FinNexus Solutions**. It shows how a policy programme can move from business context to enforceable controls, evidence expectations, traceability, and ongoing governance.

> This is a demonstration artefact, not legal advice or a complete compliance programme. Organisations should tailor the materials, control owners, risk assessments, and legal obligations to their own environment.

## Start here

- **[Browse the live policy suite](https://dedsec-terminal.github.io/PolicyForge/)** for the best reading experience.
- Read the [organisation profile](context/org-profile.md) first. It defines FinNexus's scope, operating model, regulatory context, and risk appetite.
- Review the [policy style guide](context/policy-style-guide.md) to understand the drafting conventions and control-ID format.
- Use the [control traceability matrix](mapping/control-traceability-matrix.md) to trace controls to the mapped frameworks.

## What the repository demonstrates

| Capability | Evidence in this repository |
| --- | --- |
| Governance scope and accountability | [Organisation profile](context/org-profile.md) and [policy style guide](context/policy-style-guide.md) |
| Enforceable security requirements | Eight focused policies with numbered safeguards and normative language |
| Control-to-framework traceability | [Control traceability matrix](mapping/control-traceability-matrix.md) and [audit report](mapping/ctm_audit_report.md) |
| Operational governance | [Exception log](register/exception-log.md) and [review cadence tracker](register/review-cadence-tracker.md) |

The suite maps controls to ISO/IEC 27001:2022, NIST CSF 2.0, PCI DSS v4.0.1, the Digital Personal Data Protection Act, 2023 (India), and the GDPR. A framework citation supports traceability; it does not by itself establish compliance.

## Repository map

```text
context/                       # Organisation context and policy-authoring standards
  org-profile.md               # Read first: scope, risk appetite, regulatory context
  policy-style-guide.md        # Drafting rules and control-ID conventions
policies/                      # Authoritative policy source documents
  acceptable-use.md
  access-management.md
  asset-management.md
  business-continuity-backup.md
  data-classification-handling.md
  incident-response.md
  password-authentication.md
  vendor-third-party-risk.md
mapping/                       # Control traceability and its independent review
register/                      # Exception and review-cadence governance records
docs/index.html                # Hand-authored GitHub Pages viewer
.github/workflows/             # Builds and deploys the viewer from source documents
```

## How the programme fits together

```text
Organisation profile
        ↓
Policy style guide ──→ Policies and control IDs
        ↓                       ↓
Review / exception registers ← Control traceability matrix ← Framework requirements
```

The Markdown outside `docs/` is the source of truth. On every push to `main`, GitHub Actions assembles a temporary Pages site from those source documents and `docs/index.html`, then deploys it. The generated document copies are deliberately not versioned in this repository.

## Review the suite locally

No build tools, dependencies, credentials, or environment variables are required to review the source documents.

```bash
git clone https://github.com/dedsec-terminal/PolicyForge.git
cd PolicyForge
```

Open the Markdown files in your editor, or serve the deployed viewer after creating its generated site output through the GitHub Actions workflow. The live site is the simplest option for navigating the complete set.

## Suggested review path

1. Start with the [organisation profile](context/org-profile.md).
2. Read the [policy style guide](context/policy-style-guide.md), then the policies relevant to your domain.
3. Inspect the [control traceability matrix](mapping/control-traceability-matrix.md) and its [audit report](mapping/ctm_audit_report.md).
4. Close with the [exception log](register/exception-log.md) and [review cadence tracker](register/review-cadence-tracker.md) to see how the programme is maintained.

## License

Distributed under the [MIT License](LICENSE).
