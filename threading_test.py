from typing import Dict
from fastapi import APIRouter, BackgroundTasks, FastAPI

router = APIRouter()

# 파일 읽기 작업
def read_file(file_path):
    with open(file_path, "r") as f:
        file_content = f.read()
    return file_content

# 데이터베이스 쓰기 작업
def write_to_database(data):
    # 데이터베이스 작업 수행
    pass

# 파일 가공하는 작업(async)
async def process_file(file_content):
    # 파일 가공 작업 수행
    processed_file_content = await do_something_with_file_content(file_content)
    return processed_file_content

# 병렬 처리 함수
def do_in_background(file_path: str, data: Dict):
    # 파일 읽기 작업과 데이터베이스 쓰기 작업을 수행하는 스레드 시작
    read_thread = threading.Thread(target=read_file, args=[file_path])
    read_thread.start()
    write_thread = threading.Thread(target=write_to_database, args=[data])
    write_thread.start()

    # 파일 가공 작업을 수행하기 위해 이벤트 루프를 시작
    loop = asyncio.get_event_loop()
    file_content = loop.run_in_executor(None, read_thread.join)
    processed_file_content = loop.run_until_complete(process_file(file_content))

    # 데이터베이스 쓰기 작업을 마무리
    write_thread.join()

# API 엔드포인트 함수
@router.post("/process-file")
async def post_process_file(background_tasks: BackgroundTasks, data: Dict):
    file_path = data["file_path"]
    # 병렬 처리 함수를 BackgroundTasks 개체에 등록해서 실행
    background_tasks.add_task(do_in_background, file_path, data)
    return {"message": "File processing started in background."}
