from typing import List, Optional
from schemas.live.live_schema import LiveSchema
from schemas.live.requests.item_request import ItemRequest
from schemas.live.responses.item_response import ItemResponse


class ItemFilter():
    @staticmethod
    def filter(request: ItemRequest, creators: List[LiveSchema]) -> Optional[ItemResponse]:
        return next((creator for creator in creators if creator['channelId'] == request.channelId), None)
