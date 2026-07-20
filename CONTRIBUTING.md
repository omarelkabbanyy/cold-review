# Contributing to Cold Review

Cold Review should become more useful, more evidence-bound, and easier to act
on—not merely harsher.

## Ways to contribute

- Open an Issue describing a weak, misleading, or unsupported output.
- Suggest a clearer rule or output section.
- Add a small test case showing where the prompt fails.
- Fork the repository and submit a pull request with an improvement.

Nobody can directly change the official prompt without the repository owner
accepting the proposal.

## How to submit a change

1. Fork the repository.
2. Edit the readable source in `PROMPT.md`.
3. Never edit `PROMPT.min.txt` manually; run the generation script (`python scripts/generate_min_prompt.py`) after changing `PROMPT.md`.
4. Add or update an example when behavior changes.
5. Explain the failure mode and why your change fixes it.
6. Open a pull request.

## Good contributions

- Reduce unsupported certainty.
- Improve evidence and citation requirements.
- Make similarity calculations more defensible.
- Distinguish meaningful uniqueness from different wording.
- Produce cheaper and more falsifiable tests.
- Improve browsing safety.
- Shorten the output without removing decisive reasoning.

## Changes we will not accept

- Theatrical cruelty or insults.
- Generic startup advice.
- Invented market data or citations.
- False precision.
- Treating every missing feature as a market opportunity.
- Encouraging users to copy competitors rather than understand them.
- Hidden promotion, affiliate links, or SEO spam.

## Pull-request checklist

- [ ] `PROMPT.min.txt` was regenerated automatically.
- [ ] New certainty is supported by an evidence rule.
- [ ] The change does not weaken browsing-safety instructions.
- [ ] The change does not confuse missing evidence with negative evidence.
- [ ] The example still matches the prompt behavior.
- [ ] The reason for the change is explained clearly.

