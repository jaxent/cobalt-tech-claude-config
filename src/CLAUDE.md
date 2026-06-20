# Cobalt Hospitality Tech — Source Code Rules
# Subdirectory override for /src
# Inherits all rules from root CLAUDE.md
# Only add src-specific rules here — do not repeat root rules

---

## Source Code Standards

### File Organization
Every module in /src must follow this structure:

    module_name/
        __init__.py
        models.py        — data models and schemas
        service.py       — business logic
        repository.py    — data access layer
        routes.py        — API endpoints (if applicable)
        tests/
            test_models.py
            test_service.py
            test_repository.py

Never mix business logic with data access.
Never put database queries in route handlers.

### Import Order
Follow this order strictly — enforced by isort:
1. Standard library
2. Third-party packages
3. Internal cobalt packages
4. Relative imports

### Connector Modules (/src/connectors/)
These modules interface with external PMS systems.
Extra rules apply:

- Every connector must implement the BasePMSConnector interface
- All external API calls must have explicit timeout values
- Retry logic required on all connector calls — use tenacity
- Circuit breaker pattern required for production connectors
- Never raise raw vendor exceptions — wrap in CobaltConnectorError
- Mock responses required in /src/connectors/mocks/ for every endpoint

### Agent Modules (/src/agents/)
These modules implement Claude-powered workflows.
Extra rules apply:

- Loop termination via stop_reason only — never prompt-based
- Maximum 5 tools per agent
- All tools must return structured error objects
- Escalation triggers must be programmatic — never sentiment-based
- Human review escalation required after 3 failed retries
- No guest PII in Claude conversation context beyond session scope

### Models (/src/models/)
- All models inherit from CobaltBaseModel
- Currency fields: integer cents only — field name must end in _cents
- DateTime fields: UTC only — field name must end in _utc
- PII fields: must be marked with pii=True in field metadata
- Soft deletes only — never hard delete guest or reservation records

### Services (/src/services/)
- All service methods must be stateless
- No direct database access — use repository layer
- All reservation mutations must be idempotent
- Return domain objects — never return raw database rows

---

## Plan Mode Required in /src/connectors/

Always use plan mode before modifying any connector:
- Changes here affect live PMS integrations
- A broken connector means reservations fail in production
- Two reviewers required on all connector PRs

---

## Testing in /src/

Test files live in tests/ subdirectory of each module.
Run the full test suite before any commit touching /src/:

    pytest src/ --cov=src --cov-report=term-missing

Coverage must not drop below 80% on commit.
PMS connector tests must use mocks — never hit live APIs.