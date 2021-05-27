def build_profile(primeiro, ultimo, **user_info):
    '''Constrói um dicionário contendo tudo que sabemos sobre um usuário'''
    profile = {}
    profile['first_name'] = primeiro
    profile['last_name'] = ultimo
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstein',location = 'princeton',field = 'fisico')
print(user_profile)