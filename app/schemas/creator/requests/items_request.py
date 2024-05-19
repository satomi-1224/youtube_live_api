from pydantic import BaseModel
from typing import List, Optional

class ItemsRequest(BaseModel):
    channelTag: Optional[str]
    name: Optional[str]
    tag: Optional[List[str]]