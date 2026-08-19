# PolicyForge: Policy Style Guide & Authoring Reference

> **Audience:** Any agent or author generating a new security policy for the PolicyForge suite.
> **Purpose:** Enforce structural, tonal, and specificity consistency across all FinNexus Solutions policy documents.
> Read this file in full before writing any policy. Deviate from nothing in it without explicit instruction.

---

## Part 1: Extracted Style Rules (from AM, AU, DC Policies)

### 1.1 Mandatory Document Heading Order

Every policy MUST follow this exact top-to-bottom section order — no reordering, no omissions:

1. `# [Policy Title]` — H1, title only, no subtitle
2. **Metadata table** — immediately below H1, no blank H2 separating them
3. `---` (horizontal rule) — separates every top-level section
4. `## 1. Purpose` — 2–3 paragraphs; opens with "FinNexus Solutions" (never "our organization" or "the company")
5. `## 2. Scope` — bullet list of who/what/where it covers; ends with one scoping exclusion sentence
6. `## 3. [Domain-Specific Section]` *(optional)* — used when the domain warrants a reference table or taxonomy before the control statements (e.g., classification tiers, threat categories). Omit if there is no natural pre-amble taxonomy.
7. `## [3 or 4]. Policy Statements` — contains all numbered safeguards as H3 sub-headings
8. `## [next]. Roles and Responsibilities` — formatted as a markdown table (Role | Responsibilities column headers)
9. `## [next]. Enforcement and Sanctions` — tiered Tier 1/2/3 violation model (see 1.5)
10. `## [next]. Review Cadence` — formatted as a markdown table
11. `## [next]. Revision History` — formatted as a markdown table

### 1.2 Metadata Table (Mandatory Fields, in Order)

```markdown
| Field | Details |
| :--- | :--- |
| **Policy ID**          | [2-letter prefix]                                                 |
| **Document Title**     | [Full policy name]                                               |
| **Version**            | 1.0                                                              |
| **Status**             | Active                                                           |
| **Classification**     | Internal — Restricted  OR  Internal — General                    |
| **Effective Date**     | YYYY-MM-DD                                                       |
| **Last Reviewed**      | YYYY-MM-DD                                                       |
| **Next Review Due**    | YYYY-MM-DD (exactly 12 months after Effective Date for v1.0)    |
| **Policy Owner**       | [Role], FinNexus Solutions                                       |
| **Approved By**        | [Role(s)], FinNexus Solutions                                    |
| **Framework Alignment**| ISO/IEC 27001:2022 (...); NIST CSF 2.0 (...); PCI DSS v4.0.1 (...); DPDPA 2025 (...); GDPR (...) |
```

- Framework Alignment MUST list specific control/article references (e.g., `A.5.15`, `PR.AA-01`, `Req 7.2`). Generic citations like "ISO 27001" alone are not sufficient.

### 1.3 Safeguard (Control Statement) Format

Each safeguard MUST follow this exact format:

```markdown
### [PREFIX]-[NN] — [Short Descriptive Title]

[Body text: 2–5 sentences or structured bullet list.]
[Use MUST / MUST NOT / SHOULD / MAY (RFC 2119) — never "should consider" or "is encouraged to".]
[Name FinNexus Solutions explicitly. Name roles explicitly (e.g., "the IT Security Lead", "Engineering teams"). Never use passive voice like "access should be reviewed".]

> **Framework Mapping:** [Specific citation per framework]
```

- `---` horizontal rule MUST appear after every `> **Framework Mapping:**` block, separating safeguards from each other.
- Do NOT use `####` or deeper headings inside a safeguard body. Use bold sub-labels (e.g., `**Storage:**`, `**Transmission:**`) for internal structure.

### 1.4 Safeguard Numbering and Count

- **Format:** `[PREFIX]-[NN]` where PREFIX is exactly 2 uppercase letters and NN is a zero-padded 2-digit number (e.g., `IR-01`, not `IR-1` or `IR001`).
- **Count range:** 10–11 safeguards per policy is the established norm. Do not pad below 10 or exceed 12 without a substantive reason; quality and specificity over quantity.
- **Order:** Arrange safeguards in logical governance progression — typically: foundational definitions → technical controls → operational procedures → edge cases and special scenarios.

