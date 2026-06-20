# Cobalt Hospitality Tech — Claude Code Configuration Kit

A production-grade Claude Code configuration for hospitality technology 
development teams. Built and maintained by Cobalt Hospitality Tech.

## What's Included

- **Team CLAUDE.md** — Coding standards, MCP server connections, protected 
  file patterns, and non-negotiable compliance rules
- **Subdirectory overrides** — Context-specific rules for src/ and docs/
- **Slash commands** — Custom workflows for code review, ticket generation, 
  and deployment checks tuned for hospitality software
- **Personal config template** — Engineer preference layer that never 
  overrides team standards

## Directory Structure

- cobalt-tech/
- CLAUDE.md                    ← Team standards (commit this)
- .claude/
- commands/
- cobalt-review.md       ← /cobalt-review
- cobalt-ticket.md       ← /cobalt-ticket
- cobalt-deploy-check.md ← /cobalt-deploy-check
- src/
    - CLAUDE.md                ← Source code specific rules
- docs/
    - CLAUDE.md                ← Documentation specific rules


## Domains Covered

Implements patterns from the Claude Certified Architect exam:
- Domain 3: Claude Code Configuration & Workflows
- CLAUDE.md hierarchy and override model
- Custom slash commands and skills
- Plan mode guidance for production systems
- CI/CD integration patterns

## Target Users

- Hospitality technology development teams
- Hotel software integrators (Opera, Apaleo, Cloudbeds, Maestro)
- Resort IT departments standing up AI-assisted dev workflows
- Independent consultants building hospitality AI solutions

## Usage

1. Clone this repo into your project root
2. Copy `.claude/` directory to your project
3. Customize `CLAUDE.md` with your team's standards
4. Add personal preferences to `~/.claude/CLAUDE.md` (never commit)
5. Connect your internal MCP servers in the MCP configuration section

---

Built as part of Claude Certified Architect certification preparation.