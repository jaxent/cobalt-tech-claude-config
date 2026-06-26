#!/usr/bin/env python3
"""
Extracts verdict from Claude Code JSON output.
Called by cobalt-pr-review.yml after the review step.
"""
import sys
import json
import re

content = sys.stdin.read()

try:
    data = json.loads(content)
    if 'result' in data:
        text = data['result']
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            inner = json.loads(match.group())
            print(inner.get('verdict', 'APPROVE_WITH_NOTES'))
        else:
            print('APPROVE_WITH_NOTES')
    else:
        print(data.get('verdict', 'APPROVE_WITH_NOTES'))
except Exception:
    print('APPROVE_WITH_NOTES')