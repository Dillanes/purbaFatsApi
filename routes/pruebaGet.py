from fastapi import APIRouter, File,UploadFile
import os
import shutil
from fastapi.encoders import jsonable_encoder
from PIL import Image
from uuid import uuid4
from config.settings import Settings

setting = Settings()

prueba = APIRouter(
    tags=['prueba'],
    prefix='/api/prueba'
)

@prueba.post('/')
def upload_img(image:UploadFile = File(...)):
    format_img =  image.filename.split('.')[-1]
    path_img = os.path.dirname(__file__)+'\..\static'+f'\{uuid4()}.{format_img}'
    with open(path_img,'wb') as buffer:
        shutil.copyfileobj(image.file,buffer)
    return {'result':'Image guardada'}

@prueba.delete('/{name}')
def delete_img(name:str):
    path_dir = os.path.dirname(__file__)+f'\..\static\{name}.jpg'
    os.remove(path_dir)
    return {'result':'Image eliminada'}

@prueba.get('/{name}',status_code=200)
def prueba_get(name:str):
    print('**************',os.path.dirname(__file__)+'\..\static'+f'\{name}'+'.jpg')
    image = Image.open(os.path.dirname(__file__)+'\..\static'+f'\{name}'+'.jpg')
    img = open(os.path.dirname(__file__)+'\..\static'+f'\{name}'+'.jpg')
    print('**********************IMAGEN',image)
    return {'message':f'{setting.HOST}static/{name}.jpg'}
