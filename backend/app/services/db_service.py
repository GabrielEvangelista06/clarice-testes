import aiosqlite
from typing import List, Dict, Union

DATABASE_URL = 'processed_data.db'

async def init_db():
    """
    Initialize the database.

    This function creates the 'processed_data' table if it does not exist.
    The table contains columns for the original text, extracted entities, and multi-word expressions (MWEs).
    """
    async with aiosqlite.connect(DATABASE_URL) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS processed_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_text TEXT,
                entities TEXT,
                mwes TEXT
            )
        ''')
        await db.commit()

# Armazena os dados processados no banco de dados
async def store_processed_data(original_text: str, entities: List[Dict[str, Union[str, int]]], mwes: List[Dict[str, Union[str, int]]]):
    """
    Store the processed data in the database.

    Args:
        original_text (str): The original input text.
        entities (List[Dict[str, Union[str, int]]]): A list of extracted entities.
        mwes (List[Dict[str, Union[str, int]]]): A list of extracted multi-word expressions (MWEs).
    """
    async with aiosqlite.connect(DATABASE_URL) as db:
        await db.execute('''
            INSERT INTO processed_data (original_text, entities, mwes)
            VALUES (?, ?, ?)
        ''', (original_text, str(entities), str(mwes)))
        await db.commit()

# Recupera todos os dados armazenados
async def get_all_data():
    """
    Retrieve all stored data from the database.

    Returns:
        List[Dict[str, Union[int, str]]]: A list of dictionaries containing all stored data.
    """
    async with aiosqlite.connect(DATABASE_URL) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute("SELECT * FROM processed_data")
        rows = await cursor.fetchall()
        result = [
            {
                "id": row["id"],
                "original_text": row["original_text"],
                "entities": row["entities"],
                "mwes": row["mwes"],
            }
            for row in rows
        ]
        return result
