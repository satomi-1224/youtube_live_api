import json
import aiofiles
from typing import List
from schemas.live.live_schema import LiveSchema

class LiveService:
    def __init__(self) -> None:
        pass
    
    async def get_lives(self, file_paths: str) -> List[LiveSchema]:
        lives = []
        for file_path in file_paths:
            async with aiofiles.open(file_path, mode='r') as file:
                live = await file.read()
                lives += json.loads(live)
                
        return lives