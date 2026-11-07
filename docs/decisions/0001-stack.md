# ADR 0001: Technology Stack Selection

## Status
Accepted

## Context
The project requires a scalable, production-oriented foundation for an AI-powered Telecom Assistant. The system must support complex conversational state (AI agents), handle real-time data retrieval, and provide a modern user interface.

## Decision
We have selected the following stack:
- **Frontend:** React, Vite, TypeScript, Tailwind CSS.
- **Backend:** Python 3.12, FastAPI, Pydantic v2.
- **AI Framework:** LangChain and LangGraph.
- **Database:** SQLAlchemy 2.0 with SQLite (Dev) and PostgreSQL (Prod).
- **Auth:** Supabase Auth.
- **Deployment:** Vercel and Render.

## Rationale
- **React/TS/Vite:** Provides the best ecosystem for building typed, maintainable UIs with fast developer feedback.
- **FastAPI:** Offers exceptional performance and automatic OpenAPI documentation, which is critical for frontend-backend alignment.
- **LangGraph:** Essential for building cyclic, stateful agentic workflows that go beyond simple linear chains.
- **SQLAlchemy 2.0:** The current industry standard for Python ORMs, ensuring a smooth migration from SQLite to PostgreSQL.
- **Supabase:** Reduces the overhead of managing user identity and authentication.

## Alternatives Considered
- **Next.js:** Considered for full-stack capabilities, but a separate FastAPI backend was chosen to leverage the superior AI/Data ecosystem of Python.
- **Django:** Too heavyweight for this specific use case; FastAPI's async nature is better suited for LLM API calls.
- **Node.js Backend:** Not suitable given the project's heavy reliance on Python-based AI libraries (LangChain/LangGraph).

## Trade-offs & Limitations
- **Two-Repo Feel:** Managing separate frontend and backend directories increases configuration overhead slightly.
- **SQLite Limitation:** SQLite does not support full-text search or high concurrency; migration to PostgreSQL is mandatory before production.
