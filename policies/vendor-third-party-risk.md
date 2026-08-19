# Vendor & Third-Party Risk Policy

| Field | Details |
| :--- | :--- |
| **Policy ID** | VR |
| **Document Title** | Vendor & Third-Party Risk Policy |
| **Version** | 1.0 |
| **Status** | Active |
| **Classification** | Internal - Restricted |
| **Effective Date** | DD.MM.YY |
| **Last Reviewed** | DD.MM.YY |
| **Next Review Due** | DD.MM.YY |
| **Policy Owner** | Compliance Lead, FinNexus Solutions |
| **Approved By** | Chief Information Security Officer (CISO), FinNexus Solutions |
| **Framework Alignment** | ISO/IEC 27001:2022 (A.5.19, A.5.20, A.5.21, A.5.22); NIST CSF 2.0 (GV.SC-04, GV.SC-06, GV.SC-07); PCI DSS v4.0.1 (Req 12.8.1, 12.8.2, 12.8.3, 12.8.4, 12.8.5); DPDP Act 2023 (Sec 8(1), 8(2), 8(6)); GDPR (Art 28, 33) |

---

## 1. Purpose

FinNexus Solutions relies on a complex ecosystem of third-party vendors, SaaS platforms, APIs, and managed service providers to deliver high-availability financial services to its customers across India, the United States, and the European Union. While these partnerships enable business agility and scale, they also introduce supply chain risks, data exposure vulnerabilities, and compliance dependencies under frameworks such as DPDP Act 2023, GDPR, and PCI DSS v4.0.1.

A compromise of a FinNexus Solutions vendor could directly result in the unauthorized disclosure of Personally Identifiable Information (PII) or Payment Account Data (PAD), disrupting operations and violating our regulatory obligations. This policy establishes a formalized, risk-based approach to evaluating, onboarding, monitoring, and offboarding third parties. It ensures that FinNexus Solutions extends its internal security and privacy standards to its supply chain, enforcing robust contractual obligations and technical safeguards proportionate to the risk each vendor introduces.

---

## 2. Scope

This policy applies to:

- **All third-party entities** providing services, software, infrastructure, or personnel to FinNexus Solutions, including SaaS providers, cloud infrastructure providers (e.g., AWS, Azure, GCP), managed security service providers (MSSPs), API vendors, and contractors.
- **All FinNexus Solutions personnel** responsible for procuring, managing, integrating, or evaluating third-party services and products.
- **All data assets and systems** owned or managed by FinNexus Solutions that are accessed, stored, processed, or transmitted by a third-party vendor.

This policy does not apply to the direct employment of individual full-time FinNexus Solutions employees, which is governed by HR onboarding procedures, though it does apply to agencies providing contingent or contracted workers.

---

## 3. Vendor Risk Tiers

FinNexus Solutions MUST assign all third-party vendors a risk tier during the procurement phase to determine the required level of due diligence and continuous monitoring.

| Tier | Classification Label | Description | Examples |
| :---: | :--- | :--- | :--- |
| **1** | 🔴 **High Risk / Critical** | Processes, stores, or transmits Restricted data (PII, PAD, SAD) or provides core infrastructure where downtime exceeding 4 hours directly impacts FinNexus Solutions revenue. | AWS/Azure cloud infrastructure; core payment gateways; customer identity verification (KYC) APIs; HR management SaaS |
| **2** | 🟠 **Medium Risk** | Processes or stores Confidential data, or provides operational services where downtime impacts internal productivity but not external customers. | Internal IT ticketing systems; non-sensitive analytics platforms; background check providers |
| **3** | 🟡 **Low Risk** | Processes only Internal or Public data with no access to production systems, customer data, or sensitive networks. | Marketing website hosting; catering or facilities vendors; public data syndication tools |

---

## 4. Policy Statements

### VR-01 - Vendor Inventory and Cataloguing

FinNexus Solutions MUST maintain a centralized and continuously updated inventory of all active third-party vendors, APIs, and managed services. The IT team MUST register each vendor in the approved FinNexus Solutions Vendor Management System (VMS) prior to procurement. The inventory MUST record the vendor's assigned Risk Tier (as defined in Section 3), the business owner, the types of FinNexus Solutions data accessed, and the current compliance status (e.g., active DPA, valid SOC 2 report).

> **Framework Mapping:** ISO 27001:2022 A.5.19; NIST CSF 2.0 GV.SC-04; PCI DSS v4.0.1 Req 12.8.1

---

### VR-02 - Pre-Procurement Risk Assessment

