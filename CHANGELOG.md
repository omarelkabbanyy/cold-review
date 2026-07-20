# Changelog

All notable changes to Cold Review are documented here.

## 1.1.1 — 2026-07-20

- Restored the explicit no-browsing competitor-research rule.
- Prevented unverified competitor claims, citations, and similarity scores when browsing is unavailable.
- Restored stronger competitor-learning and ethical-adaptation instructions.
- Expanded competitor output to include what can be ethically adapted.
- Reworked evaluation cases into clear, observable Pass/Fail checks.
- Corrected an unsupported benefit claim in the illustrative example.
- Strengthened repository validation for prompt rules and evaluation quality.
- Clarified how expected evaluation checks must be scored.

## 1.1.0 — 2026-07-20

- Positioned as a beta release.
- Replaced unsupported confidence percentages with High/Medium/Low.
- Added defined evidence-coverage levels (HIGH/MEDIUM/LOW).
- Withheld similarity scores when evidence is weak (fewer than 3 dimensions supported).
- Removed forced 3-5 competitor minimums.
- Condensed competitor output into a single compact table.
- Added Evidence Audit section.
- Added high-risk project checks.
- Expanded input template.
- Corrected the example.
- Added automated prompt generation script.
- Added repository validation script.
- Added 20-case evaluation suite.
- Added GitHub Actions workflow for CI.
- Added governance and security documentation.
- Corrected the MIT license.

## 1.0.0 — 2026-07-19

- Added a readable prompt source and separate minified copy.
- Made similarity percentages auditable with component scores.
- Added evidence coverage and confidence requirements.
- Added a refusal to score when evidence coverage is too low.
- Added browsing and prompt-injection safety rules.
- Added a balanced best-case-against and best-case-for pass.
- Added project-type evaluation lenses.
- Added an input template and illustrative example.
- Added clearer contribution requirements.

