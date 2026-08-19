# Business Continuity & Backup Policy

| Field | Details |
| :--- | :--- |
| **Policy ID**          | BC                                                               |
| **Document Title**     | Business Continuity & Backup Policy                              |
| **Version**            | 1.0                                                              |
| **Status**             | Draft (illustrative)                                             |
| **Classification**     | Internal - Restricted                                            |
| **Effective Date**     | DD.MM.YY                                                       |
| **Last Reviewed**      | DD.MM.YY                                                       |
| **Next Review Due**    | DD.MM.YY                                                       |
| **Policy Owner**       | CISO, FinNexus Solutions                                         |
| **Approved By**        | Chief Information Security Officer (CISO), FinNexus Solutions    |
| **Framework Alignment**| ISO/IEC 27001:2022 (A.5.29, A.5.30, A.8.13, A.8.14, A.8.24); NIST CSF 2.0 (PR.DS-11, RC.RP-01, RC.RP-03); PCI DSS v4.0.1 (Req 3.5, 10.7); DPDP Act 2023 (Sec 8); GDPR (Art 32) |

---

## 1. Purpose

FinNexus Solutions, as a high-availability financial services provider, must maintain operational resilience against cyber threats, hardware failures, and environmental disasters. Any disruption to the core financial applications or customer-facing platforms directly impacts revenue, regulatory compliance, and customer trust across our Indian, US, and EU operations.

This policy establishes the requirements for data backups, high availability, and business continuity planning to ensure that FinNexus Solutions can sustain critical operations and rapidly recover from disruptive events. It mandates concrete Recovery Point Objectives (RPO) and Recovery Time Objectives (RTO) proportionate to the criticality of the services and data involved, aligning with regulatory expectations under DPDP Act 2023, GDPR, and PCI DSS v4.0.1.

---

## 2. Scope

This policy applies to:

- **All data and systems** managed by FinNexus Solutions, including cloud-hosted infrastructure (AWS/Azure/GCP), core financial applications, and corporate IT environments.
- **All personnel** responsible for designing, operating, or maintaining backup and disaster recovery systems, particularly the Engineering / Product Development and Information Technology (IT) teams.
- **Third-Party Vendors** providing managed services or critical SaaS platforms, who must demonstrate business continuity capabilities that meet or exceed FinNexus Solutions' internal requirements as defined in their Master Service Agreements (MSAs).

This policy does not apply to non-persistent development or staging environments that do not process production or Restricted data.

---

## 3. System Criticality Tiers

All systems and services at FinNexus Solutions MUST be assigned a criticality tier to dictate their backup and recovery requirements.

| Tier | Criticality Label | RTO | RPO | Description |
| :---: | :--- | :--- | :--- | :--- |
| **1** | 🔴 **Mission Critical** | < 4 hours | < 1 hour | Core financial platforms, payment processing systems (CDE), authentication services, and databases holding Restricted data. |
| **2** | 🟠 **Business Critical** | < 12 hours | < 4 hours | Internal corporate IT systems, HR platforms, legal and compliance document repositories. |
| **3** | 🟡 **Operational** | < 48 hours | < 24 hours | Internal wikis, non-critical communication tools, and archival systems. |

---

## 4. Policy Statements

### BC-01 - Business Impact Analysis (BIA)

FinNexus Solutions MUST conduct a formal Business Impact Analysis (BIA) annually, or upon any significant architectural change to the core financial applications. The BIA MUST identify and classify all systems into the Criticality Tiers defined in Section 3, establishing precise Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) for each asset. The CISO MUST review and approve the finalized BIA.

> **Framework Mapping:** ISO/IEC 27001:2022 A.5.29; NIST CSF 2.0 ID.RA-04

---

### BC-02 - Backup Frequency and Retention

Engineering teams and IT MUST configure automated backups for all Tier 1 and Tier 2 systems in accordance with the following minimum schedules:

