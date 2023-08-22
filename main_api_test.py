from fastapi import FastAPI, Depends

import uvicorn

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware 

from fastapi.staticfiles import StaticFiles

from fastapi import APIRouter

# 라우터 추가
from app.routes import index
from app.routes import input_test
from app.routes import api_router_test
# from app.routes import chatting # 수정이 필요해서

# user 관리 라우터 추가
from app.routes import users

app = FastAPI() 

# 미들웨어 정의

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")

# 라우터 추가 부분
app.include_router(index.router)
# api 라우터 추가
app.include_router(api_router_test.router)
# input form 테스트 라우터 추가
app.include_router(input_test.router)
# 유저관리 라우터 추가
app.include_router(users.router)

# 채팅라우터 추가
# app.include_router(chatting.router) # 수정이 필요해서..


# 서버 가동 여부 테스트 
@app.get('/')
def main_index():
    return "안녕하세요 api 테스트 서버 가동중입니다."