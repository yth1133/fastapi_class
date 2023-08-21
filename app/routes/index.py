from fastapi import APIRouter
from starlette.responses import Response
from fastapi import UploadFile
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse


import os

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

STATIC_DIR ='static/'

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/index", response_class=HTMLResponse)
def index_home(request: Request):
    return templates.TemplateResponse("index.html",
                                     {"request": request})