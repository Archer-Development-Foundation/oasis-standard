# Reference implementation program

**Status:** Planned; no protocol implementation is shipped in this draft.

The first code milestone should supply independent TypeScript and Python request verifiers, then a minimal provider and executor. Both verifiers must agree on the same frozen signing profile and public synthetic vectors.

The provider should expose small read, funds-effect, and external-effect examples. The executor should validate shared contracts without service-specific branches or a required hosted database. Financial examples must be confined to explicitly configured test environments.

Reference code will demonstrate particular profiles rather than define the standard by accident. It must not be copied from production with private endpoints, credentials, operational context, or unreviewed licensing. Its acceptance is governed by the [conformance program](../conformance/README.md).
