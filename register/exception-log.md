# Security Policy Exception Register

This register illustrates the information that should be logged for formal exceptions against FinNexus Solutions security policies. The entries below are examples only; they are not approved or active exceptions.

## Exception Management Rules
1. **Time-Bound:** Exceptions are never granted indefinitely. Maximum allowable exception validity is **180 days** (renewable upon review).
2. **Compensating Controls:** All exceptions must have documented, verified compensating controls to reduce residual risk.
3. **Approval Authority:** All exceptions must be formally signed off by the **CISO** and the relevant Business Unit Head. High/Critical risk exceptions may require Executive Board / Risk Committee notification.

---

## 📋 Illustrative Exception Log

| Exception ID | Policy ID | Safeguard ID | Requestor | Business Justification | Compensating Control | Approved By | Granted Date | Expiry Date | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| EXP-XX-001 | PA | PA-01 | IT | Legacy on-prem financial reporting tool does not support SAML/OIDC or MFA plugins. Vendor upgrade planned for Q1 YY. | IP allowlist restricts access to corporate network only; dedicated SIEM monitoring on login attempts. | CISO & Business Unit Head | DD.MM.YY | DD.MM.YY | Illustrative |
| EXP-XX-002 | AM | AM-03 | Engineering | CI/CD integration with legacy payment gateway API requires a single shared service account. | Password rotated every 30 days via Vault; API access restricted strictly to CI/CD runner IPs. | CISO & Business Unit Head | DD.MM.YY | DD.MM.YY | Illustrative |
| EXP-XX-003 | DC | DC-09 | Engineering | Machine learning model training requires raw transaction data for fraud detection accuracy tuning. Anonymization degrades required signal. | Data is processed in an isolated, non-internet-facing enclave with strict access control and auditing. | CISO, Legal/Compliance & Business Unit Head | DD.MM.YY | DD.MM.YY | Illustrative |

---

## 🗄️ Closed / Expired Exceptions

*(No closed exceptions in this period)*
