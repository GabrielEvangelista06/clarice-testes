import time
import asyncio
from fastapi import Request, HTTPException

# Dictionary to keep track of request counts per IP address
request_counts = {}

# Lock to ensure thread-safe access to the request_counts dictionary
rate_limit_lock = asyncio.Lock()

# Maximum number of requests allowed within the rate limit duration
RATE_LIMIT = 5

# Duration (in seconds) for the rate limit window
RATE_LIMIT_DURATION = 60

async def rate_limiter(request: Request):
    """
    Rate limiting function to restrict the number of requests from a single IP address.

    This function checks the number of requests made by the client's IP address within the
    specified rate limit duration. If the number of requests exceeds the allowed limit, it
    raises an HTTP 429 (Too Many Requests) exception.

    Args:
        request (Request): The incoming HTTP request.

    Raises:
        HTTPException: If the number of requests exceeds the allowed limit.
    """
    ip = request.client.host
    current_time = time.time()
    async with rate_limit_lock:
        timestamps = request_counts.get(ip, [])
        timestamps = [t for t in timestamps if current_time - t < RATE_LIMIT_DURATION]
        if len(timestamps) >= RATE_LIMIT:
            raise HTTPException(status_code=429, detail="Too many requests")
        timestamps.append(current_time)
        request_counts[ip] = timestamps
