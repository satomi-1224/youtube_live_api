from fastapi import APIRouter, Depends
from typing import List
from typing import Optional
from config.app import base_dir
from services.creator.creator_service import CreatorService

from schemas.creator.responses.items_response import ItemsResponse
from schemas.creator.requests.items_request import ItemsRequest
from schemas.creator.requests.item_request import ItemRequest

from utils.filters.creator.items_filter import ItemsFilter

import aiofiles.os

router = APIRouter()
service = CreatorService()

@router.get('/items', response_model=List[ItemsResponse])
async def get_items(request: ItemsRequest = Depends(ItemsRequest)) -> List[ItemsResponse]:
    creator_dir = f'{base_dir}/creators'
    files = await aiofiles.os.listdir(creator_dir)
    file_paths = [f'{creator_dir}/{fp}' for fp in files]
    
    creators = await service.get_items(file_paths)
    filter_creators = ItemsFilter.filter(request, creators)
    
    return filter_creators

@router.get('/item')
async def get_item(request: ItemRequest = Depends(ItemRequest)) -> Optional[ItemsResponse]:
    creator_dir = f'{base_dir}/creators'
    files = await aiofiles.os.listdir(creator_dir)
    file_paths = [f'{creator_dir}/{fp}' for fp in files]
    
    creators = await service.get_items(file_paths)
    filter_creator = ItemsFilter.filterBychannelId(request, creators)
    
    return filter_creator