# Access Management Policy

| Field | Details |
| :--- | :--- |
| **Policy ID** | AM |
| **Document Title** | Access Management Policy |
| **Version** | X.X |
| **Status** | Draft (illustrative) |
| **Classification** | Internal - Restricted |
| **Effective Date** | DD.MM.YY |
| **Last Reviewed** | DD.MM.YY |
| **Next Review Due** | DD.MM.YY |
| **Policy Owner** | IT Security Lead, FinNexus Solutions |
| **Approved By** | Chief Information Security Officer (CISO), FinNexus Solutions |
| **Framework Alignment** | ISO/IEC 27001:2022 (A.5.15–A.5.18, A.8.2–A.8.5); NIST CSF 2.0 (PR.AA-01 to PR.AA-06); PCI DSS v4.0.1 (Req 7, 8); DPDP Act 2023 (Sec 8(5)); GDPR (Art 5(1)(f), 32) |

---

## 1. Purpose

FinNexus Solutions processes and stores Personally Identifiable Information (PII), Sensitive Authentication Data (SAD), and Payment Account Data (PAD) on behalf of customers and business partners across India, the United States, and the European Union. Unauthorized or improperly governed access to these systems and datasets represents FinNexus Solutions' highest single-vector threat - including insider threat, credential compromise, and privilege abuse.

This policy establishes the minimum mandatory requirements for granting, managing, monitoring, and revoking logical access to all FinNexus Solutions systems, infrastructure, applications, cloud environments, and data assets. Compliance with this policy is a prerequisite for fulfilling FinNexus Solutions' obligations under PCI DSS v4.0.1 Requirements 7 and 8, DPDP Act 2023 Section 8(5), GDPR Article 32, and ISO/IEC 27001:2022 Annex A Controls A.5.15–A.5.18 and A.8.2–A.8.5.

---

## 2. Scope

This policy applies to:

- **All personnel** employed by FinNexus Solutions in any capacity - including permanent employees, contractors, interns, and secondees - across its Mumbai headquarters and any remote or hybrid work location.
- **All third-party vendors, SaaS providers, and managed service partners** granted any form of logical access to FinNexus Solutions systems, networks, cloud environments (AWS/Azure/GCP), or data repositories.
- **All systems and environments** owned or operated by FinNexus Solutions, including but not limited to: production cloud infrastructure, internal corporate IT systems, development and staging environments, financial transaction processing systems, customer-facing applications, and data warehouses.
- **All access modalities**: user accounts, service accounts, application-to-application credentials (API keys, OAuth tokens), privileged accounts, and machine identities.

This policy does not govern physical access controls (covered by the Physical Security Policy) or customer-facing authentication flows for FinNexus Solutions' products (governed by the Secure SDLC and Customer Identity Management procedures).

---

## 3. Policy Statements

### AM-01 - Least Privilege and Need-to-Know

All access rights granted to FinNexus Solutions personnel, service accounts, and third parties MUST be provisioned on the principle of least privilege. Access MUST be scoped to the minimum permissions required to fulfil a defined, business-approved role or task. Broad, wildcard, or owner-level permissions (e.g., `*:*`, `AdministratorAccess` policies in AWS) MUST NOT be granted to any human user in a production environment without explicit, time-boxed CISO approval and a documented business justification. Engineering teams MUST NOT share application-level credentials across services where individual service identities are technically feasible.

> **Framework Mapping:** ISO 27001:2022 A.5.15, A.8.2; NIST CSF PR.AA-05; PCI DSS v4.0.1 Req 7.2; DPDP Act 2023 Sec 8(5)

---

### AM-02 - Formal Access Provisioning and Approval

Access to all FinNexus Solutions systems MUST be provisioned only upon receipt of a formal, written access request that includes: (a) the requestor's full name and employee/contractor ID; (b) the specific systems, applications, or data repositories requiring access; (c) the business justification; and (d) the approval of the requestor's direct line manager or project lead. Requests for access to systems classified as **Restricted** or **Confidential** (per the Data Classification Policy) require secondary approval from the IT Security Lead. Access provisioning MUST NOT occur via informal channels (e.g., direct messages, verbal instruction).

> **Framework Mapping:** ISO 27001:2022 A.5.18; NIST CSF PR.AA-01; PCI DSS v4.0.1 Req 7.2.2; GDPR Art 32

---

### AM-03 - Unique User Identification

