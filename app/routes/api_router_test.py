from fastapi import APIRouter

router = APIRouter(prefix="/api_test")

@router.get('/')
async def read_item():
    return {"api_test": "prefix"}

@router.get('/hello')
async def read_hello():
    return "안녕하세요"

@router.post('/post')
async def post_item(id: str, age: int):
    print(f"id is {id}, age is {age}")
    return f"id is {id}, age is {age}"
