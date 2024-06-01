from typing import List
from schemas.live.responses.items_response import ItemsResponse
from schemas.live.requests.items_request import ItemsRequest
from schemas.live.live_schema import LiveSchema


class ItemsFilter():
    @staticmethod
    def filter(request: ItemsRequest, lives: List[LiveSchema]) -> List[ItemsResponse]:
        if request.channelTag != None:
            lives = [
                live for live in lives 
                if live['channelTag'] == request.channelTag
                ]
            
        return lives