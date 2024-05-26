from pydantic import BaseModel

class ItemRequest(BaseModel):
    channelId: str