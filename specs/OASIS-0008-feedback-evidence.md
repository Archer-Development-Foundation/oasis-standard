# OASIS-0008: Feedback evidence

| Metadata | Value |
| --- | --- |
| Version | 0.1.0-draft.1 |
| Status | Informative — open research; no normative feedback mechanism selected |
| Editors | Repository maintainers, under bootstrap governance |
| Updated | 2026-10-13 |
| Proposal | Initial publication |

## Core question

**How can an independent verifier bind feedback to an authorized participant in a specific invocation and to credible outcome evidence, without depending on a cooperative provider or making manipulation cheap?**

Human principals, delegated agents, beneficiaries, payers, and independent observers can all have relevant evidence. Their eligibility to make each claim needs justification. The problem is the binding and credibility of feedback, not whether humans are allowed to participate.

## Candidate evidence chain

```text
Principal + delegation
  → authorized request + accepted quote
  → logical execution + service version
  → payment events + service observations
  → attributed receipt or independently evidenced failure
  → feedback + corrections
  → optional registry commitment
```

## Unresolved requirements for a future proposal

- **Authority:** establish who participated and which observations they are entitled to make without unnecessary identity disclosure.
- **Credibility:** distinguish claimed invocation, observed payment, predicted effects, and actual fulfillment.
- **Negative outcomes:** allow meaningful evidence of denial, timeout, failed paid work, or a withheld receipt. A successful-payment-only rule would exclude important failures.
- **Uniqueness:** identify one logical interaction across retries, split payments, agents, operators, and chains.
- **Abuse resistance:** address self-dealing, fabricated volume, identity farming, collusion, ownership changes, and delegated-agent amplification.
- **Corrections:** preserve refunds, disputes, cancellations, and corrected observations with their provenance.
- **Privacy and availability:** define what a verifier can see, who retains evidence, and how an affected participant can challenge a claim.

## Relationship to ranking and registries

Evidence semantics can be shared while indexers use different ranking policies. Signing a review proves authorship rather than honesty, uniqueness, or quality. A registry can carry identifiers and attestations without solving those problems.

[ERC-8004](https://eips.ethereum.org/EIPS/eip-8004) is relevant related work for identity, reputation, and validation interfaces. A mapping would need its own profile and an explicit evidence model; registry participation does not establish a purchase or fulfilled service.

## Review invitation

Contributions should bring a threat model, counterexample, privacy analysis, or reproducible experiment. This document is intentionally outside the initial normative core. See [open questions](../research/OPEN-QUESTIONS.md) and [conformance evidence](../conformance/README.md).
