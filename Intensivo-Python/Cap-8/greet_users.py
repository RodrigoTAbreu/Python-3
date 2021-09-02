def greet_users(names):
    '''Exibe uma saudação simples a cada usuário da lista'''
    for name in names:
        msg = 'Olá {} !'.format(name).title()
        print(msg)
usernames = ['Maria','joana','Carla','Ana Gostosa']
greet_users(usernames)