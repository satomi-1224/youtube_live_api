from pydantic import BaseModel, RootModel
from typing import List

class _Item(BaseModel):
    channelId: str
    channelTag: str
    avatar: str
    name: str
    tag: List[str]
 
class ItemsResponse(RootModel[List[_Item]]):
    pass