### 1.5 Specificity Bar — The "No Vague Measures" Rule

Every control statement that specifies a requirement MUST cite a concrete mechanism, SLA, timeframe, standard, or named tool wherever one is appropriate. The following table shows examples of prohibited vague language and the required replacement pattern:

| ❌ DO NOT WRITE | ✅ WRITE INSTEAD |
| :--- | :--- |
| "Use appropriate encryption" | "Encrypt using TLS 1.2 or higher (TLS 1.3 preferred)" |
| "Access should be reviewed periodically" | "Conduct access recertification quarterly for CDE systems; semi-annually for corporate IT" |
| "Revoke access promptly upon termination" | "Disable all accounts within **4 hours** of planned separation; within **1 hour** for termination for cause" |
| "Passwords must be strong" | "Minimum 14 characters for standard accounts; 20 for privileged/service accounts; 12-password history" |
| "Use a secure deletion method" | "Use NIST SP 800-88 or DoD 5220.22-M compliant multi-pass wipe; obtain certificate of destruction" |
| "Notify relevant parties of a breach" | "Refer to Legal and Compliance within the DPDPA 2025 / GDPR Article 33 notification window" |
| "Approved vendors must meet our standards" | "Vendors must sign a DPA or MSA containing obligations reviewed by Legal and Compliance" |
| "Implement MFA" | "Enforce FIDO2/WebAuthn or TOTP-based MFA; SMS OTP is deprecated for privileged access" |

### 1.6 Voice, Tone, and Language Rules

- **Always use "FinNexus Solutions"** as the subject, never "the organization", "our company", "the firm", or generic pronouns.
- **Use named roles**, not role categories: write "the IT Security Lead", "the CISO", "the Compliance Lead", "the Legal and Compliance team", "Engineering teams". Avoid "the security team" (too vague) or "management" (meaningless).
- **Regulatory citations**: Always include the specific section/article when citing a regulation. Write `DPDPA 2025 Section 8(6)` not just "DPDPA". Write `GDPR Article 33` not just "GDPR".
- **Cross-references between policies**: Use the control ID format `(see AM-01)` or `(per the Access Management Policy AM-01)` to link related controls across documents — never hyperlinks, as the suite is intended to be human-readable in any rendering environment.
- **RFC 2119 keywords**: Use `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY` consistently. Do not use "required", "mandatory", "forbidden" as synonyms — the RFC 2119 terms are the standard.

### 1.7 Enforcement / Sanctions Section Format

The sanctions section MUST use the three-tier structure used across AM, AU, and DC:

```markdown
- **Tier 1 — Minor Breach** (e.g., [concrete example]): [concrete consequence].
- **Tier 2 — Moderate Breach** (e.g., [concrete example]): [concrete consequence]; escalation to HR.
- **Tier 3 — Severe Breach** (e.g., [concrete example]): Immediate suspension of all access pending investigation; likely termination; potential legal referral under [specific law]; potential regulatory notification.
```

- Every tier MUST include at least one parenthetical concrete example drawn from the policy's domain.
- Tier 3 MUST explicitly name the applicable Indian statute (IT Act 2000, DPDPA 2025) and the relevant regulatory body (CERT-In, Data Protection Board of India, applicable EU supervisory authority) where a data breach is plausible.

### 1.8 Review Cadence Table Format

```markdown
| Attribute | Details |
| :--- | :--- |
| **Standard Review Frequency**  | Annual (every 12 months from effective date)                              |
| **Triggered Review Criteria**  | [2–4 specific trigger conditions relevant to the policy's domain]         |
| **Policy Owner (Review Lead)** | [Specific role], FinNexus Solutions                                       |
| **Review Approver**            | CISO [and one other if dual-approval is warranted]                        |
| **Next Scheduled Review**      | YYYY-MM-DD                                                                |
```

---

## Part 2: Safeguard-ID Prefix Registry

The following prefixes are **already assigned** to authored policies. All new policies MUST use a prefix from the **Available** column — or a newly chosen 2-letter prefix that does not conflict with any entry in this table.

### Assigned Prefixes (DO NOT REUSE)

