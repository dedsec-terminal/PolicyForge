# PolicyForge

**Enterprise Security Policy & Governance Suite for FinNexus Solutions**

A complete, authored information security policy suite demonstrating three pillars of enterprise security management—moving beyond generic templates into actionable, audit-ready governance.

[![GitHub Pages](https://img.shields.io/badge/docs-live-6366f1?style=flat-square&logo=github)](https://dedsec-terminal.github.io/PolicyForge/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## What This Is

PolicyForge is a polished, authored enterprise security policy suite designed for a hypothetical fintech environment ("FinNexus Solutions"). It demonstrates a complete operational governance lifecycle:
1. **Organizational profile and authoring style guide** defining the scope and standards.
2. **Concise, RFC-2119-style policy documents** translating regulatory clauses into enforceable, verifiable controls.
3. **Control traceability mapping** (CTM) directly linking internal safeguards to major compliance frameworks.
4. **Active governance registers** tracking exceptions and review cadences to reflect a living security program.

This repository serves as a documentation-first portfolio project, showcasing applied GRC (Governance, Risk, and Compliance) design, control traceability, and audit readiness for GRC, IT Audit, and Security Management professionals.

### The Stack & Frameworks
- **Language / Formats:** Markdown (policy & docs content); CSV (governance registers).
- **Framework / Runtime:** Static documentation published via GitHub Pages.
- **Authoritative Frameworks Mapped:** ISO/IEC 27001:2022, NIST CSF 2.0, PCI DSS v4.0.1, DPDP Act 2023, and GDPR.

## How It's Organized

`	ext
.github/                       # GitHub workflow and Pages helpers
docs/                          # GitHub Pages copy of the documentation viewer
context/
  org-profile.md               # Organizational profile & regulatory scope
  policy-style-guide.md        # Authoring rules, control ID registry & canonical example
mapping/
  control-traceability-matrix.md # CTM linking safeguards to frameworks
  ctm_audit_report.md          # Independent assessment of the traceability matrix
policies/
  acceptable-use.md            # Acceptable Use (AU) policy
  access-management.md         # Access Management (AM) policy
  asset-management.md          # Asset Management (AS) policy
  business-continuity-backup.md # Business Continuity & Disaster Recovery (BC)
  data-classification-handling.md # Data Classification & Handling (DC)
  incident-response.md         # Incident Response (IR)
  password-authentication.md   # Password & Authentication (PA)
  vendor-third-party-risk.md   # Vendor & Third-Party Risk (VR)
register/
  exception-log.md             # Exception register (with entries) + CSV
  review-cadence-tracker.md    # Review cadence tracker + CSV
`

### How It Fits Together
- The **org-profile** sets the scope and risk appetite used by the policies. 
- The **policy-style-guide** enforces consistent structure and numbering (e.g., AM-01, DC-01). 
- Each policy file contains numbered safeguards with explicit framework citations. 
- The **mapping/** artifacts detail the CTM maintenance approach and provide the actual matrix, allowing auditors to tie every safeguard to specific framework clauses. 
- The **egister/** files provide operational governance artifacts (exceptions + review cadence) that prove a living program, not a static binder of rules. 
- The **docs/** folder is the published GitHub Pages site for frictionless presentation.

## How to Run It

1. **View the live site (Best for presentation & demo):**
   - Open: [https://dedsec-terminal.github.io/PolicyForge/](https://dedsec-terminal.github.io/PolicyForge/)

2. **Clone and review locally:**
   `ash
   git clone https://github.com/dedsec-terminal/PolicyForge.git
   cd PolicyForge
   `
   Open the Markdown files directly in your preferred editor (VS Code, Obsidian, etc.), or serve the docs/ folder locally:
   `ash
   python -m http.server 8000 --directory docs
   # Open http://localhost:8000 in your browser
   `

*No build configuration, environment variables, or secrets are required—the repository is entirely documentation-driven.*

## Key Artifacts to Highlight

For professionals presenting this suite in a portfolio or interview:

- **context/org-profile.md** — Demonstrates advanced scoping and regulatory analysis (DPDP Act, GDPR, PCI DSS).
- **context/policy-style-guide.md** — Shows governance of authoring standards, naming conventions, RFC-2119 discipline, and a canonical policy example (highlighting process-oriented thinking).
- **policies/*.md** — Eight full, authored policy documents with numbered safeguards and framework mappings, demonstrating domain knowledge and the ability to translate requirements into enforceable controls.
- **mapping/control-traceability-matrix.md** — The CTM methodology and matrix: proves absolute traceability, reduces pre-audit review time, and enables targeted audit evidence collection.
- **egister/exception-log.md** & **eview-cadence-tracker.md** — Demonstrates real-world operational governance including time-bound exceptions, compensating controls, and CISO sign-off workflows.

## License

This project is licensed under the [MIT License](LICENSE).
