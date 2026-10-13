# Value registries

**Status:** Registration policy proposal; no wire values allocated yet.

The core draft names candidate capability and assessment concepts. Their wire representation and versioning require an accepted proposal. Product-specific enum labels do not automatically become protocol assignments.

Future registries should cover capabilities, authorization types, profile identifiers, fee models, settlement timing, evidence categories, and error codes. Chain and asset identifiers should reuse suitable existing standards through explicit profiles rather than creating ambiguous local aliases.

## Proposed registration policy

Each entry needs a stable identifier, definition, normative dependency, version/status, security considerations, owner or maintenance process, and test coverage. Public proposals and recorded decisions allocate values. Deprecated assignments remain documented and are not silently repurposed.

Experimental extensions need collision-resistant names and a declaration of whether their semantics are required. An optional namespace must never weaken a mandatory security or economic constraint. Unsupported required values follow [CORE-04](../specs/OASIS-0001-core.md).
