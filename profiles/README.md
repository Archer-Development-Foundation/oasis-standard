# Profile program

**Status:** Informative design requirements · v0.1.0-draft.1

Profiles turn core semantics into implementable mechanisms. This publication contains requirements for designing profiles, not registered or interoperable profile specifications.

| Area | Design document | First decisions |
| --- | --- | --- |
| Transport | [REST and MCP](transport.md) | Request/response mapping, negotiation, authentication, continuation, errors |
| Identity | [Control and recovery](identity.md) | Proof, resolution, delegation, rotation, independent recovery |
| Payments | [Card and blockchain rails](payments.md) | Quote binding, credential scope, status, fees, reversals |
| Merchant access | [Linkage and consent](merchant-linkage.md) | Issuer, principal, audience, scopes, reauthorization |
| Registry and workers | [Network research](../research/NETWORK.md) | Trust, availability, assignment, runtime, economics |

A profile proposal needs an identifier and version, exact dependency revisions, roles, wire encoding, a state machine, security/privacy analysis, positive and negative vectors, and an implementation report. Required semantics cannot be hidden in an optional extension.

No default processor, chain, token, custody provider, or hosted endpoint is mandated here. Registry contracts, network-executed adapters, cross-executor aggregate budgets, and public anchoring are later profiles with separate acceptance gates.

## Draft proposals

[Long-running operation lifecycle](../asips/ASIP-long-running-operation-lifecycle.md) proposes ongoing control, bound continuations, recovery, and attributable obligations for continuing services. It is an unnumbered Draft ASIP with candidate fields and test designs, not a registered profile or an amendment to the numbered specifications.
