# Personal Claude Code Configuration Template
# Palms Technology Group
#
# INSTRUCTIONS:
# 1. Copy this file to ~/.claude/CLAUDE.md on your machine
# 2. Customize the sections below to your preferences
# 3. NEVER commit this file — it stays on your machine only
# 4. Personal preferences here CANNOT override team rules in
#    the project CLAUDE.md — they only add to them
#
# Location: ~/.claude/CLAUDE.md

---

## My Preferences
# Customize these — examples provided

# Response style
- Be concise — I prefer shorter responses unless I ask for detail
- Show me the code first, explain after
- When I ask for options, give me max 3 with a recommendation

## My Development Setup
# Tell Claude about your local environment

- OS: Windows 11 / PowerShell
- Python version: 3.14
- Primary IDE: Cursor + Claude Code
- Terminal: PowerShell
- Git workflow: feature branches, squash merge to main

## My Expertise Areas
# Claude will calibrate explanations to your level

- Strong: Python, REST APIs, SQL, hospitality domain
- Familiar: TypeScript, Docker, CI/CD
- Learning: Async Python, MCP server development, agentic patterns

## My Preferred Workflows

### Starting a new feature
1. Check Jira for ticket details first
2. Create feature branch from main
3. Write tests before implementation (TDD)
4. Run /palm-review before PR

### Debugging
- Show me the error and relevant code together
- Suggest most likely cause first
- Give me the fix, not just the diagnosis

### Code generation
- Match the style of existing code in the project
- Include type hints always
- Include docstrings on public functions
- Flag anything that might need a migration

## Personal MCP Servers
# Add any personal MCP servers you run locally
# These are in addition to team MCP servers in project CLAUDE.md

# Example:
# - local-db-inspector — connects to my local dev database

---

## Notes to Self
# Personal reminders — Claude will see these

# - Check PCI compliance on anything touching payment flows
# - Always verify property timezone on date display
# - Ask about idempotency on any reservation mutation