Every individual who accesses any FinNexus Solutions system MUST be assigned a unique user identifier (User ID). Shared or generic accounts (e.g., `admin`, `test`, `shared-team-login`) are strictly prohibited in all production, staging, and corporate IT environments. This requirement extends to service accounts and machine identities; each service or automated process MUST operate under a dedicated, uniquely named identity. Where legacy systems technically cannot support unique accounts, an approved exception (see [Exception Log](#exception-log)) with compensating controls MUST be in place.

> **Framework Mapping:** ISO 27001:2022 A.5.16; NIST CSF PR.AA-02; PCI DSS v4.0.1 Req 8.2.1; DPDP Act 2023 Sec 8(5)

---

### AM-04 - Multi-Factor Authentication (MFA)

Multi-Factor Authentication MUST be enforced for:

- All remote access connections to FinNexus Solutions infrastructure and corporate systems (VPN, cloud console logins).
- All access to the Cardholder Data Environment (CDE) and any system component in scope for PCI DSS.
- All access to FinNexus Solutions' cloud management consoles (AWS Management Console, Azure Portal, GCP Console) - including root/global administrator accounts.
- All privileged administrative accounts (see AM-07).
- All access to repositories, CI/CD pipelines, or deployment systems used by the Engineering team.

MFA MUST use a phishing-resistant mechanism (e.g., FIDO2/WebAuthn hardware security keys, or a TOTP authenticator application). SMS-based OTP is deprecated as a sole MFA factor for Restricted-tier access and MUST NOT be used for privileged accounts.

> **Framework Mapping:** ISO 27001:2022 A.8.5; NIST CSF PR.AA-03; PCI DSS v4.0.1 Req 8.4, 8.5; GDPR Art 32(1)(b)

---

### AM-05 - Password and Authentication Credential Standards

Where password authentication is used, FinNexus Solutions systems MUST enforce the following minimum standards:

- **Minimum length:** 14 characters for standard user accounts; 20 characters for privileged/service accounts.
- **Complexity:** A combination of uppercase, lowercase, numeric, and special characters, or passphrase-equivalent entropy.
- **History:** A minimum of 12 previous passwords MUST be retained to prevent reuse.
- **Account Lockout:** Accounts MUST lock after no more than 10 consecutive failed authentication attempts.
- **No default credentials:** Default vendor-supplied or system-generated passwords MUST be changed immediately upon commissioning any new system or service.

Credentials MUST NOT be stored in source code, configuration files, CI/CD environment variables exposed in plaintext, or internal wikis/documents. All secrets MUST be stored in an approved secrets management system (e.g., AWS Secrets Manager, HashiCorp Vault).

> **Framework Mapping:** ISO 27001:2022 A.5.17; NIST CSF PR.AA-02; PCI DSS v4.0.1 Req 8.3, 8.6; GDPR Art 32

---

### AM-06 - Access Reviews and Recertification

The IT Security Lead MUST conduct a formal access recertification exercise for all FinNexus Solutions systems and environments on the following schedule:

- **Production systems and CDE:** Quarterly.
- **Corporate IT systems and SaaS platforms:** Semi-annually (every 6 months).
- **Privileged accounts (AM-07):** Quarterly, and additionally after any role change or separation.

During recertification, each access grant MUST be confirmed as still necessary by the access owner's current line manager. Any access that cannot be justified MUST be revoked within 5 business days of the recertification review being finalized.

> **Framework Mapping:** ISO 27001:2022 A.5.18; NIST CSF PR.AA-05; PCI DSS v4.0.1 Req 7.2.4, 7.2.5; GDPR Art 5(1)(f)

---

### AM-07 - Privileged Access Management (PAM)

Privileged accounts - including system administrator accounts, database administrator accounts, root accounts, cloud IAM administrative roles, and network device management accounts - MUST be subject to the following enhanced controls:

- **Separate identities:** Privileged access MUST use a dedicated privileged account, separate from the user's standard day-to-day account. Privileged accounts MUST NOT be used for browsing the internet or accessing email.
- **Just-in-Time (JIT) Access:** Where technically feasible, privileged access MUST be granted on a Just-in-Time basis, activated for a defined session duration and automatically revoked upon expiry.
- **Session Recording:** All privileged sessions on production infrastructure and CDE components MUST be logged and session recordings retained for a minimum of 12 months.
- **Break-Glass Accounts:** Emergency break-glass accounts MUST be maintained in a sealed, audited vault with dual-control activation (requiring two authorized individuals). Use of break-glass accounts MUST generate an immediate alert to the CISO.

> **Framework Mapping:** ISO 27001:2022 A.5.18, A.8.2; NIST CSF PR.AA-05, PR.AA-06; PCI DSS v4.0.1 Req 7.2.6, 8.2.2; GDPR Art 32

---

### AM-08 - Access Revocation and Offboarding

Human Resources MUST notify the IT Security team no later than the end of an employee's or contractor's final working day - or immediately upon an unplanned separation or termination for cause. Upon receipt of this notification, IT MUST:

- Disable all user accounts (corporate directory, cloud consoles, SaaS applications) within **4 hours** of a planned separation or **immediately** (within 1 hour) for terminations for cause.
- Revoke all active sessions, tokens, API keys, and SSH keys attributed to the departing individual.
- Reassign or retire any service accounts or shared credentials the individual was known to hold sole knowledge of.

Access revocation completion MUST be confirmed in writing to HR and documented in the offboarding record. The IT Security Lead MUST verify revocation as part of the next quarterly access review cycle.

> **Framework Mapping:** ISO 27001:2022 A.5.18, A.6.5; NIST CSF PR.AA-05; PCI DSS v4.0.1 Req 8.3.4; DPDP Act 2023 Sec 8(5)

---

### AM-09 - Third-Party and Vendor Access Controls

All third-party vendors, SaaS providers, and managed service partners granted access to FinNexus Solutions systems or data MUST comply with the following:

- Access MUST be provisioned on a need-to-know basis, scoped only to the systems, data, or environments necessary for contracted service delivery.
- All third-party access MUST be protected by MFA (AM-04) and utilize dedicated, uniquely named accounts (AM-03). Vendors MUST NOT use FinNexus Solutions employee credentials.
- Remote vendor access sessions MUST be time-limited and, wherever possible, conducted through a monitored and audited jump server or Privileged Access Workstation (PAW).
- Vendor access MUST be formally revoked within 5 business days of contract expiry, project completion, or vendor relationship termination, as notified by the responsible FinNexus Solutions vendor manager.

The vendor risk management process and corresponding agreements (MSAs/DPAs) are governed by the Third-Party & Vendor Risk Management Policy.

> **Framework Mapping:** ISO 27001:2022 A.5.19, A.5.20; NIST CSF GV.SC-07, PR.AA-05; PCI DSS v4.0.1 Req 8.2.1, 12.8; GDPR Art 28; DPDP Act 2023 Sec 8(2)

---

### AM-10 - Service Account and Machine Identity Governance

Service accounts and machine identities (API keys, OAuth 2.0 client credentials, service principals, workload identity certificates) used within FinNexus Solutions' cloud infrastructure and application stack MUST adhere to the following:

- Each service account MUST be assigned a unique identity scoped to a single service or application.
- Service account credentials MUST be rotated at a minimum every 90 days, or immediately upon suspected compromise.
- Service accounts MUST NOT have interactive login capabilities where technically enforceable.
- API keys with access to production data or payment-related services MUST be stored exclusively in an approved secrets management vault and MUST NOT be embedded in application source code or container images.
- An inventory of all active service accounts and their associated systems MUST be maintained by IT Security and reviewed quarterly.

> **Framework Mapping:** ISO 27001:2022 A.5.16, A.8.3; NIST CSF PR.AA-02, PR.AA-05; PCI DSS v4.0.1 Req 8.6; GDPR Art 32

---

## 4. Roles and Responsibilities

| Role | Responsibilities Under This Policy |
| :--- | :--- |
| **CISO** | Ultimate policy owner; approves privileged access exceptions; approves and oversees break-glass account procedures; receives alerts on critical access events. |
| **IT Security Lead** | Day-to-day policy enforcement; manages the access provisioning and revocation workflow; conducts access recertification reviews (AM-06); maintains service account inventory (AM-10). |
| **IT Operations / Helpdesk** | Executes access provisioning and revocation requests as directed by IT Security; enforces account lockout and MFA enrolment for all FinNexus Solutions staff. |
| **Engineering / Product Development** | Responsible for implementing least-privilege IAM roles in cloud environments and CI/CD systems; enforces secrets management standards (AM-05); onboards service accounts to PAM tooling (AM-10). |
| **Human Resources** | Initiates access provisioning upon hire and triggers access revocation upon employee or contractor separation as per AM-08 timelines. |
| **Legal and Compliance** | Ensures vendor access agreements (DPAs/MSAs) reflect access control obligations; validates GDPR Article 32 / DPDP Act 2023 compliance during access-related audits. |
| **All Employees and Contractors** | Responsible for maintaining the confidentiality of their own credentials; must not share access credentials with any other individual; must report suspected account compromise immediately to IT Security. |

---

## 5. Enforcement and Sanctions

Violations of this policy by FinNexus Solutions employees, contractors, or third-party vendors are treated with the severity commensurate with the associated risk:

- **Minor Violation** (e.g., sharing credentials with a colleague for a brief period, failing to log out of a session): Formal written warning; mandatory re-completion of the Security Awareness Training module; note in personnel file.
- **Moderate Violation** (e.g., provisioning access without following the formal approval process, failing to revoke access for a departed vendor): Mandatory retraining; temporary access privilege reduction; escalation to HR for disciplinary review.
- **Severe Violation** (e.g., granting unauthorized access to the CDE or payment systems, wilful circumvention of MFA controls, misuse of privileged credentials): Immediate suspension of all access pending investigation; potential termination of employment or contract; referral for legal action where applicable under Indian law, GDPR enforcement, or PCI DSS incident reporting requirements.

All violations MUST be documented and reported to the CISO. Violations that may constitute a personal data breach under DPDP Act 2023 or GDPR MUST be escalated immediately to the Legal and Compliance team for breach notification assessment.

---

## 6. Review Cadence

| Attribute | Details |
| :--- | :--- |
| **Standard Review Frequency** | Annual (every 12 months from effective date) |
| **Triggered Review Criteria** | Major cloud infrastructure change; material organizational restructuring; significant access-related security incident; new or amended regulatory requirement (PCI DSS, DPDP Act 2023, GDPR) |
| **Policy Owner (Review Lead)** | IT Security Lead |
| **Review Approver** | CISO |
| **Next Scheduled Review** | DD.MM.YY |

---

## 7. Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| X.X | DD.MM.YY | IT Security Lead | Initial policy draft authored and approved. |
