# AI Assistant for Telecom - Developer Guide

## Project Overview
A production-ready foundation for an intelligent AI-powered telecom assistant designed to improve customer support and service operations using LLMs, LangChain, and LangGraph.

### Core Documentation
- [Product Specification](docs/product.md)
- [Architecture Design](docs/architecture.md)
- [Development Roadmap](docs/roadmap.md)
- [ADR: Technology Stack](docs/decisions/0001-stack.md)

## Exact Commands

### Backend (FastAPI)
- **Installation:** `cd backend && pip install -r requirements.txt`
- **Run Dev Server:** `cd backend && uvicorn src.main:app --reload`
- **Lint & Format:** `cd backend && ruff check . && ruff format .`
- **Type Check:** `cd backend && mypy src`
- **Run Tests:** `cd backend && pytest`

### Frontend (React + Vite)
- **Installation:** `cd frontend && npm install`
- **Run Dev Server:** `cd frontend && npm run dev`
- **Lint:** `cd frontend && npm run lint`
- **Type Check:** `cd frontend && npm run typecheck`
- **Run Tests:** `cd frontend && npm run test`
- **Build:** `cd frontend && npm run build`

## Folder Map

### Frontend (`/frontend`)
- `src/features/`: Self-contained feature modules (e.g., billing, network).
- `src/shared/`:
  - `components/`: Reusable UI elements.
  - `lib/`: Utility functions and API clients.
  - `hooks/`: Shared React hooks.
  - `types/`: Global TypeScript definitions.
- `src/app/`: Entry point, routing, and global state.

### Backend (`/backend`)
- `src/features/`: Feature-specific business logic and API endpoints.
- `src/shared/`:
  - `config/`: Environment and application settings.
  - `database/`: SQLAlchemy models and session management.
  - `exceptions/`: Global error handlers.
  - `types/`: Shared Pydantic models.
- `src/main.py`: FastAPI application entry point.

## Naming Conventions
- **Python:** `snake_case` for modules/functions, `PascalCase` for classes.
- **React:** `PascalCase` for components, `camelCase` for functions/hooks.
- **TypeScript:** `camelCase` for variables/functions, `PascalCase` for types/interfaces.
- **API:** Kebab-case endpoints (`/api/v1/network-status`).
- **Tests:** `test_*.py` (Python), `*.test.tsx` (React).

## Hard Rules for AI Agents
1. Work on one small vertical slice at a time.
2. Always propose a plan before coding.
3. Write or update tests for every change.
4. Run relevant tests before completing a task.
5. Never add dependencies without asking for approval.
6. Do not modify shared modules or configuration files unless necessary; explain why.
7. Never commit secrets. Use environment variables.
8. Keep files small (<300 lines). Extract functionality as they grow.
9. Do not refactor unrelated code.
10. Avoid circular dependencies.
11. Maintain strict typing (TypeScript strict, Mypy strict).
12. Update documentation when architectural decisions or system behavior changes.
13. Never implement features outside the approved task scope.

## Definition of Done
A task is complete only when:
- [ ] Tests pass.
- [ ] Linting succeeds.
- [ ] Type checking succeeds.
- [ ] Build succeeds (where applicable).
- [ ] Changes are minimal and focused.
- [ ] Documentation is updated when necessary.
- [ ] No secrets are committed.
