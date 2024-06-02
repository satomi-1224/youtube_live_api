from fastapi import APIRouter, Depends
from typing import Optional
from config.app import base_dir
from services.live.live_service import LiveService

from schemas.live.responses.items_response import ItemsResponse
from schemas.live.responses.item_response import ItemResponse
from schemas.live.requests.items_request import ItemsRequest
from schemas.live.requests.item_request import ItemRequest

from utils.filters.live.items_filter import ItemsFilter
from utils.filters.live.item_filter import ItemFilter

import aiofiles.os


live_dir = f'{base_dir}/data'
router = APIRouter()
service = LiveService()

@router.get('/items', response_model=ItemsResponse)
async def get_items(request: ItemsRequest = Depends(ItemsRequest)) -> ItemsResponse:
    files = await aiofiles.os.listdir(live_dir)
    file_paths = [f'{live_dir}/{fp}' for fp in files]
    
    lives = await service.get_lives(file_paths)
    filter_lives = ItemsFilter.filter(request, lives)
    
    return filter_lives

@router.get('/item', response_model=Optional[ItemResponse])
async def get_item(request: ItemRequest = Depends(ItemRequest)) -> Optional[ItemResponse]:
    files = await aiofiles.os.listdir(live_dir)
    file_paths = [f'{live_dir}/{fp}' for fp in files]
    
    lives = await service.get_lives(file_paths)
    filter_live = ItemFilter.filter(request, lives)
    
    return filter_live