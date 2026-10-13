# Security and privacy

## Reporting

This is a draft specification repository, not a production service. Report ordinary specification ambiguities with a synthetic example in an issue. For an exploitable vulnerability or private evidence, use GitHub’s **Report a vulnerability** control if the repository has private reporting enabled. If it is unavailable, request a private maintainer channel without describing the exploit or including sensitive data. No response-time commitment or bounty program is established by this draft.

## Threat model for proposals

| Threat | Required design consideration |
| --- | --- |
| Malicious descriptor, tool description, or returned content | Treat text as data; preserve the principal’s authority boundary; sanitize display and isolate execution |
| Forged publisher, substituted key, or compromised resolver | Authenticate bindings; define trust roots, rotation, revocation, and stale-state behavior |
| Confused deputy or permission escalation | Separate principal consent, dispatcher authentication, merchant access, and payment permission |
| Replay or duplicate external effect | Bind domains and execution identity; reconcile uncertain outcomes at the actual provider |
| Concurrent overspending | Explicit reservations and coordination for aggregate limits; no guarantee from independent local counters |
| Credential or personal-data disclosure | Minimize data; scope credential recipients; keep secrets out of publication, logs, and public evidence |
| False or withheld evidence | Attribute claims and limitations; permit negative-outcome evidence; do not treat signatures as truth |
| Unavailable provider, index, or record store | Independent retrieval and disclosed dependencies; distinguish key recovery from data availability |
| Malicious worker or external endpoint | Resource/egress limits, endpoint policy, secrets isolation, and safe ownership transfer |

## Publication constraints

Examples and tests must be synthetic. Public evidence should be minimized and redactable where appropriate; a permanent public commitment can still reveal or correlate sensitive facts. Private data should not be made public merely to demonstrate verifiability.

Security-sensitive claims require explicit assumptions and reproducible evidence. A local check, mock, or successful signature verification is not an audit or proof of safe economic execution.
