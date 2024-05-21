from typing import List
from schemas.creator.responses.items_response import ItemsResponse
from schemas.creator.requests.items_request import ItemsRequest

class ItemsFilter():
    @staticmethod
    def filter(request: ItemsRequest, creators: List[ItemsResponse]) -> List[ItemsResponse]:
        if request.channelTag != None:
            creators = [creator for creator in creators if creator['channelTag'] == request.channelTag]
            
        return creators