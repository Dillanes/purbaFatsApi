from pydantic import BaseModel,EmailStr,Field,validator
from datetime import date
from typing import Optional


class register_user_model(BaseModel):
    nombre:str = Field(...,min_length=3,max_length=50)
    apellido_paterno:str = Field(...,min_length=3,max_length=50)
    apellido_materno:str = Field(...,min_length=3,max_length=50)
    tel:str= Field(...)
    fecha_nacimiento: date = Field(...)
    curp:str = Field(...,min_length=18,max_length=18)
    rfc:str = Field(...,min_length=12,max_length=13)
    cargo:str = Field(...,min_length=3,max_length=50)
    email:EmailStr = Field(...)
    password:str = Field(...,min_length=3, max_length=50)
    nombre_col:str = Field(...,min_length=3, max_length=50)
    calle:str = Field(...)
    no_int:int = Field(...)
    no_ext:int = Field(...)
    id_cp:str = Field(...,min_length=24, max_length=24)
    id_departamento:str =Field(...,min_length=24, max_length=24)

    class Config:
        anystr_strip_whitespace= True

    @validator('cargo')
    def validate_cargo(cls,cargo):
        new_cargo = cargo.lower()
        if new_cargo == 'admin' or new_cargo == 'empleado':
            return cargo
        raise ValueError('Tipo de cargo no valido intenta enviando: cargo:admin or cargo:empleado')
    
    @validator('no_int')
    def validate_no_int(cls,no_int):
        if no_int < 1:
            raise ValueError('not_int invalid: make sure it is greater than zero')
        no_int_text = str(no_int)
        if len(no_int_text) < 5 and len(no_int_text)>1:
            return no_int
        raise ValueError('not_int invalid: make sure its length is greater than one and less than 5 ')

    @validator('no_ext')
    def validate_no_ext(cls,no_ext):
        if no_ext <1:
            raise ValueError('not_ext invalid: make sure it is greater than zero')
        no_ext_text = str(no_ext)
        if len(no_ext_text) < 5 and len(no_ext_text)>1:
            return no_ext
        raise ValueError('not_iext invalid: make sure its length is greater than one and less than 5 ')

