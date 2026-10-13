# Illustrative flows

**Status:** Informative examples, not wire fixtures or executed tests.

All participants below are fictional roles. No real keys, accounts, endpoints, or payment credentials are used. The diagrams show relationships; exact messages require the future schemas and profiles.

## Read-only service

```text
Principal → delegate permission to Agent
Agent → Independent index: discover an analysis capability
Index → Agent: attributable descriptor + supported profiles
Agent → Executor: bound request + applicable authority
Executor → Provider: verified read invocation
Provider → Executor: data envelope + attributable observation
Executor → Agent: result + receipt reference
Principal → Independent record store: retrieve authorized evidence
```

If the service charges for the read, quote and payment negotiation precede billable work. “Read-only” does not mean “free.” A timeout is recorded as an observation with its limits, not proof that the provider did nothing.

## Card-funded reservation

```text
Agent ↔ Provider: prepare availability and quote
Agent → Principal: request bounded reservation/payment permission
Principal → Agent: approve bound action, or deny
Agent ↔ Payment provider: obtain seller-scoped credential / extra approval
Executor → Merchant: invoke under supported merchant and payment profiles
Merchant → Executor: payment event + reservation outcome (distinct)
Executor → Principal: attributable receipt + reservation record
Later correction → Record store: cancellation / refund / dispute update
```

The exact order of reservation, card authorization, and capture depends on the selected profile and merchant behavior. The credential travels only to its authorized recipient. A lost response triggers reconciliation against the original logical operation before another reservation or charge is attempted.

## Provider switch

```text
Original operator becomes unavailable
Principal proves authority to another compatible operator
New operator retrieves and verifies an available service descriptor
Merchant access is delegated or reauthorized if required
Bounded invocation proceeds; records remain independently retrievable
```

This scenario requires actual independence of identity, publication, execution, and record availability. The description alone does not demonstrate that property.
