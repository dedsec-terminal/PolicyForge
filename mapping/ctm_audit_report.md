# Control Traceability Matrix Assessment Report

## Document Control

| Field           | Value                        |
| --------------- | ---------------------------- |
| Document ID     | CTM-AR-XX                  |
| Version         | XX                         |
| Classification  | Internal - General         |
| Status          | Final                      |
| Effective Date  | DD.MM.YY                   |
| Assessment Date | DD.MM.YY                   |
| Last Reviewed   | DD.MM.YY                   |

## 1. Executive Summary

A formal assessment of the Control Traceability Matrix (CTM) was conducted to verify mapping accuracy between internal FinNexus Solutions security controls and specified primary-source compliance frameworks. The matrix mappings for ISO/IEC 27001:2022, NIST SP 800-88 Rev. 2, PCI DSS v4.0.1, GDPR, and DPDP Act 2023 were found to be technically accurate. Corrections were implemented to align legacy NIST CSF 1.1 citations to NIST CSF 2.0 taxonomy. One control (PA-10) remains in 'Review Required' status pending DPO adjudication on privacy implications. 

## 2. Objective

Verify the technical accuracy, version currency, and semantic alignment of control mappings documented in the Control Traceability Matrix.

## 3. Scope

* **Target Artifact:** mapping/control-traceability-matrix.md (Version XX)
* **Policy Population:** 8 authored security policies (83 total controls)
* **Frameworks Assessed:** ISO/IEC 27001:2022, NIST CSF 2.0, PCI DSS v4.0.1, GDPR, DPDP Act 2023, DPDP Rules 2025, NIST SP 800-88 Rev. 2.

## 4. Criteria and Sources

Mappings were assessed against the current authoritative texts:
* NIST SP 800-88 Rev. 2
* NIST CSF 2.0
* PCI DSS v4.0.1
* ISO/IEC 27001:2022
* Digital Personal Data Protection Act, 2023
* Digital Personal Data Protection Rules, 2025
* General Data Protection Regulation (GDPR)

## 5. Methodology

The assessment utilized the following procedure:
1. **Version Validation:** Confirmed that referenced frameworks reflect currently active standard versions.
2. **Semantic Applicability Review:** Compared the control objective against the explicit text of the cited framework requirement.
3. **Consistency Testing:** Verified that mappings do not conflate separate technical or legal requirements (e.g., separating DPDP Act statutory requirements from DPDP Rules notification timelines).
4. **Exception Review:** Validated the rationale for any controls flagged for 'Review'.

## 6. Findings

| ID | Control | Criterion | Observation | Assessment | Recommendation | Status |
| -- | ------- | --------- | ----------- | ---------- | -------------- | ------ |
| **BC-06** | Multi-AZ active-active failover | NIST CSF 2.0 | Matrix cited PR.DS-11 (Data Security/Backups) instead of resilience mechanisms. | Incorrect Category | Map to PR.IR-03. | Corrected |
| **BC-08** | Alternate workspace VPN | NIST CSF 2.0 | Matrix cited PR.AC-03, a deprecated CSF 1.1 subcategory. | Deprecated Version | Map to PR.IR-03. | Corrected |
| **DC-08** | Secure data disposal | NIST SP 800-88 | Matrix referenced strict multi-pass wipes under Rev 1. Rev 2 prioritizes programmatic sanitization and verification. | Outdated Standard | Update to NIST SP 800-88 Rev. 2. | Corrected |
| **IR-06** | Regulatory breach notification | DPDP Rules 2025 | Matrix stated "without undue delay". DPDP Rules 2025 mandate a strict 72-hour window for DPBI notification. | Inaccurate Timeline | Update wording to specify 72 hours under Rules 2025. | Corrected |
| **VR-05** | Right to Audit clause | PCI DSS v4.0.1 | Matrix lacked clear TPSP compliance monitoring citation. | Missing Mapping | Map to Req 12.8.2, 12.8.4. | Corrected |
| **VR-08** | Vendor access revocation | NIST CSF 2.0 | Matrix suggested PR.DS-03 (deprecated). | Deprecated Version | Map to ID.AM-08. | Corrected |
| **VR-10** | CI/CD vulnerability blocking | ISO 27001:2022 | Mapped to A.8.30, A.8.32. | Incomplete Mapping | Add A.5.21 (ICT Supply Chain). | Corrected |

## 7. Open Items / Limitations

* **Legal Interpretation Dependency (PA-10):** Control PA-10 specifies comparing user password hashes against external breach databases (e.g., HIBP). Transmitting or processing personal data hashes externally triggers personal data processing considerations under both GDPR (Art. 6) and the DPDP Act 2023. This is an implementation-dependent assessment. No explicit compliance citation can be ratified until the Data Protection Officer (DPO) and Legal counsel review the technical implementation (on-premises versus external transmission) and establish the lawful basis. 

## 8. Overall Conclusion

Mapping accuracy was assessed across 83 organizational controls. The matrix demonstrates precise control-mapping judgment and relies on defensible semantic relationships rather than abstract assertions. Subject to the resolution of the single pending privacy review (PA-10), the Control Traceability Matrix serves as a reliable evidence artifact for external audit and assurance activities.
