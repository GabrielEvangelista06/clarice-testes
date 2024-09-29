from fastapi import FastAPI
from app.api import endpoints
from app.database.connection import on_startup

# Initialize the FastAPI application
app = FastAPI()

# Add the API routes from the endpoints module
app.include_router(endpoints.router)

@app.on_event("startup")
async def startup():
    """
    Event handler for the FastAPI startup event.
    
    This function is called when the FastAPI application starts up.
    It initializes the database connection by calling the on_startup function.
    """
    await on_startup()