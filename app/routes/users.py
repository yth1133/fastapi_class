from fastapi import APIRouter

from model import UserTable
from database import session

router = APIRouter(prefix="/users")

@router.get("/{user_id}")
def read_users(user_id: int):
    users = session.query(UserTable).filter(UserTable.id == user_id).first()
    return read_users

@router.post("/")
def create_users(id: str, name: str, age: int):
    user = UserTable()
    user.id = id
    user.name = name
    user.age = age
    session.add(user)
    session.commit()
    return f"{name} created... "

@router.put("/{user_id}")
def update_users(users):
    user = session.query(UserTable).filter(UserTable.id == users.id).first()
    user.name = users.name
    user.age = users.age
    session.commit()

    return f"{users.name} updated... "

@router.delete("/{user_id}")
def delete_users(user_id:int):
    user = session.query(UserTable).filter(UserTable.id == user_id).delete()
    session.commit()
    return read_users
