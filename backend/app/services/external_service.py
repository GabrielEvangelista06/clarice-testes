import httpx
import logging

logger = logging.getLogger(__name__)

async def call_external_api():
    """
    Make an external API call to a predefined URL.

    This function uses an asynchronous HTTP client to send a GET request to the external API.
    It logs the response status code if the request is successful, or logs an error message if an exception occurs.

    The external API endpoint used in this example introduces a delay of 3 seconds.

    Raises:
        Exception: If an error occurs during the API call.
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get("https://httpbin.org/delay/3")
            logger.info(f"External API response: {response.status_code}")
        except Exception as e:
            logger.error(f"External API error: {e}")
