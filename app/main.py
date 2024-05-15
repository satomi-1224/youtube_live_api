import uvicorn

from fastapi import FastAPI, Request, Response
from routes import router
from config.app import address, port
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from config.logging import error_logger, info_logger
from typing import Awaitable, Callable
from middlewares.logging_middleware import log_requests

app = FastAPI(
    title='YoutubeLiveAPI',
    description='YoutubeLiveの配信情報を取得するAPIです',
    version='1.0.0'
    )

app.include_router(router)

# ミドルウェアを追加
app.middleware('http')(log_requests)

# エラーハンドラーの設定
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    error_logger.error(f'HTTP error: {exc.detail}')
    return JSONResponse(status_code=exc.status_code, content={'detail': exc.detail})

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    error_logger.error(f'Validation error: {exc.errors()}')
    return JSONResponse(status_code=400, content={'detail': exc.errors()})

@app.middleware('http')
async def log_info_middleware(request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    response = await call_next(request)
    info_logger.info(f'Request completed - Method: {request.method} - URL: {request.url.path}')
    return response

# サーバーを起動するためのコード
if __name__ == '__main__':
    uvicorn.run('main:app', host=address, port=port, reload=True)