# Asset Management Policy

| Field | Details |
| :--- | :--- |
| **Policy ID**          | AS                                                               |
| **Document Title**     | Asset Management Policy                                          |
| **Version**            | 1.0                                                              |
| **Status**             | Draft (illustrative)                                             |
| **Classification**     | Internal - Restricted                                            |
| **Effective Date**     | DD.MM.YY                                                       |
| **Last Reviewed**      | DD.MM.YY                                                       |
| **Next Review Due**    | DD.MM.YY                                                       |
| **Policy Owner**       | IT Asset Manager, FinNexus Solutions                             |
| **Approved By**        | Chief Information Security Officer (CISO), FinNexus Solutions    |
| **Framework Alignment**| ISO/IEC 27001:2022 (A.5.9, A.5.10, A.8.1, A.8.9); NIST CSF 2.0 (ID.AM-01, ID.AM-02, ID.AM-03, ID.AM-04); PCI DSS v4.0.1 (Req 9.3); DPDP Act 2023 (Sec 8); GDPR (Art 32) |

---

## 1. Purpose

FinNexus Solutions relies on a diverse array of physical and logical assets to deliver high-availability financial services and process sensitive payment and customer data. These assets range from employee laptops and physical office infrastructure to cloud-based servers, software applications, and third-party APIs. Without rigorous visibility and lifecycle management, untracked assets present significant security risks, including unpatched vulnerabilities, unauthorized access to Personally Identifiable Information (PII), and non-compliance with regulatory frameworks such as DPDP Act 2023, GDPR, and PCI DSS v4.0.1.

This policy establishes the mandatory lifecycle controls for all IT and information assets at FinNexus Solutions, from procurement and inventory through to secure decommissioning. It ensures that every asset is centrally tracked, formally owned, adequately protected based on its criticality, and disposed of securely. By maintaining an accurate and continuous inventory, FinNexus Solutions can effectively manage its attack surface and respond swiftly to emerging threats in its hybrid and cloud-hosted environments.

---

## 2. Scope

This policy applies to:

- **All physical hardware** owned or leased by FinNexus Solutions, including employee laptops, mobile devices, servers, and networking equipment across all corporate offices and remote work environments.
- **All logical and software assets** procured, developed, or utilized by FinNexus Solutions, including cloud infrastructure instances (AWS/Azure/GCP), SaaS applications, source code repositories, databases, and third-party APIs.
- **All personnel** employed or contracted by FinNexus Solutions, including permanent employees, contractors, and third-party vendors who are issued or manage FinNexus Solutions assets.

This policy excludes the classification and handling of data assets, which are governed separately under the Data Classification & Handling Policy (DC-01).

---

## 3. Asset Categories

To facilitate appropriate tracking and control, FinNexus Solutions categorizes assets as follows:

| Category | Description | Examples |
| :---: | :--- | :--- |
| **Physical Endpoints** | Devices assigned to individual personnel for daily operations. | Laptops (Windows/macOS), corporate-issued smartphones, hardware security keys (YubiKeys). |
| **Infrastructure Assets** | Hardware and virtualized resources supporting core network and application services. | Cloud compute instances (EC2/VMs), load balancers, physical switches/routers in office MDF/IDF rooms. |
| **Software & Applications** | Commercial off-the-shelf (COTS) software, SaaS subscriptions, and custom-developed applications. | GitHub Enterprise, AWS Management Console, internally developed payment processing services, Microsoft 365. |
| **Information Assets** | Databases, file shares, and intellectual property repositories (data classification is managed under DC-01, but the storage medium is an asset). | PostgreSQL databases, S3 buckets, source code repositories. |

---

## 4. Policy Statements

### AS-01 - Centralized Asset Inventory

FinNexus Solutions MUST maintain a centralized, dynamic inventory of all physical and logical assets using the approved IT Service Management (ITSM) platform and Cloud Security Posture Management (CSPM) tools. The inventory MUST record, at a minimum, the asset's unique identifier (e.g., serial number, MAC address, instance ID), current status, classification/criticality, location (physical or logical), and assigned owner. IT teams MUST automate the discovery of cloud infrastructure assets using API integrations with AWS/Azure/GCP, scanning at least every **24 hours**.

> **Framework Mapping:** ISO/IEC 27001:2022 A.5.9; NIST CSF 2.0 ID.AM-01, ID.AM-02; PCI DSS v4.0.1 Req 2.4

---

### AS-02 - Asset Ownership

