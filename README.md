# TrenBot Enterprise

TrenBot Enterprise is a professional starter foundation for an internal HR conversational platform. It is designed to support guided HR flows today while preparing the architecture for future enterprise capabilities such as orchestration, knowledge retrieval, SAP-connected tools, and persistent session management.

## Goals

- Build a configurable conversational platform with a clear enterprise architecture.
- Provide a mobile-first employee-facing chat experience.
- Enable UI iteration independent of the backend through Storybook and MSW.
- Keep the codebase clean, modular, and credible as a portfolio and internal demo project.

## Repository Structure

```text
trenbot-enterprise/
├── apps/
│   ├── backend/      # FastAPI service
│   └── frontend/     # Next.js app router application
├── docs/             # Architecture and product notes
├── infra/            # Future infrastructure placeholders
└── shared/           # Shared contracts and types
```

## Architecture Summary

- `apps/backend` exposes a lightweight FastAPI API with clear separation between routing, orchestration, flow logic, and session management.
- `apps/frontend` provides a mobile-first internal HR assistant interface using reusable chat components.
- `shared/contracts` contains shared request/response models for future contract synchronization between backend and frontend.
- `docs/architecture.md` explains how the foundation can evolve toward SAP integration, orchestration, RAG, Redis, and PostgreSQL without forcing early complexity.

## Backend

Features included:

- FastAPI starter application
- `GET /health`
- `POST /chat`
- modular package layout
- placeholder conversation orchestrator
- placeholder flow engine
- placeholder session store
- structured logging

Run locally:

```bash
cd apps/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
uvicorn app.main:app --reload
```

Backend URL: `http://127.0.0.1:8000`

## Frontend

Features included:

- Next.js App Router structure
- mobile-first HR assistant layout
- reusable chat components
- API client abstraction
- local development with MSW

Run locally after installing Node.js 20+:

```bash
cd apps/frontend
npm install
npm run dev
```

Frontend URL: `http://localhost:3000`

## Storybook

Storybook is configured to support isolated UI development for the chat components and states.

Run locally:

```bash
cd apps/frontend
npm install
npm run storybook
```

Storybook URL: `http://localhost:6006`

## MSW

MSW is set up for:

- successful chat replies
- delayed loading scenarios
- fallback conversational replies
- error scenarios

The app enables mocking in development when `NEXT_PUBLIC_API_MOCKING=enabled`.

Example:

```bash
cd apps/frontend
NEXT_PUBLIC_API_MOCKING=enabled npm run dev
```

## Documentation

- Architecture notes: [docs/architecture.md](/home/giuli/trenbot-enterprise/docs/architecture.md)
- Shared contracts: [shared/contracts/README.md](/home/giuli/trenbot-enterprise/shared/contracts/README.md)
- Infrastructure placeholders: [infra/README.md](/home/giuli/trenbot-enterprise/infra/README.md)

## Notes

- SAP, Redis, PostgreSQL, and RAG are intentionally not implemented yet.
- The current codebase focuses on a professional foundation that is easy to extend.
- This environment did not include Node.js, so the frontend and Storybook scaffolding were created but not executed locally here.