Before onboarding any new vendor or renewing a contract, the FinNexus Solutions business owner MUST initiate a formalized risk assessment through the VMS. The IT Security Lead and Compliance Lead MUST review and approve the assessment for all High Risk (Tier 1) and Medium Risk (Tier 2) vendors. Procurement MUST NOT execute any vendor agreement or issue payment until the risk assessment is complete and the vendor is formally approved by the CISO or delegated authority.

> **Framework Mapping:** ISO 27001:2022 A.5.21; NIST CSF 2.0 GV.SC-06; PCI DSS v4.0.1 Req 12.8.3

---

### VR-03 - Security Validation and Evidence

Vendors classified as High Risk (Tier 1) MUST provide independent, third-party validation of their security controls before onboarding. The IT Security Lead MUST collect and review a current SOC 2 Type II report, an ISO/IEC 27001 certificate, or a PCI DSS Attestation of Compliance (AOC). If the vendor cannot provide these, they MUST complete the FinNexus Solutions Standardized Information Gathering (SIG) questionnaire and remediate any critical findings identified by the IT Security team prior to processing any FinNexus Solutions Restricted data.

> **Framework Mapping:** ISO 27001:2022 A.5.21; NIST CSF 2.0 GV.SC-06; PCI DSS v4.0.1 Req 12.8.4

---

### VR-04 - Contractual Security and Privacy Obligations

FinNexus Solutions MUST establish formal, binding contractual agreements with all third-party vendors outlining their security and privacy obligations. Legal and Compliance MUST ensure that all vendors processing personal data sign a Data Processing Agreement (DPA) that explicitly details purpose limitation, data minimization, and cross-border transfer mechanisms compliant with DPDP Act 2023 and GDPR. Vendors processing payment data MUST explicitly acknowledge their responsibility for the security of cardholder data under PCI DSS v4.0.1 Requirement 12.8.2.

> **Framework Mapping:** ISO 27001:2022 A.5.20; NIST CSF 2.0 GV.SC-07; PCI DSS v4.0.1 Req 12.8.2; DPDPA Sec 8(2); GDPR Art 28

---

### VR-05 - Right to Audit and Compliance Verification

All contracts for High Risk (Tier 1) vendors MUST include a "Right to Audit" clause, permitting FinNexus Solutions or an appointed independent auditor to verify the vendor's security posture and compliance with contractual obligations. The Compliance Lead MUST exercise this right proactively if a vendor fails to provide updated annual compliance reports (SOC 2, ISO 27001) or if FinNexus Solutions discovers a material vulnerability within the vendor's environment.

> **Framework Mapping:** ISO 27001:2022 A.5.22; NIST CSF 2.0 GV.SC-06; GDPR Art 28(3)(h)

---

### VR-06 - Continuous Monitoring and Periodic Re-assessment

FinNexus Solutions MUST continuously monitor its vendor ecosystem. The IT Security Lead MUST conduct formalized re-assessments of all High Risk (Tier 1) vendors annually and Medium Risk (Tier 2) vendors biennially. This review MUST verify that the vendor's security posture has not degraded, that they maintain valid compliance certifications, and that their access to FinNexus Solutions systems remains strictly limited to least-privilege requirements.

> **Framework Mapping:** ISO 27001:2022 A.5.22; NIST CSF 2.0 GV.SC-06; PCI DSS v4.0.1 Req 12.8.4

---

### VR-07 - Vendor Incident Response and Breach Notification

Third-party contracts MUST mandate that the vendor notify FinNexus Solutions of any confirmed or suspected data breach affecting FinNexus Solutions data within **24 hours** of discovery. The IT Security Lead MUST integrate vendor breach notifications into the internal Incident Response plan. If a vendor breach involves Restricted data (e.g., PII under DPDPA/GDPR), Legal and Compliance MUST direct the regulatory notification process and instruct the vendor on required containment and forensic preservation steps.

> **Framework Mapping:** ISO 27001:2022 A.5.22; NIST CSF 2.0 GV.SC-06; DPDPA Sec 8(6); GDPR Art 33(2)

---

### VR-08 - Vendor Offboarding and Data Destruction

Upon termination of a vendor relationship, the IT team MUST revoke all vendor access to FinNexus Solutions systems and physical premises within **4 hours**. The vendor MUST return or provably destroy all FinNexus Solutions data in their possession. The Compliance Lead MUST obtain a formal Certificate of Destruction (CoD) from High Risk (Tier 1) vendors confirming that all Restricted and Confidential data has been cryptographically erased or securely wiped using a NIST SP 800-88 Rev. 2 compliant method within **30 days** of contract termination.

> **Framework Mapping:** ISO 27001:2022 A.5.22, A.8.10; PCI DSS v4.0.1 Req 12.8.5; DPDPA Sec 8(7); GDPR Art 28(3)(g)

---

