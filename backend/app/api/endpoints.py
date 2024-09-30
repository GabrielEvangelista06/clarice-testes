from fastapi import APIRouter, Request, Depends
from app.models.schemas import TextPayload
from app.services import nlp_service, db_service, external_service
from app.utils.rate_limiter import rate_limiter

router = APIRouter()

@router.post("/process-text")
async def process_text(payload: TextPayload, request: Request, _: None = Depends(rate_limiter)):
    """
    Endpoint to process the input text, extract entities and multi-word expressions (MWEs),
    store the processed data in the database, and call an external API.

    Args:
        payload (TextPayload): The input text payload.
        request (Request): The request object.
        _ (None): Dependency injection for rate limiting.

    Returns:
        dict: A dictionary containing the original text, extracted entities, and MWEs.
    """
    text = payload.text

    # Process the text and extract entities and MWEs
    entities, mwes = await nlp_service.process_text(text)

    # Store the processed data in the database
    await db_service.store_processed_data(text, entities, mwes)

    # Call the external API asynchronously
    await external_service.call_external_api()

    # Return the processed data
    return {
        "original_text": text,
        "entities": entities,
        "multi_word_expressions": mwes,
    }

@router.get("/data")
async def get_data(_: None = Depends(rate_limiter)):
    """
    Endpoint to retrieve all stored data from the database.

    Returns:
        list: A list of all stored data.
    """
    # Return all stored data from the database
    return await db_service.get_all_data()
