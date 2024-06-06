from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ItemsRequest(BaseModel):
    channelId: Optional[str] = None
    channelTag: Optional[str] = None
    tag: Optional[str] = None
    title: Optional[str] = None
    status: Optional[str] = None
    startDatetimeFrom: Optional[datetime] = None
    startDatetimeTo: Optional[datetime] = None
    endDatetimeFrom: Optional[datetime] = None
    endDatetimeTo: Optional[datetime] = None
    limit: Optional[int] = None
    