# Payment profiles: cards and blockchain rails

**Status:** Informative design requirements · v0.1.0-draft.1

A card-funded action can carry cryptographically attributable permission and outcome records. The payment rail, identity proof, execution evidence, and optional blockchain anchor are separate choices.

## Shared requirements for a profile proposal

1. Bind the accepted quote to service/version, logical execution, payer, beneficiary where relevant, payee, asset/currency, exact amount or enforceable maximum, fees, validity, and settlement timing.
2. Negotiate supported methods before billable work. Unsupported payment semantics cannot silently become free execution.
3. Deliver redeemable credentials only to authorized recipients. Public descriptors, routine logs, receipts, and chain state must not contain raw card details or reusable payment secrets.
4. Define authorization, settlement/capture, failure, refund, dispute, cancellation, and any additional approval continuation as distinct events where the rail supports them.
5. Bind processor or chain evidence to execution without equating payment with service fulfillment.
6. State exact units, rounding, finality, fee allocation, idempotency, and ambiguous-outcome reconciliation.

## Candidate profiles

| Candidate | Role | Work before interoperability can be claimed |
| --- | --- | --- |
| Free / externally settled | Explicitly identifies no charge through this interaction or a separate authorized settlement arrangement | Disclosure, external evidence if required, and refusal of undisclosed charges |
| Flat blockchain payment | A precisely quoted transfer for a service | Chain/asset identifiers, fee breakdown, signature domain, contract/transfer rules, finality, replay and refund behavior |
| x402 binding | Reuse a supported x402 scheme, network, and transport | Pin the dependency; map challenges, credentials, settlement evidence, execution identity, and retries |
| MPP / card-token binding | Reuse supported processor credentials, including a candidate Shared Payment Token path | Pin the method; define issuer, seller scope, eligibility, approval, capture, evidence, and reversal handling |

[x402](https://github.com/x402-foundation/x402) separates payment schemes and networks. [Stripe’s MPP documentation](https://docs.stripe.com/payments/machine/mpp) describes agent payment flows including Shared Payment Tokens. These are integration candidates; neither reference establishes OASIS compatibility or merchant acceptance.

## Cards are not universal bearer money

A processor token is only usable under its issuer’s restrictions and the seller’s supported integration. The profile must describe who can redeem it and for what transaction, along with any required customer action. A token does not automatically work at every checkout, merchant, or processor.

Approval can pause and resume the same logical purchase. Profile tests must distinguish mock flows from processor-supported tests and authorized live evidence. Product access, fees, limits, and eligibility remain provider-specific; this standard does not freeze commercial terms.

## Evidence and network compensation

A processor-confirmed payment may be privately verifiable to the merchant; a signed adapter assertion identifies its attestor without becoming public processor proof. A blockchain receipt commitment neither settles a card charge nor prevents a chargeback. A future network-fee profile must explain reversals, who funds operator compensation, and any separate fiat-to-chain arrangement.

No payment profile is normative or implemented by this initial documentation package. See [conformance scenarios](../conformance/scenarios.md).
