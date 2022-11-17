from pydantic import BaseModel, validator, EmailStr,Field

class empleado_insert_model(BaseModel):
    rfc:str =  Field(...,min_length=12,max_length=13)
    cargo:str = Field(...)
    email:EmailStr = Field(...)
    password:str = Field(...)
    id_departamento:str = Field(...,min_length=24,max_length=24)
    id_per:str = Field(...,min_length=24,max_length=24)

    class Config:
        anystr_strip_whitespace=True





