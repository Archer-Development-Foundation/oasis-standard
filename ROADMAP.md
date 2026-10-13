# Roadmap

**Status:** Proposed, evidence-gated program · v0.1.0-draft.1

| Milestone | Deliverable | Exit evidence |
| --- | --- | --- |
| **First public draft** | Core semantics, profile boundaries, review process, threat model, scenarios | Internally consistent documents, explicit gaps, public-safe contents |
| **Implementable contract** | Exact schemas, signing/identity profiles, state transitions, registries, payment baseline | Shared valid/invalid fixtures and independently reproduced signing bytes |
| **Independent interoperability** | Reference verifiers, provider and executor; external implementations | Multi-provider continuity, principal control/recovery, and failure-path reports |
| **Usable service pilots** | Connected services and supported card/blockchain profiles | Clearly classified mock, provider-supported, and authorized live evidence |
| **Open coordination tooling** | Extensible reference harness for bounded multi-agent workflows | Useful cross-service tasks, tested delegation, recovery, and evidence retrieval |
| **Network experiments** | Independent operator research, optional registry/worker/evidence profiles | Published trust, privacy, availability, security, and cost findings |

The wider foundation charter places service pilots and early coordination/network research around 2027, a usable open coordination harness around 2028, and groundwork for independent node operators around 2029. These are planning goals, not protocol requirements or delivery commitments. Progress depends on evidence from the preceding milestones; no L1/L2 choice or token launch is committed.

## Immediate next proposal

Define a small read-only interoperability slice: independently published descriptor → authenticated request → `data` envelope → attributable receipt and retrieval. Choose exact bytes and identifiers, produce positive/negative vectors, and have two independent verifiers agree. The slice should include denied/expired/replayed requests and original-operator unavailability.

Build paid and external-effect profiles on that verified binding, while specifying their failure and consent semantics in parallel. The narrow first demonstration is not a claim that the full service lifecycle is complete.
