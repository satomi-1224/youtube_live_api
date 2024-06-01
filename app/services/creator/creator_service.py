import json
import aiofiles
from typing import List
from schemas.creator.creator_schema import CreatorSchema

class CreatorService:
    def __init__(self) -> None:
        pass
    
    async def get_creators(self, file_paths: str) -> List[CreatorSchema]:
        creators = []
        for file_path in file_paths:
            async with aiofiles.open(file_path, mode='r') as file:
                content = await file.read()
                creators += json.loads(content)
                
        return creators