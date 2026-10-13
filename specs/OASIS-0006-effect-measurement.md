# OASIS-0006: Effect measurement

| Metadata | Value |
| --- | --- |
| Version | 0.1.0-draft.1 |
| Status | Editor’s Draft — proposed normative |
| Editors | Repository maintainers, under bootstrap governance |
| Updated | 2026-10-13 |
| Proposal | Initial publication |

## Abstract

An `EffectReport` describes what an assessor can determine about a proposed action before execution. It supplies evidence to permission checks without conflating measurement with authorization or final outcome.

## Candidate information model

Bind the report to the exact assessed authorization/payload, service descriptor, instrument description when needed, assessor identity, assessment method, source state and time, measured values and bounds, confidence limitations, and any price source with its freshness. Instrument metadata describes the object being assessed; its publisher and version need an explicit trust basis.

| Candidate assessment category | Meaning |
| --- | --- |
| `SIMULATED` | Predicted effects under a named simulator and state snapshot |
| `DECODED_BOUNDED` | Known payload structure supports specified bounds, without full simulation |
| `OPAQUE` | Available evidence cannot establish the effects or bounds required for automatic approval |

These are different methods with limitations, not a universal quality ranking or post-execution success levels.

## Proposed requirements

- **EFFECT-01.** A report MUST bind the exact action assessed. A change in payload, descriptor, or relevant state MUST trigger reassessment or invalidate the report under an explicit freshness policy.
- **EFFECT-02.** A report MUST identify its method, assessor, provenance, relevant state, and unsupported effects. Missing evidence MUST NOT be represented as a zero effect.
- **EFFECT-03.** An executor MUST NOT infer principal permission from a report. A favorable simulation does not authorize execution.
- **EFFECT-04.** If a permission limit depends on a measurement that remains opaque, the executor MUST refuse that automatic approval path or obtain a different supported, sufficiently bounded authorization.
- **EFFECT-05.** Pre-execution assessments MUST NOT be recorded as fulfillment evidence. Later observations belong in a receipt with their own provenance.

## Rationale and compatibility

Effects differ across domains, so the core carries generic bounded measurements and profile references. A transaction decoder can be one profile; booking conditions or asset permissions can use others. Profiles must say which values are enforceable and which are predictions.

## Security and privacy

Malicious metadata, manipulated prices, stale snapshots, and time-of-check/time-of-use changes can invalidate an assessment. Minimize private payload disclosure to third-party assessors. Verification requires an explicit trust policy for the assessor and data sources.

## Open decisions and conformance

Common units, descriptor trust roots, profile-specific bounds, and stale-state rules need further work. See C-11 in the [scenario catalog](../conformance/scenarios.md).
