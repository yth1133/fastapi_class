from fastapi import FastAPI

app = FastAPI() 

@app.get('/')
def main_index():
    return "안녕하세요 서버 가동중입니다."