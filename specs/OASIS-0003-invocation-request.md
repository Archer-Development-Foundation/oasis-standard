# OASIS-0003: Invocation request

| Metadata | Value |
| --- | --- |
| Version | 0.1.0-draft.1 |
| Status | Editor’s Draft — proposed normative |
| Editors | Repository maintainers, under bootstrap governance |
| Updated | 2026-10-13 |
| Proposal | Initial publication |

## Abstract

An `InvocationRequest` binds a caller’s intended operation to the service, authority, economics, and replay boundary under which it may run. Transport authentication and principal authorization are separate checks.

## Candidate information model

The authenticated representation needs a protocol/profile version; principal and agent identities; executor audience; service and operation identifiers; descriptor version or commitment; arguments or an unambiguous argument commitment; logical execution and attempt identifiers; authorization and accepted-quote references; validity interval; and replay domain. The signing profile specifies the exact covered representation and key resolution.

## Proposed requirements

- **REQ-01.** The authenticated request MUST bind all execution-relevant elements above. Referenced permission or quote content MUST be immutable or verified against its bound commitment.
- **REQ-02.** A verifier MUST validate the signature or profile-defined proof, signer authority, target, audience, validity interval, and replay boundary before accepting the request. A valid dispatcher signature alone is insufficient user consent.
- **REQ-03.** Retries and approval resumptions MUST preserve the logical execution identity and link distinct attempts. An execution identifier reused with materially changed arguments, target, or quote MUST NOT be treated as the same authorized operation.
- **REQ-04.** An executor MUST reject a request requiring unsupported signing, authorization, or payment semantics before billable work or side effects.
- **REQ-05.** Implementations MUST distinguish request deduplication from provider-side effect reconciliation. A local request cache does not establish idempotency at an external service.

## Signing and canonicalization — decision required

The draft does **not** define signable bytes. A signing proposal must select canonical encoding, domain separation, algorithm identifiers, proof placement, key resolution, rotation/revocation rules, timestamp representation, and number handling together. [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785) is a candidate JSON canonicalization method; sorting JSON keys is not an adequate substitute.

The proposal needs cross-language vectors covering Unicode, numeric boundaries, duplicate keys, altered arguments, unknown fields, expiry, wrong audience, and replay. Reference implementations must agree on exact bytes before the profile freezes.

## Rationale and compatibility

Signed application requests can provide implementation experience. Existing field names or signatures cannot be assumed compatible with a new authenticated representation. A migration profile must name its mapping and verification limits; signatures cannot be relabeled without signing the new representation.

## Security and privacy

Request commitments can leak low-entropy data through guessing. Arguments and evidence need access controls even when their hashes are public. Key ownership does not imply control over merchant accounts or permission to spend. See [authorization](OASIS-0005-authorization.md).

## Open decisions and conformance

Cryptographic profile selection and deduplication/reconciliation scope are release blockers. See C-02, C-03, C-04, and C-06 in the [scenario catalog](../conformance/scenarios.md).
