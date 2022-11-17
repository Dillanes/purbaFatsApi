from fastapi import APIRouter,status
from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from schemas.empleadoSchema import all_empleados_schema,empleado_schema
from models.responsedefaultModel import response_petition_model



empleado = APIRouter(
    prefix='/api/empleado',
    tags=['Crud Empleado']
)

msg = Message()

@empleado.get('/',name='Get employed',response_model=response_petition_model,status_code=status.HTTP_200_OK)
def get_all_items():
    try:
        new_entity = CrudFunctions.get_all_register('empleado')
        data =  all_empleados_schema(new_entity)
        return CustomMessage(200,detailMessagge=msg.msg_get,data=data,Where='empleado') 
    except:
        CustomMessage(400,detailMessagge=msg.msg_error_dafault,Where='empleado')

@empleado.get('/{id}',response_model=response_petition_model,status_code=status.HTTP_200_OK,name='get single item')
def get_single_item(id:str):
    try:
        if (new_item := CrudFunctions.get_single_register('empleado',id,where='empleado')) is not None:
            data = empleado_schema(new_item)
            return CustomMessage(200,msg.msg_get,data,Where='persona') 
        CustomMessage(404,f'Register with ID {id} not found',Where='persona')
    except:
        CustomMessage(404,f'Register with ID {id} not found',Where='persona')

# @empleado.put('/{id}',response_model=response_petition_model,status_code=status.HTTP_200_OK,name='get single item')
# def put_item(id:str,body:persona_insert_model):
#     try:
#         eddit_item = CrudFunctions.put_register('persona',id,body,where='persona')
#         print('**********************',eddit_item)
#         if eddit_item is not None:
#             user = CrudFunctions.get_single_register('persona',id,where='persona')
#             new_user = jsonable_encoder( persona_schema(user))
#             return CustomMessage(resiveStatus=200,detailMessagge=msg.msg_update,data=new_user,Where='persona',method='put')
#         CustomMessage(404,f'Register with ID {id} not found',Where='persona',method='put')
#     except:
#         CustomMessage(404,f'Register with ID {id} not found',Where='persona',method='put')