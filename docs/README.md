# PolicyForge

**Enterprise Security Policy & Governance Suite for FinNexus Solutions**

A complete, authored information security policy suite demonstrating three pillars of enterprise security management - not a collection of generic templates.

[![GitHub Pages](https://img.shields.io/badge/docs-live-6366f1?style=flat-square&logo=github)](https://dedsec-terminal.github.io/PolicyForge/)

---

## What's in here

| Directory | Contents |
|---|---|
| [Context](https://dedsec-terminal.github.io/PolicyForge/#org-profile) | Organisational profile, risk appetite, and operational baseline |
| [Policies](https://dedsec-terminal.github.io/PolicyForge/#acceptable-use) | Eight authored control policies (Access, Incident Response, etc.) |
| [Mapping](https://dedsec-terminal.github.io/PolicyForge/#ctm) | Control Traceability Matrix - ISO 27001, NIST CSF, PCI DSS, DPDPA, GDPR |
| [Register](https://dedsec-terminal.github.io/PolicyForge/#exception-log) | Exception log and review cadence tracker |
| [Docs](https://dedsec-terminal.github.io/PolicyForge/) | GitHub Pages source for the online documentation viewer |

## Three core pillars

1. **Authored security policy** - policies tailored to a specific organisational profile and risk appetite, not boilerplate.
2. **Independent control traceability** - every internal control mapped to primary-source requirements across five frameworks, then independently audited in [CTM Audit Report](https://dedsec-terminal.github.io/PolicyForge/#ctm-audit).
3. **Operational governance lifecycle** - exception management and review cadences that reflect a living security program, not a point-in-time snapshot.

## How to read this

Follow a control end-to-end through the traceability chain:

- **PA-04** (Password Policy) satisfies **PCI DSS v4.0.1 Req 8.3.9** on deprecating arbitrary time-based expiry
- **IR-06** (Incident Response) maps to **GDPR Art. 33/34** and **DPDPA s.8(6)** for mandatory breach notification
- **AM-04** (Access Management) satisfies **ISO 27001:2022 A.8.5** enforcing MFA and deprecating SMS OTP

> Control **PA-10** (continuous monitoring of compromised credentials) is flagged open pending DPO/Legal sign-off - an intentional reflection of real-world governance where technical controls negotiate with privacy constraints before ratification.

## Documentation viewer

Browse all documents online: **[dedsec-terminal.github.io/PolicyForge](https://dedsec-terminal.github.io/PolicyForge/)**