| Prefix | Policy | Control Range | File |
| :--- | :--- | :--- | :--- |
| `AM` | Access Management | AM-01 → AM-10 | `/policies/access-management.md` |
| `AU` | Acceptable Use | AU-01 → AU-10 | `/policies/acceptable-use.md` |
| `DC` | Data Classification & Handling | DC-01 → DC-11 | `/policies/data-classification-handling.md` |

### Reserved Prefixes (Assigned for Upcoming Policies)

These prefixes are reserved for the next five policies to be authored. Agents MUST adopt the reserved prefix for their assigned domain. Claiming a different prefix requires updating this registry.

| Prefix | Intended Policy Domain | Suggested Control Range |
| :--- | :--- | :--- |
| `IR` | Incident Response & Breach Notification | IR-01 → IR-NN |
| `VR` | Vulnerability & Patch Management | VR-01 → VR-NN |
| `PA` | Privileged Access / PAM (if authored as standalone) OR Physical & Environmental Security | PA-01 → PA-NN |
| `AS` | Asset Management | AS-01 → AS-NN |
| `BC` | Business Continuity & Disaster Recovery | BC-01 → BC-NN |

> **Registry Maintenance:** This table MUST be updated by the authoring agent or human reviewer immediately after a new policy is finalized. Add the assigned prefix to the "Assigned" table with the finalized control range and file path before committing.

---

## Part 3: Reference Example

> **REFERENCE EXAMPLE — match this structure, tone, and specificity exactly.**
>
> The following is the full text of `/policies/data-classification-handling.md`, selected as the canonical reference policy for the PolicyForge suite. It represents the highest standard of specificity, org-grounding, cross-framework citation depth, and structural discipline among the three authored policies. Every subsequent policy MUST match this bar across all dimensions.

---

# Data Classification & Handling Policy

| Field | Details |
| :--- | :--- |
| **Policy ID** | DC |
| **Document Title** | Data Classification & Handling Policy |
| **Version** | 1.0 |
| **Status** | Active |
| **Classification** | Internal — Restricted |
| **Effective Date** | 2026-01-10 |
| **Last Reviewed** | 2026-01-10 |
| **Next Review Due** | 2027-01-10 |
| **Policy Owner** | Compliance Lead, FinNexus Solutions |
| **Approved By** | Chief Information Security Officer (CISO) & Data Protection Officer (DPO), FinNexus Solutions |
| **Framework Alignment** | ISO/IEC 27001:2022 (A.5.9, A.5.10, A.5.12, A.5.13, A.5.14); NIST CSF 2.0 (ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-05); PCI DSS v4.0.1 (Req 3, 4, 9.4); DPDPA 2025 (Sec 4, 6, 8); GDPR (Art 5, 9, 25, 32) |

---

## 1. Purpose

FinNexus Solutions, as a financial services provider operating across India, the United States, and the European Union, handles a wide and varied portfolio of data assets. These range from routine internal operational records to highly sensitive payment account data (PAD), Sensitive Authentication Data (SAD), and the Personally Identifiable Information (PII) of hundreds of thousands of customers — all governed by distinct and demanding legal frameworks including DPDPA 2025, GDPR, and PCI DSS v4.0.1.

A uniform, undifferentiated approach to data handling creates unnecessary risk: applying controls too loosely to sensitive data exposes FinNexus Solutions to breach liability and regulatory sanction; applying them too rigidly to routine data impedes business agility. This policy establishes a formal, tiered data classification scheme and the corresponding mandatory handling requirements for each tier. It ensures that every FinNexus Solutions employee, contractor, and system interacting with data does so in a manner proportionate to that data's sensitivity, regulatory significance, and potential for harm if disclosed.

---

## 2. Scope

This policy applies to:

- **All data** created, received, stored, processed, or transmitted by FinNexus Solutions personnel and systems — regardless of format (digital, physical, or verbal) and regardless of location (Mumbai HQ, remote employee environments, cloud infrastructure, or third-party vendor systems).
- **All personnel** employed or contracted by FinNexus Solutions, including permanent employees, contractors, interns, and secondees who interact with FinNexus Solutions data assets.
- **All systems and environments** that store or process FinNexus Solutions data, including cloud infrastructure (AWS/Azure/GCP production and staging environments), corporate IT systems, SaaS platforms, development and CI/CD pipelines, and third-party managed services.
- **All third-party vendors and partners** who process or have access to FinNexus Solutions data in the course of contracted service delivery. Third parties are contractually obligated to uphold the handling standards defined in this policy as specified in their Data Processing Agreements (DPAs) or Master Service Agreements (MSAs).

