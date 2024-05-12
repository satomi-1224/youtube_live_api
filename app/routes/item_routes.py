from fastapi import APIRouter
from config.app import port

router = APIRouter()

@router.get('/')
def get_items():
    return {'items': ['item1', port]}