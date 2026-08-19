# Incident Response Policy

| Field | Details |
| :--- | :--- |
| **Policy ID**          | IR                                                               |
| **Document Title**     | Incident Response Policy                                         |
| **Version**            | 1.0                                                              |
| **Status**             | Active                                                           |
| **Classification**     | Internal — Restricted                                            |
| **Effective Date**     | DD.MM.YY                                                       |
| **Last Reviewed**      | DD.MM.YY                                                       |
| **Next Review Due**    | DD.MM.YY                                                       |
| **Policy Owner**       | IT Security Lead, FinNexus Solutions                             |
| **Approved By**        | Chief Information Security Officer (CISO), FinNexus Solutions    |
| **Framework Alignment**| ISO/IEC 27001:2022 (A.5.24, A.5.25, A.5.26, A.5.27, A.5.28); NIST CSF 2.0 (RS.MA-02, RS.AN-03, RS.MA-03, RS.CO-02, RS.IM-01); PCI DSS v4.0.1 (Req 12.10); DPDPA 2025 (Sec 8); GDPR (Art 33, 34) |

---

## 1. Purpose

FinNexus Solutions operates a high-availability financial services platform processing significant volumes of Personally Identifiable Information (PII) and payment account data across India, the United States, and the European Union. In the event of a cybersecurity incident, rapid, coordinated, and effective response is critical to minimizing operational impact, preventing data loss, and maintaining the trust of our customers.

This policy establishes the formal requirements for reporting, managing, and resolving security incidents at FinNexus Solutions. It ensures that all personnel understand their obligations during an incident and that FinNexus Solutions complies with strict breach notification timelines mandated by DPDPA 2025, GDPR, and PCI DSS v4.0.1. By standardizing our response methodology, we reduce the duration and impact of security events while facilitating continuous improvement through post-incident review.

---

## 2. Scope

This policy applies to:

- **All personnel** employed or contracted by FinNexus Solutions, including permanent employees, contractors, interns, and third-party vendors who access FinNexus Solutions systems or data.
- **All systems and environments** owned, managed, or leased by FinNexus Solutions, including cloud infrastructure, corporate IT networks, endpoints, and third-party SaaS applications.
- **All security events and incidents**, ranging from suspected phishing attempts and malware infections to confirmed data breaches and widespread service outages caused by malicious activity.
- **All third-party vendors** providing managed services or acting as data processors, who must report incidents to FinNexus Solutions in accordance with their contractual Data Processing Agreements (DPAs) or Master Service Agreements (MSAs).

This policy does not cover standard IT helpdesk operations (e.g., routine password resets or hardware failures) unless those events are indicative of a broader security compromise.

---

## 3. Incident Severity Levels

FinNexus Solutions classifies security incidents into four severity levels to dictate the required response velocity, escalation paths, and external notification obligations.

| Severity Level | Description | Examples |
| :---: | :--- | :--- |
| **SEV-1 (Critical)** | Confirmed breach of Restricted data; severe disruption of core financial services; active ransomware deployment; regulatory notification highly likely. | Exfiltration of customer PII or PAD; complete outage of the primary transaction processing API; compromise of a Tier 0 infrastructure credential. |
| **SEV-2 (High)** | Confirmed compromise of Confidential data; partial disruption of customer-facing services; successful phishing leading to account takeover of a privileged user. | Compromise of an IT administrator's account; discovery of a web shell on a public-facing staging server; theft of unencrypted corporate laptops. |
| **SEV-3 (Medium)** | Isolated security event with no immediate impact on Restricted data or core services, but requiring formal investigation and containment. | Localized malware infection on a standard employee endpoint; successful phishing of a non-privileged user; unauthorized access attempt blocked by MFA. |
| **SEV-4 (Low)** | Suspected security event or anomaly that requires triage but poses minimal risk to the organization. | Receipt of a suspicious email (phishing attempt); automated vulnerability scanner alerts; unsuccessful brute-force login attempts. |

---

## 4. Policy Statements

### IR-01 — Incident Reporting Obligations

