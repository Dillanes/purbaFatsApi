def empleado_schema(item)->dict:
    return {
        '_id': str(item['_id']),
        'rfc': item['rfc'],
        'cargo':item['cargo'],
        'email':item['email'],
        'password':item['password'],
        'id_per':item['id_per'],
        'id_departamento':item['id_departamento']
    }

def empleado_insert(item)->dict:
    return {
        'rfc': item['rfc'],
        'cargo':item['cargo'],
        'email':item['email'],
        'password':item['password'],
        'id_departamento':item['id_departamento']
    }





def all_empleados_schema(entity)->list:
    return [empleado_schema(item) for item in entity]