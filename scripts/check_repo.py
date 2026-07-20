import os
import sys
import json
import re
from pathlib import Path

def main():
    repo_dir = Path(__file__).parent.parent
    errors = []

    required_files = [
        ".github/ISSUE_TEMPLATE/config.yml",
        ".github/ISSUE_TEMPLATE/improvement.md",
        ".github/ISSUE_TEMPLATE/prompt-problem.md",
        ".github/workflows/quality.yml",
        ".github/PULL_REQUEST_TEMPLATE.md",
        "evals/cases.json",
        "evals/results/README.md",
        "scripts/check_repo.py",
        "scripts/generate_min_prompt.py",
        "CHANGELOG.md",
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING.md",
        "EVALUATION.md",
        "EXAMPLE.md",
        "INPUT_TEMPLATE.md",
        "LICENSE",
        "PROMPT.md",
        "PROMPT.min.txt",
        "README.md",
        "RELEASE_CHECKLIST.md",
        "SECURITY.md",
        "SUPPORT.md"
    ]

    for req_file in required_files:
        if not (repo_dir / req_file).exists():
            errors.append(f"Missing required file: {req_file}")

    # PROMPT.md checks
    prompt_md_path = repo_dir / "PROMPT.md"
    if prompt_md_path.exists():
        prompt_content = prompt_md_path.read_text(encoding="utf-8")
        text_blocks = re.findall(r'```text\n(.*?)\n```', prompt_content, re.DOTALL)
        if len(text_blocks) != 1:
            errors.append(f"PROMPT.md contains {len(text_blocks)} text fenced blocks. Expected exactly 1.")

        required_prompt_headings = [
            "Cold Verdict", "What This Project Really Is", "Evidence Limits",
            "Competitor Comparison", "Best Case Against", "Best Case For",
            "What Is Actually Unique Here", "Evidence Audit", "Feedback Decoded",
            "The Real Gap", "Biggest Risk", "How to Make It Successful",
            "What to Avoid", "Cheapest Real Test", "Kill Condition",
            "Final Decision", "Next Move", "Sources"
        ]

        for heading in required_prompt_headings:
            if f"# {heading}" not in prompt_content:
                errors.append(f"PROMPT.md missing required heading: # {heading}")

        retired_rules = [
            "evidence coverage is below 40%",
            "confidence percentage",
            "3-5 competitors",
            "3–5 competitors"
        ]
        for rule in retired_rules:
            if rule.lower() in prompt_content.lower():
                errors.append(f"PROMPT.md contains retired rule: {rule}")

        required_prompt_texts = [
            "Competitor research could not be performed",
            "do not present unverified competitor claims as facts",
            "do not invent citations or similarity scores",
            "what can be ethically adapted",
            "do not recommend copying names, visual identity, proprietary content"
        ]
        for text in required_prompt_texts:
            if text.lower() not in prompt_content.lower():
                errors.append(f"PROMPT.md missing required text: '{text}'")

    # EXAMPLE.md checks
    example_md_path = repo_dir / "EXAMPLE.md"
    if example_md_path.exists():
        example_content = example_md_path.read_text(encoding="utf-8")

        for heading in required_prompt_headings:
            if f"# {heading}" not in example_content:
                errors.append(f"EXAMPLE.md missing required heading: # {heading}")

        if "No external sources were available" not in example_content:
            errors.append("EXAMPLE.md missing required text: 'No external sources were available'")

        if re.search(r'\b\d{1,3}%\s+confidence', example_content, re.IGNORECASE):
            errors.append("EXAMPLE.md contains numeric confidence percentages.")

        if "Similarity unavailable" not in example_content:
            errors.append("EXAMPLE.md must show 'Similarity unavailable' for weak evidence.")

        if "Why someone would switch: Saves time and reduces end-of-day guilt" in example_content:
            errors.append("EXAMPLE.md contains the unsupported switch benefit claim.")
    # LICENSE checks
    license_path = repo_dir / "LICENSE"
    if license_path.exists():
        license_content = license_path.read_text(encoding="utf-8")
        if "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND" not in license_content:
            errors.append("LICENSE does not contain the canonical MIT warranty paragraph.")

    # Evals checks
    cases_path = repo_dir / "evals" / "cases.json"
    if cases_path.exists():
        try:
            cases_data = json.loads(cases_path.read_text(encoding="utf-8"))
            if len(cases_data) < 20:
                errors.append(f"evals/cases.json contains {len(cases_data)} cases. Expected at least 20.")

            seen_ids = set()
            for i, case in enumerate(cases_data):
                for key in ["id", "title", "input", "expected_checks"]:
                    if key not in case:
                        errors.append(f"evals/cases.json case {i} missing key: {key}")
                if "id" in case:
                    if case["id"] in seen_ids:
                        errors.append(f"evals/cases.json contains duplicate ID: {case['id']}")
                    seen_ids.add(case["id"])

                if not case.get("input", "").strip():
                    errors.append(f"evals/cases.json case {case.get('id')} has empty input.")
                if not case.get("title", "").strip():
                    errors.append(f"evals/cases.json case {case.get('id')} has empty title.")

                checks = case.get("expected_checks", [])
                if len(checks) < 3:
                    errors.append(f"evals/cases.json case {case.get('id')} has fewer than 3 expected checks.")
                for check in checks:
                    if not check.strip():
                        errors.append(f"evals/cases.json case {case.get('id')} has an empty expected check.")
                    elif len(check) < 20:
                        errors.append(f"evals/cases.json case {case.get('id')} has an expected check shorter than 20 characters: '{check}'")
                    elif " " not in check:
                        errors.append(f"evals/cases.json case {case.get('id')} has an expected check with no spaces: '{check}'")
                    elif re.match(r'^[a-z0-9_-]+$', check):
                        errors.append(f"evals/cases.json case {case.get('id')} has a symbolic-only expected check: '{check}'")
        except json.JSONDecodeError:
            errors.append("evals/cases.json is not valid JSON.")

    if errors:
        print("Repository validation failed:")
        for err in errors:
            print(f" - {err}")
        sys.exit(1)
    else:
        print("Repository validation passed.")

if __name__ == "__main__":
    main()
