from pydantic import BaseModel,Field,validator
from typing import Optional


class colonia_model(BaseModel):
    id:Optional[str] = Field(alias='_id')
    nombre_col:str = Field(...,min_length=3,max_length=50)
    calle:str = Field(...,min_length=3,max_length=50)
    no_int:int = Field(...)
    no_ext:int = Field(...)




class colonia_insert_model(BaseModel):
    
    nombre_col:str = Field(...,min_length=3,max_length=50)
    calle:str = Field(...,min_length=3,max_length=50)
    no_int:int = Field(...)
    no_ext:int = Field(...)

    class Config:
        anystr_strip_whitespace = True

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
