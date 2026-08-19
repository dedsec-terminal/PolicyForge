# PolicyForge

**Enterprise Security Policy & Governance Suite for FinNexus Solutions**

A complete, authored information security policy suite demonstrating three pillars of enterprise security management — not a collection of generic templates.

[![GitHub Pages](https://img.shields.io/badge/docs-live-6366f1?style=flat-square&logo=github)](https://dedsec-terminal.github.io/PolicyForge/)

---

## What's in here

| Directory | Contents |
|---|---|
| [`/context`](context/org-profile.md) | Organisational profile, risk appetite, and operational baseline |
| [`/policies`](policies/) | Eight authored control policies (Access, Incident Response, etc.) |
| [`/mapping`](mapping/control-traceability-matrix.md) | Control Traceability Matrix — ISO 27001, NIST CSF, PCI DSS, DPDPA, GDPR |
| [`/register`](register/) | Exception log and review cadence tracker |
| [`/docs`](docs/index.html) | GitHub Pages source for the online documentation viewer |

## Three core pillars

1. **Authored security policy** — policies tailored to a specific organisational profile and risk appetite, not boilerplate.
2. **Independent control traceability** — every internal control mapped to primary-source requirements across five frameworks, then independently audited in [`ctm_audit_report.md`](mapping/ctm_audit_report.md).
3. **Operational governance lifecycle** — exception management and review cadences that reflect a living security program, not a point-in-time snapshot.

## How to read this

Follow a control end-to-end through the traceability chain:

- **PA-04** (Password Policy) → satisfies **PCI DSS v4.0.1 Req 8.3.9** on deprecating arbitrary time-based expiry
- **IR-06** (Incident Response) → maps to **GDPR Art. 33/34** and **DPDPA s.8(6)** for mandatory breach notification
- **AM-04** (Access Management) → satisfies **ISO 27001:2022 A.8.5** enforcing MFA and deprecating SMS OTP

> Control **PA-10** (continuous monitoring of compromised credentials) is flagged open pending DPO/Legal sign-off — an intentional reflection of real-world governance where technical controls negotiate with privacy constraints before ratification.

## Documentation viewer

Browse all documents online: **[dedsec-terminal.github.io/PolicyForge](https://dedsec-terminal.github.io/PolicyForge/)**
