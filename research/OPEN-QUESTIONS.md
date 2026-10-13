# Open technical questions

**Status:** Research agenda · v0.1.0-draft.1

| ID | Decision to resolve | Evidence needed |
| --- | --- | --- |
| Q-01 | Bind feedback to authorized participation and credible outcomes, including failures | Threat model, counterexamples, privacy and anti-abuse experiments; see [OASIS-0008](../specs/OASIS-0008-feedback-evidence.md) |
| Q-02 | Select identity, signing, and canonicalization profiles | Exact bytes and key-resolution rules; independent cross-language vectors |
| Q-03 | Enforce shared budgets across concurrent agents and executors | Reservation/consumption/release semantics under races, partitions, revocation, and changing valuations |
| Q-04 | Reconcile uncertain external side effects | Provider-supported idempotency, ownership transfer, status evidence, and safe operator recovery |
| Q-05 | Preserve private evidence independently of its original operator | Retrieval, encryption, rotation, retention, deletion, and availability experiments |
| Q-06 | Authenticate and update a rebuildable catalog | Versioning, revocation, publisher recovery, malicious-descriptor handling, and censorship/availability analysis |
| Q-07 | Map card-token and blockchain payments without conflating fulfillment | Credential restrictions, extra approval, payment-state transitions, reversals, and real interoperability evidence |
| Q-08 | Decide which network functions justify consensus | Comparable costs and guarantees across offchain coordination, existing chains, and L2 designs |
| Q-09 | Select a standards-specific patent policy and durable governance | Public proposals and explicit participation commitments before ratification |

Answering a question may narrow the specification or show that a proposed guarantee is not achievable under its current assumptions. Record that outcome openly through the [proposal process](../asips/ASIP-0000-process.md).
