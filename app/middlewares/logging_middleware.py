from fastapi import Request, Response
from typing import Awaitable, Callable
from config.logging import access_logger

async def log_requests(request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    ip = request.client.host
    method = request.method
    url = request.url.path
    access_logger.info(f'IP: {ip} - Method: {method} - URL: {url}')
    response = await call_next(request)
    access_logger.info(f'Response status: {response.status_code} - Method: {method} - URL: {url}')
    return response
