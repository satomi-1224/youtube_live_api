from fastapi import APIRouter, Depends
from typing import List, Optional
from config.app import base_dir
from services.creator.creator_service import CreatorService

from schemas.creator.responses.items_response import ItemsResponse
from schemas.creator.responses.item_response import ItemResponse
from schemas.creator.requests.items_request import ItemsRequest
from schemas.creator.requests.item_request import ItemRequest

from utils.filters.creator.items_filter import ItemsFilter
from utils.filters.creator.item_filter import ItemFilter

import aiofiles.os

creator_dir = f'{base_dir}/creators'
router = APIRouter()
service = CreatorService()

@router.get('/items', response_model=List[ItemsResponse])
async def get_items(request: ItemsRequest = Depends(ItemsRequest)) -> List[ItemsResponse]:
    files = await aiofiles.os.listdir(creator_dir)
    file_paths = [f'{creator_dir}/{fp}' for fp in files]
    
    creators = await service.get_creators(file_paths)
    filter_creators = ItemsFilter.filter(request, creators)
    
    return filter_creators

@router.get('/item', response_model=Optional[ItemResponse])
async def get_item(request: ItemRequest = Depends(ItemRequest)) -> Optional[ItemResponse]:
    files = await aiofiles.os.listdir(creator_dir)
    file_paths = [f'{creator_dir}/{fp}' for fp in files]
    
    creators = await service.get_creators(file_paths)
    filter_creator = ItemFilter.filter(request, creators)
    
    return filter_creator