# Control Traceability Matrix Assessment Report

## Document Control

| Field           | Value              |
| --------------- | ------------------ |
| Document ID     | CTM-AR-XX          |
| Version         | X.X                |
| Classification  | Internal - General |
| Status          | Portfolio draft    |
| Effective Date  | Not adopted        |
| Assessment Date | Illustrative       |
| Last Reviewed   | Not applicable     |

## 1. Executive Summary

This illustrative assessment shows how a mapping-quality review can test the relationship between internal controls and cited primary-source frameworks. It is not an independent audit, legal opinion, certification, or evidence that a control operates effectively. The recorded corrections align legacy NIST CSF 1.1 citations to the NIST CSF 2.0 taxonomy; PA-10 remains in “Review Required” status pending DPO assessment of the proposed implementation.

## 2. Objective

Verify the technical accuracy, version currency, and semantic alignment of control mappings documented in the Control Traceability Matrix against authoritative primary-source frameworks.

## 3. Scope

* **Target Artifact:** Control Traceability Matrix (CTM)
* **Policy Population:** 8 authored security policies (83 total controls)
* **Frameworks Assessed:** ISO/IEC 27001:2022, NIST CSF 2.0, PCI DSS v4.0.1, GDPR, DPDP Act 2023, DPDP Rules 2025, NIST SP 800-88 Rev. 2.

## 4. Criteria and Authoritative Sources

The exercise references the following authoritative texts. Their current version, applicability, and effective date must be reconfirmed before operational use:
* NIST SP 800-88 Rev. 2 (Guidelines for Media Sanitization)
* NIST CSF 2.0 (Cybersecurity Framework)
* PCI DSS v4.0.1 (Payment Card Industry Data Security Standard)
* ISO/IEC 27001:2022 (Information Security Management Systems)
* Digital Personal Data Protection Act, 2023 (India)
* Digital Personal Data Protection Rules, 2025 (India)
* General Data Protection Regulation (GDPR) (EU)

## 5. Methodology

The assessment utilized the following procedure:
1. **Version Validation:** Compare cited framework versions with the versions designated for the review; reconfirm current versions and effective dates before use.
2. **Semantic Applicability Review:** Compared the control objective against the explicit text of the cited framework requirement.
3. **Consistency Testing:** Verified that mappings do not conflate separate technical or legal requirements (e.g., separating DPDP Act 2023 statutory requirements from DPDP Rules 2025 notification timelines).
4. **Exception Review:** Validated the rationale for any controls flagged for 'Review'.

## 6. Findings

| ID | Control | Criterion | Observation | Assessment | Recommendation | Status |
| -- | ------- | --------- | ----------- | ---------- | -------------- | ------ |
| **BC-06** | Multi-AZ active-active failover | NIST CSF 2.0 | Matrix cited PR.DS-11 (Data Security/Backups) instead of resilience mechanisms. | Incorrect Category | Map to PR.IR-03. | Corrected |
| **BC-08** | Alternate workspace VPN | NIST CSF 2.0 | Matrix cited PR.AC-03, a deprecated CSF 1.1 subcategory. | Deprecated Version | Map to PR.IR-03. | Corrected |
| **DC-08** | Secure data disposal | NIST SP 800-88 | Matrix referenced strict multi-pass wipes under Rev. 1. Rev. 2 prioritizes programmatic sanitization and verification. | Outdated Standard | Update to NIST SP 800-88 Rev. 2. | Corrected |
| **IR-06** | Regulatory breach notification | DPDP Rules 2025 | Matrix stated "without undue delay". DPDP Rules 2025 mandate a strict 72-hour window for DPBI notification. | Inaccurate Timeline | Update wording to specify 72 hours under Rules 2025. | Corrected |
| **PA-10** | Compromised password monitoring | GDPR / DPDP Act | Continuous monitoring of password hashes externally triggers privacy considerations under GDPR Art. 6 and DPDP Act 2023. | Missing Implementation Facts | Requires DPO review of data flows to establish lawful basis. | Review Required |
| **VR-05** | Right to Audit clause | PCI DSS v4.0.1 | Matrix lacked clear TPSP compliance monitoring citation. | Missing Mapping | Map to Req 12.8.2, 12.8.4. | Corrected |
| **VR-08** | Vendor access revocation | NIST CSF 2.0 | Matrix suggested PR.DS-03 (deprecated). | Deprecated Version | Map to ID.AM-08. | Corrected |
| **VR-10** | CI/CD vulnerability blocking | ISO 27001:2022 | Mapped to A.8.30, A.8.32. | Incomplete Mapping | Add A.5.21 (ICT Supply Chain). | Corrected |

## 7. Open Items and Limitations

* **Legal Interpretation Dependency (PA-10):** Control PA-10 specifies comparing user password hashes against external breach databases (e.g., HIBP). Transmitting or processing personal data hashes externally triggers personal data processing considerations under both GDPR (Art. 6) and the Digital Personal Data Protection Act, 2023. This is an implementation-dependent assessment. No explicit compliance citation can be ratified until the Data Protection Officer (DPO) and Legal counsel review the technical implementation (on-premises versus external transmission) and establish the lawful basis. 

## 8. Overall Conclusion

The exercise covers 83 illustrative controls and demonstrates a repeatable approach to control mapping. It does not verify legal compliance or control operation. Before the matrix is used outside this portfolio, the control owners, Legal/Compliance, and an independent reviewer should validate applicability, mapping accuracy, implementation evidence, and the PA-10 privacy review.

## 9. References

* Control Traceability Matrix (Version X.X, illustrative)
* FinNexus Solutions Policy Suite (illustrative drafts)
