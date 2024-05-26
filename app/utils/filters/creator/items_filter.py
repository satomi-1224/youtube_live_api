from typing import List, Optional
from schemas.creator.responses.items_response import ItemsResponse
from schemas.creator.requests.items_request import ItemsRequest
from schemas.creator.requests.item_request import ItemRequest


class ItemsFilter():
    @staticmethod
    def filter(request: ItemsRequest, creators: List[ItemsResponse]) -> List[ItemsResponse]:
        if request.channelTag != None:
            creators = [creator for creator in creators if creator['channelTag'] == request.channelTag]
            
        return creators
    
    @staticmethod
    def filterByChannelId(request: ItemRequest, creators: List[ItemsResponse]) -> Optional[ItemsResponse]:
        if request.channelId != None:
            for creator in creators:
                if creator['channelId'] == request.channelId:
                    return creator
                            
        return None