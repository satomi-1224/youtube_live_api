from typing import List, Optional
from schemas.creator.creator_schema import CreatorSchema
from schemas.creator.requests.item_request import ItemRequest
from schemas.creator.responses.item_response import ItemResponse


class ItemFilter():
    @staticmethod
    def filter(request: ItemRequest, creators: List[CreatorSchema]) -> Optional[ItemResponse]:
        return next((creator for creator in creators if creator['channelId'] == request.channelId), None)