- **Tier 1 (Mission Critical):** Continuous replication or transaction-log backups every **15 minutes** (to meet < 1 hour RPO), with daily full backups retained for **30 days** in hot storage, and **1 year** in cold storage (e.g., AWS S3 Glacier).
- **Tier 2 (Business Critical):** Daily incremental backups, with weekly full backups retained for **60 days**.
- **Tier 3 (Operational):** Weekly full backups retained for **30 days**.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.13; NIST CSF 2.0 PR.DS-11; PCI DSS v4.0.1 Req 10.7.2

---

### BC-03 - Backup Encryption

All backups of FinNexus Solutions systems and data MUST be encrypted both in transit and at rest, regardless of the system's criticality tier. Backups MUST use AES-256 bit encryption for data at rest and TLS 1.2 or higher (TLS 1.3 preferred) for data in transit. Cryptographic keys used for backup encryption MUST be stored in a centralized, hardware-backed Key Management System (KMS) physically and logically separated from the backup storage environment.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.24; NIST CSF 2.0 PR.DS-01; PCI DSS v4.0.1 Req 3.5; GDPR Art 32

---

### BC-04 - Immutable Storage and Offsite Replication

To defend against ransomware and data destruction attacks, all Tier 1 and Tier 2 backups MUST be stored using Write-Once-Read-Many (WORM) immutable storage for at least the first **30 days** of their retention period. Additionally, all backups MUST be automatically replicated to a geographically separate cloud region (e.g., from Mumbai ap-south-1 to ap-south-2) immediately upon creation.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.13; NIST CSF 2.0 PR.DS-11; GDPR Art 32(1)(c)

---

### BC-05 - Backup Restoration Testing

IT and Engineering teams MUST perform formal, documented restoration tests of backup media and recovery procedures. Tier 1 system backups MUST be tested **quarterly**; Tier 2 system backups MUST be tested **semi-annually**. The tests MUST verify that the data is recoverable, uncorrupted, and can be restored within the mandated RTO. Results of these tests, including any failures or delays, MUST be documented and submitted to the IT Security Lead for review.

> **Framework Mapping:** ISO/IEC 27001:2022 A.5.30, A.8.13; NIST CSF 2.0 RC.RP-03; PCI DSS v4.0.1 Req 10.7.3

---

### BC-06 - High Availability Architecture

All Tier 1 (Mission Critical) platforms and customer-facing financial services MUST be deployed in a highly available architecture. Engineering teams MUST utilize multi-Availability Zone (Multi-AZ) deployments with active-active or automated active-passive failover capabilities to ensure that a single datacenter or zone failure does not result in an outage exceeding the 4-hour RTO.

> **Framework Mapping:** ISO/IEC 27001:2022 A.8.14; NIST CSF 2.0 PR.DS-11

---

### BC-07 - Disaster Recovery Plan (DRP)

FinNexus Solutions MUST maintain a comprehensive Disaster Recovery Plan (DRP) that documents the specific technical steps required to failover, recover, and restore all Tier 1 and Tier 2 systems. The DRP MUST be updated **annually** or within **30 days** of any major infrastructure change. The DRP MUST include contact details for the incident response team, vendor support escalation paths, and manual processing fallbacks where applicable.

> **Framework Mapping:** ISO/IEC 27001:2022 A.5.30; NIST CSF 2.0 RC.RP-01

---

### BC-08 - Alternate Workspace and Access

To ensure the hybrid workforce can continue operations during a regional disruption or headquarters outage, IT MUST maintain redundant, load-balanced VPN gateways and secure remote access solutions. Critical personnel (e.g., IT, Security, and essential customer support) MUST be provided with company-issued laptops configured with failover access to secondary cloud environments.

> **Framework Mapping:** ISO/IEC 27001:2022 A.5.30; NIST CSF 2.0 PR.AC-03

---

### BC-09 - Business Continuity Tabletop Exercises

The CISO MUST facilitate a formal Business Continuity Tabletop Exercise at least **bi-annually** (every six months). The exercise MUST simulate a severe disruption (e.g., widespread ransomware deployment or primary cloud region failure) and involve key stakeholders from IT, Engineering, Legal and Compliance, and Human Resources. Lessons learned and action items MUST be tracked in the internal risk register and remediated within **90 days**.

