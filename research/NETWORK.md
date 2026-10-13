# Decentralized network research

**Status:** Informative research agenda · v0.1.0-draft.1

The long-term objective is an independently operated discovery, execution, and attestation network built on the shared contracts. No chain, native token, consensus mechanism, L1, or L2 is selected by this draft.

## What a blockchain could contribute

| Candidate responsibility | Possible shared state | Separate problem to solve |
| --- | --- | --- |
| Publication and authority | Descriptor commitments, publisher updates, revocations | Available descriptor content and key recovery |
| Coordination | Job assignment, reservations, ordering or dispute commitments | Safe external effects under timeouts and worker failure |
| Evidence | Receipt commitments or batch roots | Truth, privacy, independent retrieval, retention |
| Compensation | Explicit fees, deposits, or settlement references | Sybil resistance, fair attribution, reversals, operating costs |

Use consensus where a specific shared-state guarantee justifies its cost. Compare signed offchain publication, contracts on an existing L1, and an L2 before considering a dedicated chain. An RPC is an access mechanism, not the complete service-discovery or execution system.

## Adapter execution models

**Provider-hosted first.** The provider runs its service and exposes a supported binding. Independent executors enforce request and permission contracts without moving application code onto a network.

**Network-hosted later.** A worker runtime would need signed packages, immutable version binding, resource and egress limits, protected merchant credentials, observable execution, upgrade/revocation rules, and containment of malicious code. Ordinary offchain APIs are not deterministic replicated blockchain computation.

Do not fan out a purchase to several workers as though it were a read query. Worker ownership, lease expiry, provider idempotency, and reconciliation must prevent uncertain failover from creating duplicate side effects. An open protocol cannot impose a universal fee on calls that bypass its network facilities.

## Coordination harness and community

A future open-source reference harness could translate a user goal into scoped tasks, discover compatible services, request permission, coordinate agents, and retain attributable outcomes. It should be one implementation of the contracts, usable across providers, rather than a mandatory client.

Community pilots should connect real services and demonstrate usable workflows. Research must separate intent interpretation from authorization: natural-language output cannot itself establish permission to spend or act.

## Gates before a network commitment

1. Stable core contracts and independent implementations.
2. Measured descriptor/evidence availability and privacy behavior.
3. Safe ownership transfer and external-effect reconciliation under failures.
4. Explicit consensus, trust, upgrade, and economic assumptions.
5. Published cost and security comparisons for the candidate architectures.

No grant relationship, network partnership, launch date, or chain affiliation is implied by these research directions.
