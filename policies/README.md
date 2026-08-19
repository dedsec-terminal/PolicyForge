# Security Policies Directory

This directory contains the individual, modular security policy documents for **FinNexus Solutions**.

## Authoring Standards & Conventions

Every policy document in this directory must adhere to the standard template structure:

1. **Metadata Header:** Document ID, Version, Status, Effective Date, Owner (e.g., CISO), Approver, and Classification.
2. **Purpose & Scope:** Clear articulation of intent and boundary (systems, employees, vendors).
3. **Policy Statements:** Actionable, enforceable requirements (using RFC 2119 keywords: MUST, MUST NOT, SHOULD, MAY).
4. **Roles & Responsibilities:** Segregation of duties across CISO, IT, Engineering, Legal, and HR.
5. **Compliance & Framework Alignment:** Explicit citations to ISO 27001:2022, NIST CSF 2.0, PCI DSS v4.0.1, and DPDPA/GDPR.
6. **Enforcement & Disciplinary Action:** Consequences of violation.
7. **Revision History:** Version tracking table.

## Naming Convention

- File names should use kebab-case: `[domain]-policy.md` (e.g., `access-control-policy.md`, `data-protection-privacy-policy.md`, `incident-response-policy.md`).
