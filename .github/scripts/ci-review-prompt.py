#!/usr/bin/env python3
"""
Cobalt CI Review Prompt Script
Reads PR diff and runs Claude Code review.
"""
import subprocess
import os
import sys

# Read the diff
try:
    with open('pr_diff.txt', 'r') as f:
        diff_content = f.read()
except FileNotFoundError:
    diff_content = "No diff file found."

pr_number = os.environ.get('PR_NUMBER', 'unknown')
pr_title = os.environ.get('PR_TITLE', 'unknown')
pr_author = os.environ.get('PR_AUTHOR', 'unknown')
base_ref = os.environ.get('BASE_REF', 'main')

prompt = f"""You are running as part of the Cobalt Hospitality Tech CI pipeline.
Review this PR diff against our CLAUDE.md hospitality standards.

PR #{pr_number}
Title: {pr_title}
Author: {pr_author}
Base branch: {base_ref}

DIFF:
{diff_content}

Run these checks:
1. Security (blocking): hardcoded secrets, PII in logs, SQL injection, PCI surface
2. Hospitality domain (blocking): currency as cents, UTC dates, idempotent reservations, no live PMS calls in tests
3. Code quality (warning): function length over 50 lines, error object shape, docstrings, type hints
4. Test coverage (warning): new code has tests, 80% coverage floor

Output ONLY a JSON object with this exact structure, no other text:
{{
  "verdict": "APPROVE or APPROVE_WITH_NOTES or REQUEST_CHANGES",
  "blocking_issues": ["issue 1", "issue 2"],
  "warnings": ["warning 1"],
  "suggestions": ["suggestion 1"],
  "summary": "one sentence summary"
}}"""

result = subprocess.run(
    ['claude', '-p', '--output-format', 'json', '--max-turns', '3'],
    input=prompt,
    capture_output=True,
    text=True
)

if result.returncode != 0:
    print(f"Claude Code error: {result.stderr}", file=sys.stderr)
    sys.exit(1)

print(result.stdout)