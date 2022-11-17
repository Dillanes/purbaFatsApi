from pydantic import BaseModel,Field,validator
from typing import Optional
from datetime import date


class persona_model(BaseModel):
    id: Optional[str]= Field(alias='_id')
    nombre:str = Field(...,min_length=3,max_length=50)
    apellido_paterno:str = Field(...,min_length=3,max_length=50)
    apellido_materno:str = Field(...,min_length=3,max_length=50)
    tel:str= Field(...)
    fecha_nacimiento: date = Field(...)
    curp:str = Field(...,min_length=18,max_length=18)
    id_colonia:str = Field(...,min_length=23, max_length=23)



class persona_insert_model(BaseModel):
    nombre:str = Field(...,min_length=3,max_length=50)
    apellido_paterno:str = Field(...,min_length=3,max_length=50)
    apellido_materno:str = Field(...,min_length=3,max_length=50)
    tel:str= Field(...)
    fecha_nacimiento: date = Field(...)
    curp:str = Field(...,min_length=18,max_length=18)
    id_colonia:str = Field(...,min_length=23, max_length=23)

    @validator('nombre')
    def nombre_validator(cls,nombre):
        if nombre.upper() == 'ISRAEL':
            raise ValueError('Este nombre esta cancelado')

    class Config:
        anystr_strip_whitespace = True
    

