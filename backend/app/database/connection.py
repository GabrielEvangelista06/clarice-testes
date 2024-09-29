from app.services.db_service import init_db

# Inicializa o banco de dados no startup do app
async def on_startup():
    """
    Initialize the database when the application starts up.

    This function is called during the startup event of the FastAPI application.
    It initializes the database by calling the init_db function.
    """
    await init_db()
