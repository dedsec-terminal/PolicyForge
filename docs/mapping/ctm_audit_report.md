# CTM Independent Audit Report
## FinNexus Solutions — Control-Traceability-Matrix Verification
**Audited:** 2026-08-19  
**Scope:** [control-traceability-matrix.md](file:///d:/PolicyForge/mapping/control-traceability-matrix.md)  
**Method:** Each reference independently verified against primary-source searches of the applicable standard before any verdict was rendered. The existing matrix entries were not assumed correct.

---

## Part 1 — Six Specifically Requested Verifications

---

### 1. AM-04 — ISO 27001:2022 Reference for MFA Enforcement

**Matrix cites:** `A.8.5`  
**Investigated area:** A.5.17 (Authentication Information) vs. A.8.5 (Secure Authentication)

**Finding:**  
Both controls exist in ISO/IEC 27001:2022 Annex A and are clearly distinct:

| Control | Theme | Actual scope |
| :--- | :--- | :--- |
| **A.5.17** | Organizational | Lifecycle management of authentication *secrets* (passwords, PINs, tokens) — their issuance, rotation, confidentiality, and revocation |
| **A.8.5** | Technological | The *authentication process* itself — strength of methods, replay protection, MFA requirements, session management |

AM-04 mandates **MFA enforcement** (the authentication process, method strength, and deprecation of SMS OTP for privileged use). This is squarely the subject of **A.8.5**. A.5.17 governs the management of the secrets used *within* that process, not the MFA enforcement mandate itself.

> **VERDICT: ✅ CONFIRMED CORRECT**  
> `A.8.5` is the correct citation for MFA enforcement. A.5.17 is correctly used separately in AM-05 (password standards), not here.

---

### 2. DC-08 — NIST SP 800-88 Citation for Secure Disposal

**Matrix cites:** `NIST SP 800-88` (narrative text reference, not a section/requirement number)  
**Policy control:** "Secure disposal: crypto-shredding or NIST SP 800-88 wipe for digital; cross-cut shred + CoD for physical; hardware cleared before reuse"

**Finding:**  
NIST SP 800-88 *Revision 1* — "Guidelines for Media Sanitization" — is the correct and current standard (published December 2014; no superseding revision exists as of 2026). It defines exactly the three-tier sanitization taxonomy that DC-08 references:
- **Clear** — software/hardware overwrite for lower-sensitivity media
- **Purge** — cryptographic erase or degauss; resists lab-level recovery
- **Destroy** — physical destruction (shredding, pulverizing)

The matrix cites this standard correctly by name. The only nuance: the matrix does not cite a specific section within 800-88 (e.g., §2.3 Media Sanitization Decision Factors, Appendix A media-type tables), but that level of granularity is not typical in a CTM. The standard name itself is accurate.

> **VERDICT: ✅ CONFIRMED CORRECT**  
> "NIST SP 800-88" is the right standard for crypto-shredding and physical destruction guidance. No correction needed.

---

### 3. IR-01 / IR-02 — Breach Notification: DPDPA Section & GDPR Article 33

**Matrix cites (IR-06 row, which carries the breach notification obligation):**  
- DPDPA: `Sec 8(6)` — "notify Board without undue delay"  
- GDPR: `Art 33, 34`

**Note:** IR-01 and IR-02 themselves do not carry DPDPA/GDPR references in the matrix (those columns are blank); IR-06 is the row that actually maps breach notification. The user's question about IR-01/IR-02 timelines was investigating whether IR-06's citations are accurate — verified below.

**DPDPA Finding:**  
Section 8(6) of the DPDPA 2023 is confirmed as the foundational breach notification provision. It requires the Data Fiduciary to give the **Data Protection Board of India** and each affected Data Principal **intimation of the breach** in the form and manner prescribed. The specific 72-hour operational timeline flows from **Rule 7 of the DPDP Rules 2025** (subordinate legislation), not from Section 8(6) itself, which uses "form and manner as may be prescribed." The matrix saying "DPDPA Board without undue delay" against `Sec 8(6)` is accurate for the parent Act. The 72-hour mechanism is in the Rules, but Section 8(6) is the correct Act-level citation.

**GDPR Finding:**  
Article 33 is confirmed as the correct citation for supervisory-authority notification within **72 hours** of becoming aware of a breach (with a risk-threshold exception). Article 34 covers data-subject notification for high-risk breaches. The matrix cites both `Art 33, 34` at IR-06, which is accurate.

> **VERDICT: ✅ CONFIRMED CORRECT**  
> - DPDPA `Sec 8(6)` is the right Act-level citation; the "without undue delay" language is consistent (72-hr specifics are in Rules 2025).  
> - GDPR `Art 33` (72-hr supervisory authority) and `Art 34` (data-subject notification for high-risk breaches) are both correct.

---

### 4. PA-04 — PCI DSS v4.0.1 Requirement for Password Expiration / Service Account Rotation

**Matrix cites:** `Req 8.3.9`  
**Control:** "No arbitrary time-based password expiration; force-reset on confirmed compromise; service account/API keys rotate every 90 days"  

> **Important distinction:** PA-04 in this matrix is about *password expiration policy*, NOT MFA/FIDO2 (which is PA-01/PA-07). The user's question conflated PA-04 with MFA. The MFA enforcement row is AM-04/PA-01 and those cite Req 8.4/8.5 correctly (see AM-04 above).

**Finding on Req 8.3.9 (password expiration):**  
PCI DSS v4.0.1 Requirement **8.3.9** is confirmed to address periodic credential change requirements — specifically that passwords/passphrases used for user accounts do not need to change at arbitrary periodic intervals unless there is confirmed compromise, aligning with NIST SP 800-63B guidance. This is exactly what PA-04 mandates.

**On the v3.2.1 vs v4.0 renumbering flag:**  
In PCI DSS v3.2.1, MFA was primarily in **Req 8.3**. In v4.0/v4.0.1, MFA moved to **Req 8.4** (implementation scope) and **Req 8.5** (MFA system security configuration). The matrix citations for MFA controls (AM-04 = `Req 8.4, 8.5`; PA-01 = `Req 8.4.2`) use **v4.0-style numbering** — not the old v3.2.1 Req 8.3 style. No outdated numbering detected.

> **VERDICT: ✅ CONFIRMED CORRECT**  
> `Req 8.3.9` is the correct v4.0.1 reference for the no-arbitrary-expiry/force-reset-on-compromise password policy. The matrix uses v4.0-style MFA numbering (8.4/8.5) throughout, not the deprecated v3.2.1 Req 8.3.

---

### 5. VR-10 — ISO 27001:2022 Controls A.8.30 and A.8.32

**Matrix cites:** `A.8.30, A.8.32` — flagged as needing verification  
**Control:** "Software supply chain: CI/CD blocks CVSS 7.0+ components; API connections require TLS 1.2+ and OAuth 2.0/mTLS"

**Finding:**  
Both control numbers are confirmed to exist in ISO/IEC 27001:2022 Annex A's Technological Controls section:

| Control | Title | Relevance to VR-10 |
| :--- | :--- | :--- |
| **A.8.30** | Outsourced Development | Addresses security when third parties (vendors) develop software — including security requirements in contracts, oversight of secure coding/testing. Relevant to vendor software supply chain. |
| **A.8.32** | Change Management | Mandates controlled, risk-assessed management of changes to information systems, including software/component updates. Relevant to CI/CD pipeline controls and patch management. |

However, there is a **precision concern** worth flagging: the VR-10 control is about *software supply chain* (blocking vulnerable third-party CVSS 7.0+ components, TLS + OAuth for API connections). The most directly applicable ISO 27001:2022 controls are arguably:
- **A.8.30** — covers outsourced/vendor development ✅ relevant
- **A.8.32** — covers change management ✅ partially relevant (controls deployment of components)
- **A.5.21** — "Managing Information Security in the ICT Supply Chain" — this is the Organizational Control explicitly for supply chain risk, and may be *more* precise for the supply-chain-blocking aspect than A.8.32

The matrix's citations are not *wrong*, but a more complete mapping would add `A.5.21`.

> **VERDICT: ✅ CONFIRMED CORRECT (with enhancement suggestion)**  
> `A.8.30` and `A.8.32` both exist in ISO/IEC 27001:2022 Annex A and are applicable. The flag in the matrix can be **resolved/closed**. Consider also adding `A.5.21` (ICT Supply Chain) as a supplementary citation for the CI/CD component-blocking aspect.

---

### 6. BC-08 — NIST CSF 1.1 PR.AC-03 → CSF 2.0 Equivalent

**Matrix cites:** `PR.AC-03` (flagged as CSF 1.1)  
**Control:** "Alternate workspace: redundant load-balanced VPN gateways; critical personnel issued failover-configured laptops"

**Finding:**  
`PR.AC-03` ("Remote access is managed") is confirmed as a CSF **1.1** subcategory that was removed in the CSF 2.0 restructuring. NIST's official mapping identifies its CSF 2.0 successors as:

| CSF 2.0 Subcategory | Description | Applicability to BC-08 |
| :--- | :--- | :--- |
| **PR.AA-05** | Access permissions, entitlements, and authorizations defined in policy, managed, enforced, and reviewed; incorporates least privilege | Covers the *access management* aspect of VPN gateway access for alternate workspace |
| **PR.AA-03** | Users, services, and hardware are authenticated | Covers the *authentication* of remote/alternate-site connections |
| **PR.IR-03** | Mechanisms to achieve resilience requirements in normal and adverse situations | **Most precise** for redundant VPN gateways and failover infrastructure |

For BC-08 specifically — which is about **alternate workspace infrastructure** (redundant VPN, failover laptops) rather than access authorization policy — **PR.IR-03** is the most semantically accurate CSF 2.0 mapping. PR.AA-05 is more access-policy focused.

> **VERDICT: ✅ CORRECTED**  
> Replace `PR.AC-03` with **`PR.IR-03`** (Technology Infrastructure Resilience — mechanisms to achieve resilience in normal and adverse situations). Optionally add `PR.AA-05` for the access-permissions angle of VPN management.  
> **Recommended cell value:** `PR.IR-03` (primary); `PR.AA-05` (supplementary)

---

## Part 2 — The Seven Flagged "Review" Items

The matrix lists 7 items in the Open Review table. The user asked about IR-06, VR-05, VR-08, PA-10, BC-06, and the "7th unlisted" one (which is VR-10, already handled above in Part 1 #5, and BC-08 in Part 1 #6).

---

### IR-06 — NIST CSF Ref (Blank; RS.CO-03 suggested as plausible)

**Control:** Regulatory breach notification — DPDPA Board without undue delay; GDPR within 72 hrs; IT provides technical details within 24 hrs

**Finding:**  
In NIST CSF 2.0, the RS.CO category covers Incident Response Reporting and Communication:
- **RS.CO-02** — "Internal and external stakeholders are notified of incidents" — covers formal breach notification to regulators, customers, and partners
- **RS.CO-03** — "Information is shared with designated internal and external stakeholders" — broader, ongoing information exchange during response

IR-06 is specifically about **regulatory breach notification** (formal reporting to DPDPA Board and GDPR supervisory authority). This aligns more precisely with **RS.CO-02** (formal stakeholder/regulatory notification) than RS.CO-03 (ongoing information sharing). The matrix's own note says "RS.CO-03 plausible" — but RS.CO-02 is the better fit.

> **VERDICT: ✅ CORRECTED**  
> Replace blank NIST CSF cell with **`RS.CO-02`** (formal notification to internal/external stakeholders, including regulators). RS.CO-03 is about ongoing information sharing, not the formal regulatory breach-report obligation. If dual citations are preferred: `RS.CO-02, RS.CO-03`.

---

### VR-05 — PCI DSS Ref (Blank; Req 12.9 suggested as plausible)

**Control:** Right to Audit clause in all Tier 1 contracts; Compliance Lead may invoke proactively on failed certifications

**Finding:**  
In PCI DSS v4.0.1:
- **Req 12.9** applies to **service providers** (their obligation to acknowledge and support customer compliance verification)
- **Req 12.8.4** is the requirement placed on the *entity* (FinNexus) to monitor TPSP compliance annually — this is the more apt requirement from FinNexus's perspective as the customer enforcing a right-to-audit
- **Req 12.8.2** requires a written agreement with acknowledgement of responsibility, which is the contractual vehicle a "right to audit" clause would be embedded in

The "right to audit" is not a single explicit numbered requirement in PCI DSS v4.0 — it is an implied contractual tool to satisfy the monitoring obligation in Req 12.8.4. The matrix's suggestion of "Req 12.9" is slightly misdirected (that's a service-provider obligation, not FinNexus's right as a customer). The better citation from FinNexus's perspective is **Req 12.8.4** (annual monitoring obligation) paired with **Req 12.8.2** (written agreement).

> **VERDICT: ✅ CORRECTED**  
> Replace blank with **`Req 12.8.2, 12.8.4`**. Req 12.8.2 = written agreement (vehicle for the audit clause); Req 12.8.4 = annual compliance monitoring (the obligation the audit clause satisfies). Req 12.9 is an outbound service-provider obligation, not FinNexus's right as a customer.

---

### VR-08 — NIST CSF Ref (Blank; PR.DS-03 suggested as plausible)

**Control:** Vendor offboarding: access revoked within 4 hrs; Certificate of Destruction for Restricted/Confidential data within 30 days

**Finding:**  
`PR.DS-03` existed in CSF **1.1** ("Assets are formally managed throughout removal, transfers, and disposition") but was **removed in CSF 2.0**. Its successor is **ID.AM-08** ("Systems, hardware, software, services, and data are managed throughout their life cycles") — which covers data lifecycle/disposal activities. Additionally:
- **GV.SC-07** — supply chain risk management; ensuring appropriate controls in supplier contracts — could cover the offboarding data destruction requirement
- **PR.DS-11** — data backups managed — not applicable here

The most direct CSF 2.0 mapping for vendor offboarding data destruction is **ID.AM-08**.

> **VERDICT: ✅ CORRECTED**  
> The suggested `PR.DS-03` no longer exists in CSF 2.0. Replace with **`ID.AM-08`** (data/service lifecycle management, including secure disposal when a vendor is offboarded). The existing `GV.SC-07` already in the matrix could alternatively absorb this, but `ID.AM-08` is more specific to the data-destruction obligation.

---

### PA-10 — DPDPA/GDPR (Blank; noted as "may apply")

**Control:** Continuous monitoring against known-compromised password databases (HIBP); force reset on match

**Finding:**  
The concern is whether checking employee passwords against HIBP involves personal data processing under DPDPA/GDPR.

**GDPR analysis:** Checking a hashed or partial password hash against a compromised-credential database does involve *employee personal data* (account credentials are personal data). The lawful basis under GDPR is **Article 6(1)(f)** — legitimate interests of the controller (information security). However, GDPR also requires transparency (Art 13/14) and a Data Protection Impact Assessment may be recommended. The existing `AU-09` row already covers monitoring disclosure via the Employee Privacy Notice. No new GDPR article needs to be added to PA-10 *specifically* beyond the existing Art 32 security obligation, which is already cited in AM-05. The flag is valid as an awareness note for the DPO.

**DPDPA analysis:** DPDPA Section 6 covers consent and purpose limitation. If the organization is using employee personal data for monitoring purposes, processing must be within consented purposes or legitimate use under Section 4. This is a judgment call requiring DPO confirmation. The act of comparing a hash against a public breach database is likely covered under Section 8(4) — reasonable security safeguards — rather than requiring separate consent.

The matrix note "DPDPA Sec 6 / GDPR Art 6(1)(f) may apply — confirm with DPO" is accurate as a caution flag. There is no definitive answer without specific DPO/legal analysis of how the monitoring is technically implemented.

> **VERDICT: ⚠️ STILL UNCERTAIN — Leave as "Review"**  
> The flag is legitimate. GDPR Art 6(1)(f) is plausible and DPDPA Sec 8(4) may also be relevant. This genuinely requires DPO judgment on the specific technical implementation (client-side hashing vs. any data leaving premises). Do not add a specific citation without legal review.

---

### BC-06 — NIST CSF (PR.DS-11 cited but flagged as imprecise; PR.PT-05 or RC.RP-01 suggested)

**Control:** Tier 1 platforms: Multi-AZ active-active or auto active-passive failover; single-zone failure cannot exceed 4-hr RTO

**Finding:**  
- **PR.DS-11** ("Data backups are created, protected, maintained, and tested") — confirmed as backup-focused; not appropriate for High Availability architecture
- **PR.PT-05** was a CSF 1.1 subcategory ("Mechanisms such as failsafe, load balancing, hot swap are implemented") — this does NOT exist in CSF 2.0 under that identifier
- **RC.RP-01** — "Recovery plan is executed during or after a cybersecurity incident" — this is recovery execution, not HA architecture design
- **PR.IR-03** — "Mechanisms to achieve resilience requirements in normal and adverse situations are implemented" — this is the correct CSF 2.0 subcategory for load balancing, failover, and HA architecture

The matrix note suggested PR.PT-05, which does not exist in CSF 2.0. The correct answer is the same as BC-08: **PR.IR-03**.

> **VERDICT: ✅ CORRECTED**  
> Replace `PR.DS-11` with **`PR.IR-03`** (Technology Infrastructure Resilience — implements resilience mechanisms for normal and adverse conditions, including Multi-AZ failover and load balancing). PR.PT-05 does not exist in CSF 2.0. RC.RP-01 is for incident recovery execution, not HA design.

---

## Summary Table

| Control | Framework | Matrix As-Is | Verdict | Correct Reference |
| :--- | :--- | :--- | :--- | :--- |
| **AM-04** | ISO 27001:2022 | `A.8.5` | ✅ CONFIRMED CORRECT | `A.8.5` |
| **DC-08** | NIST SP 800-88 | `NIST SP 800-88` | ✅ CONFIRMED CORRECT | `NIST SP 800-88` |
| **IR-01/IR-02** | DPDPA + GDPR | `Sec 8(6)` + `Art 33, 34` (on IR-06 row) | ✅ CONFIRMED CORRECT | `Sec 8(6)` + `Art 33, 34` |
| **PA-04** | PCI DSS v4.0.1 | `Req 8.3.9` | ✅ CONFIRMED CORRECT | `Req 8.3.9` (v4.0.1 numbering confirmed) |
| **VR-10** | ISO 27001:2022 | `A.8.30, A.8.32` (flagged) | ✅ CONFIRMED CORRECT + suggest adding `A.5.21` | `A.8.30, A.8.32` (+ optionally `A.5.21`) |
| **BC-08** | NIST CSF | `PR.AC-03` (flagged, CSF 1.1) | ✅ CORRECTED | **`PR.IR-03`** (primary); `PR.AA-05` (supplementary) |
| **IR-06** | NIST CSF | Blank (RS.CO-03 suggested) | ✅ CORRECTED | **`RS.CO-02`** (formal notification) |
| **VR-05** | PCI DSS | Blank (Req 12.9 suggested) | ✅ CORRECTED | **`Req 12.8.2, 12.8.4`** |
| **VR-08** | NIST CSF | Blank (PR.DS-03 suggested) | ✅ CORRECTED | **`ID.AM-08`** (PR.DS-03 removed in CSF 2.0) |
| **PA-10** | DPDPA/GDPR | Blank (flag only) | ⚠️ STILL UNCERTAIN | Retain "Review" — confirm with DPO |
| **BC-06** | NIST CSF | `PR.DS-11` (flagged) | ✅ CORRECTED | **`PR.IR-03`** (PR.PT-05 does not exist in CSF 2.0) |

---

## Recommended Matrix Updates

The following cells need to be changed before the CTM is used as audit evidence:

| Row | Column | Change |
| :--- | :--- | :--- |
| BC-08 | NIST CSF Ref | `PR.AC-03` → **`PR.IR-03`** (add `PR.AA-05` as supplementary) |
| IR-06 | NIST CSF Ref | *(blank)* → **`RS.CO-02`** |
| VR-05 | PCI DSS Ref | *(blank)* → **`Req 12.8.2, 12.8.4`** |
| VR-08 | NIST CSF Ref | *(blank)* → **`ID.AM-08`** |
| BC-06 | NIST CSF Ref | `PR.DS-11` → **`PR.IR-03`** |
| VR-10 | ISO 27001 Ref | `A.8.30, A.8.32` → `A.8.30, A.8.32` (flag resolved; optionally add `A.5.21`) |
| PA-10 | Notes | Retain "Review" flag; leave DPDPA/GDPR cells blank pending DPO review |

> [!NOTE]
> BC-08 and BC-06 both resolve to the same CSF 2.0 subcategory (`PR.IR-03`), which makes sense — both controls are about infrastructure resilience mechanisms.

> [!CAUTION]
> `PR.DS-03` (suggested for VR-08) and `PR.PT-05` (suggested for BC-06) do **not exist** in NIST CSF 2.0. Using them in audit evidence packages would be an error.
