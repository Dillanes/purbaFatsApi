def persona_schema(item) -> dict:
    return {
        '_id': str(item['_id']),
        'nombre':item['nombre'],
        'apellido_paterno':item['apellido_paterno'],
        'apellido_materno':item['apellido_materno'],
        'tel':item['tel'],
        'fecha_nacimiento':item['fecha_nacimiento'],
        'curp':item['curp'],
        'id_colonia':item['id_colonia']
    }

def persona_insert(item)->dict:
    return {
        'nombre':item['nombre'],
        'apellido_paterno':item['apellido_paterno'],
        'apellido_materno':item['apellido_materno'],
        'tel':item['tel'],
        'fecha_nacimiento':item['fecha_nacimiento'],
        'curp':item['curp'],
        'id_colonia':item['id_colonia']
    }
def persona_insert_register(item)->dict:
    return {
        'nombre':item['nombre'],
        'apellido_paterno':item['apellido_paterno'],
        'apellido_materno':item['apellido_materno'],
        'tel':item['tel'],
        'fecha_nacimiento':item['fecha_nacimiento'],
        'curp':item['curp'],
    }


def all_pesona_schema(entity) -> list:
    return [persona_schema(item) for item in entity]


# def personalAllEntity(entity) -> list:
#     return [persona_schema(item) for item in items]