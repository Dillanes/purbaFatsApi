from fastapi import APIRouter,status,Depends,Header,Request
from fastapi.encoders import jsonable_encoder
from models.personaModel import persona_insert_model,persona_model
from models.responsedefaultModel import response_petition_model
from schemas.personaSchema import persona_schema,all_pesona_schema
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from auth.jwt_bearer import jwtBearer
from config.messages import Message

msg = Message()

# async def type_user(reques=Request):

#     new_res =  reques.method
#     print('*******************REQUEST',new_res)
persona = APIRouter(
    tags=['Crud Persona'],
    dependencies=[Depends(jwtBearer())]
)


@persona.get('/',response_model=response_petition_model, status_code=status.HTTP_200_OK,name='get all items')
def get_all_items():
    try:
        new_entity = CrudFunctions.get_all_register('persona')
        data =  all_pesona_schema(new_entity)
        return CustomMessage(200,detailMessagge=msg.msg_get,data=data,Where='persona') 
    except:
        CustomMessage(400,detailMessagge=msg.msg_error_dafault,Where='persona')


@persona.get('/{id}',response_model=response_petition_model,status_code=status.HTTP_200_OK,name='get single item')
def get_single_item(id:str):
    try:
        if (new_item := CrudFunctions.get_single_register('persona',id,where='persona')) is not None:
            data = persona_schema(new_item)
            return CustomMessage(200,msg.msg_get,data,Where='persona') 
        CustomMessage(404,f'Register with ID {id} not found',Where='persona')
    except:
        CustomMessage(404,f'Register with ID {id} not found',Where='persona')


@persona.post('/',name='add item',response_model=response_petition_model,status_code=status.HTTP_201_CREATED)
def post_item(body:persona_insert_model):
    id_item = CrudFunctions.post_register('persona',body,True)
    if id_item is not None:
        user = CrudFunctions.get_single_register('persona',id_item)
        if user is not None:
            new_user = persona_schema(user)
            return CustomMessage(201,msg.msg_add,new_user,Where='persona',method='post')
    CustomMessage(400,msg.msg_error_add,Where='persona',method='post')


@persona.put('/{id}',name='eddit person',status_code=status.HTTP_200_OK,response_model=response_petition_model)
def put_item(id:str,body:persona_insert_model):
    try:
        eddit_item = CrudFunctions.put_register('persona',id,body,where='persona')
        print('**********************',eddit_item)
        if eddit_item is not None:
            user = CrudFunctions.get_single_register('persona',id,where='persona')
            new_user = jsonable_encoder( persona_schema(user))
            return CustomMessage(resiveStatus=200,detailMessagge=msg.msg_update,data=new_user,Where='persona',method='put')
        CustomMessage(404,f'Register with ID {id} not found',Where='persona',method='put')
    except:
        CustomMessage(404,f'Register with ID {id} not found',Where='persona',method='put')





# @persona.delete('/{id}',name='delete item',response_model=response_petition_model,status_code=status.HTTP_200_OK)
# def delete_item(id:str):
#     try:
#         dete_item = CrudFunctions.delete_register('persona',id,True,where='persona')
#         if dete_item == 1:
#             return CustomMessage(200,msg.msg_delete,Where='persona')
#         CustomMessage(404,f'Register with ID {id} not found',Where='persona')
#     except:
#         CustomMessage(404,f'Register with ID {id} not found',Where='persona')
    

# @persona.post('/',status_code=status.HTTP_201_CREATED,name='insert item',response_description='Item add')
# def post_item(body:persona_insert_model):
#         new_body = jsonable_encoder(body)
#         id_persona = conn['persona'].insert_one(new_body).inserted_id
#         if id_persona is not None:
#             user = conn['persona'].find_one({'_id':id_persona})
#             return persona_schema(user)
#         CustomMessage(400,"couldn't add record",'persona')

        # id_item = crud.post_register('persona',body)
        # return  {'detail':'item add','_id':str(id_item)}  

 
# @persona.delete('/{id}',status_code=status.HTTP_200_OK,name='deleted item',response_description='the item has been deleted')
# def delte_item(id:str):
#     try:
#         delete_result = crud.delete_register('persona',id,True) 
#         # conn.persona.delete_one({'_id':ObjectId(id)})
#         if delete_result == 1:
#             return {'detail':msg.msg_delete}
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Register with ID {id} not found')
#     except:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Register with ID {id} not found')

