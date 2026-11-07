# Architecture Design

## Technology Stack & Rationale
- **Frontend:** React + Vite + TypeScript. Fast build times, industry standard for scalable UIs.
- **Styling:** Tailwind CSS. Utility-first approach for rapid, consistent UI development.
- **Backend:** FastAPI (Python 3.12+). High performance, native async support, and excellent type validation via Pydantic.
- **AI Orchestration:** LangChain + LangGraph. Modular framework for building complex, stateful AI workflows.
- **Database:** SQLite (Development) $\rightarrow$ PostgreSQL (Production). SQLAlchemy 2.0 for an abstract ORM layer.
- **Authentication:** Supabase Auth. Managed identity provider to avoid building auth from scratch.
- **Deployment:** Vercel (Frontend) and Render (Backend).

## High-Level Architecture
The system follows a **Modular Monolith** architecture. Features are organized as independent modules within the backend and frontend, communicating through explicit shared interfaces.

### Repository Folder Layout
```text
/
├── frontend/             # React application
│   ├── src/
│   │   ├── features/     # Feature-based modules (e.g., billing, network)
│   │   ├── shared/       # Shared UI components, hooks, and types
│   │   └── app/          # App entry point and routing
├── backend/              # FastAPI application
│   ├── src/
│   │   ├── features/     # Feature-based logic (e.g., billing, network)
│   │   ├── shared/       # Shared config, database, and exceptions
│   │   └── main.py       # Application entry point
├── docs/                 # Product, architecture, and decision records
└── tests/                # End-to-end tests
```

## Data Model (Conceptual)
- **User:** Account details, authentication ID (Supabase).
- **Conversation:** Session history, user ID, timestamps.
- **Message:** Content, role (user/assistant), timestamp, conversation ID.
- **Case/Ticket:** Status, priority, assigned agent, conversation link.

## Module Boundaries
- **Frontend $\rightarrow$ Backend:** Communication via REST API using JSON.
- **Internal Backend:** Features must not import from other features directly. Communication happens via the `shared` layer or service interfaces.

## API Conventions
- **Versioning:** `/api/v1/...`
- **Naming:** Kebab-case for endpoints (`/api/v1/network-status`).
- **Responses:** Standardized JSON envelopes:
  ```json
  {
    "success": true,
    "data": { ... },
    "error": null
  }
  ```

## Authentication Approach
- Frontend obtains a JWT from Supabase.
- JWT is sent in the `Authorization: Bearer <token>` header.
- Backend validates the JWT using the Supabase public key.

## Environment & Configuration
- Use `.env` files (ignored by git).
- Configuration managed via Pydantic `BaseSettings`.
- Separate profiles: `development`, `staging`, `production`.

## Security Considerations
- **Secret Management:** No secrets in git. Use environment variables.
- **Data Validation:** Strict Pydantic models for all API inputs/outputs.
- **PII Protection:** Avoid logging sensitive customer data.
- **CORS:** Strict whitelist for allowed origins in production.

## Future Scalability
- Transition to PostgreSQL for production concurrency.
- Potential move to microservices if specific features (e.g., Network Diagnostics) require separate scaling.
- Introduction of Redis for session caching and LangGraph state persistence.