Physical document handling and secure disposal requirements within this policy apply to FinNexus Solutions' Mumbai headquarters and any other office location operated by the organization.

---

## 3. FinNexus Solutions Data Classification Tiers

All data assets managed by FinNexus Solutions MUST be assigned to one of the following four classification tiers. The classification determines the minimum mandatory handling, storage, transmission, and disposal controls applicable to that data.

| Tier | Classification Label | Description | Examples |
| :---: | :--- | :--- | :--- |
| **1** | 🔴 **Restricted** | Highest sensitivity. Unauthorized disclosure would cause severe regulatory, financial, or reputational harm. Subject to the strictest regulatory controls. | Customer PII (name, Aadhaar number, PAN, financial account numbers); Payment Account Data (PAD); Sensitive Authentication Data (SAD: CVVs, PINs, full track data); cryptographic private keys; CISO/Board-level strategic plans |
| **2** | 🟠 **Confidential** | High sensitivity. Unauthorized disclosure would cause significant competitive, legal, or operational harm. | Internal audit reports; employee salary and HR records; vendor contracts and commercial terms; security architecture diagrams; vulnerability assessment reports; source code for core financial applications |
| **3** | 🟡 **Internal** | Moderate sensitivity. Intended for use within FinNexus Solutions only. Not approved for external distribution without authorization. | Internal policies and procedures; project plans; non-sensitive internal communications; system run books; team roadmaps; general employee directories |
| **4** | 🟢 **Public** | Intended for or approved for unrestricted public distribution. Has been formally approved for external release. | FinNexus Solutions' public website content; press releases; public product documentation; published job listings; regulatory filings made publicly available |

---

## 4. Policy Statements

### DC-01 — Mandatory Data Classification

All data assets created or received by FinNexus Solutions personnel and systems MUST be assigned a classification tier (as defined in Section 3) at the point of creation or first receipt. Classification is the responsibility of the data asset's creator or the FinNexus Solutions business unit that first receives the data from an external source. Where the appropriate classification is ambiguous, the data MUST be treated as **Confidential** (Tier 2) as a default pending formal review by the Compliance team. No data asset may be labelled as **Public** (Tier 4) without explicit approval from the CISO or an authorized member of the Legal and Compliance team.

> **Framework Mapping:** ISO 27001:2022 A.5.12; NIST CSF ID.AM-05; PCI DSS v4.0.1 Req 9.4.2; DPDPA Sec 8(5); GDPR Art 5(1)(f)

---

### DC-02 — Data Labelling and Marking

All documents, data files, and records containing **Restricted** or **Confidential** data MUST be clearly labelled with their classification tier:

- **Digital documents and files** (e.g., PDFs, spreadsheets, presentations, internal wiki pages): MUST include the classification label in the document header, footer, or metadata using a standardized label format (e.g., `[RESTRICTED — FinNexus Solutions]`). Templates for each classification level are maintained by IT and available in the internal document management system.
- **Emails:** MUST include the classification label in the subject line prefix (e.g., `[RESTRICTED]`) when the email body or attachments contain Restricted or Confidential data.
- **Databases and data repositories:** MUST have classification metadata applied at the schema, table, or field level where technically feasible, using FinNexus Solutions' approved data cataloguing and tagging tools.
- **Physical documents:** MUST display the classification label prominently on every page. **Public** and **Internal** data files require no active labelling but must not be mislabelled as higher classifications.

> **Framework Mapping:** ISO 27001:2022 A.5.13; NIST CSF PR.DS-01; PCI DSS v4.0.1 Req 9.4.2

---

### DC-03 — Handling Requirements: Restricted Data (Tier 1)

**Restricted** data — including customer PII, payment account data, and Sensitive Authentication Data — represents FinNexus Solutions' highest-risk data tier and is subject to the following mandatory handling controls:

