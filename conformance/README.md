# Conformance program

**Status:** Proposed test program · v0.1.0-draft.1

This repository currently contains a documentation draft and scenario definitions. There is no executable protocol harness, frozen signing suite, or verified implementation report. Passing repository checks does not confer protocol compliance.

## Claims must name their scope

An implementation report must identify its role, specification revision, supported profile versions, test artifacts, and limitations. A client, publisher, indexer, executor, verifier, or record store can implement different parts; a partial result must not be labeled universal OASIS conformance.

## Evidence gates

1. **Specification completeness:** choose the mandatory profile set, exact schemas, signing bytes, state transitions, error behavior, registries, and security requirements.
2. **Shared vectors:** independent verifiers agree on valid and invalid inputs, canonical bytes, identity resolution, signatures, expiry, domain separation, and replay rejection.
3. **Multi-provider continuity:** an independent index and executor complete a bounded operation and retrieve attributable evidence while the original operator is unavailable.
4. **User-controlled identity and recovery:** a new principal works without an account at the original operator; each advertised recovery/migration profile is exercised under its stated failure model.
5. **Cross-domain behavior:** read, funds, external-effect, and combined operations share the core contracts, including denial, partial failures, retries, corrections, and required-profile refusal.
6. **Payment interoperability:** supported card and blockchain profiles have separate evidence, with merchant/processor dependencies and approval behavior recorded.

These gates are proposed acceptance criteria. They are not completed demonstrations.

## Test evidence categories

| Category | What it can support |
| --- | --- |
| Static/schema checks | Structure and declared validation rules |
| Local deterministic vectors | Agreement on a particular encoding or verifier behavior |
| Mock integration | Local control flow under simulated dependencies |
| Live upstream read | Reachability and actual read behavior at the time tested |
| Provider-supported test flow | Behavior in the provider’s stated test environment |
| Authorized live execution | Observed behavior for the particular operation, amount, and environment |
| Independent interoperability | Demonstrated behavior across independently controlled implementations and dependencies |

Do not promote one category into another. Two wrappers around the same proprietary backend do not demonstrate provider independence.

Use the [scenario catalog](scenarios.md) and [report template](REPORT-TEMPLATE.md). Published reports must use synthetic or minimized evidence and omit credentials and personal transaction details.
