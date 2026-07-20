# Cold Review

> A second opinion with no emotional investment.

Current version: v1.1.0 beta.

Cold Review is an evidence-first AI prompt for early-stage businesses, apps,
products, services, and content projects. Cold Review instructs browsing-capable AI systems to research competitors. It makes similarity scores auditable, separates real differentiation
from different wording, decodes feedback, and ends with a direct decision:
**Kill, Pivot, Test, or Build**.

## Why it is different

- **Evidence before confidence.** Facts, inferences, hopes, and unknowns are
  labeled instead of blended together.
- **Auditable competitor scores.** Every similarity percentage shows its
  component scores, evidence coverage, and confidence.
- **Useful competitor lessons.** It explains what each competitor owns, what is
  genuinely unique, what can be learned, and how that lesson helps your project.
- **No imaginary market gaps.** Opportunities are marked Verified, Supported,
  or Hypothesis.
- **Balanced pressure testing.** It makes the strongest case against the
  project and the strongest case for it before deciding.
- **Action over encouragement.** Every review ends with a falsifiable test, a
  kill condition, and one immediate move.

## Limitations

Cold Review is decision support and does not replace:
- market validation;
- legal review;
- financial review;
- safety review;
- security review.

Results depend on:
- model quality;
- browsing access;
- source availability;
- citation accuracy;
- input quality.

## Quick start

1. Open [`PROMPT.min.txt`](PROMPT.min.txt).
2. Copy the complete line.
3. Paste it into an AI with web research enabled.
4. Add your project using [`INPUT_TEMPLATE.md`](INPUT_TEMPLATE.md).

Prefer readable instructions? Use [`PROMPT.md`](PROMPT.md). Both versions carry
the same behavior; `PROMPT.md` is the source contributors should edit.

## What to give it

- What you are making.
- Who it is for.
- The problem it solves.
- How it works.
- Evidence you already have.
- Feedback you received.
- Your time, money, skill, and distribution constraints.
- The decision you are trying to make.

The more concrete the evidence, the more reliable the verdict.

## What you get

- A direct cold verdict.
- Researched competitors with dated citations.
- A transparent similarity calculation for each competitor.
- What is genuinely unique about every competitor and your project.
- What you can learn and ethically adapt from each competitor.
- A balanced case against and for the project.
- Feedback separated into signal, noise, and contradiction.
- A defensible market gap—or an honest admission that none was found.
- Project-specific success moves and expensive mistakes to avoid.
- The cheapest real test, a kill condition, and one next move.

See [`EXAMPLE.md`](EXAMPLE.md) for a compact illustrative review.

## Validation

The repository checks validate consistency, not model accuracy. Automated scripts ensure prompt parity and the presence of rules, but do not imply a model pass rate.

## Files

| File | Purpose |
| --- | --- |
| [`PROMPT.md`](PROMPT.md) | Readable source of truth |
| [`PROMPT.min.txt`](PROMPT.min.txt) | One-line copy version |
| [`INPUT_TEMPLATE.md`](INPUT_TEMPLATE.md) | Project submission template |
| [`EXAMPLE.md`](EXAMPLE.md) | Illustrative input and output |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to propose improvements |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history |
| [`SECURITY.md`](SECURITY.md) | Security policies and reporting |
| [`SUPPORT.md`](SUPPORT.md) | Support and usage help |
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | Code of conduct |
| [`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md) | Checklist for releases |
| [`EVALUATION.md`](EVALUATION.md) | Evaluation methodology |
| `scripts/` | Validation and automation scripts |
| `evals/` | Evaluation cases and results |

## Design principle

Cold Review is brutal toward the project and respectful toward the person. It
does not perform cruelty, invent research, confuse missing evidence with
negative evidence, or turn unsupported assumptions into confident advice.

## Contributing

Issues and pull requests are welcome. The official prompt changes only when the
repository owner accepts a proposal. Read
[`CONTRIBUTING.md`](CONTRIBUTING.md) before suggesting a change.

## Support the project

If Cold Review helps you make a better decision, **star the repository** so
more builders can find it.

## License

Licensed under the MIT License.
