# Schema work

**Status:** Planned; no normative JSON Schemas published in this draft.

The next proposal should define versioned schemas for service descriptors, requests, envelopes, authorizations, delegations, quotes, effect reports, instrument descriptions, receipts, and record updates.

Before schemas become a conformance target:

- Agree exact field names, required fields, units, formats, null/absence semantics, and extension policy.
- Pin a JSON Schema dialect and validator behavior, including referenced-resource resolution and format assertions.
- Define canonical signing separately from structural validation; schema success is not signature or authorization validity.
- Validate positive and negative fixtures across independent implementations.
- Bind every schema and fixture set to its document revision and compatibility policy.

Semantic tables in the [specifications](../specs/README.md) are review material, not wire schemas. Publishing placeholders that accept arbitrary input would not make the protocol implementable.
