def create_user(objects, **kwargs):
    return objects.create_user(**kwargs)

def create_token(objects, **kwargs):
    return objects.create(**kwargs)
