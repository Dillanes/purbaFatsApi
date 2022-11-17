def departamento_schema(item)->dict:
    return {
        '_id':str(item['_id']),
        'nombre': item['nombre']
    }


def all_departamentos_schema(entity)->list:
    return [departamento_schema(item) for item in entity]

 