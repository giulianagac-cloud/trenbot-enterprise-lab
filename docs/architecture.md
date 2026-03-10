# Architecture Overview

## Intent

TrenBot Enterprise is structured as an enterprise-ready conversational platform foundation, not as a single-purpose chatbot. The current implementation keeps the runtime simple while preserving the boundaries needed for future platform growth.

## Current Building Blocks

### Frontend

- Next.js App Router application for the employee-facing interface
- reusable chat UI components for app pages and Storybook
- MSW-based mock API layer for independent UI development

### Backend

- FastAPI HTTP layer for health and chat APIs
- conversation orchestrator as the main composition boundary
- flow engine placeholder for guided HR journeys
- in-memory session store placeholder for conversation state

### Shared

- request and response contracts prepared for future backend/frontend synchronization

## Design Principles

- Keep runtime dependencies low and understandable
- separate domain boundaries early
- make future adapters additive rather than invasive
- prefer configuration and composition over hard-coded flow logic

## Evolution Path

### Near-term

- add more HR flow definitions
- persist conversation sessions
- introduce authentication and role context
- enrich chat responses with citations and metadata

### Mid-term

- orchestration layer for tool selection and response planning
- knowledge layer for policy search and retrieval
- Redis for active session storage
- PostgreSQL for persistence and audit trails

### Future Enterprise Expansion

- SAP adapter layer for transactional actions
- approval workflows and audit logging
- analytics and observability
- multi-channel support

## Why This Structure Works

- `api` contains transport concerns only.
- `services` coordinates the application behavior.
- `domain` models conversation behavior independently from transport and storage.
- `infrastructure` isolates implementation details such as logging and session storage.

This separation keeps the project presentable today while making future enterprise additions straightforward.

