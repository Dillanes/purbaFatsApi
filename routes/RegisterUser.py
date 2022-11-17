from fastapi import APIRouter,status
from models.registerUserModel import register_user_model
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from config.messages import Message
from fastapi.encoders import jsonable_encoder
from schemas.empleadoSchema import empleado_insert
from schemas.personaSchema import persona_insert_register
from schemas.coloniaSchema import colonia_insert_schema
from bson import ObjectId
from passlib.hash import pbkdf2_sha256
from models.responsedefaultModel import response_petition_model
from config.db import conn
from schemas.empleadoSchema import all_empleados_schema

registerUSer = APIRouter(
    prefix='/api/register',
    
    tags=['Registrar Usuario']
)



msg = Message()

#VERIFY THAT THE DNI IS VALID
def verify_user_ids(body:register_user_model):
    new_user = jsonable_encoder(body)
    if not ObjectId.is_valid(new_user['id_cp']):
        CustomMessage(400,'Id Cp is invalid',Where='Register User')
    if not ObjectId.is_valid(new_user['id_departamento']):
        CustomMessage(400,'Id Departament is invalid',Where='Register User')
    if CrudFunctions.get_single_register('codigoPostal',new_user['id_cp']) is None:
        CustomMessage(400,'ID of cp not exists',Where='Register User')
    if CrudFunctions.get_single_register('departamento',new_user['id_departamento']) is None:
        CustomMessage(400,'ID of departament not exists',Where='Register User')
    return new_user

# def verify_exist_user(body:register_user_model)

@registerUSer.get('/')
def many_prueba(email:str,id:str):
    prueba = conn['empleado'].find({'$and':[{"email" : email},{'_id':{'$ne':ObjectId(id)}}]})
    result = all_empleados_schema(prueba)
    print('**************************LEN',len(result))
    print('**************************',result)
    return {'data':result}


#FUNCION ADD USER
#USE DOCUMENTS: COLONIA,PERSONA,EMPLEADO
@registerUSer.post('/',name='Insert data user',status_code=status.HTTP_201_CREATED,response_model=response_petition_model)
def register_user(body:register_user_model):
    user_exists = CrudFunctions.get_single_register(nameDocument='empleado',register=body,where='Register User Email')
    if  user_exists:
        CustomMessage(400,'The email address alrady exist',Where='empleado',method='post')
    
    #use function verify_user_ids
    new_user = verify_user_ids(body)
    
    persona = persona_insert_register(new_user)
    empleado = empleado_insert(new_user)
    colonia = colonia_insert_schema(new_user)

    id_colonia = CrudFunctions.post_register('colonia',colonia,True)
    if id_colonia is None:
        CustomMessage(400,msg.msg_error_add,Where='Register user',method='post')
    persona['id_colonia'] = str(id_colonia) 
    id_person = CrudFunctions.post_register('persona',persona,True)
    if id_person is None:
        CustomMessage(400,msg.msg_error_add,Where='Register user',method='post')
    empleado['id_per'] = str(id_person)
    empleado['password'] = pbkdf2_sha256.hash(empleado['password'])
    id_empleado = CrudFunctions.post_register('empleado',empleado,True)
    if id_empleado is None:
        CustomMessage(400,msg.msg_error_add,Where='empleado',method='post')
    return CustomMessage(201,detailMessagge=msg.msg_add,data={'_id':str(id_empleado)},Where='registerUser',method='post')



#FUNCION EDIT USER
#USE DOCUMENTS: COLONIA,PERSONA,EMPLEADO
@registerUSer.put('/{id}',name='delete user',status_code=status.HTTP_200_OK,response_model=response_petition_model)
def delete_user(id:str,body:register_user_model):
    find_empleado = CrudFunctions.get_single_register('empleado',where='Register User',id=id)
    #use function verify_user_ids
    new_user = verify_user_ids(body)
    prueba = conn['empleado'].find({'$and':[{"email" : new_user['email']},{'_id':{'$ne':ObjectId(id)}}]})
    print('************************************',prueba,type(prueba))
    result = all_empleados_schema(prueba)
    print('*************************',result)
    print('***************',type(len(result)),len(result))
    if len(result) > 0:
        CustomMessage(400,'The email address alrady exist',Where='empleado',method='post')
    
    return CustomMessage(200,method='put', detailMessagge=msg.msg_update,Where='registerUser')
