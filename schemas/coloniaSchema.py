def colonia_insert_schema(item)->dict:
    return {
        'nombre_col':item['nombre_col'],
        'calle':item['calle'],
        'no_int':item['no_int'],
        'no_ext':item['no_ext'],
        'id_cp':item['id_cp']
    }

def colonia_schema(item)->dict:
    return {
        '_id':item['_id'],
        'nombre_col':item['nombre_col'],
        'calle':item['calle'],
        'no_int':item['no_int'],
        'no_ext':item['no_ext'],
        'id_cp':item['id_cp']
    }

def all_colonias_schema(entity)->list:
    return [colonia_schema(item) for item in entity]