- **Storage:** MUST be stored only in designated, security-hardened storage systems approved by the IT Security Lead. Cloud storage of Restricted data MUST be in encrypted-at-rest buckets or databases with access restricted to named, authorised IAM roles. Restricted data MUST NOT be stored on local device storage, personal cloud accounts, removable media, or development/test environment databases unless formally authorised and anonymised or tokenized.
- **Transmission:** MUST be transmitted only over encrypted channels using TLS 1.2 or higher (TLS 1.3 preferred). Transmission of Restricted data via unencrypted email or messaging tools is strictly prohibited.
- **Access:** MUST be restricted to individuals and service accounts with a documented, approved business need (least-privilege, per Access Management Policy AM-01). All access to Restricted data in production environments MUST be logged and auditable.
- **Sharing:** MUST NOT be shared with external parties without a fully executed DPA or equivalent legal agreement reviewed by Legal and Compliance. Where Restricted data must be shared for testing, analytics, or vendor processing, it MUST first be pseudonymized, anonymized, or tokenized to the extent technically feasible.
- **Cardholder Data Environment (CDE):** All payment account data and SAD handled within the CDE is additionally governed by PCI DSS v4.0.1 Requirements 3 and 4 and the PCI DSS Compliance Programme maintained by the Compliance team.

> **Framework Mapping:** ISO 27001:2022 A.5.14, A.8.10, A.8.24; NIST CSF PR.DS-01, PR.DS-02; PCI DSS v4.0.1 Req 3.1–3.7, 4.1–4.2; DPDPA Sec 4, 6, 8; GDPR Art 9, 25, 32

---

### DC-04 — Handling Requirements: Confidential Data (Tier 2)

**Confidential** data is subject to the following handling standards:

- **Storage:** MUST be stored on FinNexus Solutions-managed systems or approved and contracted cloud platforms. MUST NOT be stored on unapproved personal cloud accounts or removable media without IT Security approval and encryption.
- **Transmission:** MUST be transmitted via encrypted channels (TLS 1.2+) or encrypted email. Physical transmission of Confidential data must use sealed, tracked courier services.
- **Access:** Restricted to personnel with a role-based business need. External sharing requires written authorization from the relevant business unit head and, where personal data is involved, Legal and Compliance sign-off.
- **Sharing with Third Parties:** Permitted only under a valid NDA, DPA, or MSA containing appropriate confidentiality and data protection obligations reviewed by Legal and Compliance.

> **Framework Mapping:** ISO 27001:2022 A.5.14, A.8.10; NIST CSF PR.DS-01, PR.DS-05; PCI DSS v4.0.1 Req 9.4; GDPR Art 5, 32

---

### DC-05 — Handling Requirements: Internal Data (Tier 3)

**Internal** data is for FinNexus Solutions personnel use only. It MUST NOT be published externally or shared with third parties unless reclassified as Public (DC-01) or shared under a confidentiality agreement. Internal data transmitted via email does not require encryption beyond standard corporate email security controls, but MUST NOT be sent from a FinNexus Solutions corporate account to a personal email account without IT authorization.

> **Framework Mapping:** ISO 27001:2022 A.5.14; NIST CSF PR.DS-05

---

### DC-06 — Handling Requirements: Public Data (Tier 4)

**Public** data may be freely shared and distributed. However, personnel MUST NOT reclassify higher-tier data to Public without the formal approval process (DC-01). The Marketing or Communications team, in coordination with Legal and Compliance, maintains authority over what content FinNexus Solutions publishes externally and on what channels.

> **Framework Mapping:** ISO 27001:2022 A.5.12; NIST CSF ID.AM-05

---

### DC-07 — Data Minimization and Retention

FinNexus Solutions MUST collect, process, and retain data only to the minimum extent necessary for the specified, lawful business purpose for which it was collected — consistent with DPDPA 2025 Section 4 (purpose limitation) and GDPR Article 5(1)(c) (data minimization).

- Engineering and Product teams MUST design data flows and schemas to collect only the data fields demonstrably required for product functionality. Requests to add new personal data fields to FinNexus Solutions products MUST go through a Privacy Impact Assessment (PIA) reviewed by Legal and Compliance.
- Data retention periods for each Restricted data category MUST be documented in the FinNexus Solutions Data Retention Schedule, maintained by Compliance. Retained data MUST NOT be kept beyond its defined retention period without a documented legal obligation or regulatory hold.
- Data exceeding its retention period MUST be disposed of in accordance with DC-08.

