from fastapi import APIRouter
import os
from fastapi.encoders import jsonable_encoder
from PIL import Image

prueba = APIRouter(
    tags=['prueba'],
    prefix='/api/prueba'
)


@prueba.get('/{name}',status_code=200)
def prueba_get(name:str):

    print('**************',os.path.dirname(__file__)+'\..\static'+f'\{name}'+'.jpg')
    img = open(os.path.dirname(__file__)+'\..\static'+f'\{name}'+'.jpg')
    print('**********************IMAGEN',img)
    return {'message':'Hello world'}
