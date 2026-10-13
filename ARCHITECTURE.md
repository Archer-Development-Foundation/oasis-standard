# Architecture

**Status:** Informative design overview · v0.1.0-draft.1 · 2026-10-13

## A shared contract between independent participants

```text
Person or organization
  └─ principal identity + bounded delegation
      └─ chosen agent / coordination harness
          ├─ independent catalog → signed service descriptor
          └─ compatible executor
              ├─ permission + quote + supported profiles
              ├─ provider adapter → external service or blockchain
              └─ attributable receipt + recoverable record
                  ├─ authorized private storage / independent retrieval
                  └─ optional public evidence commitment
```

The principal, payer, beneficiary, agent, executor, provider, and attestor can be different parties. Each relationship needs explicit authority; none follows merely from sharing an execution identifier.

## Contract boundaries

| Boundary | Proposed contract | What it does not establish |
| --- | --- | --- |
| Publication → discovery | `ServiceDescriptor` | Quality, availability, or a universally best ranking |
| Agent → executor/provider | `InvocationRequest` | Permission merely because a dispatcher signed |
| Principal → agent/executor | Authorization and delegation | Unbounded spending or transferable merchant credentials |
| Provider → executor | `InvocationEnvelope` | Permission to run every returned action |
| Assessment → decision | `EffectReport` and instrument description | A guarantee of future execution or fulfillment |
| Execution → history | `ExecutionReceipt` and `RecordUpdate` | Truth solely because an assertion is signed |
| History → discovery | Proposed feedback evidence | Sybil resistance or a universal reputation score |

## Keep the layers separable

1. **Core semantics:** identity relationships, service descriptions, invocation binding, authorization, and outcome provenance.
2. **Profiles:** exact transport, identity, payment, merchant-consent, storage, and verification behavior.
3. **Implementations:** agent tools, SDKs, hosted APIs, service adapters, indexers, executors, and reference software.
4. **Optional network:** shared publication, coordination, evidence availability, and compensation under a defined security model.

A profile must expose its dependencies and failures. A protocol can be openly implementable while a particular service still requires authentication, customer eligibility, or a supported processor.

## Discovery is broader than a blockchain lookup

Signed descriptors need available storage, authenticated updates and revocations, and reproducible indexing inputs. An indexer can provide semantic search and its own ranking policy. A chain RPC could help retrieve registry state or evidence commitments; it does not itself perform semantic search or execute merchant HTTP requests.

The first demonstration should work with independently available descriptors and provider-hosted adapters. Decentralizing registry or worker operation is a separate experiment, described in [network research](research/NETWORK.md).

## Execution is not a single atomic transaction

A paid booking can involve a quote, consent, payment authorization, reservation, capture, fulfillment, and later cancellation. These events can fail separately. Logical execution identifiers, distinct attempt identifiers, explicit continuations, and reconciliation protect against treating a timeout as permission to purchase again.

The standard seeks interoperable evidence of those events. It cannot make arbitrary external systems atomic, force a merchant to accept an agent, or recover records that nobody retained.
