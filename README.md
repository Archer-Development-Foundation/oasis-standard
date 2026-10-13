# OASIS

**Open Agent Systems Interoperability Standard**

### Specialized services. Portable identity. Verifiable execution records.

OASIS proposes a shared language through which people and agents can discover services, authorize bounded actions, and carry their outcome records across compatible providers.

A service creator publishes capabilities and retains their application logic. Agents use common contracts to invoke those capabilities, from research and curated commerce to bookings and financial operations. Identity, discovery, execution, and history should remain usable beyond any single platform.

**Status: v0.1.0-draft.1 · Editor’s Draft · Open for discussion.** This first publication establishes the architecture, proposed requirements, and review process. It is not a ratified standard, a frozen wire protocol, or a claim of independent interoperability. No conformant implementation or decentralized network is certified by this repository.

## Start here

- **Understand the design:** [Architecture](ARCHITECTURE.md) and [core specification](specs/OASIS-0001-core.md).
- **Review the contracts:** [Specification index](specs/README.md).
- **Evaluate an implementation:** [Conformance program](conformance/README.md) and [test scenarios](conformance/scenarios.md).
- **Contribute a decision:** [Contribution guide](CONTRIBUTING.md), [governance](GOVERNANCE.md), and [proposal process](asips/ASIP-0000-process.md).
- **Choose the next work:** [Roadmap](ROADMAP.md) and [open questions](research/OPEN-QUESTIONS.md).

## Four portability objectives

| Property | Intended result |
| --- | --- |
| **User-controlled identity** | A principal proves authority across providers, with explicit delegation, recovery, and migration paths. |
| **Rebuildable discovery** | Independently available, attributable service descriptions let multiple indexers build catalogs. |
| **Multi-provider execution** | Compatible operators invoke a service through shared contracts without adding service-specific core logic. |
| **Recoverable history** | Authorized participants retrieve attributable outcome records independently of the original operator. |

These are requirements to demonstrate. A key alone does not recover missing records, an email address alone does not prove cryptographic control, and changing operators does not automatically transfer merchant permissions.

## The execution lifecycle

```text
Discover → Verify → Route → Authorize → Consume → Attest
```

The contracts underneath that lifecycle bind the service description, principal, delegated agent, request, quote, permission, and outcome. Preparation and additional approval can pause and resume the same logical execution. Payment confirmation and service fulfillment remain distinct events.

The proposed response model has four composable parts: `data`, `cost`, `authorizations[]`, and `record`. A service may return information, request permission, declare agreed charges, and describe a durable outcome without teaching the shared executor its business domain.

## Scope of this publication

| Included now | Subsequent milestones |
| --- | --- |
| Eight numbered specification drafts; profile design requirements | Frozen JSON Schemas, signing formats, and registered profile versions |
| Contribution and bootstrap stewardship process | Broader governance and a specification-specific patent policy |
| Threat model, test scenarios, and implementation-report template | Shared cryptographic vectors and independent implementations |
| Explicit card-token and blockchain payment boundaries | Provider-supported payment interoperability demonstrations |
| Decentralized-network research scope | Registry, worker execution, and evidence-availability profiles |

This repository defines interfaces, not a required hosted backend, agent harness, ranking algorithm, payment processor, token, or blockchain. REST and MCP are candidate transport bindings. Card tokens and blockchain payments fit through explicit payment profiles. Network operators and a future coordination harness can build on the contracts without becoming prerequisites for the first specification.

## Stewardship and reuse

The [Archer Development Foundation](https://archer.foundation/) hosts the initial repository and describes the wider research mission. Independent implementers, service creators, researchers, and working groups are invited to review and extend the draft through public proposals. Repository hosting does not establish community ratification; the [bootstrap governance rules](GOVERNANCE.md) make current authority and its proposed evolution explicit.

OASIS is this project’s working name and does not imply affiliation with OASIS Open or another standards organization. Related work is credited in [References](REFERENCES.md).

Specification text, original examples, and repository tooling are licensed under [Apache-2.0](LICENSE). The [patent-policy statement](PATENTS.md) explains the limits of the initial policy. No confidential integration material or personal agent context belongs in contributions.

To check this documentation package locally:

```sh
python3 tools/check_repository.py
```

That check validates repository integrity; it does not test protocol conformance.
