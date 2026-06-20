# Cobalt Hospitality Tech — Documentation Rules
# Subdirectory override for /docs
# Inherits all rules from root CLAUDE.md

---

## Documentation Standards for /docs

This directory contains developer-facing documentation that lives
with the codebase. It is the source of truth for API references,
integration guides, and code-level architecture notes.

For architectural decisions, operational runbooks, and user guides
see Confluence. Do not duplicate content between GitHub and Confluence.

---

## What Lives Here

    docs/
        api/             — API reference (auto-generated + hand-written)
        guides/          — Integration guides for PMS connectors
        examples/        — Working code examples with explanations
        adr/             — Architecture Decision Records index
            README.md    — Links to full ADRs in Confluence
        changelog/       — Per-module changelogs

## What Does NOT Live Here

- Operational runbooks → Confluence Operations Space
- User guides → Confluence Product Space  
- Incident post-mortems → Confluence Operations Space
- Meeting notes → Confluence

---

## Writing Standards

- Write for a developer integrating with our systems
- Assume familiarity with REST and Python/TypeScript
- Do not assume familiarity with hospitality domain — define terms
- Every code example must be tested and runnable
- No screenshots — use code blocks and text diagrams only
- American English spelling

### Hospitality Terms to Define on First Use

Always define these on first use in any document:
- PMS (Property Management System)
- ADR (Average Daily Rate) — not to be confused with Architecture Decision Record
- RevPAR (Revenue Per Available Room)
- OTA (Online Travel Agency)
- GDS (Global Distribution System)
- POS (Point of Sale)
- Folio (guest billing record)

---

## API Documentation Requirements

Every public API endpoint must have:
- Description of what it does
- Request parameters with types and constraints
- Response schema with all fields documented
- Error responses — all possible error codes
- Working curl example
- Rate limit information

New endpoints must be documented before or in the same PR as the code.
Undocumented endpoints will be rejected in /cobalt-review.

---

## ADR Index (docs/adr/README.md)

Keep this index current. Format:

| ADR | Title | Status | Date | Confluence Link |
|---|---|---|---|---|
| ADR-0001 | Use MCP for tool integration | Accepted | 2026-06-15 | [Link] |
| ADR-0002 | Integer cents for currency | Accepted | 2026-06-15 | [Link] |

---

## Changelog Format

Per-module changelogs follow Keep a Changelog format:
https://keepachangelog.com

Sections: Added, Changed, Deprecated, Removed, Fixed, Security
Version format: Semantic versioning (MAJOR.MINOR.PATCH)