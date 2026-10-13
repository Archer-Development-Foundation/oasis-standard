# OASIS-0005: Authorization and delegation

| Metadata | Value |
| --- | --- |
| Version | 0.1.0-draft.1 |
| Status | Editor’s Draft — proposed normative |
| Editors | Repository maintainers, under bootstrap governance |
| Updated | 2026-10-13 |
| Proposal | Initial publication |

## Abstract

Specify the authority an agent or executor needs to commit an action for a principal. Identity authentication, user intent, merchant access, and permission to pay are related but distinct.

## Candidate information model

An authorization identifies its issuer, principal, delegate, permitted service/operation and descriptor version, effect or argument bounds, intended recipients, assets and amounts where relevant, execution/audience binding, validity, revocation mechanism, and delegation limits. A delegation chain records each narrowing grant. Merchant linkage names its issuer and supported recipient rather than assuming bearer credentials transfer between operators.

## Proposed requirements

- **AUTH-01.** An executor MUST establish valid authority for each committed effect. Authentication of a dispatcher, agent session, or wallet sign-in alone MUST NOT substitute for permission to execute or spend.
- **AUTH-02.** A delegate MUST NOT widen inherited scopes, recipients, amount bounds, validity, or further-delegation rights. The verifier MUST validate the applicable chain and revocation state.
- **AUTH-03.** Numeric limits MUST specify exact units, comparison/rounding rules, and any valuation source and freshness bound. Missing valuation required for a limit MUST prevent the dependent action.
- **AUTH-04.** A principal MUST be able to deny or stop an approval continuation without that denial being treated as a new execution request. Revocation races and already-committed effects need explicit profile behavior.
- **AUTH-05.** Unsupported effects MAY be displayed for review, but MUST NOT execute until a supported authorization mechanism binds the exact action. Human approval text alone cannot make an unknown machine format safe.
- **AUTH-06.** Merchant linkage MUST be checked for issuer, principal, audience, scope, expiry, and revocation. Switching operators MUST use supported delegation or reauthorization where required.

## Recovery and identity portability

The [identity profile requirements](../profiles/identity.md) distinguish principal control from an operator-issued session credential. Independent recovery must state how authority is restored, old keys are revoked, delegated permissions are handled, and encrypted records remain retrievable. Mandatory private-key export is not the only acceptable mechanism. A lost unrecoverable key cannot be restored by specification language.

## Rationale and compatibility

Per-purchase approval is one valid model; bounded standing delegation requires its own demonstrable enforcement. A per-request limit does not enforce a shared daily allowance. Until a coordinated-budget profile exists, implementations MUST NOT claim cross-executor aggregate limits from independent local checks.

## Security and privacy

Delegation can create confused-deputy and privilege-escalation paths. Minimize disclosed identity and merchant data. Revocation services can be unavailable or stale; the profile must define the safe behavior before an effect, not after it.

## Open decisions and conformance

Delegation encoding, revocation ordering, concurrent reservations, and recovery proofs remain open. See C-02, C-04, C-05, and C-09 in the [scenario catalog](../conformance/scenarios.md).
