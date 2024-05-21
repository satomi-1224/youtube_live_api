from pydantic import BaseModel
from typing import List, Optional

class ItemsRequest(BaseModel):
    channelTag: Optional[str] = None
    name: Optional[str] = None
    tag: Optional[str] = None