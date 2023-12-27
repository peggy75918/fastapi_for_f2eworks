from fastapi import APIRouter
from db.homeworkJson import homework

router = APIRouter(
    prefix='/homeworks',
    tags=['homeworks']
)

@router.get('/')
def get_all_homeworks():
    return homework

