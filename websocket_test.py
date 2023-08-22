from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import csv


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def get(request: Request):
    # return templates.TemplateResponse("ws.html", {"request": request})
    return templates.TemplateResponse("ws_pretty_2.html", {"request": request})

@app.websocket("/chatting") # 현재, 소켓통신은 ws://localhost:8000/chatting 을 통해 통신중
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json() # json 형식으로 데이터 받기
        message = data["message"]
        id = data["id"]

        print(data, "데이터 형식 확인하세요")
        print("id is :"+ id, "message is :"+ message) 
        
        with open('result.csv', mode='a', newline='', encoding="utf-8-sig") as file: # 파일 저장 부분
            writer = csv.writer(file)
            writer.writerow([id, message])

        # 다시 소켓으로 전송하기 위한 reply 데이터 만들기 
        reply = {
            "message": message,
            "id": id
        }
        
        await websocket.send_json(reply) # json 형태로 다시 전달
