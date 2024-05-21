import json
import aiofiles
from typing import List
from schemas.creator.responses.items_response import ItemsResponse

class CreatorService:
    def __init__(self) -> None:
        pass
    
    async def get_items(self, file_paths: str) -> List[ItemsResponse]:
        creators = []
        for file_path in file_paths:
            async with aiofiles.open(file_path, mode='r') as file:
                content = await file.read()
                creators += json.loads(content)
                
        return creators