from .item_routes import router as item_router
from .user_routes import router as user_router

from fastapi import APIRouter

router = APIRouter(prefix='/api')

# Add routes to application
router.include_router(user_router, prefix='/users')
router.include_router(item_router, prefix='/items')

__all__ = ['router']