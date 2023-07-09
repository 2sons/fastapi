from fastapi import FastAPI
from typing import List
from starlette.middleware.cors import CORSMiddleware

from db import session
from model import UserTable, User

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    #allow_hearders=["*"],
)


# 1.사용자 조회
@app.get("/users")
async def get_users():
    users = session.query(UserTable).all()
    return users


# 1-1.사용자 조회(조건)
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    users = session.query(UserTable).filter(UserTable.id == user_id).first()
    return users


# 2.사용자 생성
@app.post("/users")
async def post_users(name: str, age: int):

    user = UserTable()
    user.name = name
    user.age = age

    session.add(user)
    session.commit()

    return f'{name} create success'


# 3.사용자 수정
@app.put("/users")
async def put_users(users: List[User]):

    for i in users:
        user = session.query(UserTable).filter(UserTable.id == i.id).first()
        user.name = i.name
        user.age = i.age
        session.commit()

    return f'"message": {user.name} update'


# 4.사용자 삭제
@app.delete("/users")
async def delete_users(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).delete()
    session.commit()

    return get_users