Every asset recorded in the FinNexus Solutions inventory MUST have a designated, named owner (a specific role or individual) responsible for the asset's security and lifecycle. For physical endpoints, the owner is the assigned employee or contractor. For infrastructure and software applications, the owner MUST be the respective Engineering or IT manager. Asset ownership MUST be verified during the quarterly access recertification process. Orphaned assets identified during inventory scans MUST be quarantined or decommissioned within **72 hours** by the IT Security Lead if no owner can be identified.

> **Framework Mapping:** ISO/IEC 27001:2022 A.5.9; NIST CSF 2.0 ID.AM-03; PCI DSS v4.0.1 Req 2.4

---

### AS-03 - Acceptable Use of Assets

Personnel MUST use FinNexus Solutions-issued assets exclusively for authorized business purposes and in accordance with the Acceptable Use Policy (AU-01). Personnel MUST NOT install unauthorized or unapproved software, circumvent installed endpoint detection and response (EDR) agents, or disable mobile device management (MDM) profiles on physical endpoints. Use of personal, unmanaged devices (BYOD) to access Restricted or Confidential data is strictly prohibited unless explicitly authorized and enrolled in the FinNexus Solutions MDM solution.

> **Framework Mapping:** ISO/IEC 27001:2022 A.5.10; NIST CSF 2.0 PR.AT-01; DPDP Act 2023 Sec 8

---

### AS-04 - Endpoint Device Hardening and Management

All physical endpoints (laptops, mobile devices) issued by FinNexus Solutions MUST be enrolled in the centralized MDM platform prior to deployment. The IT team MUST configure endpoints with full-disk encryption (BitLocker for Windows, FileVault for macOS), host-based firewalls, and active EDR agents. Devices MUST be configured to lock automatically after a maximum of **15 minutes** of inactivity, requiring biometric or strong password authentication to unlock.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.1, A.8.9; NIST CSF 2.0 PR.AA-03; PCI DSS v4.0.1 Req 8.2

---

### AS-05 - Cloud and Infrastructure Asset Provisioning

The provisioning of all cloud infrastructure and virtualized assets MUST be performed using Infrastructure as Code (IaC) templates approved by the IT Security Lead. Engineering teams MUST NOT manually deploy unmanaged compute instances or storage buckets in production environments. All IaC templates MUST undergo static security analysis via the CI/CD pipeline prior to deployment to enforce baseline security configurations and tagging requirements.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.8; NIST CSF 2.0 PR.IP-01; PCI DSS v4.0.1 Req 2.2

---

### AS-06 - Software Asset Management (SAM)

FinNexus Solutions MUST strictly control the procurement and installation of software applications to mitigate licensing risks and supply chain vulnerabilities. Personnel MUST only install software from the pre-approved IT self-service portal or obtain explicit authorization from IT via a documented ticketing process. The IT team MUST conduct a semi-annual review of all installed software across the endpoint fleet to identify and remove unauthorized (shadow IT), unsupported, or vulnerable applications.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.19; NIST CSF 2.0 ID.AM-02; PCI DSS v4.0.1 Req 2.4

---

### AS-07 - Asset Tracking and Physical Security

All physical assets (e.g., laptops, hardware tokens) MUST be physically secured when not in use. Employees operating in the Mumbai HQ or remote locations MUST NOT leave devices unattended in public spaces or visible in unattended vehicles. Devices stored in office environments MUST be secured using cable locks or stored in locked cabinets if left overnight. IT MUST track the physical location of endpoints via the MDM platform, and devices that fail to check in for **30 days** MUST be automatically marked as lost and subject to remote wipe commands.

> **Framework Mapping:** ISO/IEC 27001:2022 A.7.10; NIST CSF 2.0 PR.DS-01; PCI DSS v4.0.1 Req 9.3

---

### AS-08 - Asset Return and Offboarding

Upon planned termination or transition of an employee or contractor, all assigned FinNexus Solutions physical assets MUST be returned to the IT department by the end of the final working day. For immediate or for-cause terminations, HR and IT MUST coordinate to retrieve physical assets and revoke logical access to software and infrastructure assets within **1 hour**. The IT department MUST log the receipt of all returned physical assets in the ITSM platform within **24 hours** of return.

> **Framework Mapping:** ISO/IEC 27001:2022 A.5.11; NIST CSF 2.0 PR.IP-03; GDPR Art 32

---

### AS-09 - Secure Decommissioning and Disposal