### VR-09 - Fourth-Party Risk and Sub-processors

Vendors MUST NOT engage sub-processors (fourth parties) to handle FinNexus Solutions Restricted or Confidential data without prior written authorization from FinNexus Solutions Legal and Compliance. High Risk (Tier 1) vendors MUST maintain an updated list of all sub-processors and flow down all contractual security and privacy obligations to these entities. If a sub-processor fails to meet FinNexus Solutions standards, the primary vendor remains fully liable for the breach.

> **Framework Mapping:** ISO 27001:2022 A.5.20; NIST CSF 2.0 GV.SC-07; GDPR Art 28(2), 28(4)

---

### VR-10 - Software Supply Chain and API Security

Engineering teams MUST NOT integrate third-party software libraries (e.g., open-source components, npm packages) or external APIs into FinNexus Solutions production environments without automated security scanning. The IT Security Lead MUST configure CI/CD pipelines to block deployments containing third-party components with known Critical or High vulnerabilities (CVSS 7.0+). API connections to external vendors MUST enforce TLS 1.2+ encryption and use robust authentication (e.g., OAuth 2.0, mutual TLS).

> **Framework Mapping:** ISO 27001:2022 A.8.30, A.8.32; NIST CSF 2.0 GV.SC-06; PCI DSS v4.0.1 Req 6.3.2

---

## 5. Roles and Responsibilities

| Role | Responsibilities Under This Policy |
| :--- | :--- |
| **CISO** | Ultimately responsible for the Vendor Risk Management program; approves onboarding of High Risk vendors; authorizes exceptions to standard vendor security requirements. |
| **IT Security Lead** | Evaluates vendor SOC 2/ISO certifications and SIG questionnaires; conducts annual re-assessments of Tier 1 vendors; manages continuous monitoring and CI/CD supply chain controls. |
| **Compliance Lead / DPO** | Ensures DPAs and cross-border transfer agreements comply with DPDP Act 2023 and GDPR; exercises the Right to Audit; oversees vendor breach notification timelines. |
| **Legal and Compliance** | Drafts, reviews, and negotiates vendor MSAs, NDAs, and DPAs; ensures legal obligations flow down to sub-processors. |
| **Business Owners** | Initiates pre-procurement risk assessments for new vendors; justifies the business need for third-party services; assists in tracking vendor performance and SLA adherence. |
| **Information Technology (IT)** | Maintains the centralized Vendor Management System (VMS); manages vendor access provisioning and revokes access upon offboarding. |
| **Engineering / Product Development** | Secures API integrations with third parties; performs vulnerability scanning on open-source dependencies and third-party libraries before deployment. |

---

## 6. Enforcement and Sanctions

Violations of this policy are assessed in proportion to the vendor risk tier involved, the nature of the violation, and whether it was deliberate or inadvertent:

- **Tier 1 - Minor Breach** (e.g., failing to update a vendor contact in the VMS; delay in completing an annual re-assessment for a Medium Risk vendor): Formal reminder and re-training; completion of the missing documentation within 5 business days.
- **Tier 2 - Moderate Breach** (e.g., procuring a Medium Risk vendor without initiating the pre-procurement risk assessment; failure to revoke an offboarded vendor's non-production access within 4 hours): Written warning; suspension of procurement privileges for the business owner; mandatory completion of Vendor Risk Management training; escalation to HR.
- **Tier 3 - Severe Breach** (e.g., sharing Restricted customer PII with an unvetted High Risk vendor; deploying a third-party API without encryption or Legal review; concealing a vendor data breach): Immediate suspension of system access pending investigation; likely termination of employment or contract; potential legal action and/or criminal referral under DPDP Act 2023 and the Indian IT Act 2000; notification to relevant regulators (CERT-In, Data Protection Board of India, or EU supervisory authority) as required by law.

All Tier 3 violations MUST be treated as potential data breach events and immediately referred to Legal and Compliance for breach notification assessment under DPDP Act 2023 Section 8(6) and GDPR Article 33.

---

## 7. Review Cadence

| Attribute | Details |
| :--- | :--- |
| **Standard Review Frequency** | Annual (every 12 months from effective date) |
| **Triggered Review Criteria** | Identification of a systemic supply chain vulnerability (e.g., Log4j-style event); significant changes to DPDP Act 2023 rules regarding data fiduciaries; a Tier 3 policy violation involving a third party |
| **Policy Owner (Review Lead)** | Compliance Lead, FinNexus Solutions |
| **Review Approver** | CISO |
| **Next Scheduled Review** | DD.MM.YY |

---

## 8. Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | DD.MM.YY | Compliance Lead, FinNexus Solutions | Initial policy authored, reviewed, and approved. |
