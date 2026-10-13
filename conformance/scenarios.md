# Proposed conformance scenarios

**Status:** Test designs, not executed results · v0.1.0-draft.1

Each executable case will need pinned specifications/profiles, fixture data, deterministic setup, observed results, and independently reproducible instructions. Existing scenario IDs are stable review references, not a claim that a harness exists.

| ID | Setup and action | Expected property | Requirements |
| --- | --- | --- | --- |
| C-01 | Make the original operator unavailable; discover and invoke via an independent index/executor, then retrieve evidence | Continuity using available descriptors, valid permission, and independent records | CORE-01, DESC-04, REC-04 |
| C-02 | Start with a new bare-key principal; separately exercise each advertised assisted-recovery path | Authority without an original-provider account; recovery assumptions and limitations observable | REQ-02, AUTH-01, REC-04 |
| C-03 | Alter arguments, descriptor version, quote, audience, expiry, or replay domain after authentication | Verification rejects the changed request before billable work or effects | DESC-02, REQ-01–04 |
| C-04 | Offer an unknown required fee/profile/authorization; compare an unknown optional display hint | Mandatory semantics refuse; optional presentation degrades safely | CORE-03–04, ENV-06, AUTH-05 |
| C-05 | Deny approval; expire or revoke a delegation; resume an additional-approval continuation | No unauthorized effect; valid resumption remains bound to the same logical operation | ENV-04, AUTH-02–04 |
| C-06 | Lose a response after the provider may have committed; retry or switch executor | Reconcile the original effect; do not infer safe retry or exactly-once behavior | REQ-03, REQ-05, ENV-05 |
| C-07 | Confirm payment but fail or withhold service fulfillment | Distinct payment/outcome states; attributable failure and defined refund behavior | CORE-05–06, REC-01, REC-03 |
| C-08 | Cancel, refund, dispute, or correct a previously recorded success | Preserve the original claim and attributable updates; detect conflicting updates | REC-02–03 |
| C-09 | Two executors race to consume one shared allowance, or consume while revoked | A declared aggregate-budget profile enforces its guarantee; unsupported profiles cannot claim it | AUTH-02–03 and future budget profile |
| C-10 | Revoke a descriptor; rotate a principal key; lose an evidence replica | Apply declared freshness, recovery, retention, and access rules; hash-only storage does not pass retrieval | DESC-04–05, REC-04–06 |
| C-11 | Supply stale simulation, opaque payload, missing price, or substituted instrument metadata | Refuse unsupported automated approval; distinguish prediction from outcome | EFFECT-01–05, AUTH-03 |
| C-12 | Run card and blockchain cases through their supported providers, including extra approval and reversals | Preserve credential restrictions, logical identity, and distinct payment states; classify evidence accurately | CORE-03, ENV-02–04, REC-01–03 |

C-09 is a later-profile test and cannot be passed by independent per-request counters. C-12 may initially be reported as untested; mock success is not payment-provider interoperability.

For C-01, independence includes the actual trust and availability dependencies: identity resolution, catalog content, execution, and record retrieval. The selected merchant or payment processor can remain a declared external dependency.
