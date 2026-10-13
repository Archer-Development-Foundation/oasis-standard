# OASIS-0001: Core model

| Metadata | Value |
| --- | --- |
| Version | 0.1.0-draft.1 |
| Status | Editor’s Draft — proposed normative |
| Editors | Repository maintainers, under bootstrap governance |
| Updated | 2026-10-13 |
| Proposal | Initial publication; [ASIP-0000](../asips/ASIP-0000-process.md) defines subsequent changes |

## Abstract

Define common roles and semantics for discovering, authorizing, invoking, and accounting for services across independently operated systems. Domain-specific logic belongs in providers and their adapters; shared executors interpret declared contracts and supported profiles.

## Terminology

The uppercase terms MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY use [BCP 14](https://www.rfc-editor.org/rfc/rfc8174). In this draft they express proposed requirements. Text marked informative is explanatory.

| Role or term | Meaning |
| --- | --- |
| Principal | Person, organization, or other authority whose permissions are exercised |
| Agent | Software acting under a principal’s authority |
| Provider | Party offering a service and controlling its application logic |
| Adapter | Interface binding a service’s operations to the shared contracts |
| Indexer | Party building a catalog from available service descriptions and evidence |
| Executor | Party validating and coordinating an invocation |
| Attestor | Party making a signed claim about an event or observation |
| Profile | Versioned rules binding abstract semantics to a concrete mechanism |
| Logical execution | One intended operation, potentially involving several attempts or resumptions |

An operator may perform multiple roles. Authentication of one role MUST NOT be interpreted as authority to act as another.

## Proposed requirements

- **CORE-01 — Bound contracts.** Execution MUST bind a descriptor version, request, applicable permissions, accepted quote when payment is required, and the profiles used.
- **CORE-02 — Capabilities compose.** A descriptor MUST declare a set of capabilities. Candidate values are `RETURNS_DATA`, `MUTATES_USER_FUNDS`, and `EXTERNAL_SIDE_EFFECT`; they are not mutually exclusive classes. Paying an access fee remains a separately authorized economic action.
- **CORE-03 — Compatibility is explicit.** Participants MUST negotiate supported versions and required profiles before billable work or committed effects. Compatibility does not require an operator to accept requests contrary to its published admission or risk policy.
- **CORE-04 — Extensions preserve constraints.** Unknown required semantics MUST fail before the affected work or effect. A field cannot evade this rule merely by being placed in an extension namespace.
- **CORE-05 — Separate state dimensions.** Permission, execution attempt, payment, and service outcome MUST remain distinguishable. A signature, submission, payment, and fulfillment are different events.
- **CORE-06 — Evidence is attributable.** Outcome claims MUST identify their attestor and provenance. Cryptographic validity MUST NOT be presented as proof that the claim is true.

### Unknown-value handling

| Unknown input | Required behavior |
| --- | --- |
| Optional display hint or advisory metadata | MAY omit or safely render as inert text; never execute embedded content |
| Record kind or optional action label | MAY preserve as opaque data; an unknown action is not executable authority |
| Required capability, payment method, fee semantics, or permission type | MUST refuse or negotiate a supported alternative before commitment |
| Human-readable description of an unknown effect | MAY display for review; execution still requires a supported authorization mechanism |
| Required extension or incompatible major version | MUST refuse the affected operation |

## Lifecycle and rationale

Discover → Verify → Route → Authorize → Consume → Attest describes responsibilities, not a compulsory sequence of six network calls. Quotes and preparation can precede approval; continuation can return to approval. Settlement ordering belongs to an agreed payment profile. Returning a `cost` object after unapproved billable work does not establish consent.

## Compatibility

Existing products can map their identifiers, payloads, and credentials through explicit compatibility profiles. Renaming fields or opening client code alone does not establish conformance. [Registries](../registries/README.md) will distinguish assigned values from implementation aliases.

## Security and privacy

Descriptors, tool text, returned data, and remote evidence are untrusted input. They cannot override principal policy. Profiles need bounded parsing, endpoint validation, isolation, and protection against confused-deputy behavior, replay, and unauthorized disclosure. See the [threat model](../SECURITY.md).

## Open decisions and conformance

Identifier resolution, extension negotiation, exact state vocabulary, and the minimum mandatory profile set remain open. Requirements map to the [scenario catalog](../conformance/scenarios.md); no complete core-conformance claim is defined yet.
