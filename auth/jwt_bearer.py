# The function of this file is to check whether 
# the request is authorized or not
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from fastapi import Request,Header
from fastapi.encoders import jsonable_encoder
from utils.customMessages import CustomMessage
from .jwt_handler import decodeJWT




class jwtBearer(HTTPBearer):
    def __init__(self,autoError:bool = True):
        super(jwtBearer,self).__init__(auto_error=autoError)
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(jwtBearer,self).__call__(request)
     
        new_credentials = dict(credentials)
        if credentials:
            if not new_credentials['scheme'] == "Bearer":
                CustomMessage(401,'invalid or Expired Token not!')
            if not self.verify_jwt(new_credentials['credentials'],request.method):
                CustomMessage(401,'invalid or Expired Token!')
            return new_credentials['credentials']
        else:
            CustomMessage(401,'invalid or Expired Token 2!')

    def verify_jwt(self,jwtoken:str,method:str):
        print('*******************VERIFY_TOKEN',self)
        isTokenValid: bool = False #A false flag
        payload = decodeJWT(jwtoken)
        print('***********************payload',payload)
        if not Authorization_rol(method,payload['cargo']):
            CustomMessage(resiveStatus=401,detailMessagge="You're not authorized to realize this action",method=method,user=payload['_id'],Where='valide token')
        # if not :
        #     CustomMessage(400,"You're not authorized to realize this action")
        # print('********************payload',payload)
        if payload:
            isTokenValid = True
        return isTokenValid
    
def  Authorization_rol(method:str,rol:str):

        if method.lower() == 'get':
            if rol.lower() == 'empleado':
                return False
        if method.lower() == 'post':
            if rol.lower() == 'empleado':
                return False
        if method.lower() == 'put':
            if rol.lower() == 'empleado':
                return False
        if method.lower() == 'delete':
            if rol.lower() == 'empleado':
                return False
        return True