> **Framework Mapping:** ISO/IEC 27001:2022 A.5.30; NIST CSF 2.0 RC.RP-03; DPDP Act 2023 Sec 8

---

### BC-10 - Supply Chain Continuity

Any third-party vendor providing a service classified as Tier 1 MUST be contractually obligated via a Master Service Agreement (MSA) or Service Level Agreement (SLA) to meet a minimum **99.9% uptime** and demonstrate their own compliant DRP. Legal and Compliance, alongside the IT Security Lead, MUST review vendor continuity plans during the annual vendor risk assessment cycle.

> **Framework Mapping:** ISO/IEC 27001:2022 A.5.21, A.5.22; NIST CSF 2.0 GV.SC-06

---

### BC-11 - Continuity Incident Communication

In the event of a declared disaster or significant disruption affecting Tier 1 systems, the CISO or designated incident commander MUST notify all internal stakeholders and the Executive Board within **1 hour**. If the disruption affects the availability of Restricted personal data or customer funds, Legal and Compliance MUST be engaged immediately to evaluate regulatory notification requirements under DPDP Act 2023 Section 8(6) and GDPR Article 33.

> **Framework Mapping:** ISO/IEC 27001:2022 A.5.24; NIST CSF 2.0 RC.CO-03; DPDP Act 2023 Sec 8(6); GDPR Art 33

---

## 5. Roles and Responsibilities

| Role | Responsibilities Under This Policy |
| :--- | :--- |
| **CISO** | Approves the BIA and DRP; facilitates bi-annual tabletop exercises; declares formal disaster events. |
| **IT Security Lead** | Reviews backup architecture for immutability and encryption; monitors quarterly restoration test results; oversees vendor continuity assessments. |
| **Engineering / Product Development** | Implements Multi-AZ high availability; configures automated backups and replication for core financial applications; executes restoration testing. |
| **Information Technology (IT)** | Manages backups for corporate systems; maintains redundant VPN and remote access infrastructure; provisions alternate workspaces. |
| **Legal and Compliance** | Evaluates regulatory notification requirements during downtime incidents; reviews vendor SLAs for continuity obligations. |
| **Human Resources (HR)** | Maintains emergency contact directories for personnel; communicates alternate work arrangements during physical disruptions. |

---

## 6. Enforcement and Sanctions

Violations of this policy are assessed in proportion to the severity of the control failure and the risk it introduces to FinNexus Solutions' resilience:

- **Tier 1 - Minor Breach** (e.g., failing to update the DRP documentation within 30 days of a minor system change; missing a scheduled backup test by one week): Formal reminder and re-training; immediate remediation of the delayed task within 48 hours.
- **Tier 2 - Moderate Breach** (e.g., misconfiguring backup schedules resulting in failure to meet the RPO for a Tier 2 system; storing backups without encryption): Written warning; mandatory audit of all systems managed by the responsible individual; escalation to HR.
- **Tier 3 - Severe Breach** (e.g., disabling immutable storage on Tier 1 backups; deliberate failure to implement Multi-AZ redundancy for core financial platforms leading to a massive outage): Immediate suspension of system access pending investigation; likely termination of employment or contract; potential legal referral under applicable corporate liability laws; potential regulatory notification to CERT-In or the relevant EU supervisory authority if downtime results in severe consumer harm.

All Tier 3 violations MUST be treated as critical risk events and reported immediately to the CISO and Legal and Compliance.

---

## 7. Review Cadence

| Attribute | Details |
| :--- | :--- |
| **Standard Review Frequency** | Annual (every 12 months from effective date) |
| **Triggered Review Criteria** | Major migration to a new cloud provider; significant changes in core banking/financial regulatory uptime requirements; following the activation of the DRP during a real-world incident. |
| **Policy Owner (Review Lead)** | CISO, FinNexus Solutions |
| **Review Approver** | Legal and Compliance |
| **Next Scheduled Review** | DD.MM.YY |

---

## 8. Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | DD.MM.YY | CISO, FinNexus Solutions | Initial policy authored, reviewed, and approved. |
