from pydantic import BaseModel
from typing import Optional

class ItemRequest(BaseModel):
    channelId: Optional[str] = None