# References and relationships

These are design precedents and candidate dependencies, not endorsements or completed integrations. A future normative profile must pin the exact revision it depends on. This draft imports no external protocol wholesale.

| Source | Relevance and boundary |
| --- | --- |
| [x402](https://github.com/x402-foundation/x402) | Payment protocol structure and separation of schemes, networks, and transports; a candidate payment binding |
| [Machine Payments Protocol](https://mpp.dev/) and [Stripe MPP](https://docs.stripe.com/payments/machine/mpp) | Candidate agent-payment and card-token integration paths; issuer and merchant support remain dependencies |
| [EIP-6963](https://eips.ethereum.org/EIPS/eip-6963) | Precise multi-provider discovery and security behavior for injected wallets; not a global agent-service registry |
| [ERC-3643](https://eips.ethereum.org/EIPS/eip-3643) | Modular identity/compliance interfaces for permissioned tokens; not this standard’s default access model |
| [ERC-8004](https://eips.ethereum.org/EIPS/eip-8004) | Identity, reputation, and validation interfaces to evaluate; registry entries do not establish credible fulfillment evidence |
| [MCP specification](https://modelcontextprotocol.io/specification) | A candidate tool/transport binding, distinct from principal payment authority |
| [CAIP-10](https://standards.chainagnostic.org/CAIPs/caip-10) and [CAIP-19](https://standards.chainagnostic.org/CAIPs/caip-19) | Account and asset identification candidates |
| [EIP-4361 / SIWE](https://eips.ethereum.org/EIPS/eip-4361) | Ethereum account authentication; sign-in is not delegated spending consent |
| [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785) | Candidate canonical JSON encoding for interoperable signatures |
| [RFC 8174 / BCP 14](https://www.rfc-editor.org/rfc/rfc8174) | Interpretation of uppercase requirement terms |
| [W3C Process](https://www.w3.org/policies/process/) | Public review, document states, and implementation evidence as process precedents; no W3C affiliation or adoption is implied |
| [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) | Repository reuse terms; see the separate patent-policy disclosure |

External projects retain their own governance, licenses, and trademarks. Compatibility requires a profile and evidence rather than a reference link.
