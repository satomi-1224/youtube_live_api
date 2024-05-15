from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def get_users():
    return {'users': ['user1', 'user2']}