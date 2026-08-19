# Password & Authentication Policy

| Field | Details |
| :--- | :--- |
| **Policy ID** | PA |
| **Document Title** | Password & Authentication Policy |
| **Version** | 1.0 |
| **Status** | Draft (illustrative) |
| **Classification** | Internal - Restricted |
| **Effective Date** | DD.MM.YY |
| **Last Reviewed** | DD.MM.YY |
| **Next Review Due** | DD.MM.YY |
| **Policy Owner** | IT Security Lead, FinNexus Solutions |
| **Approved By** | Chief Information Security Officer (CISO), FinNexus Solutions |
| **Framework Alignment** | ISO/IEC 27001:2022 (A.5.17, A.8.2, A.8.5, A.8.24); NIST CSF 2.0 (PR.AA-01, PR.DS-01); PCI DSS v4.0.1 (Req 8.2, 8.3, 8.4); DPDP Act 2023 (Sec 8); GDPR (Art 32) |

---

## 1. Purpose

FinNexus Solutions, as a financial services provider operating across India, the United States, and the European Union, relies on robust authentication mechanisms to protect its critical infrastructure, sensitive customer data, and operational systems. The compromise of user credentials remains one of the most prevalent and high-impact vectors for cyberattacks, particularly within the fintech sector where financially motivated threat actors actively target authentication boundaries.

This policy establishes the mandatory cryptographic, procedural, and behavioral standards for user and system authentication at FinNexus Solutions. It ensures that all access to corporate resources-whether by employees, contractors, service accounts, or customers-is governed by strong, context-aware authentication controls that mitigate the risk of credential theft, brute-force attacks, and unauthorized access, in strict alignment with PCI DSS v4.0.1, DPDP Act 2023, and industry best practices.

---

## 2. Scope

This policy applies to:

- **All users** authenticating to FinNexus Solutions systems, including employees, contractors, interns, temporary staff, and third-party vendors with provisioned access.
- **All systems and applications** operated or managed by FinNexus Solutions, including on-premises infrastructure, cloud environments (AWS/Azure/GCP), corporate IT applications, and SaaS platforms containing FinNexus Solutions data.
- **All automated identities**, including service accounts, API keys, and machine-to-machine authentication tokens used within FinNexus Solutions environments.
- **Customer authentication** mechanisms implemented within FinNexus Solutions' client-facing financial applications and web portals.

This policy does not cover physical access control authentication mechanisms, which are governed by the respective Physical & Environmental Security Policy.

---

## 3. Policy Statements

### PA-01 - Mandatory Multi-Factor Authentication (MFA)

All interactive access to FinNexus Solutions systems, applications, and network infrastructure MUST require Multi-Factor Authentication (MFA). FinNexus Solutions IT MUST enforce FIDO2/WebAuthn (e.g., hardware security keys, platform authenticators) or time-based one-time password (TOTP) applications as the primary MFA mechanisms. SMS-based and voice-call OTPs are deprecated and MUST NOT be used for employee or contractor authentication. Customer-facing applications SHOULD support FIDO2/WebAuthn and MUST NOT rely solely on SMS OTP for high-risk transactions.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.5; NIST CSF 2.0 PR.AA-01; PCI DSS v4.0.1 Req 8.4.2

---

### PA-02 - Password Complexity and Length

Where passwords or passphrases are used for authentication, FinNexus Solutions IT MUST enforce strict length and complexity requirements. Standard user accounts MUST utilize a minimum password length of **14 characters**. Privileged accounts and system administrator accounts MUST utilize a minimum length of **20 characters**. Passwords MUST NOT be subject to arbitrary composition rules (e.g., requiring specific special characters) that degrade memorability; length is the primary factor. Customer-facing applications MUST enforce a minimum of 12 characters.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.5; NIST CSF 2.0 PR.AA-01; PCI DSS v4.0.1 Req 8.3.6

---

### PA-03 - Password History and Reuse Restriction

