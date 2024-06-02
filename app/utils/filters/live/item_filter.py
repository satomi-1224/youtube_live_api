from typing import List, Optional
from schemas.live.live_schema import LiveSchema
from schemas.live.requests.item_request import ItemRequest
from schemas.live.responses.item_response import ItemResponse


class ItemFilter():
    @staticmethod
    def filter(request: ItemRequest, lives: List[LiveSchema]) -> Optional[ItemResponse]:
        return next((live for live in lives if live['id'] == request.id), None)
