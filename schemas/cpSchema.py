def cp_schema(item)->dict:
    return {
        '_id':str(item['_id']),
        'cp':item['cp'],
        'id_municipio':item['id_municipio']
    }

def cp_insert_schema(item)->dict:
    return {
        'cp':item['cp'],
        'id_municipio':item['id_municipio']
    }


def all_cp_schema(entity)->list:
    return [cp_schema(item) for item in entity]