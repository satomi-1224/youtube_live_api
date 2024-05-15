from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    address: str
    port: int

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        
# 設定をインスタンス化して使用
settings = Settings()

# .env内
address = settings.address
port = settings.port

__all__ = ['address', 'port']