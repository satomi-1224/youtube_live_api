from fastapi import APIRouter
from typing import List
from config.app import base_dir
import json

from schemas.creator.responses.items_response import ItemsResponse
from schemas.creator.requests.items_request import ItemsRequest

import aiofiles
import aiofiles.os

router = APIRouter()

@router.get('/items', response_model=List[ItemsResponse])
async def get_items(items: ItemsRequest) -> List[ItemsResponse]:
    creator_dir = f'{base_dir}/creators'
    files = await aiofiles.os.listdir(creator_dir)
    file_paths = [f'{creator_dir}/{fp}' for fp in files]
    
    creators = []
    for file_path in file_paths:
        async with aiofiles.open(file_path, mode='r') as file:
            content = await file.read()
            creators += json.loads(content)
    
    return creators

@router.get('/item')
async def get_items():
    return {'items': ['item1', 'port']}