FinNexus Solutions systems MUST technically enforce password history limits to prevent the reuse of compromised or predictable credentials. The Active Directory and centralized identity providers MUST be configured to enforce a **12-password history** restriction for all internal user accounts. Users MUST NOT reuse the same password across different FinNexus Solutions systems, nor reuse their corporate password for personal external accounts.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.5; NIST CSF 2.0 PR.AA-01; PCI DSS v4.0.1 Req 8.3.7

---

### PA-04 - Password Expiration and Rotation

FinNexus Solutions MUST NOT enforce arbitrary, time-based password expiration (e.g., 90-day forced rotation) for user accounts, provided that MFA is enforced and continuous compromised credential checking (PA-10) is active. Passwords MUST only be force-reset by the IT Helpdesk upon suspected compromise, identified breach, or user request. However, service accounts and API keys that do not support MFA MUST be rotated automatically every **90 days** by the Engineering teams.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.5; NIST CSF 2.0 PR.AA-01; PCI DSS v4.0.1 Req 8.3.9

---

### PA-05 - Account Lockout and Brute-Force Protection

All systems authenticating FinNexus Solutions identities MUST implement protections against brute-force and credential-stuffing attacks. The IT Security Lead MUST configure identity providers to lock an account after a maximum of **10 consecutive invalid authentication attempts**. Lockouts MUST persist for a minimum of **30 minutes** or until formally unlocked by the IT Helpdesk after verifying the user's identity via an out-of-band communication channel. Customer-facing platforms MUST implement equivalent rate-limiting and CAPTCHA mechanisms to deter automated attacks.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.5; NIST CSF 2.0 PR.AA-01; PCI DSS v4.0.1 Req 8.3.4

---

### PA-06 - Elimination of Default and Hardcoded Passwords

Engineering teams and IT MUST NOT use vendor-supplied default passwords or hardcoded credentials within any FinNexus Solutions environment, source code, or configuration file. Prior to the deployment of any new hardware, software, or appliance, the IT team MUST change all default administrative passwords to unique, complex values stored securely in the approved password manager. Source code repositories MUST be continuously scanned by CI/CD pipeline tools to prevent the committal of hardcoded secrets.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.5; NIST CSF 2.0 PR.AA-01; PCI DSS v4.0.1 Req 8.2.2

---

### PA-07 - Privileged Account Authentication

Privileged accounts (e.g., root, Domain Admin, AWS root user) MUST adhere to the strictest authentication standards. FinNexus Solutions IT MUST ensure that privileged access requires a hardware-bound FIDO2 security key. Interactive logins using shared privileged accounts are strictly prohibited; administrators MUST use their named, individual administrative accounts. Access to the Cardholder Data Environment (CDE) MUST require step-up authentication via the corporate Privileged Access Management (PAM) solution.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.2; NIST CSF 2.0 PR.AA-01; PCI DSS v4.0.1 Req 8.2.1

---

### PA-08 - Service Account and API Authentication

Non-human identities, including service accounts and API integrations, MUST authenticate using cryptographically strong mechanisms such as mutual TLS (mTLS), OAuth 2.0, or heavily restricted access tokens. Engineering teams MUST NOT configure service accounts for interactive login. All service account credentials MUST be managed, rotated, and dynamically injected at runtime by the FinNexus Solutions approved secrets management platform (e.g., HashiCorp Vault or AWS Secrets Manager).

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.5; NIST CSF 2.0 PR.AA-01; PCI DSS v4.0.1 Req 8.2.7

---

### PA-09 - Password Storage and Transmission

FinNexus Solutions MUST strictly protect passwords from unauthorized interception or disclosure. All databases and systems storing FinNexus Solutions credentials MUST hash passwords using a strong, computationally intensive cryptographic algorithm with a unique salt (e.g., Argon2id, bcrypt, or PBKDF2 with at least 600,000 iterations). Passwords MUST NOT be stored in plaintext, reversible encryption, or weak hash formats (e.g., MD5, SHA-1). Transmission of passwords across any network MUST occur strictly over TLS 1.2 or higher (TLS 1.3 preferred).

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.24; NIST CSF 2.0 PR.DS-01; PCI DSS v4.0.1 Req 8.3.2

