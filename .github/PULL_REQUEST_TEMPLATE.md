## What changed
(Describe the changes introduced by this pull request.)

## Failure mode
(What was the prompt doing wrong before this PR?)

## Why the fix is better
(Explain why this approach solves the problem robustly.)

## Validation
(How was this validated against the evaluation suite?)

## Tradeoffs
(Are there any downsides to this change? e.g. longer output, stricter rules that might cause false negatives.)

## Checklist
- [ ] Updated `PROMPT.md`
- [ ] Regenerated `PROMPT.min.txt` using the generation script
- [ ] Added or updated an evaluation case in `evals/cases.json`
- [ ] Updated `EXAMPLE.md` when needed
- [ ] Ran repository checks (`python scripts/check_repo.py`)
- [ ] Preserved browsing-safety rules
- [ ] Documented tradeoffs
