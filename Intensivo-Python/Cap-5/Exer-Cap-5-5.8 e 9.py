
usuario = []
log = input(print("Bem vindo ao Sistema novamente. Informe seu usuário de LOGIN: "))

if usuario:
    for log in usuario:
        if log == 'admin':
            print("Bem vindo Administrador")
        else:
            print("Bem vindo mais uma vez {}".format(log))
else:
    print("Precisamos encontrar alguns usuários.")