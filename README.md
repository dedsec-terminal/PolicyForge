# PolicyForge: Enterprise Security Policy & Governance Suite

Welcome to **PolicyForge**. This repository demonstrates a complete, authored information security policy suite for a modern fintech organization—not just a collection of generic templates or a static document store. 

It showcases three core pillars of enterprise security management:
1. **Authored Security Policy:** Custom-written policies tailored to a specific organizational profile and risk appetite.
2. **Independent Control Traceability:** Rigorous mapping of internal controls to global frameworks (ISO/IEC 27001:2022, NIST CSF 2.0, PCI DSS v4.0.1, DPDPA 2025, and GDPR).
3. **Operational Governance Lifecycle:** Active management of policy exceptions and review cadences to reflect a living security program.

## 📂 Repository Structure

The repository is structured to reflect a real-world governance lifecycle:

* **[`/context`](file:///d:/PolicyForge/context/org-profile.md)** defines the organizational scope, risk profile, and operational baseline that inform the policies.
* **[`/policies`](file:///d:/PolicyForge/policies/)** contains the authored control requirements (e.g., Access Management, Incident Response).
* **[`/mapping`](file:///d:/PolicyForge/mapping/)** provides control traceability to external frameworks, including an independent audit of the mappings.
* **[`/register`](file:///d:/PolicyForge/register/)** tracks operational governance, maintaining exception logs and review cadences.

## 📖 How to Read This Repository

The power of this suite lies in its traceability. You can follow a specific requirement from the policy document directly to its regulatory justification. 

For example, open the [Control Traceability Matrix (CTM)](file:///d:/PolicyForge/mapping/control-traceability-matrix.md) to see how:
* **PA-04** (from the Password & Authentication Policy) satisfies **PCI DSS v4.0.1 Requirement 8.3.9** regarding the deprecation of arbitrary time-based password expiration.
* **IR-06** (from the Incident Response Policy) maps to **GDPR Articles 33 & 34** and **DPDPA Section 8(6)** to enforce mandatory regulatory breach notification timelines.
* **AM-04** (from the Access Management Policy) satisfies **ISO/IEC 27001:2022 Control A.8.5** by enforcing MFA and deprecating SMS OTP for privileged access.

## 🔍 Independent Audit & Real-World Governance

A robust compliance program does not assume its own mappings are flawless. Included in this repository is an **independent verification pass**: the [`ctm_audit_report.md`](file:///d:/PolicyForge/mapping/ctm_audit_report.md). This report independently verified the CTM mappings against primary-source standards, representing a deliberate governance and quality-assurance step.

Finally, realistic policy programs always have ongoing alignment work. In the CTM's "Open Review Items," you will note that control **PA-10** (continuous monitoring of compromised credentials) remains flagged pending formal DPO/Legal sign-off regarding privacy implications. This reflects the reality of operational security governance, where technical controls must continuously negotiate with legal and privacy constraints before final ratification.
