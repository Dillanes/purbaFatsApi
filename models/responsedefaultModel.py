from pydantic import BaseModel,validator

class response_petition_model(BaseModel):
    detail:list = [{'data':'str','msg':'dict or list'}]