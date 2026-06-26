#!/bin/bash
# Cobalt CI Review Prompt Script
# Reads the diff from pr_diff.txt and runs Claude Code review

DIFF_CONTENT=$(cat pr_diff.txt)

claude -p \
  --output-format json \
  --max-turns 3 \
  "You are running as part of the Cobalt Hospitality Tech CI pipeline.
Review this PR diff against our CLAUDE.md hospitality standards.

PR #${PR_NUMBER}
Title: ${PR_TITLE}
Author: ${PR_AUTHOR}
Base branch: ${BASE_REF}

DIFF:
${DIFF_CONTENT}

Run these checks:
1. Security (blocking): hardcoded secrets, PII in logs, SQL injection, PCI surface
2. Hospitality domain (blocking): currency as cents, UTC dates, idempotent reservations, no live PMS calls in tests
3. Code quality (warning): function length over 50 lines, error object shape, docstrings, type hints
4. Test coverage (warning): new code has tests, 80% coverage floor

Output ONLY a JSON object with this exact structure, no other text:
{
  \"verdict\": \"APPROVE or APPROVE_WITH_NOTES or REQUEST_CHANGES\",
  \"blocking_issues\": [\"issue 1\", \"issue 2\"],
  \"warnings\": [\"warning 1\"],
  \"suggestions\": [\"suggestion 1\"],
  \"summary\": \"one sentence summary\"
}"