from fastapi import APIRouter,status
from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from models.responsedefaultModel import response_petition_model
from schemas.departamentoSchema import all_departamentos_schema

msg = Message()

departamento = APIRouter(
    prefix='/api/departamento',
    tags=['Crud Departamento']

)


@departamento.get('/',response_model=response_petition_model,name='get all departaments',status_code=status.HTTP_200_OK)
def get_all_items():
    try:
        entity = CrudFunctions.get_all_register('departamento')
        new_entity = all_departamentos_schema(entity)
        return CustomMessage(resiveStatus=200, detailMessagge=msg.msg_get,data=new_entity,Where='Departamento')
    except:
        CustomMessage(resiveStatus=400, detailMessagge=msg.msg_error_dafault,Where='departamento')