from .creator_routes import router as creator_router
from .live_routes import router as live_router

from fastapi import APIRouter

router = APIRouter()

# Add routes to application
router.include_router(live_router, prefix='/live')
router.include_router(creator_router, prefix='/creator')

__all__ = ['router']