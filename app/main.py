import uvicorn

from fastapi import FastAPI
from routes import router
from config.app import address, port

app = FastAPI(
    title='YoutubeLiveAPI',
    description='YoutubeLiveの配信情報を取得するAPIです',
    version='1.0.0'
    )

app.include_router(router)

# サーバーを起動するためのコード
if __name__ == '__main__':
    uvicorn.run(app, host=address, port=port)