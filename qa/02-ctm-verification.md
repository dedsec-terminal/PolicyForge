# CTM Verification

## Metadata

| Field | Result |
|---|---|
| Version | Removed specific minor versions unless part of audit trailing. Set primary table to XX. |
| Date format | DD.MM.YY across all artifacts. |
| Classification | Maintained default (Internal - General implied). |

## Identifier Normalization

| Policy | Metadata ID | Control Prefix | Final State |
|---|---|---|---|
| Vendor & Third-Party Risk | VD | VR- | Metadata updated to VR to match authoritative controls. |
| Password & Authentication | PW | PA- | Metadata updated to PA to match authoritative controls. |

## Framework Currency

| Framework | Version | Verified | Notes |
|---|---|---|---|
| NIST SP 800-88 | Rev. 2 | PASS | Referenced correctly in descriptions. |
| DPDP Act | 2023 | PASS | Distinguished Act 2023 from Rules 2025 across all documents. |
| DPDP Rules | 2025 | PASS | Used strictly for 72-hour notification timeline. |
| NIST CSF | 2.0 | PASS | Updated mappings from CSF 1.1 deprecations. |
| PCI DSS | v4.0.1 | PASS | Used appropriately for access/vendor mapping. |

## Mapping Changes

| Control | Previous | Final | Reason |
|---|---|---|---|
| BC-08 | PR.AC-03 | PR.IR-03 | NIST CSF 1.1 subcategory deprecated in CSF 2.0. |
| VR-05 | Blank | Req 12.8.2, 12.8.4 | PCI DSS v4.0.1 mapping for Right to Audit clause. |
| VR-08 | PR.DS-03 | ID.AM-08 | NIST CSF 1.1 subcategory deprecated in CSF 2.0. |
| IR-06 | DPDPA Board | DPDP Rules 2025 (72 hrs) | Aligned terminology to 72-hour rule mandate. |

## Source-to-CSV Parity

| Check | Result |
|---|---|
| md_to_csv extraction script updated | PASS (updated to target Control ID \| Policy / Control \| Objective) |
| CSV generated successfully | PASS |

## Defects Remaining

| ID | Defect | Severity |
|---|---|---|
| None | All detected transcript artifacts removed, normalization applied, and metadata aligned without contradiction. | N/A |
