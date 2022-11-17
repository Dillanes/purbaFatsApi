from fastapi import APIRouter,status
from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from models.responsedefaultModel import response_petition_model
from schemas.cpSchema import all_cp_schema

msg = Message()

cp = APIRouter(
    prefix='/api/cp',
    tags=['Crud CP']

)


@cp.get('/',name='Get all postal code',status_code=status.HTTP_200_OK,response_model=response_petition_model)

def get_all_items():
    try:
        new_user = CrudFunctions.get_all_register('codigoPostal')
        data = all_cp_schema(new_user)
        return CustomMessage(resiveStatus=200,detailMessagge=msg.msg_get,Where='CP',data=data)
    except:
        CustomMessage(400,msg.msg_error_dafault,Where='CP')