All FinNexus Solutions employees and contractors MUST immediately report any suspected or confirmed security incident to the IT Security Helpdesk via the internal ticketing system, dedicated Slack channel (`#security-alerts`), or the emergency hotline. Personnel MUST NOT attempt to investigate or remediate the incident themselves unless explicitly authorized by the IT Security Lead. Reports MUST be submitted within **2 hours** of discovering the anomaly.

> **Framework Mapping:** ISO 27001:2022 A.5.24; NIST CSF 2.0 RS.MA-02; PCI DSS v4.0.1 Req 12.10.1

---

### IR-02 — Incident Triage and Classification

Upon receiving a security incident report, the IT Security team MUST conduct initial triage and assign a severity level (SEV-1 to SEV-4) within **1 hour** for potential SEV-1/SEV-2 incidents, and within **4 hours** for SEV-3/SEV-4 incidents. The IT Security Lead MUST validate the classification of any SEV-1 or SEV-2 incident and immediately escalate it to the CISO.

> **Framework Mapping:** ISO 27001:2022 A.5.25; NIST CSF 2.0 RS.AN-03; PCI DSS v4.0.1 Req 12.10.1

---

### IR-03 — Incident Containment

For any confirmed SEV-1, SEV-2, or SEV-3 incident, the IT Security team MUST implement containment measures to prevent further unauthorized access or data exfiltration. Containment actions MUST be executed within **2 hours** of classification for SEV-1 incidents. Permissible containment actions include, but are not limited to, isolating affected endpoints from the network, revoking compromised user sessions and credentials, and suspending vulnerable application services.

> **Framework Mapping:** ISO 27001:2022 A.5.26; NIST CSF 2.0 RS.MA-03; PCI DSS v4.0.1 Req 12.10.1

---

### IR-04 — Evidence Preservation

During containment and eradication, the IT Security team and Engineering teams MUST preserve forensic evidence. Teams MUST NOT destroy, alter, or overwrite system logs, memory dumps, or disk images of compromised systems. Snapshots or forensic images of affected systems MUST be captured prior to initiating eradication or recovery procedures.

> **Framework Mapping:** ISO 27001:2022 A.5.28; NIST CSF 2.0 RS.AN-03; PCI DSS v4.0.1 Req 12.10.1

---

### IR-05 — Eradication and Recovery

The IT Security and Engineering teams MUST identify and eliminate the root cause of the incident before restoring systems to normal operations. For SEV-1 and SEV-2 incidents, the CISO MUST formally approve the recovery plan before affected systems are reconnected to the production network. Recovery procedures MUST include password resets for all involved accounts, deployment of necessary security patches, and enhanced monitoring of the recovered assets for a minimum of **14 days**.

> **Framework Mapping:** ISO 27001:2022 A.5.27; NIST CSF 2.0 RS.MA-04; PCI DSS v4.0.1 Req 12.10.1

---

### IR-06 — Breach Notification (Regulatory)

In the event of a personal data breach (SEV-1), Legal and Compliance MUST evaluate the regulatory notification requirements. Under DPDPA 2025 Section 8(6), notifications to the Data Protection Board of India and affected data principals MUST occur as prescribed by law. Under GDPR Article 33, notifications to the competent supervisory authority MUST occur within **72 hours** of FinNexus Solutions becoming aware of the breach. The IT Security team MUST provide all necessary technical details to Legal and Compliance within **24 hours** of breach confirmation to support these timelines.

> **Framework Mapping:** DPDPA 2025 Sec 8(6); GDPR Art 33, 34; ISO 27001:2022 A.5.24

---

### IR-07 — External Communications

Only authorized spokespersons (the CEO, CISO, or designated Public Relations lead) MAY issue public statements or communicate with the media regarding a security incident. All external communications MUST be reviewed and approved by Legal and Compliance prior to release. Employees MUST NOT discuss security incidents on social media or with unauthorized third parties.

> **Framework Mapping:** ISO 27001:2022 A.5.24; NIST CSF 2.0 RS.CO-02

---

### IR-08 — Post-Incident Review

A formal post-incident review (PIR) MUST be conducted for all SEV-1 and SEV-2 incidents. The IT Security Lead MUST convene the PIR within **5 business days** of incident closure. The PIR MUST document the root cause, a timeline of events, the effectiveness of the response, and specific, actionable lessons learned. The resulting PIR report MUST be distributed to the CISO, Engineering teams, and Legal and Compliance.

