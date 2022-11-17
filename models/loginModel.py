from pydantic import BaseModel,EmailStr,Field


class login_model(BaseModel):
    email:EmailStr = Field(...)
    password:str = Field(...,max_length=50,min_length=3)

    class Config:
        anystr_strip_whitespace = True

        schema_extra = {
            'post_demo':{
                "email":"some_email",
                "password":"some_pasword"
            }
        }