---

### PA-10 - Compromised Credential Checking

The IT Security Lead MUST implement continuous monitoring of active FinNexus Solutions credentials against known-compromised password databases (e.g., HaveIBeenPwned API or enterprise threat intelligence feeds). If an active FinNexus Solutions password is mathematically matched against a known breach corpus, the identity provider MUST immediately force a password reset upon the user's next login attempt and log the event for security review.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.5; NIST CSF 2.0 PR.AA-01; PCI DSS v4.0.1 Req 8.3.6

---

### PA-11 - Authentication Session Management

FinNexus Solutions applications and identity providers MUST enforce secure session management to prevent session hijacking. The IT Security Lead MUST configure corporate identity sessions to expire after a maximum of **12 hours** of inactivity. Customer-facing financial applications MUST enforce an idle timeout of no more than **15 minutes**. All authentication sessions MUST be immediately invalidated upon password change, account suspension, or explicit user logout.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.5; NIST CSF 2.0 PR.AA-01; PCI DSS v4.0.1 Req 8.2.8

---

## 4. Roles and Responsibilities

| Role | Responsibilities Under This Policy |
| :--- | :--- |
| **CISO** | Policy ultimate owner; approves any exceptions to MFA requirements or cryptographic standards; oversees authentication security posture. |
| **IT Security Lead** | Configures and maintains corporate identity providers; enforces password complexity, MFA, and lockout policies; manages the enterprise PAM and secrets management platforms. |
| **Engineering / Product Development** | Implements secure authentication and session management in customer-facing applications; ensures no hardcoded secrets in source code; integrates applications with the central secrets manager. |
| **IT Helpdesk** | Facilitates secure password resets after verifying user identity; supports employees with MFA token enrollment and recovery. |
| **Human Resources** | Notifies IT promptly regarding employee offboarding or role changes to trigger immediate credential revocation. |
| **All Employees and Contractors** | Protect their assigned credentials; utilize approved password managers; never share passwords or MFA tokens with others; report suspected credential compromise immediately. |

---

## 5. Enforcement and Sanctions

Violations of this policy are assessed in proportion to the risk posed to FinNexus Solutions and whether the violation was deliberate or inadvertent:

- **Tier 1 - Minor Breach** (e.g., attempting to set a weak password; failing to lock a workstation when unattended): Formal reminder and re-training; required to reset password immediately to compliant standards.
- **Tier 2 - Moderate Breach** (e.g., storing a FinNexus Solutions corporate password in an unapproved personal password manager or plaintext file; temporarily sharing an account with a colleague): Written warning; access privileges reviewed; mandatory completion of Authentication Security training module; escalation to HR.
- **Tier 3 - Severe Breach** (e.g., deliberately disabling MFA without authorization; hardcoding critical production credentials in a public repository; unauthorized sharing of privileged administrator credentials): Immediate suspension of system access pending investigation; likely termination of employment or contract; potential legal action and/or criminal referral under the Indian IT Act 2000 and DPDP Act 2023; potential regulatory notification to CERT-In or relevant authorities.

All Tier 3 violations MUST be treated as potential security incidents and referred to Legal and Compliance for investigation.

---

## 6. Review Cadence

| Attribute | Details |
| :--- | :--- |
| **Standard Review Frequency** | Annual (every 12 months from effective date) |
| **Triggered Review Criteria** | Major upgrade or replacement of the corporate identity provider; significant change in NIST digital identity guidelines (e.g., NIST SP 800-63); following a Tier 3 credential-related breach |
| **Policy Owner (Review Lead)** | IT Security Lead, FinNexus Solutions |
| **Review Approver** | CISO |
| **Next Scheduled Review** | DD.MM.YY |

---

## 7. Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | DD.MM.YY | IT Security Lead, FinNexus Solutions | Initial policy authored, reviewed, and approved. |
