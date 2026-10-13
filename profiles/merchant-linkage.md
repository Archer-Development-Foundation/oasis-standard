# Merchant linkage and consent

**Status:** Informative design requirements · v0.1.0-draft.1

A portable principal may still need merchant authorization to access an account, reservation, cart, subscription, or other protected resource. The standard should describe that relationship without claiming every merchant supports common sign-in or transferable credentials.

A linkage proposal should define:

- Issuer, principal, merchant/service, intended executor audience, granted scopes, validity, and revocation.
- The supported authorization mechanism and proof that the issuer can grant access.
- A safe linking or additional-approval continuation tied to the intended operation.
- Credential storage, least-privilege delivery, renewal, and revocation behavior.
- Whether another executor can use delegated access or must request reauthorization.
- What happens to in-flight work and records after unlinking.

Identity portability and merchant linkage are separate conformance claims. Recovery of a principal must not silently reactivate an expired merchant grant. Merchant API tokens and personal customer data do not belong in public descriptors, test reports, or examples.
