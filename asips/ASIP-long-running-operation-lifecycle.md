# ASIP: Long-running operation lifecycle

- Identifier: unassigned
- Status: Draft
- Type: profile
- Author or editor: [archerfdn](https://github.com/archerfdn)
- Created: 2026-10-18
- Affected specifications and versions: OASIS-0001 through OASIS-0007, v0.1.0-draft.1
- Public discussion: [long-running operation lifecycle](https://github.com/Archer-Development-Foundation/oasis-standard/issues/1)
- Replaces: none
- Depends on: future versioned signing, identity, transport, evidence, and applicable payment profiles

## Abstract

Define how a principal controls an ongoing service after its initial invocation: observe its state, stop new work, revoke future authority, cancel pending commitments, and recover remaining assets or other deliverables. Bind each continuation and control request to its authority, immutable terms, prior evidence, and logical execution. Preserve uncertainty when an external effect cannot yet be established.

The principle is: **delegation must remain bounded and accountable throughout a service's lifetime, including termination and recovery.**

This proposal supplies candidate semantics, state tables, message fields, synthetic examples, and test designs for public review. It does not register a profile, freeze wire schemas or signable bytes, amend the numbered specifications, or establish implementation conformance. Uppercase requirement terms below express proposed obligations for implementations that explicitly negotiate the eventual profile.

## Motivation and scope

A scheduled purchase, a continuing research service, and a reservation workflow can all outlive the request that started them. Their control surfaces must distinguish stopping future activity from undoing an external commitment. Authentication can expire while a provider still holds assets or owes a result. A worker can disappear after submission but before recording the response.

The existing draft already requires separate state dimensions (CORE-05), bound resumptions (REQ-03 and ENV-04), uncertainty-aware errors (ENV-05), bounded delegation (AUTH-01 through AUTH-06), and attributable record updates (REC-01 through REC-06). This proposal makes their application to continuing work explicit.

The base lifecycle profile applies when a service advertises ongoing work or recoverable continuations. Simple read-only adapters need not implement financial fields or ongoing controls. Domain logic remains in the service and its adapter. No blockchain, token, custody model, hosted operator, or universal withdrawal mechanism is required.

## Specification

### 1. Identity and immutable commitments

Three identities serve different purposes:

| Identity | Scope | Rule |
| --- | --- | --- |
| Lifecycle identity | The continuing service instance and its durable record | Survives changes of executor and related control operations; does not itself grant authority |
| Logical execution identity | One authorized operation, such as creation, cancellation, or recovery | Preserved across approval resumptions and retries of that operation |
| Step and attempt identities | A named effect within an operation, and each attempt to perform or observe it | Attempts link to the same step; issuing another attempt must not create another intended effect |

**LIFE-01.** Requests and receipts MUST bind these identities, the provider/service, descriptor version or commitment, principal, acting agent/executor, and required profile revisions. A control initiating a distinct effect, such as cancellation or recovery, MUST have its own logical execution identity linked to the lifecycle it controls. Approval, denial, and resumption of an existing operation remain events within that operation; they MUST NOT silently create another intended effect. Scheduled effects MUST have distinct effect identities under the accepted schedule, even when one grant authorizes several effects.

**LIFE-02.** The accepted terms MUST bind the relevant schedule, duration, argument/effect limits, intended recipients, quantities/units, price or quote rules, expiry, and amendment policy. Each limit MUST identify its enforcement point and whether it is mechanically enforced, provider-enforced, or advisory. A requested limit that the service cannot enforce MUST be disclosed and either explicitly renegotiated before commitment or refused. A session login MUST NOT stand in for spending or service authority.

An amendment is a separately authorized operation with a new terms commitment and a reference to the prior one. It cannot silently widen a live grant or turn materially changed arguments into a retry. The applicable profile must order amendments against work already submitted or scheduled. Until that ordering is known, the executor must block the affected new work and report uncertainty.

### 2. Descriptor and control capabilities

**LIFE-03.** A descriptor advertising this profile MUST declare each supported control, its target and scope, prerequisite authority, enforcement party, expected acknowledgment evidence, and limits under provider or operator failure. Unsupported controls MUST be explicit. Display labels alone MUST NOT establish supported behavior.

| Control | Intended effect | Required distinction |
| --- | --- | --- |
| Observe | Retrieve a scoped current assessment and attributable history | Observation alone does not restart work or authorize a new external effect |
| Decline approval | Reject a pending approval step | It neither creates a new operation nor proves that earlier effects were undone |
| Stop new work | Prevent additional scheduled work at a named enforcement point | Request receipt, effective stop, and already-submitted work are separate facts |
| Revoke authority | Invalidate a named grant for future use within its declared scope | Existing provider commitments or previously signed artifacts may remain effective |
| Cancel pending work | Ask the external service to cancel identified commitments | Cancellation may be rejected, partial, charged, or irreversible after a cutoff |
| Recover | Retrieve remaining assets, outputs, or other recoverable entitlements | Requires its own authority and outcome evidence; may remain pending or unavailable |
| Resume or amend | Start additional work under accepted current terms | Requires fresh applicable authority; recovery must not implicitly resume the service |

**LIFE-04.** A control response MUST identify the affected scope and distinguish `requested`, `effective`, `rejected`, `partial`, and `unknown` dispositions. `Effective` MUST identify the enforcement evidence and boundary. Logout, session expiry, local stop, and operator outage MUST NOT be represented as external cancellation or grant revocation without such evidence.

Providers MUST disclose custody or possession, external locks, cancellation conditions, residual authority, and the available exit route before the relevant commitment. If recovery depends on the original provider, that dependency remains visible. This profile cannot promise recovery from an uncooperative or insolvent provider.

### 3. Separate state dimensions

**LIFE-05.** State MUST be represented as scoped observations with issuer, observation time, evidence references, and freshness policy. Implementations MUST preserve the dimensions below separately; they MUST NOT collapse them into one success flag. An unknown or stale observation cannot authorize work that requires a known current state.

| Dimension | Candidate values | Meaning |
| --- | --- | --- |
| Grant validity | `pending`, `valid`, `denied`, `expired`, `revoked`, `unknown` | Whether a particular grant currently permits the proposed action; expiry or revocation is not evidence of reversal |
| Step submission | `not_submitted`, `submitted`, `unknown` | What evidence establishes about dispatch to the external service, independently of effect status |
| Step effect | `not_observed`, `pending`, `partial`, `fulfilled`, `failed`, `unknown` | Attributable assessment of the intended effect; a failed step may still have incurred a fee or other recorded side effect |
| Activity admission | `running`, `stop_requested`, `stopped`, `ended`, `unknown` | Whether new work is admitted at the declared enforcement point |
| Outstanding obligations | `open`, `recovering`, `settled`, `disputed`, `unknown`, `not_applicable` | Remaining delivery, recovery, fee, or refund obligations within a defined scope |

Payment authorization, capture, settlement, reversal, and dispute states remain defined by the negotiated payment profile. The obligations dimension summarizes what remains due; it does not replace payment-provider state or demonstrate payment finality.

The following are guarded transition patterns, not a complete executable state machine:

| Trigger | Permitted transition or observation | Guard and residual obligation |
| --- | --- | --- |
| Approval denied or expired before dispatch | Grant becomes `denied` or `expired`; step remains `not_submitted` only if supported by dispatch evidence | No signing or dispatch under that grant; preserve prior effects and other grants |
| Submit responsibility durably claimed | Record an attempt and its dispatch intent before external I/O | Bind the exact effect, replay boundary, and reconciliation reference |
| Dispatch acknowledged | Submission becomes `submitted`; effect is whatever the acknowledgment actually establishes | Acceptance alone does not establish fulfillment |
| Dispatch response lost | Submission or effect becomes `unknown` as appropriate | Reconcile before another potentially duplicative dispatch; local absence of a receipt proves nothing |
| Stop accepted locally | Activity becomes `stop_requested` | External work may continue; identify the remaining enforcement boundary |
| Stop proven effective | Activity becomes `stopped` for that scope | Outstanding effects and obligations retain their separate states |
| Cancellation confirmed; recovery unsigned | Relevant pending work is cancelled; obligations remain `open` or `recovering` | A denied recovery signature must not restart the original activity |
| Refund or output observed before provider status catches up | Append attributable delivery evidence; retain conflicting provider observation | Correlate the same event to prevent double counting; apply the evidence/finality policy |
| Recovery response lost or worker restarts | Recover from durable identities and prior evidence | Resolve whether recovery already occurred before a new attempt |
| All declared obligations discharged | Obligations may become `settled` with evidence and scope | Later disputes, reorgs, or corrected observations append updates; earlier claims remain attributable |

An observation may become `unknown` when freshness expires without implying that the external system reversed its state. A grant that is denied, expired, or revoked cannot be revived by changing its status field; replacement authority requires a new attributable grant. Activity may resume only through an authorized control with current terms. A record can remain readable after activity ends, and settlement does not require all privacy-restricted evidence to be public.

### 4. Continuation and recovery messages

These are candidate field names and constraints for schema review. The identifier grammar, canonical encoding, proof format, complete error registry, and placement within transport/envelope metadata remain open. No fifth response arm is proposed. Required lifecycle semantics must be negotiated and authenticated; placing them in optional display `data` cannot make them optional to an executor.

| Candidate object | Required semantic content |
| --- | --- |
| Lifecycle binding | Profile/revision; lifecycle identity; principal; service and descriptor commitment; accepted terms commitment; applicable grant references |
| Continuation | Lifecycle/logical execution/step/attempt identities; prior receipt or continuation reference; requested next action; action/argument commitment; audience and endpoint binding; expiry; accepted quote reference when applicable; prerequisite state/evidence |
| Submission policy | Named signing and broadcast responsibilities; external effect/idempotency reference and scope; provider observation method; finality/freshness rules; recovery behavior after an uncertain dispatch |
| Control request | Control execution identity; target lifecycle and control scope; requested action; expected record predecessor or equivalent concurrency condition; applicable authority, terms and quote references |
| Lifecycle update | Attributed event and receipt; prior update references; separate observed state dimensions; remaining obligations; permissible next actions and their authority requirements |
| Recovery package | Bound descriptor/terms; authorized identities; invocation/attempt and external-effect references; attributable updates; scoped evidence retrieval information; key-recovery and provider-reauthorization instructions |

**LIFE-06.** Before acting on a continuation, an executor MUST validate its authenticated binding, the applicable grant and audience, exact payload/terms, expiry, quote, and required current state. Changing the payload or relevant state requires reassessment under the selected effect profile. A signature returned by a sign-only step MUST NOT be treated as broadcast evidence. Only the designated and currently authorized submitter may broadcast or relay the artifact.

**LIFE-07.** The executor MUST durably retain enough authorized evidence before dispatch to distinguish intended effects and reconcile them after a crash. A timeout, missing journal entry, expired local lease, or change of executor MUST NOT alone authorize another dispatch. Retries MUST preserve the provider idempotency scope where supported. If the provider cannot resolve uncertainty or prevent duplicates, the operation MUST enter an explicit recovery/intervention path without claiming safe automatic retry.

The profile must specify how a lost response is observed, who may perform that observation, and how authorization for recovery is obtained. Reapproval does not establish that the first effect did not occur. An intentional replacement despite unresolved prior effects is a distinct operation requiring explicit disclosure and acceptance of the duplicate-effect risk, where supported.

**LIFE-08.** Executors claiming safe ownership transfer MUST specify and test exclusion/fencing or provider-supported deduplication at the effect boundary, including the case where the previous executor resumes. A transferable journal or distributed lease alone is insufficient. If the advertised mechanism cannot establish that boundary, the receiving executor MUST restrict itself to authorized observation and recovery until safe submission authority and effect state are established. Aggregate allowance enforcement requires a separately supported coordination profile.

### 5. Evidence, remaining obligations, and financial extensions

**LIFE-09.** Pre-execution assessments MUST identify the assessor, exact payload, method, source state, freshness, supported coverage, and trust basis under OASIS-0006. Post-execution receipts and updates MUST identify the event, attestor, observation time, provenance, and relationship to earlier evidence under OASIS-0007. Provider assertion, independently checked observation, and finalized chain event MUST remain distinguishable. Self-declared verification flags do not establish independent verification.

**LIFE-10.** A record MUST identify remaining obligations and the evidence required to discharge them. Activity ending, a successful cancellation, or record closure MUST NOT imply delivery, refund, or economic finality. Corrections MUST preserve the original claim and identify what they supersede. Conflicting evidence MUST remain visible until resolved under the selected profile.

An optional financial extension needs exact asset and network identity, quantity and scale, provenance, finality/reorg policy, and distinct event roles for principal, fee, refundable reserve, held balance, delivery, and return. It must distinguish cumulative deposits from current holdings and delivered amounts, and historical basis from current valuation. Missing or stale prices must remain unknown rather than becoming zero. The same economic event reported by two sources must not be counted twice. Tickers and an adapter's asserted total value are insufficient accounting evidence. Accounting methods and performance claims require separate specification and validation.

Card-based and blockchain-based payments remain possible through their declared profiles. Credential audience, per-purchase approval, validity, capture and reversal rules still apply. A payment token does not establish standing authority for future purchases, nor prove fulfillment. Redeemable credentials and signed artifacts that can still cause effects are restricted capability material, not public receipts.

### 6. Authorized portability

**LIFE-11.** A portability claim MUST identify how an authorized independent executor and record reader obtain descriptor content, terms, identities, histories, and recovery references while the original operator is unavailable. Specify retention, access control, encryption/key recovery, rotation, deletion, freshness, and remaining provider dependencies. A content hash without retrievable content does not satisfy this requirement. Private signing keys and merchant bearer credentials need not be exported.

Observation/recovery authority MUST be separately scoped from authority to initiate more work. Expiry or revocation of a work grant must not implicitly erase the history or require restarting the service to seek recovery. Access still requires valid authority, potentially through a new authentication or provider-reauthorization step. Deletion and retention limits must be disclosed because they bound later verification and recovery.

**LIFE-12.** Unsupported mandatory lifecycle, signing, authorization, evidence, or economic semantics MUST be refused before affected billable work or effects. Negotiation cannot silently drop a control or guarantee on which the principal's consent depends. An adapter may advertise a narrower supported capability set with explicit limits.

## Illustrative traces

All identifiers and quantities below are synthetic. The JSON excerpts demonstrate candidate bindings only; they omit proofs and other required request fields and are not complete, signable wire messages. The `urn:example:` profile name is unregistered. No example establishes production behavior or an implementation result.

### Scheduled purchase and recovery

A principal authorizes three scheduled purchases of 10 units each, within a total of 30 units of a synthetic input asset, with separately disclosed fee bounds. One purchase completes. The principal stops remaining work, the provider acknowledges cancellation of the unfilled schedule, and 20 input units remain recoverable under the example's zero-fee assumptions.

```json
{
  "profile": "urn:example:oasis:long-running:proposal-1",
  "lifecycleId": "urn:example:lifecycle:scheduled-purchase-1",
  "executionId": "urn:example:execution:recover-1",
  "stepId": "urn:example:step:return-remainder",
  "attemptId": "urn:example:attempt:return-1",
  "nextAction": "request_signature",
  "termsRef": "urn:example:commitment:recovery-terms-v1",
  "authorizationRef": "urn:example:grant:recovery-1",
  "priorReceiptRef": "urn:example:receipt:cancel-confirmed-1",
  "actionRef": "urn:example:commitment:return-payload-v1",
  "audience": "urn:example:executor:recovery-b",
  "expiresAt": "2026-10-20T12:05:00Z"
}
```

The principal declines the recovery signature. Activity remains stopped; the remaining obligation stays open. A later authorized recovery request refers to the same intended recovery operation if its committed action and terms are unchanged, uses a new attempt, and establishes fresh authority. If its terms change, it becomes a new linked operation after reconciliation of the prior one. Neither path reinstates the purchase schedule.

If a signed recovery submission loses its response, its outcome becomes uncertain. A replacement executor first looks up the original external effect. A verified return discharges only the correlated obligation; stale provider balance data does not create another 20-unit holding. The already-delivered output asset is recorded under its own identity and delivery location, even if it is on another network. Price data can remain unavailable without erasing the quantities.

### Continuing research service

A principal authorizes a research service to monitor a synthetic public dataset and produce three reports, with no monetary charge. After the first report is delivered, the principal requests a stop. One report is already in progress. The descriptor says that new jobs can be stopped, but in-progress computation can only be cancelled on a best-effort basis.

```json
{
  "lifecycleId": "urn:example:lifecycle:research-1",
  "executionId": "urn:example:execution:stop-research-1",
  "control": "stop_new_work",
  "scope": "urn:example:schedule:remaining-reports",
  "authorizationRef": "urn:example:grant:stop-research-1",
  "expectedRecordRef": "urn:example:update:research-4",
  "disposition": "effective",
  "evidenceRef": "urn:example:receipt:scheduler-stop-1",
  "activityState": "stopped",
  "obligationsState": "open"
}
```

This is an illustrative control result, not the request granting authority. The remaining in-progress report may still arrive. Its attributable delivery updates the record without restarting monitoring. An authorized reader can retrieve earlier reports independently while the original operator is offline, if the advertised storage and identity dependencies remain available. A failed retrieval is reported as unavailable, not as proof that the reports never existed. No asset valuation or blockchain fields are required.

## Rationale and alternatives

Separate state dimensions preserve facts such as "no more jobs admitted, but a refund is pending." One terminal flag cannot express that combination. Stable execution identities bind retries; a distinct lifecycle identity lets related control operations carry different permissions without rewriting the initial request.

Mandating universal cancellation would exclude services whose external commitments cannot be reversed. The proposed descriptor instead exposes enforceable controls and their limits before commitment. Mandatory recovery disclosure can identify that an exit depends on the provider; it cannot make that dependency disappear.

A common envelope extension is a candidate home for continuation metadata. Transport-specific headers are another option, provided they preserve authenticated semantics across transports. Neither placement is selected here. Financial accounting is separated because a report-delivery service can satisfy the lifecycle rules without an asset ledger.

## Compatibility and migration

Existing implementations may map their handles, sessions, journals, transaction observations, and records through a documented compatibility profile. The mapping must name exact versions, identity resolution, trust dependencies, signing coverage, and unsupported semantics. Renaming existing fields or signatures does not establish compatibility with a future OASIS authenticated representation.

The four response arms remain unchanged. An implementation requiring lifecycle semantics must advertise and negotiate the eventual registered profile. Legacy clients that cannot enforce the required semantics must refuse the affected operation or negotiate an explicitly narrower supported service before consent.

If accepted, integrate the descriptor/control declarations into OASIS-0002; identity and continuation rules into OASIS-0003/0004; ongoing authority boundaries into OASIS-0005; evidence binding into OASIS-0006; and obligation/update semantics into OASIS-0007. OASIS-0001's separate-state rule remains the organizing principle. Integration must update status/version metadata, the changelog, and applicable scenarios together after public review.

## Security and privacy

- **Submission authority:** exact payload, audience, destination, replay domain, and validity must survive relay. Recovery endpoints and redirects require endpoint policy checks; a mutable URL in display content is not executable authority.
- **Revocation races:** the profile must identify the enforcement point and ordering relative to signatures already issued, scheduled jobs, external acceptance, and in-flight effects. An unavailable revocation service needs a declared safe behavior.
- **Concurrent workers:** shared files or journals alone do not prevent duplicate submission. Fencing, provider deduplication, and the case of a resumed former worker need adversarial tests.
- **Evidence trust:** manipulated prices, inflated balances, stale observations, and provider self-attestation must not silently increase authority or establish completion. Pre-execution simulation cannot prove later delivery.
- **Recovery data:** journals and records may reveal private activity or contain usable capabilities. Apply bounded retrieval, least disclosure, retention limits, encryption, and independent key-recovery analysis. Public commitments to predictable private data can enable guessing.
- **Recovery costs:** observation, cancellation, and recovery can themselves be billable or effectful. Required permission and quote checks still apply; revoking work does not authorize an undisclosed recovery fee.

## Conformance evidence

**Current evidence: none.** These are test designs and illustrative traces. This proposal ships no executable protocol harness, cross-language signing vectors, registered profiles, or verified implementation report. Documentation checks establish only repository integrity.

| Local case | Setup | Expected observation | Existing scenario |
| --- | --- | --- | --- |
| L-01 | Alter payload, schedule, recipient, quote, or audience after approval | Refuse affected signing/dispatch; changed terms require a separately authorized operation | C-03 |
| L-02 | Deny or expire approval; then attempt continuation | No effect under invalid authority; prior effects and valid recovery paths remain separately recorded | C-05 |
| L-03 | Produce a sign-only artifact, then replay it at another audience or step | No implied broadcast; reject substituted binding and duplicate intended effects | C-03, C-06 |
| L-04 | Crash before send, during send, or after provider acceptance but before acknowledgment | Retain dispatch intent; distinguish proven non-submission from uncertainty; reconcile before retry | C-06 |
| L-05 | Stop a partially completed schedule while further work is in flight | Record enforcement boundary, partial effects, and residual commitments; no unsupported cancellation claim | C-05, C-08 |
| L-06 | Confirm cancellation; deny recovery signing | Activity remains stopped and outstanding obligation remains open | C-05, C-08 |
| L-07 | Lose a recovery response; restart or change executor | Observe the original external effect before another attempt; never restart original work implicitly | C-01, C-06 |
| L-08 | Observe a refund before provider balance/status updates | Correlate source evidence for the same event; preserve conflict without double counting | C-08 |
| L-09 | Supply a missing/stale price or forged inflated balance | Unknown valuation stays unknown; no increase in permitted spend or unsupported performance claim | C-11 |
| L-10 | Deliver output under another asset or network identity | Preserve exact delivery identity and evidence; do not substitute a home-network balance | C-07, C-08 |
| L-11 | Disable the original operator and rotate a principal key | Authorized independent retrieval and supported reauthorization work under declared dependencies, or fail with explicit limits | C-01, C-02, C-10 |
| L-12 | Old and new executors both attempt submission; shared allowance is nearly exhausted | Demonstrate the declared effect-boundary mechanism; report unsupported aggregate-budget guarantees explicitly | C-06, C-09 |
| L-13 | Offer an unknown mandatory lifecycle profile or silently remove a required control | Refuse affected commitment before billable work/effects | C-04 |
| L-14 | Run the continuing research trace, including late delivery after stop | Preserve delivery and retrieval evidence without financial fields or renewed monitoring | C-05, C-08 |
| L-15 | Correct a previously settled observation after dispute or finality reversal | Append a linked correction; expose the reopened obligation and retain the original claim | C-08, C-10 |

Before making the profile implementable, each case needs pinned dependencies, concrete fixtures, deterministic setup, exact messages/signing bytes, and an expected transcript. Test unknown evidence, forged updates, and expired access as negative variants. Implementation reports must distinguish local fixture tests, live upstream observations, single-provider execution, and independent interoperability. Use the existing [report template](../conformance/REPORT-TEMPLATE.md); preserve untested and unsupported outcomes.

## Open questions and decision record

| Decision | Current position | Needed before a stable profile |
| --- | --- | --- |
| Registered identifier, schema, and extension placement | Candidate fields only; no assigned profile identifier | Required/optional fields, limits, unknown-field rules, complete transitions and errors |
| Signing and commitments | Depend on a versioned authenticated representation | Canonical bytes, algorithms, key resolution, proof placement, replay and cross-language vectors |
| Revocation and amendment ordering | Enforceable boundary must be declared | Rules for pre-signed artifacts, in-flight effects, scheduled provider activity, and stale revocation information |
| Reconciliation and executor ownership | No automatic failover guarantee | Provider idempotency scope/lifetime, fencing assumptions, partition behavior, and intervention semantics |
| Obligation scope and financial extension | Keep delivery/return evidence separate from activity status | Units, event correlation, valuation provenance, finality, and contested evidence resolution |
| Independent retrieval | Availability and authorization are separate requirements | Retention, encryption/key recovery, deletion, and provider reauthorization experiments |

Decision record: initial unnumbered draft submitted for discussion. No consensus or acceptance is asserted. Allow at least the public-review period required by [ASIP-0000](ASIP-0000-process.md) before integrating substantive requirements; maintainers allocate the proposal number when it is ready for review.

## References

The proposal baseline is OASIS v0.1.0-draft.1, public repository revision [fa011ae68ea7dd40358a48d1b627a8997b9b2438](https://github.com/Archer-Development-Foundation/oasis-standard/tree/fa011ae68ea7dd40358a48d1b627a8997b9b2438).

- [Core model and separate state dimensions](../specs/OASIS-0001-core.md), CORE-01 through CORE-06.
- [Service descriptor](../specs/OASIS-0002-service-descriptor.md), DESC-01 through DESC-05.
- [Invocation request](../specs/OASIS-0003-invocation-request.md), REQ-01 through REQ-05.
- [Invocation envelope](../specs/OASIS-0004-invocation-envelope.md), ENV-01 through ENV-06.
- [Authorization and delegation](../specs/OASIS-0005-authorization.md), AUTH-01 through AUTH-06.
- [Effect measurement](../specs/OASIS-0006-effect-measurement.md), EFFECT-01 through EFFECT-05.
- [Receipts and records](../specs/OASIS-0007-receipts-and-records.md), REC-01 through REC-06.
- [Profile program](../profiles/README.md), [payment profile requirements](../profiles/payments.md), and [conformance scenarios](../conformance/scenarios.md), v0.1.0-draft.1.