All physical and logical assets MUST be securely decommissioned at the end of their lifecycle to prevent data leakage. Physical endpoints and storage drives MUST be cryptographically wiped or physically destroyed in accordance with the Data Classification & Handling Policy (DC-08) prior to disposal or recycling. Cloud infrastructure assets MUST be decommissioned using automated teardown scripts that ensure the secure deletion of attached storage volumes and the revocation of associated IAM roles. A certificate of destruction MUST be retained for all physically destroyed storage media.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.10; NIST CSF 2.0 PR.DS-03; PCI DSS v4.0.1 Req 9.4.6; DPDP Act 2023 Sec 8(7)

---

### AS-10 - Lost or Stolen Assets Incident Response

Personnel MUST report lost or stolen physical assets (e.g., laptops, smartphones, hardware keys) to the IT Helpdesk and IT Security Lead immediately, and no later than **12 hours** after discovery. The IT Security team MUST initiate an incident response protocol that includes issuing a remote wipe command via the MDM platform and revoking all active sessions and VPN certificates associated with the device. If the device contained Restricted data, Legal and Compliance MUST be notified immediately to assess regulatory breach notification requirements.

> **Framework Mapping:** ISO/IEC 27001:2022 A.5.24; NIST CSF 2.0 RS.CO-02; DPDP Act 2023 Sec 8(6); GDPR Art 33

---

## 5. Roles and Responsibilities

| Role | Responsibilities Under This Policy |
| :--- | :--- |
| **CISO** | Ultimate owner of the Asset Management Policy; ensures alignment with FinNexus Solutions' risk appetite and regulatory obligations. |
| **IT Asset Manager** | Manages the centralized asset inventory; oversees procurement, tracking, and physical disposal processes. |
| **IT Security Lead** | Defines endpoint hardening baselines; manages MDM and EDR deployments; executes remote wipe commands for lost/stolen devices. |
| **Engineering / Product Development** | Manages lifecycle of cloud infrastructure assets using approved IaC templates; ensures software assets are properly secured and patched. |
| **Legal and Compliance** | Advises on regulatory requirements for asset security and disposal; leads breach notification assessments for lost/stolen assets containing personal data. |
| **Human Resources** | Coordinates with IT to ensure timely return of physical assets during employee offboarding. |
| **All Employees and Contractors** | Maintain physical security of assigned assets; report lost or stolen assets within 12 hours; adhere to acceptable use requirements. |

---

## 6. Enforcement and Sanctions

Violations of this policy are assessed in proportion to the criticality of the asset involved, the nature of the violation, and whether it was deliberate or inadvertent:

- **Tier 1 - Minor Breach** (e.g., failure to log a peripheral asset in the inventory system; leaving a laptop unlocked in a secure FinNexus Solutions office area): Formal reminder and re-training; immediate correction of the inventory or security posture.
- **Tier 2 - Moderate Breach** (e.g., installing unauthorized "shadow IT" software on a corporate laptop; failing to return an asset promptly upon request during offboarding): Written warning; mandatory completion of Security Awareness training; temporary suspension of administrative privileges; escalation to HR.
- **Tier 3 - Severe Breach** (e.g., intentionally disabling EDR/MDM agents on a physical endpoint; losing a laptop containing unencrypted Restricted customer PII and failing to report it; manual deployment of unmanaged, internet-facing cloud infrastructure bypassing IaC controls): Immediate suspension of all access pending investigation; likely termination of employment or contract; potential legal action and/or criminal referral under DPDP Act 2023 and the Indian IT Act 2000; notification to relevant regulators (CERT-In, Data Protection Board of India, or applicable EU supervisory authority) if a data breach occurs.

All Tier 3 violations involving lost or compromised assets MUST be treated as potential data breach events and immediately referred to Legal and Compliance for breach notification assessment under DPDP Act 2023 Section 8(6) and GDPR Article 33.

---

## 7. Review Cadence

| Attribute | Details |
| :--- | :--- |
| **Standard Review Frequency**  | Annual (every 12 months from effective date)                              |
| **Triggered Review Criteria**  | Major changes to FinNexus Solutions' physical footprint (e.g., opening a new headquarters); significant shifts in cloud provider strategy; after any Tier 3 violation involving asset loss or mismanagement. |
| **Policy Owner (Review Lead)** | IT Asset Manager, FinNexus Solutions                                      |
| **Review Approver**            | CISO                                                                      |
| **Next Scheduled Review**      | DD.MM.YY                                                                |

---

## 8. Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | DD.MM.YY | IT Asset Manager, FinNexus Solutions | Initial policy authored, reviewed, and approved. |