> **Framework Mapping:** ISO 27001:2022 A.5.9, A.8.10; NIST CSF PR.DS-01; PCI DSS v4.0.1 Req 3.2; DPDPA Sec 4, 8(7); GDPR Art 5(1)(c), 5(1)(e)

---

### DC-08 — Secure Data Disposal and Destruction

When data reaches the end of its retention period, or when storage media is decommissioned, FinNexus Solutions MUST ensure secure destruction in proportion to the data's classification:

- **Restricted data (digital):** MUST be cryptographically erased (crypto-shredding by destroying encryption keys) or overwritten using a NIST SP 800-88 or DoD 5220.22-M compliant multi-pass wipe. Cloud storage resources containing Restricted data MUST be purged using the cloud provider's certified secure deletion mechanism before decommissioning.
- **Confidential data (digital):** MUST be securely deleted using approved tools; standard OS-level deletion is insufficient.
- **Physical documents (Restricted or Confidential):** MUST be cross-cut shredded using an onsite shredder or collected and destroyed by a contracted, certified secure destruction vendor. A certificate of destruction MUST be obtained and retained.
- **Decommissioned hardware** (laptops, servers, storage drives) containing any Restricted or Confidential data MUST be cleared by IT before redeployment or disposal, with the disposal method and outcome recorded in the asset decommissioning log.

> **Framework Mapping:** ISO 27001:2022 A.8.10; NIST CSF PR.DS-03; PCI DSS v4.0.1 Req 3.2, 9.4.6; DPDPA Sec 8(7); GDPR Art 5(1)(e), 17

---

### DC-09 — Data in Development and Test Environments

Production data — particularly Restricted data including customer PII and payment account data — MUST NOT be used in development, testing, staging, or QA environments unless there is no viable alternative, and only with explicit written approval from the CISO and Compliance Lead.

Where any use of production Restricted data in a non-production environment is approved as an exception:
- The data MUST be pseudonymized or anonymized prior to use, and the anonymisation technique MUST be reviewed by the Compliance team to verify it meets the standards required under DPDPA 2025 and GDPR.
- Access to the non-production environment containing that data MUST be restricted with controls equivalent to those applied in production.
- The exception MUST be logged in `/register/exception-log.md` with the CISO's sign-off.

FinNexus Solutions Engineering teams MUST use synthetically generated or purpose-built test datasets for all standard development and testing activities.

> **Framework Mapping:** ISO 27001:2022 A.8.31; NIST CSF PR.DS-01; PCI DSS v4.0.1 Req 3.3.2; DPDPA Sec 6, 8; GDPR Art 25, 32

---

### DC-10 — Cross-Border Data Transfers

FinNexus Solutions transfers personal data across jurisdictions by virtue of operating in India, the US, and EU simultaneously. All cross-border transfers of **Restricted** personal data — including customer PII — MUST comply with:

- **DPDPA 2025:** Transfers of digital personal data outside India are permissible only to countries or territories notified as permissible by the Indian Government, or where FinNexus Solutions has implemented an approved transfer mechanism (e.g., standard contractual obligations as specified under DPDPA rules). The Compliance team MUST maintain a current Transfer Impact Assessment for each cross-border transfer arrangement.
- **GDPR:** Transfers of personal data from the EU to India MUST be covered by an appropriate transfer mechanism under GDPR Chapter V (e.g., Standard Contractual Clauses, adequacy decision if applicable). Legal and Compliance MUST review and approve all such mechanisms.
- Any new data flow that would result in a new cross-border transfer of personal data MUST be identified during engineering design, assessed via a Privacy Impact Assessment (DC-07), and approved by Legal and Compliance before the data flow goes live.

> **Framework Mapping:** ISO 27001:2022 A.5.14; NIST CSF GV.SC-07; DPDPA Sec 16; GDPR Art 44–49

---

### DC-11 — Special Category and Sensitive Personal Data

Certain categories of personal data warrant heightened protection beyond the standard **Restricted** tier controls due to the nature of harm that could result from their disclosure. At FinNexus Solutions, this includes:

- Government-issued identifiers (Aadhaar, PAN card numbers) processed for KYC/AML compliance.
- Biometric data used for customer authentication.
- Financial health data (credit scores, loan histories) where processed directly by FinNexus Solutions.
- Any data classified as a "special category" under GDPR Article 9 (e.g., health data, political opinions) that may be incidentally collected.

