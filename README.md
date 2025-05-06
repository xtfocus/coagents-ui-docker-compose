# Research Canvas - AI Agent Demo
A research canvas application powered by AI agents implemented using LangGraph.

## Features
- Research canvas with AI agents
- Python backend using LangGraph with PostgreSQL checkpointing
- Next.js frontend with modern UI components
- Dockerized deployment for both backend and frontend

## Prerequisites
- Docker and Docker Compose
- OpenAI API key
- Tavily API key (for web search capabilities)

## Quick Start
1. Set up environment variables:
   You'll need to create two .env files:

   For the agent service (./agent/.env):
   ```
   OPENAI_API_KEY=your_key_here
   TAVILY_API_KEY=your_key_here
   DB_HOST=postgres
   DB_PORT=5432
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_NAME=postgres
   ```

   For the UI service (./ui/.env):
   ```
   OPENAI_API_KEY=your_key_here
   NEXT_PUBLIC_AGENT_URL=http://agent:8000
   NEXT_TELEMETRY_DISABLED=1  # Optional: Disable Next.js telemetry
   ```

2. Start the application:
   ```
   docker compose up --build
   ```

   This will:
   - Build the Python agent image with uv package manager
   - Build the Next.js UI image
   - Start the PostgreSQL service for LangGraph checkpointing
   - Set up networking between containers
   - Mount appropriate volumes for development

4. Access the application:
   - Frontend UI: http://localhost:3000
   - Backend API: http://localhost:8000
   - PostgreSQL: localhost:5442

To stop the application:
```bash
docker compose down
```

To view logs:
```bash
docker compose logs -f
```

To rebuild after making changes:
```bash
docker compose up --build
```

## Development

### Backend (Python Agent)
The backend uses uv for dependency management. Requirements are specified in `agent/requirements.txt`.

To run the backend locally:
```bash
cd agent
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
uv pip install -r requirements.txt
uvicorn research_canvas.langgraph.demo:app --host 0.0.0.0 --port 8000 --reload
```

Make sure to set up PostgreSQL locally or update the database connection environment variables to point to your PostgreSQL instance.

### Frontend
The frontend is built with Next.js and uses pnpm for package management.

To run the frontend locally:
```bash
cd ui
pnpm install
pnpm dev
```

## Architecture
The application consists of three main components:
1. Python Agent: Implements the AI research capabilities using LangGraph
2. Next.js UI: Provides the user interface and canvas interaction
3. PostgreSQL: Provides persistent storage for LangGraph checkpointing

## Learn More About the Frontend
- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial

## Contributing
Feel free to submit issues and pull requests.