> **Framework Mapping:** ISO 27001:2022 A.5.27; NIST CSF 2.0 RS.IM-01; PCI DSS v4.0.1 Req 12.10.6

---

### IR-09 — Incident Response Testing

The IT Security team MUST conduct a tabletop exercise or simulation testing the Incident Response Plan at least **annually**. The exercise MUST include participation from IT Security, Engineering, Legal and Compliance, and Human Resources. Lessons learned from these exercises MUST be incorporated into updates of the Incident Response Plan and associated playbooks within **30 days** of the exercise conclusion.

> **Framework Mapping:** ISO 27001:2022 A.5.25; NIST CSF 2.0 RS.CO-01; PCI DSS v4.0.1 Req 12.10.2

---

### IR-10 — Third-Party Incident Coordination

When an incident involves a third-party vendor (e.g., a SaaS provider or managed service), the IT Security team MUST coordinate the response with the vendor's designated security contact. Legal and Compliance MUST ensure that vendor DPAs mandate incident notification to FinNexus Solutions within **24 hours** of the vendor confirming a breach affecting FinNexus Solutions data.

> **Framework Mapping:** ISO 27001:2022 A.5.24, A.5.26; NIST CSF 2.0 GV.SC-08; GDPR Art 33

---

## 5. Roles and Responsibilities

| Role | Responsibilities Under This Policy |
| :--- | :--- |
| **CISO** | Policy ultimate owner; oversees the incident response program; approves recovery plans for SEV-1/SEV-2 incidents; serves as executive escalation point. |
| **IT Security Lead** | Manages day-to-day incident response operations; validates incident severity classifications; leads containment, eradication, and post-incident reviews; maintains IR playbooks. |
| **Engineering / Product Development** | Assists in investigating and containing application-level incidents; implements eradication and recovery tasks; preserves forensic evidence during response activities. |
| **Legal and Compliance** | Evaluates regulatory notification requirements (DPDPA, GDPR); leads communication with data protection authorities; reviews and approves external breach communications. |
| **Human Resources** | Coordinates employee-related communications; manages disciplinary actions for policy violations leading to incidents; assists with insider threat investigations. |
| **All Employees, Contractors, and Vendors** | Promptly report suspected security incidents; adhere to containment instructions; do not discuss incidents externally without authorization. |

---

## 6. Enforcement and Sanctions

Violations of this policy are assessed based on the severity of the incident and the nature of the violation:

- **Tier 1 — Minor Breach** (e.g., delaying the report of a SEV-4 phishing email by 4 hours): Formal reminder and re-training; correction of the reporting process.
- **Tier 2 — Moderate Breach** (e.g., attempting to clean up a malware infection locally without reporting it, destroying potential evidence): Written warning; mandatory completion of Incident Response training module; escalation to HR.
- **Tier 3 — Severe Breach** (e.g., failure to report a known SEV-1 data breach; unauthorized external disclosure of incident details to the media): Immediate suspension of system access pending investigation; likely termination of employment or contract; potential legal action under DPDPA 2025 and the Indian IT Act 2000; notification to relevant regulators (CERT-In, Data Protection Board of India, or EU supervisory authority) if the failure constitutes a regulatory breach.

All Tier 3 violations MUST be treated as potential data breach events and immediately referred to Legal and Compliance for breach notification assessment under DPDPA 2025 Section 8(6) and GDPR Article 33.

---

## 7. Review Cadence

| Attribute | Details |
| :--- | :--- |
| **Standard Review Frequency** | Annual (every 12 months from effective date) |
| **Triggered Review Criteria** | Following any SEV-1 incident; material changes to DPDPA or GDPR breach notification timelines; significant changes to FinNexus Solutions infrastructure or organizational structure. |
| **Policy Owner (Review Lead)** | IT Security Lead, FinNexus Solutions |
| **Review Approver** | CISO |
| **Next Scheduled Review** | DD.MM.YY |

---

## 8. Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | DD.MM.YY | IT Security Lead, FinNexus Solutions | Initial policy authored, reviewed, and approved. |
