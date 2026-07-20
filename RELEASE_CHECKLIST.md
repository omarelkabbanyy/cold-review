# Release Checklist

Before tagging and publishing a new release, ensure the following requirements are met:

- [ ] Version consistency across `README.md`, `PROMPT.md`, `CHANGELOG.md`, and issue templates.
- [ ] Generated prompt parity: `PROMPT.min.txt` exactly matches `PROMPT.md` without formatting errors.
- [ ] Repository validation checks passing locally (`python scripts/check_repo.py`).
- [ ] GitHub Actions CI workflows passing on `main`.
- [ ] `EXAMPLE.md` behavior accurately reflects the latest rules in the prompt.
- [ ] Evaluation results run and passed against target models according to `EVALUATION.md` requirements.
- [ ] `README.md` claim accuracy confirmed (no unsupported pass rates or fabricated capabilities).
- [ ] `CHANGELOG.md` updated with the new version, date, and significant changes.
- [ ] Release tag created matching the version (e.g., `v1.1.0`).
