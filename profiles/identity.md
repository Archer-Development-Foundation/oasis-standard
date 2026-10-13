# Identity profiles: control, delegation, and recovery

**Status:** Informative design requirements · v0.1.0-draft.1

The objective is user-controlled authority across compatible providers, including independent recovery and migration. Identity, an operator account, a merchant account, and a session credential are distinct objects.

| Candidate profile | Control model | Required design evidence |
| --- | --- | --- |
| Bare-key principal | Principal proves control of a key/account accepted by the selected profile | Proof format, resolver, audience/nonce/expiry checks, signature validation, rotation and recovery limits |
| Assisted principal | A recovery or custody mechanism assists the principal | Custodian powers, independent recovery/migration path, revocation, availability assumptions, record decryption after recovery |
| Operator-issued credential | A session credential resolves to a principal and bounded delegation | Issuer and audience, scope, expiration/revocation, underlying principal binding; no assumption of portability of the credential itself |

An Ethereum-specific candidate can use [CAIP-10](https://standards.chainagnostic.org/CAIPs/caip-10) for account identification and [Sign-In with Ethereum](https://eips.ethereum.org/EIPS/eip-4361) for authentication. Account naming and sign-in do not supply purchase consent, universal recovery, or a cross-chain delegation format. Other key and smart-account profiles remain possible.

An assisted profile must demonstrate the advertised fallback while the original operator is unavailable. Private-key export is one possible approach, not a mandatory design. Passkeys and email are interaction/recovery mechanisms whose actual custody and control assumptions need explanation.

## Required failure cases

- New principal with no account at the original platform.
- Wrong domain/audience, expired challenge, replayed proof, or substituted delegate.
- Rotated or revoked authority with outstanding delegated permissions.
- Original operator unavailable during recovery or migration.
- Recovered principal that also needs access to encrypted historical records.
- Lost key without an enrolled recovery mechanism: state the limit instead of implying recovery is guaranteed.

Persistent identifiers create correlation risks. A proposal should minimize cross-service disclosure and distinguish independent verification from publishing identity and purchase history globally.
