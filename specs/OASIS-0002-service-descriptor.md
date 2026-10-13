# OASIS-0002: Service descriptor

| Metadata | Value |
| --- | --- |
| Version | 0.1.0-draft.1 |
| Status | Editor’s Draft — proposed normative |
| Editors | Repository maintainers, under bootstrap governance |
| Updated | 2026-10-13 |
| Proposal | Initial publication |

## Abstract

A `ServiceDescriptor` describes an invocable capability independently of a particular catalog database. Multiple indexers should be able to retrieve the same attributable description and apply their own discovery policies.

## Candidate information model

These are semantic elements, not frozen JSON member names.

| Element | Purpose |
| --- | --- |
| Provider and service identifiers | Identify the publisher and the service without relying on an operator-local row ID |
| Descriptor version and content commitment | Bind invocation to an immutable description |
| Publisher proof and key-resolution profile | Attribute publication and determine update authority |
| Operations, input/output schemas, capability set | Describe what can be invoked and its effects |
| Transport bindings and required profiles | Identify compatible endpoints and required semantics |
| Pricing and quote mechanism | Disclose economic requirements before billable work |
| Discovery metadata | Human-readable purpose, examples, categories, and advisory presentation |
| Validity, update, and revocation information | Detect expired or superseded descriptions |

## Proposed requirements

- **DESC-01.** The descriptor MUST authenticate its publisher, service identity, version, and content through a specified publication profile. A mutable handle or URL alone is insufficient authority.
- **DESC-02.** Changes affecting invocation semantics MUST produce a new descriptor version. An accepted request MUST bind the intended version or its unambiguous commitment.
- **DESC-03.** The descriptor MUST disclose required capability, transport, authorization, and payment semantics before execution. Optional discovery metadata MUST NOT silently alter authority or price.
- **DESC-04.** A portability claim MUST state how independent indexers obtain descriptor content, updates, and revocations, including freshness and availability assumptions.
- **DESC-05.** A resolver MUST check the applicable trust and freshness rules before treating a descriptor as current. Unavailable revocation information MUST be handled according to a declared profile, not silently interpreted as proof of validity.

## Rationale and compatibility

Discovery and quality ranking are separate. The specification supplies common inputs and attribution; it does not prescribe a ranking algorithm or guarantee a globally complete catalog. Existing manifests can seed a mapping, but local publisher IDs and unsigned mutable endpoints are not automatically portable identifiers.

## Security and privacy

Endpoints and referenced schemas can become SSRF or resource-exhaustion vectors. Resolvers need endpoint policies, retrieval limits, and explicit redirect behavior. Published descriptors MUST NOT contain merchant secrets, customer records, or redeemable payment credentials. Publication signatures attest provenance, not service quality.

## Open decisions and conformance

Identifier syntax, publication signing format, update ordering, revocation transport, schema dialect, and storage-availability requirements need proposals and test vectors. See scenarios C-01, C-03, and C-10 in the [catalog](../conformance/scenarios.md).
