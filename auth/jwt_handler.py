import time
from jwt import decode,encode
from config.settings import Settings
from datetime import datetime,timedelta
from fastapi.encoders import jsonable_encoder
settings = Settings()

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


def token_response(token:str,id:str):
    return {
        'access_token':token,
        '_id':id
    }


def singJWT(user):
    print('*****************************',user)
    
    # new_user = jsonable_encoder(user)
    payload = {
        '_id':str(user['_id']),
        'cargo':user['cargo'],
        'expiry': datetime.now()+timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    }

    print('payload***************',jsonable_encoder(payload))
    token = encode(jsonable_encoder(payload),SECRET_KEY,algorithm=ALGORITHM)
    return token_response(token,str(user['_id']))


def decodeJWT(token:str):
    
    try:
        decode_token = decode(token,SECRET_KEY,algorithms=ALGORITHM)
        print('********************* time now',datetime.now())
        print('***********************DECODE TOKEN',decode_token)
        print('***********************DATE TIME',datetime.strptime(decode_token['expiry'],"%Y-%m-%dT%H:%M:%S.%f"))
        
        
        return decode_token  if datetime.strptime(decode_token['expiry'],"%Y-%m-%dT%H:%M:%S.%f") >= datetime.now() else None
    except:
        return None

