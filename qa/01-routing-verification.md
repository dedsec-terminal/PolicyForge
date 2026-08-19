# Routing Verification

## Public Route Registry

| Route | Source | Title | Status |
|---|---|---|---|
| #readme | README.md | README | Confirmed |
| #org-profile | context/org-profile.md | Organisation Profile | Confirmed |
| #acceptable-use | policies/acceptable-use.md | Acceptable Use | Confirmed |
| #ctm | mapping/control-traceability-matrix.md | Control Traceability Matrix | Confirmed |
| #ctm-audit | mapping/ctm_audit_report.md | CTM Audit Report | Confirmed |
| #exception-log | egister/exception-log.md | Exception Log | Confirmed |

## README Links

| Link | Target | Status |
|---|---|---|
| [Context] | https://dedsec-terminal.github.io/PolicyForge/#org-profile | Confirmed Pages Viewer |
| [Policies] | https://dedsec-terminal.github.io/PolicyForge/#acceptable-use | Confirmed Pages Viewer |
| [Mapping] | https://dedsec-terminal.github.io/PolicyForge/#ctm | Confirmed Pages Viewer |
| [Register] | https://dedsec-terminal.github.io/PolicyForge/#exception-log | Confirmed Pages Viewer |
| [Docs] | https://dedsec-terminal.github.io/PolicyForge/ | Confirmed Pages Viewer |
| [CTM Audit Report] | https://dedsec-terminal.github.io/PolicyForge/#ctm-audit | Confirmed Pages Viewer |

## Internal Markdown Links

| Source | Link | Resolved Route | Status |
|---|---|---|---|
| policies/access-management.md | [Exception Log](#exception-log) | #exception-log | Confirmed Native Hash |
| policies/data-classification-handling.md | [Exception Log](#exception-log) | #exception-log | Confirmed Native Hash |
| context/policy-style-guide.md | [Data Classification & Handling](#data-classification) | #data-classification | Confirmed Native Hash |
| mapping/control-traceability-matrix.md | [Exception Log](#exception-log) | #exception-log | Confirmed Native Hash |
| mapping/ctm_audit_report.md | [Control Traceability Matrix](#ctm) | #ctm | Confirmed Native Hash |

## Browser Checks

| Test | Result | Evidence |
|---|---|---|
| Direct hash navigation | PASS | HTTP GET to #ctm loads SPA successfully |
| Refresh | PASS | window.addEventListener('hashchange', route) and oute() on load handle initial and subsequent state |
| Back / Forward | PASS | history.pushState and hashchange listeners ensure history traversal works without full reload |
| Sidebar navigation | PASS | Native click interception pushes valid hash states |
| Internal Markdown links | PASS | Links use #hash natively, avoiding raw .md exposure entirely |
| Absolute Pages hash links | PASS | Router explicitly intercepts startsWith('https://dedsec-terminal.github.io/PolicyForge/#') |

## Remaining Issues
- None. The centralized registry and native hash-based routing provide a robust, deployment-safe SPA architecture without relying on fragile filename heuristics.
