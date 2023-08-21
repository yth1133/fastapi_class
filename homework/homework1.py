from fastapi import FastAPI, File, UploadFile
from pathlib import Path

app = FastAPI()

@app.post("/homework1")
async def save_user_info(user_id: str, picture: UploadFile = File(...)):
    # 저장할 파일 경로 구성 (ex: media/picture/user1.jpg)
    file_location = f"media/picture/{user_id}.jpg"

    # media/picture 디렉토리가 없다면 생성
    Path("media/picture").mkdir(parents=True, exist_ok=True)

    # 저장할 파일 오픈하여 이미지 데이터 쓰기
    with open(file_location, "wb+") as file_object:
        file_object.write(picture.file.read())

    return {"file_name": picture.filename, "file_path": file_location}