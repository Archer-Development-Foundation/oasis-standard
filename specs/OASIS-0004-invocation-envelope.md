# OASIS-0004: Invocation envelope

| Metadata | Value |
| --- | --- |
| Version | 0.1.0-draft.1 |
| Status | Editor’s Draft — proposed normative |
| Editors | Repository maintainers, under bootstrap governance |
| Updated | 2026-10-13 |
| Proposal | Initial publication |

## Abstract

An `InvocationEnvelope` describes the service response through composable information, economic, authorization, and record parts. It avoids a different executor branch for each business domain.

## Candidate response model

| Part | Meaning | Boundary |
| --- | --- | --- |
| `data` | User-consumable result or preparation information | Untrusted content, not authority |
| `cost` | Charge or payment-state information under an agreed quote/profile | Cannot authorize new or changed charges retroactively |
| `authorizations[]` | Actions requiring validated principal authority | Presence does not permit automatic signing or execution |
| `record` | Durable outcome description or record update | Requires provenance and lifecycle semantics |

Illustrative compositions: read → `data`; paid query → `cost` + `data`; committed reservation → `record`; prepared effect → `authorizations[]` plus preparation information. A prepared record is not proof that the reservation or transaction exists.

## Proposed requirements

- **ENV-01.** Every response MUST bind to its logical execution and attempt and distinguish preparation, continuation, error, and committed outcome. The precise status encoding remains to be specified.
- **ENV-02.** Required economic and authorization semantics MUST be negotiated before affected work. A returned arm MUST NOT expand a previously accepted permission or quote.
- **ENV-03.** Authorization and settlement MUST be separate operations with profile-defined ordering. The executor MUST NOT infer one from the other.
- **ENV-04.** A continuation MUST identify the same logical operation, required next action, and validity boundary. Resumption MUST revalidate applicable authority, quote, and state.
- **ENV-05.** Errors MUST identify the failed stage and whether an effect is known to have occurred, known not to have occurred, or remains uncertain. An uncertain outcome MUST NOT be reported as a safe automatic retry.
- **ENV-06.** Display content MUST remain inert. Unsupported display hints MAY degrade to safe text, but unknown mandatory permissions or economics MUST prevent the affected action.

## Rationale and compatibility

The four parts express shared responsibilities rather than a fixed processing order. A transport profile can map legacy flat read responses to a `data` arm. That mapping must not invent absent consent, settlement, or receipt evidence.

## Security and privacy

Action payloads, links, and human-readable explanations can disagree. Consent must bind the machine-relevant effect, with accurate disclosure to the principal. Merchant tokens and raw payment credentials MUST NOT appear in general display data or public outcome records.

## Open decisions and conformance

Error registry, empty-envelope validity, multiple records, continuation binding, and partial-result semantics need exact schemas. See C-04 through C-08 in the [scenario catalog](../conformance/scenarios.md).