Such data MUST be subject to an additional layer of technical control beyond standard Restricted data requirements — including field-level encryption at rest, strict audit logging of every access event, and a documented legal basis for each processing activity maintained by Legal and Compliance. Collection of special category data MUST be the minimum necessary and approved by the DPO prior to implementation.

> **Framework Mapping:** ISO 27001:2022 A.5.12, A.8.24; NIST CSF PR.DS-01; DPDPA Sec 8; GDPR Art 9, 35

---

## 5. Roles and Responsibilities

| Role | Responsibilities Under This Policy |
| :--- | :--- |
| **CISO** | Policy ultimate owner; approves exceptions for production data use in non-production environments (DC-09); approves Public-tier reclassification; oversees audit of data handling compliance. |
| **Compliance Lead / DPO** | Day-to-day policy stewardship; maintains the Data Retention Schedule and Transfer Impact Assessments; reviews Privacy Impact Assessments; leads DPDPA/GDPR compliance for data handling practices; approves special category data processing (DC-11). |
| **IT Security Lead** | Maintains the list of approved storage systems for Restricted data; oversees implementation of encryption and access controls for data at rest and in transit; reviews technical handling controls for each classification tier. |
| **Engineering / Product Development** | Implements data minimisation in product design (DC-07); uses synthetic test data by default (DC-09); applies encryption and access controls at the application and infrastructure layer; routes new data flows through PIA process. |
| **Legal and Compliance** | Reviews and approves cross-border transfer mechanisms (DC-10); signs off on third-party DPAs and NDA agreements for Confidential/Restricted data sharing; advises on legal basis for special category data (DC-11). |
| **Human Resources** | Handles employee data records (Confidential tier) in accordance with this policy; ensures HR systems storing employee data are compliant with DPDPA 2025 and applicable Indian employment data obligations. |
| **All Employees, Contractors, and Vendors** | Classify data correctly at point of creation (DC-01); apply appropriate labels (DC-02); adhere to handling requirements for each tier; report suspected misclassification or data mishandling to the IT Security team or Compliance Lead immediately. |

---

## 6. Enforcement and Sanctions

Violations of this policy are assessed in proportion to the classification tier of the data involved, the nature of the violation, and whether it was deliberate or inadvertent:

- **Tier 1 — Minor Breach** (e.g., failure to label an Internal document correctly; brief use of an unencrypted channel to share Internal-tier data): Formal reminder and re-training; correction of the data handling error within 24 hours.
- **Tier 2 — Moderate Breach** (e.g., storing Confidential data in an unapproved personal cloud account; transmitting Restricted data without encryption): Written warning; access privileges reviewed and potentially reduced; mandatory completion of Data Protection training module; escalation to HR.
- **Tier 3 — Severe Breach** (e.g., unauthorized exfiltration or external disclosure of Restricted customer PII or payment data; use of production Restricted data in a development environment without approval; deliberate misclassification to circumvent controls): Immediate suspension of system access pending investigation; likely termination of employment or contract; potential legal action and/or criminal referral under DPDPA 2025 and the Indian IT Act 2000; notification to relevant regulators (CERT-In, Data Protection Board of India, or EU supervisory authority) as required by law.

All Tier 3 violations MUST be treated as potential data breach events and immediately referred to Legal and Compliance for breach notification assessment under DPDPA 2025 Section 8(6) and GDPR Article 33.

---

## 7. Review Cadence

| Attribute | Details |
| :--- | :--- |
| **Standard Review Frequency** | Annual (every 12 months from effective date) |
| **Triggered Review Criteria** | New product lines or data types introduced; material change in DPDPA rules or GDPR guidance (e.g., new SCCs, Data Protection Board guidance); PCI DSS version update affecting Req 3/4; following any Tier 3 violation or regulatory enquiry involving data classification |
| **Policy Owner (Review Lead)** | Compliance Lead / Data Protection Officer (DPO) |
| **Review Approver** | CISO |
| **Next Scheduled Review** | 2027-01-10 |

---

## 8. Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2026-01-10 | Compliance Lead / DPO, FinNexus Solutions | Initial policy authored, reviewed, and approved. |
