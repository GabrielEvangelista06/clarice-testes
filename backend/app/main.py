from fastapi import FastAPI
from app.api import endpoints
from app.database.connection import on_startup, on_shutdown
from contextlib import asynccontextmanager

# Define the lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    await on_startup()
    yield
    # Shutdown event
    await on_shutdown()


# Initialize the FastAPI application with the lifespan context manager
app = FastAPI(lifespan=lifespan)

# Add the API routes from the endpoints module
app.include_router(endpoints.router)