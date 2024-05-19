from pydantic import BaseModel
from typing import List

class ItemsResponse(BaseModel):
    channelId: str
    channelTag: str
    avatar: str
    name: str
    tag: List[str]