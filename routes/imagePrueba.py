from fastapi import APIRouter
# from fastapi.responses import HTMLResponse, StreamingResponse
# from deta import Deta
# import os

pruebaImg = APIRouter()
# deta = Deta("Project_Key")  
# drive = deta.Drive("images") 

@pruebaImg.get("api/image/{name}")
def get_img(name:str):
    # print('*********************',os)
    return 'HELLO'

# @pruebaImg.post("/upload")
# def upload_img(file: UploadFile = File(...)):
#     name = file.filename
#     f = file.file
#     res = drive.put(name, f)
#     return res


