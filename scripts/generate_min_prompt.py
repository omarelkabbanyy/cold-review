import argparse
import re
import sys
from pathlib import Path

def extract_prompt(content: str) -> str:
    # Find all text code blocks
    matches = re.findall(r'```text\n(.*?)\n```', content, re.DOTALL)
    
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one ```text block in PROMPT.md, found {len(matches)}")
        
    prompt_text = matches[0]
    
    # Collapse whitespace into one line
    # Replace multiple whitespaces/newlines with a single space
    minified = re.sub(r'\s+', ' ', prompt_text).strip()
    return minified

def main():
    parser = argparse.ArgumentParser(description="Generate PROMPT.min.txt from PROMPT.md")
    parser.add_argument("--check", action="store_true", help="Check if PROMPT.min.txt matches the generated output")
    args = parser.parse_args()

    repo_dir = Path(__file__).parent.parent
    prompt_md_path = repo_dir / "PROMPT.md"
    prompt_min_path = repo_dir / "PROMPT.min.txt"

    if not prompt_md_path.exists():
        print(f"Error: {prompt_md_path} does not exist.")
        sys.exit(1)

    content = prompt_md_path.read_text(encoding="utf-8")
    
    try:
        minified = extract_prompt(content)
    except Exception as e:
        print(f"Error extracting prompt: {e}")
        sys.exit(1)

    if args.check:
        if not prompt_min_path.exists():
            print("Error: PROMPT.min.txt does not exist but --check was requested.")
            sys.exit(1)
            
        current_minified = prompt_min_path.read_text(encoding="utf-8").strip()
        if current_minified != minified:
            print("Error: PROMPT.min.txt does not match the generated output from PROMPT.md.")
            print("Run python scripts/generate_min_prompt.py to update it.")
            sys.exit(1)
        else:
            print("Check passed: PROMPT.min.txt matches PROMPT.md.")
    else:
        prompt_min_path.write_text(minified + "\n", encoding="utf-8")
        print("Generated PROMPT.min.txt successfully.")

if __name__ == "__main__":
    main()
