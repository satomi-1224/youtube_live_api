from pydantic import BaseModel, RootModel
from typing import Optional, List
from datetime import datetime

class _Creator(BaseModel):
      channelId: str
      channelTag: str
      channelName: str
      channelUrl: str
      channelIcon: str
      tag: List[str]

class _Item(BaseModel):
    creator: _Creator
    id: str
    title: str
    url: str
    thumbnail: str
    status: str
    isLive: bool
    isLiveContent: bool
    isUpcoming: bool
    viewCount: int
    startDatetime: datetime
    endDatetime: datetime
    category: Optional[str]
    videoId: str
    seconds: float
    
class ItemsResponse(RootModel[List[_Item]]):
    pass