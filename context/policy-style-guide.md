# PolicyForge Policy Style Guide

> **Audience:** Policy authors and reviewers.
> **Purpose:** Establish consistent structure, tone, and specificity across FinNexus Solutions policy documents.
> **Scope:** The eight documents in [`policies/`](../policies/). The organisation profile, mapping artefacts, registers, README, and Pages viewer have their own purpose and are not policy templates.

This guide establishes the common drafting discipline and quality checks for the policy suite. It is intentionally concise: the canonical implementation is the [Data Classification & Handling Policy](../policies/data-classification-handling.md), not a duplicate copy of it.

## 1. Required Policy Structure

Every policy uses the following sequence. A domain-specific taxonomy may be inserted between Scope and Policy Statements when it materially aids interpretation.

1. `# [Policy Title]`
2. Document-control metadata table
3. `---`
4. `## 1. Purpose`
5. `## 2. Scope`
6. Optional `## 3. [Domain taxonomy]`
7. `## [3 or 4]. Policy Statements`
8. `## [next]. Roles and Responsibilities`
9. `## [next]. Enforcement and Sanctions`
10. `## [next]. Review Cadence`
11. `## [next]. Revision History`

Use a horizontal rule after the metadata table, between safeguards, and before each subsequent top-level governance section.

## 2. Document-Control Metadata

Place this table immediately beneath the H1. Keep fields in this order.

```markdown
| Field | Details |
| :--- | :--- |
| **Policy ID** | [Two-letter prefix] |
| **Document Title** | [Full policy name] |
| **Version** | X.X |
| **Status** | Draft (illustrative) |
| **Classification** | Internal - Restricted or Internal - General |
| **Effective Date** | DD.MM.YY |
| **Last Reviewed** | DD.MM.YY |
| **Next Review Due** | DD.MM.YY |
| **Policy Owner** | [Role], FinNexus Solutions |
| **Approved By** | [Role(s)], FinNexus Solutions |
| **Framework Alignment** | Specific ISO, NIST, PCI DSS, DPDP, and GDPR references as applicable |
```

`X.X` and the date placeholders are deliberate portfolio placeholders. Do not invent an approval date, adopted version, or operating status. If this suite is adopted, replace them through the formal document-control process.

## 3. Policy Statements and Safeguards

Each safeguard is an H3 using a unique, sequential control ID.

```markdown
### [PREFIX]-[NN] - [Short Descriptive Title]

[Clear requirement text or structured bullets.]

> **Framework Mapping:** [Specific framework references]

---
```

- Use a two-letter uppercase prefix and zero-padded number, for example `AM-01`.
- Provide 10–11 safeguards unless the domain has a documented reason to vary.
- State an actionable control outcome using RFC 2119 keywords (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`) for normative requirements.
- Name FinNexus Solutions and accountable roles where that improves clarity. Avoid vague owners such as “management” or “the security team.”
- Specify the mechanism, timeframe, evidence, or named standard when it is material. For example, use “TLS 1.2 or higher” rather than “appropriate encryption.”
- Include a framework-mapping block for every safeguard and separate safeguards with `---`.
- Do not use H4 or deeper headings inside a safeguard; use concise paragraphs, bullets, or bold labels instead.

Use control IDs for cross-policy references, such as “per AM-01.” Links to a governance register may use an in-site anchor when it helps a reader navigate the published viewer.

## 4. Governance Sections

### Roles and Responsibilities

Use a two-column table headed `Role` and `Responsibilities`. Assign named roles and describe their concrete duties; do not restate the policy controls verbatim.

### Enforcement and Sanctions

Use all three tiers below. Each tier needs a domain-relevant example and consequence.

```markdown
- **Tier 1 - Minor Breach** (e.g., [concrete example]): [consequence].
- **Tier 2 - Moderate Breach** (e.g., [concrete example]): [consequence]; escalation to HR.
- **Tier 3 - Severe Breach** (e.g., [concrete example]): suspension pending investigation; potential termination or legal referral; regulatory-notification assessment where applicable.
```

For a policy that can involve a personal-data breach, Tier 3 must refer to the Indian IT Act 2000, the DPDP Act 2023, and the relevant notification authorities where applicable.

### Review Cadence

Use the following table and specify triggers relevant to the policy’s domain.

```markdown
| Attribute | Details |
| :--- | :--- |
| **Standard Review Frequency** | Annual (every 12 months from effective date) |
| **Triggered Review Criteria** | [2–4 domain-specific triggers] |
| **Policy Owner (Review Lead)** | [Specific role] |
| **Review Approver** | CISO [and another approver where warranted] |
| **Next Scheduled Review** | DD.MM.YY |
```

### Revision History

Use a four-column table with `Version`, `Date`, `Author`, and `Summary of Changes`. Keep placeholder values while the policy remains illustrative.

## 5. Control-ID Registry

| Prefix | Policy | Control Range | Source |
| :--- | :--- | :--- | :--- |
| `AM` | Access Management | AM-01 to AM-10 | [`access-management.md`](../policies/access-management.md) |
| `AU` | Acceptable Use | AU-01 to AU-10 | [`acceptable-use.md`](../policies/acceptable-use.md) |
| `AS` | Asset Management | AS-01 to AS-10 | [`asset-management.md`](../policies/asset-management.md) |
| `BC` | Business Continuity & Backup | BC-01 to BC-11 | [`business-continuity-backup.md`](../policies/business-continuity-backup.md) |
| `DC` | Data Classification & Handling | DC-01 to DC-11 | [`data-classification-handling.md`](../policies/data-classification-handling.md) |
| `IR` | Incident Response | IR-01 to IR-10 | [`incident-response.md`](../policies/incident-response.md) |
| `PA` | Password & Authentication | PA-01 to PA-11 | [`password-authentication.md`](../policies/password-authentication.md) |
| `VR` | Vendor & Third-Party Risk | VR-01 to VR-10 | [`vendor-third-party-risk.md`](../policies/vendor-third-party-risk.md) |

Before adding a policy, reserve a new unused two-letter prefix, document it here, and add every new control to the control traceability matrix.

## 6. Author Quality Check

Before submitting a policy, confirm that:

- the document-control fields are complete, ordered, and use portfolio placeholders where applicable;
- control IDs are unique, sequential, and match the assigned prefix;
- every safeguard has a specific framework mapping and separator;
- roles, three enforcement tiers, review cadence, and revision history are present;
- requirements are testable and use precise ownership, mechanisms, or timeframes;
- policy-to-policy references use control IDs; and
- the policy, control traceability matrix, and review-cadence tracker remain consistent.
