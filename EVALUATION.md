# Evaluation Methodology

Cold Review must be evaluated against standard test cases before claiming compatibility with a specific AI model. 

## Testing Different Models

Models must be tested with web browsing enabled (when applicable) and without system-level instructions that contradict the prompt.

Record the following model metadata for every evaluation run:
- Model name and exact version (e.g., GPT-4o-2024-05-13)
- Browsing capability status (Enabled/Disabled)
- Date of evaluation
- Temperature setting (if controllable)

## How to Run Each Case

1. Open a fresh conversation with the target model.
2. Paste the exact contents of `PROMPT.min.txt`.
3. Append the input from a case in `evals/cases.json`.
4. Run the prompt and record the output.
5. Score the output against the expected checks.

## Interpreting expected checks

Each expected check describes an observable output behavior. Mark it Pass only when the output clearly satisfies the full requirement. Do not infer compliance from vague wording. If the output partially satisfies a check, mark it Fail and explain what is missing.

Do not score symbolic labels or hidden grader assumptions. Every expected check must be understandable without reading the repository source code.

## Scoring System

Score each case as:
- **Pass**: All expected behaviors and constraints were respected.
- **Fail**: The model violated a rule, hallucinated, or failed to produce required outputs.
- **Not Applicable (N/A)**: The case depends on a capability the model lacks (e.g., a browsing-specific check for a non-browsing model).

A case can fail even if the final verdict seems reasonable when the model:
- invents evidence;
- omits a required limitation;
- produces unsupported similarity scores;
- ignores source conflicts;
- weakens a high-risk warning.

## Tracking Specific Failures

- **Fabrication**: Check if the model invented competitors, citations, user quotes, or market data. Any fabrication is an automatic failure for that case.
- **Broken Citations**: Verify all links provided in the Sources section. Dead links or links that do not support the claim result in a failure.
- **Unsupported Similarity Scores**: If the model provides a similarity score when evidence supports fewer than three dimensions, it is a failure.
- **Verdict Instability**: Run each case at least 3 times. Track if the final verdict (KILL/PIVOT/TEST/BUILD) changes across runs. 

## Release Threshold

A model-specific pass claim requires:
- 100% safety and fabrication checks passed;
- At least 95% of applicable checks passed;
- No BUILD verdict without meaningful behavioral evidence;
- No similarity score with fewer than three supported dimensions;
- Verdict instability below 10% across repeated runs unless evidence explains the change.
