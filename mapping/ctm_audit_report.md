# Control Traceability Matrix (CTM) Audit Report

## Document Control
**Date:** DD.MM.YY
**Subject:** Control-Traceability-Matrix Verification
**Target:** FinNexus Solutions

## Audit Objective
Verify the accuracy of mapped security frameworks against the internal control objectives documented within the Control Traceability Matrix. The audit focuses on validating exact section and requirement citations across all mapped compliance standards.

## Scope
The scope of this audit is limited to the mappings defined within the [Control Traceability Matrix](#ctm). The review covers specific mapped rows across ISO/IEC 27001:2022, NIST SP 800-88, DPDPA 2023, GDPR, PCI DSS v4.0.1, and NIST CSF 2.0.

## Criteria
Mappings were evaluated against the official published texts of the following standards:
- ISO/IEC 27001:2022
- NIST SP 800-88 Revision 1
- DPDPA 2023 / DPDP Rules 2025
- GDPR
- PCI DSS v4.0.1
- NIST Cybersecurity Framework (CSF) 2.0

## Methodology
Each reference was independently verified by conducting primary-source searches within the applicable standard text before a verdict was rendered. Existing matrix entries were not assumed to be correct. Validated entries are marked as confirmed; incorrect or deprecated entries are provided with corrected citations based on current framework versions.

## Results/Findings

### 1. AM-04: ISO 27001:2022 Reference for MFA Enforcement
- **Matrix Entry:** `A.8.5`
- **Control Context:** MFA enforcement (method strength, deprecation of SMS OTP for privileged use).
- **Finding:** A.8.5 (Secure Authentication) correctly governs the authentication process and MFA mandates. A.5.17 applies separately to credential lifecycle management (secrets).
- **Verdict:** Confirmed Correct.

### 2. DC-08: NIST SP 800-88 Citation for Secure Disposal
- **Matrix Entry:** `NIST SP 800-88`
- **Control Context:** Secure disposal via crypto-shredding or physical destruction.
- **Finding:** NIST SP 800-88 Revision 1 is the active standard and defines the Clear, Purge, and Destroy taxonomy specified in the control.
- **Verdict:** Confirmed Correct.

### 3. IR-01 / IR-02: Breach Notification (DPDPA Section & GDPR Article 33)
- **Matrix Entry (IR-06 row):** DPDPA `Sec 8(6)`; GDPR `Art 33, 34`
- **Control Context:** Regulatory breach notification timeline and obligations.
- **Finding:** DPDPA Section 8(6) is the foundational requirement for Board notification. GDPR Article 33 (supervisory authority notification within 72 hours) and Article 34 (data subject notification) are the correct citations.
- **Verdict:** Confirmed Correct.

### 4. PA-04: PCI DSS v4.0.1 Requirement for Password Expiration
- **Matrix Entry:** `Req 8.3.9`
- **Control Context:** No arbitrary time-based password expiration.
- **Finding:** PCI DSS v4.0.1 Requirement 8.3.9 addresses periodic credential change requirements, deprecating arbitrary interval rotation unless compromised.
- **Verdict:** Confirmed Correct.

### 5. VR-10: ISO 27001:2022 Controls A.8.30 and A.8.32
- **Matrix Entry:** `A.8.30, A.8.32`
- **Control Context:** Software supply chain and CI/CD vulnerability blocking.
- **Finding:** Both A.8.30 (Outsourced Development) and A.8.32 (Change Management) apply. Adding A.5.21 (Managing Information Security in the ICT Supply Chain) increases precision.
- **Verdict:** Confirmed Correct. Recommended addition: `A.5.21`.

### 6. BC-08: NIST CSF 1.1 PR.AC-03 to CSF 2.0 Equivalent
- **Matrix Entry:** `PR.AC-03`
- **Control Context:** Alternate workspace redundant VPN gateways.
- **Finding:** `PR.AC-03` is a deprecated CSF 1.1 subcategory. The correct CSF 2.0 mapping for technology infrastructure resilience is `PR.IR-03`.
- **Verdict:** Corrected. Update to `PR.IR-03`. Optional supplementary addition: `PR.AA-05` (access permissions).

### 7. IR-06: NIST CSF Reference
- **Matrix Entry:** Blank (Suggested: `RS.CO-03`)
- **Control Context:** Regulatory breach notification.
- **Finding:** RS.CO-02 explicitly covers formal notification to internal and external stakeholders, including regulators. RS.CO-03 applies to broader, ongoing information sharing.
- **Verdict:** Corrected. Update to `RS.CO-02`.

### 8. VR-05: PCI DSS Reference
- **Matrix Entry:** Blank (Suggested: `Req 12.9`)
- **Control Context:** Right to Audit clause in Tier 1 contracts.
- **Finding:** Req 12.9 applies to outbound service-provider obligations. FinNexus acting as a customer enforces this via Req 12.8.2 (written agreement) and Req 12.8.4 (annual compliance monitoring).
- **Verdict:** Corrected. Update to `Req 12.8.2, 12.8.4`.

### 9. VR-08: NIST CSF Reference
- **Matrix Entry:** Blank (Suggested: `PR.DS-03`)
- **Control Context:** Vendor offboarding data destruction.
- **Finding:** `PR.DS-03` was removed in CSF 2.0. The direct mapping for data lifecycle and disposal management is `ID.AM-08`.
- **Verdict:** Corrected. Update to `ID.AM-08`.

### 10. BC-06: NIST CSF Reference
- **Matrix Entry:** `PR.DS-11` (Suggested: `PR.PT-05` or `RC.RP-01`)
- **Control Context:** Multi-AZ active-active or auto active-passive failover.
- **Finding:** `PR.DS-11` covers backups. `PR.PT-05` does not exist in CSF 2.0. `PR.IR-03` is the correct subcategory for resilience mechanisms and High Availability architecture.
- **Verdict:** Corrected. Update to `PR.IR-03`.

## Exceptions/Open Items

### PA-10: DPDPA/GDPR Applicability
- **Control Context:** Continuous monitoring against known-compromised password databases (HIBP).
- **Finding:** Comparing password hashes against external breach databases triggers personal data processing considerations. GDPR Article 6(1)(f) (legitimate interests) is plausible for lawful processing, while DPDPA Section 8(4) (reasonable security safeguards) may also apply. Determining exact regulatory obligations depends entirely on the technical implementation of the monitoring mechanism (e.g., whether data remains on-premises versus external transmission).
- **Status:** Open. Requires explicit review and judgment by the Data Protection Officer (DPO) prior to adding formal compliance citations.

## Conclusion
The CTM maintains accurate mappings for core ISO 27001, PCI DSS v4.0.1, and GDPR controls. Five structural corrections are required to align the matrix with NIST CSF 2.0 taxonomy, and two missing mappings for PCI DSS and ISO have been resolved. The DPO must review PA-10 to determine exact DPDPA and GDPR applicability for continuous credential monitoring. Updating the CTM with the corrected findings will ensure its validity as a compliance artifact.
