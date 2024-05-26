from pydantic import BaseModel
from typing import List, Optional

class ItemRequest(BaseModel):
    channelId: Optional[str] = None