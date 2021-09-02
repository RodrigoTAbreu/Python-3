def dados_pessoais(name, lastname,idade=''):
    '''Devolve um dicionario com informações sobre uma pessoa'''
    person = {'First': name,'Last':lastname}
    if idade:
        person['age'] = idade
    return person

musico = dados_pessoais('jimi','hendrix')
print(musico)