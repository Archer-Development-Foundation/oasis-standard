# Transport profiles: REST and MCP

**Status:** Informative design requirements · v0.1.0-draft.1

The core contracts should be usable across different agent harnesses. Transport adapters map messages and errors; they do not independently redefine authority, spending policy, or outcome semantics.

## REST binding to specify

- Endpoint discovery from an authenticated descriptor, including HTTPS and redirect policy.
- Content types, method semantics, size limits, supported-version negotiation, and required-profile discovery.
- Authenticated request placement, response integrity, replay protection, and transport credentials.
- Quote/preparation, invocation, status, continuation, cancellation, and receipt retrieval operations.
- Mapping between transport errors and logical execution state; a disconnected response cannot establish that no effect occurred.
- Idempotency scope at the executor and provider, including response loss after commitment.

No header names or endpoint paths are allocated by this draft.

## MCP binding to specify

Map descriptor operations to tool discovery and invocation using a pinned [MCP specification](https://modelcontextprotocol.io/specification). Preserve schema and capability meaning, invocation identity, permission checks, continuations, and evidence across that mapping.

MCP transport authentication or a connected session does not itself authorize purchases. Tool descriptions and annotations are input to discovery and disclosure, not security authority. A generic tool result must not discard the permission or evidence fields needed by the client.

## Cross-transport acceptance

The same principal, descriptor, and bounded operation should produce equivalent permission decisions and attributable outcomes through each supported binding. A transport-specific implementation report must disclose unsupported behaviors; presenting an HTTP service through a tool wrapper alone is not conformance evidence.
