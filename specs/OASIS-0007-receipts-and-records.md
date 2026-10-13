# OASIS-0007: Receipts and records

| Metadata | Value |
| --- | --- |
| Version | 0.1.0-draft.1 |
| Status | Editor’s Draft — proposed normative |
| Editors | Repository maintainers, under bootstrap governance |
| Updated | 2026-10-13 |
| Proposal | Initial publication |

## Abstract

An `ExecutionReceipt` is an attributable claim about an event in an invocation. A durable record represents a continuing outcome such as an order, reservation, or other user-relevant state. `RecordUpdate` preserves changes and corrections without rewriting earlier signed claims.

## Candidate information model

Receipts bind execution and attempt identifiers, service and descriptor, relevant permission/quote commitments, claimed event and observation time, attestor identity, provenance, and evidence references. A record identifies its subject, kind, issuer, current lifecycle state, access policy, update predecessors, and supported follow-up actions.

Evidence should distinguish a provider assertion, processor-confirmed payment, finalized chain event, and independently observed outcome. A signature identifies the speaker; an anchor identifies a commitment. Neither proves delivery by itself.

## Proposed requirements

- **REC-01.** Each receipt MUST identify the asserted event, attestor, provenance, and related invocation. It MUST distinguish payment evidence from service fulfillment evidence.
- **REC-02.** Updates MUST preserve attribution and their relationship to prior state. The selected profile MUST define ordering, conflict detection, correction, and fork resolution; a timestamp alone is insufficient conflict resolution.
- **REC-03.** Cancellation, refund, dispute, or corrected observation MUST be representable without erasing the original claim. An anchored claim MUST NOT be treated as irreversible service success.
- **REC-04.** A portability profile MUST specify principal-authorized retrieval, retention, independent availability, key rotation, recovery, and deletion behavior. Publishing only a content hash does not satisfy record availability.
- **REC-05.** A record’s follow-up action MUST be invoked under fresh applicable permission and supported profiles. An action label or record possession alone MUST NOT grant authority.
- **REC-06.** Public records and commitments MUST exclude redeemable credentials and unnecessary personal data. Access to private evidence MUST be explicit and bounded.

## Rationale and compatibility

An execution attempt can end while its resulting record remains active. Record closure does not imply every financial obligation is final. Existing product ledgers need an explicit export, proof, and retrieval mapping before their records are portable.

## Security and privacy

Evidence references can reveal private purchase details or become unavailable. Encrypted storage needs key management and availability guarantees separate from the signing key. Public commitments to predictable private data can enable correlation or guessing; a storage profile must assess that exposure.

## Open decisions and conformance

Receipt encoding, conflicting attestors, record-update ordering, independent failure evidence, retention incentives, and privacy-preserving retrieval remain open. See C-01, C-06, C-07, C-08, and C-10 in the [scenario catalog](../conformance/scenarios.md).
