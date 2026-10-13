# ASIP-0000: Improvement proposal process

**Version:** 0.1.0-draft.1

**Status:** Bootstrap process

**Editors:** Repository maintainers

**Updated:** 2026-10-13

ASIP means **Agent Systems Improvement Proposal**. It records a proposed change and its reasoning; an accepted proposal does not by itself ratify a standard.

## Workflow

1. **Discuss:** open an issue describing the problem, affected contracts, and known alternatives. Small editorial corrections can go directly to a pull request.
2. **Draft:** copy the [template](ASIP-template.md). Use a descriptive filename while the number is unassigned; maintainers allocate the next available number when the proposal is ready for review.
3. **Review:** publish complete requirements, compatibility and security analysis, unresolved points, and test implications. Allow at least 14 calendar days for substantive public review unless a documented security correction needs expedited handling.
4. **Decide:** maintainers record acceptance, rejection, withdrawal, or a request for revision, with rationale and material objections. No response is not approval.
5. **Integrate:** update affected documents, status/version metadata, scenarios, registries or schemas where applicable, and the changelog together.
6. **Demonstrate:** implementation reports establish whether the proposed behavior works. The [governance lifecycle](../GOVERNANCE.md) controls promotion beyond drafts.

## Proposal states

Draft → Review → Accepted / Rejected / Withdrawn. An accepted proposal can later be Superseded through another proposal. Preserve its record and link its replacement.

An editor can improve wording without claiming working-group consensus. Governance changes, normative behavior, cryptographic profiles, and patent policies require substantive review rather than an editorial shortcut.

## Public record

Use public issue and pull-request references. Include synthetic examples and primary references; exclude internal discussions, unpublished correspondence, credentials, personal context, and private infrastructure details. Contributors may use a public handle rather than personal contact information.
