# Governance

**Status:** Bootstrap editorial process · v0.1.0-draft.1

## Current authority

The Archer Development Foundation GitHub organization is the initial repository host. Its repository maintainers manage review, merges, releases, and moderation under this bootstrap process. This arrangement is not an elected technical steering committee, an appointed academic board, or consortium ratification.

The project invites independent implementers, researchers, service creators, and users to participate. Contributions and technical objections do not require purchasing a product, creating a provider account, or joining a paid membership program.

## Decisions in public

- Substantive changes use the [ASIP process](asips/ASIP-0000-process.md), with motivation, alternatives, compatibility, security/privacy effects, and test implications.
- Maintainers record technical rationale and unresolved objections in the public proposal or pull request. Silence is not consensus.
- Editorial corrections may use a normal pull request when they do not alter protocol requirements.
- Disagreement can be raised in a linked public issue; maintainers should request an uninvolved reviewer where feasible and record the disposition.
- Private security details follow [SECURITY.md](SECURITY.md). Public decisions can describe the resulting correction without exposing exploitable or personal information.

## Document lifecycle

| State | Meaning | Exit evidence |
| --- | --- | --- |
| Editor’s Draft | Actively changing proposal | Complete scope, requirements, dependencies, and known gaps |
| Review Draft | Defined target for implementer review | Public review period, resolved blocking issues, schemas and vectors |
| Candidate | Frozen enough for interoperability testing | Independent implementation evidence and security review |
| Ratified | Accepted through an adopted governance process | Documented decision authority, patent policy, review record, and conformance evidence |
| Superseded / Withdrawn | Retained for history, not the current target | Replacement or withdrawal rationale |

**No document can be ratified under this bootstrap process alone.** Ratification requires an adopted governance and patent policy, plus documented independent review. A maintainer merge or repository tag does not substitute for those gates.

## Evolving stewardship

A governance proposal should define working-group charters, editor appointment/removal, representation and conflict-of-interest rules, voting or consensus procedures, appeals, security authority, and succession. The transition itself must have a public review and decision record. Do not list organizations or individuals as participating without their agreement.

Working groups may explore identity, execution, payments, evidence, and network architecture. Their formation, membership, mandates, and deliverables remain proposals until publicly recorded.

## Versioning

Document identifiers remain stable. Draft package versions use a prerelease suffix such as `0.1.0-draft.1`; they are not stable wire-protocol versions. Substantive changes update the proposal record and changelog. Exact transport/profile versions will be separately negotiated once defined.

Published tags should not be moved. Corrections receive a new version and a clear change record. Compatibility claims must refer to a revision and profile set rather than “latest.”

## Intellectual property

The repository license governs reuse of its contents. [PATENTS.md](PATENTS.md) records the limits of the initial policy and the work required before ratification. Hosting, contributing, or citing another project does not imply endorsement or authority to grant rights owned by others.
