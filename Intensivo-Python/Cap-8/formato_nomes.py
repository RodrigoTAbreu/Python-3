def formatando_nomes(first_name, last_name, midle_name=''):
    '''Devolve um nome completo de modo mais elegante'''
    if midle_name:
        full_name = 'Meu nome é {} {} {}'.format(first_name,midle_name,last_name)
    else:
        full_name = 'Meu nome é {} {}'.format(first_name,last_name)
    return full_name.title()

musico = formatando_nomes('jimi','hendrix')
print(musico)

musico = formatando_nomes('jhon','lee','hooker')
print(musico)