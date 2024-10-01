from app.services.db_service import init_db, on_shutdown_db

# Inicializa o banco de dados no startup do app
async def on_startup():
    """
    Initialize the database when the application starts up.

    This function is called during the startup event of the FastAPI application.
    It initializes the database by calling the init_db function.
    """
    await init_db()

async def on_shutdown():
    """
    Perform cleanup tasks on shutdown.
    """
    # Example: Close any persistent connections or perform other cleanup tasks
    await on_shutdown_db()
