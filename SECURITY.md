# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.1.0   | :white_check_mark: |
| 1.0.0   | :x:                |

## Scope

Cold Review is a text prompt, not executable software. Security concerns involve prompt injection, unauthorized external actions, and fabricated evidence by the AI models running the prompt.

We address:
- Prompt injection and hidden instructions within external sources.
- Prevention of unsafe external actions (executing commands, downloading files, contacting individuals).
- Prevention of fabricated citations and invented evidence.
- High-risk project safety and required expert review.
- Ensuring the prompt itself does not contain or request automation secrets.

## Reporting a Vulnerability

If you discover a prompt vulnerability that causes a model to consistently ignore safety constraints, execute unsafe actions, or confidently recommend dangerous behavior for high-risk projects, please do not open a public issue.

Send a private report outlining the model used, the input provided, the exact failure mode, and the steps to reproduce it to the repository maintainers.
