from config.db import conn
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from config.messages import Message
from utils.customMessages import CustomMessage
msg = Message()

class CrudFunctions():
    def get_all_register(nameDocument:str):
        return conn[nameDocument].find()

    def get_single_register(nameDocument:str, id:str=None,register=None,where:str='somewhere'):            
            if id is not None:
                if not ObjectId.is_valid(id):
                    CustomMessage(resiveStatus=400,detailMessagge=msg.msg_idInvalid,Where=where,method='get')
                return conn[nameDocument].find_one({'_id':ObjectId(id)})
            new_register = jsonable_encoder(register)
            return conn[nameDocument].find_one({'email':new_register['email']})
        

    def post_register(nameDocument:str,body,with_id:bool=False):
        new_resgister = jsonable_encoder(body)
        if with_id:
            return conn[nameDocument].insert_one(new_resgister).inserted_id
        return conn[nameDocument].insert_one(new_resgister)


    def put_register(nameDocument:str,id:str,body,where:str='somewhere'):
        if not ObjectId.is_valid(id):
                CustomMessage(resiveStatus=400,detailMessagge=msg.msg_idInvalid,Where=where,method='put')
        new_user = jsonable_encoder(body)
        return conn[nameDocument].find_one_and_update({'_id':ObjectId(id)},{'$set': new_user})

    
    def delete_register(nameDocument:str,id:str,delete_count:bool=False,where:str='somewhere'):
        if not ObjectId.is_valid(id):
                CustomMessage(resiveStatus=400,detailMessagge=msg.msg_idInvalid,Where=where,method='delete')
        if delete_count:
            return conn[nameDocument].delete_one({'_id':ObjectId(id)}).deleted_count
        return conn[nameDocument].delete_one({'_id':ObjectId(id)})