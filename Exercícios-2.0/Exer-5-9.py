usuario = []

if usuario:
    for usuario in usuario:
        if usuario == 'admin':
            print('Seja bem vindo ADMIN. Deseja ver o relatorio?')
        else:
            print('Olá {}, seja bem vindo novamente.'.format(usuario))
else:
    print('Não temos usuários cadastrados.')
    print('Até breve.')