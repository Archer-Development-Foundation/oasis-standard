# Contributing

Independent implementers, researchers, service providers, and users are welcome. Begin with the [specification index](specs/README.md), [open questions](research/OPEN-QUESTIONS.md), and [governance](GOVERNANCE.md).

## Choose the contribution

- **Clarification or editorial fix:** open a focused pull request explaining the ambiguity.
- **Protocol or profile change:** use the [ASIP template](asips/ASIP-template.md) and [process](asips/ASIP-0000-process.md).
- **Counterexample or security property:** identify the requirement, assumptions, failure mode, and a minimal synthetic scenario.
- **Implementation evidence:** use the [report template](conformance/REPORT-TEMPLATE.md), naming exact revisions, profile coverage, and untested behavior.

Keep core contracts generic. A new service should provide a descriptor and supported binding rather than require a new branch in every executor. Product-specific tutorials and policies belong with their implementations.

## Public contribution hygiene

All issues, pull requests, examples, and commit history in this repository are public. Use synthetic data and reserved example domains. Do not submit secrets, real customer records, personal agent context, internal planning notes, private correspondence, unpublished partner details, or private infrastructure references. Review both file contents and commit metadata before pushing; a GitHub noreply address can avoid publishing a personal email.

Do not post exploitable vulnerabilities or sensitive evidence in public issues. Follow [SECURITY.md](SECURITY.md).

## Review checklist

- Identify whether text is proposed normative, informative, or a tested implementation claim.
- Explain compatibility, security, privacy, recovery, and failure behavior.
- Bind economic or permission changes to explicit consent and supported profiles.
- Add or update a conformance scenario for changes in required behavior.
- Cite primary specifications and pin versions before making interoperability claims.
- Update the changelog for substantive changes; retain unresolved questions honestly.
- Run `python3 tools/check_repository.py` and `git diff --check`.

## Rights and conduct

Submit only material you have the right to contribute. Unless explicitly excluded before submission, contributions are made under the repository’s [Apache-2.0 license](LICENSE); its terms govern contributions. Do not claim a patent commitment on behalf of an employer or another party. See [PATENTS.md](PATENTS.md) and the [code of conduct](CODE_OF_CONDUCT.md).

No personal biography, institutional affiliation, real-name signature, or customer evidence is required to propose a technical improvement.
