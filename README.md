# AI Assistant for Telecom

An intelligent AI-powered telecom assistant designed to help telecom companies improve customer support, streamline operations, and provide faster assistance to consumers.

## Technology Stack
- **Frontend:** React, TypeScript, Vite, Tailwind CSS.
- **Backend:** Python 3.12+, FastAPI, Pydantic v2.
- **AI Orchestration:** LangChain, LangGraph.
- **Database:** SQLAlchemy 2.0 (SQLite for Dev, PostgreSQL for Prod).
- **Auth:** Supabase Auth.

## Quick Start

### Prerequisites
- Node.js (v20+)
- Python 3.12+

### Installation

1. **Clone Repository**
   ```bash
   git clone <repo-url>
   cd TelecomAgent
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Unix:
   source venv/bin/activate
   pip install -r requirements.txt
   cd ..
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   cd ..
   ```

4. **Environment Configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your Supabase credentials
   ```

### Running the Application
- **Start Backend:** `cd backend && uvicorn src.main:app --reload`
- **Start Frontend:** `cd frontend && npm run dev`

## Command Reference

| Action | Backend Command | Frontend Command |
|---|---|---|
| Run | `uvicorn src.main:app --reload` | `npm run dev` |
| Test | `pytest` | `npm run test` |
| Lint | `ruff check .` | `npm run lint` |
| Typecheck | `mypy src` | `npm run typecheck` |
| Build | N/A | `npm run build` |

## Project Structure
- `/frontend`: React application with feature-based organization.
- `/backend`: FastAPI application with modular monolith architecture.
- `/docs`: Product, architecture, and ADR documentation.
- `/tests`: End-to-end testing foundation.

## Development Guidelines
Refer to [AGENTS.md](./AGENTS.md) for strict engineering rules, naming conventions, and the Definition of Done.
