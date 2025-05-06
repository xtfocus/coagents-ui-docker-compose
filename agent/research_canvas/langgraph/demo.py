"""Demo"""

import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv

load_dotenv()

from copilotkit import CopilotKitRemoteEndpoint, LangGraphAgent
from copilotkit.integrations.fastapi import add_fastapi_endpoint
# pylint: disable=wrong-import-position
from fastapi import FastAPI
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from psycopg_pool import AsyncConnectionPool
from research_canvas.langgraph.agent import workflow


def get_db_uri():
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5442")
    user = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASSWORD", "postgres")
    db_name = os.getenv("DB_NAME", "postgres")
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}?sslmode=disable"


DB_URI = get_db_uri()

connection_kwargs = {
    "autocommit": True,
    "prepare_threshold": 0,
}


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncConnectionPool(
        conninfo=DB_URI,
        max_size=20,
        kwargs=connection_kwargs,
    ) as pool:
        checkpointer = AsyncPostgresSaver(pool)
        await checkpointer.setup()

        graph = workflow.compile(checkpointer=checkpointer)

        # Create SDK with the graph
        sdk = CopilotKitRemoteEndpoint(
            agents=[
                LangGraphAgent(
                    name="research_agent",
                    description="Research agent.",
                    graph=graph,
                ),
                LangGraphAgent(
                    name="research_agent_google_genai",
                    description="Research agent.",
                    graph=graph,
                ),
            ],
        )

        # Add the CopilotKit FastAPI endpoint
        add_fastapi_endpoint(app, sdk, "/copilotkit")
        yield


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health():
    """Health check."""
    return {"status": "ok"}


def main():
    """Run the uvicorn server."""
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(
        "research_canvas.langgraph.demo:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        reload_dirs=(
            ["."]
            + (
                ["../../../../sdk-python/copilotkit"]
                if os.path.exists("../../../../sdk-python/copilotkit")
                else []
            )
        ),
    )
