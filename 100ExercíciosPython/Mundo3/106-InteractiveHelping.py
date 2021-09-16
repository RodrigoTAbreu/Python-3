from time import sleep
c = ('\033[m',        # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;34m;'    # 6 - fundo azul fonte opaca
)


def ajuda(comando):
    titulo(f'Acessando o manunal do comando \'{comando}\'',4)
    print(c[6],end='')
    help(comando)
    print(c[0],end='')
    sleep(1)


def titulo(msg,cor = 0):
    tam = len(msg)
    print(c[cor],end='')
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)
    print(c[0],end='')
    sleep(2)

comando = ' '

while True:
    titulo('SISTEMA DE AJUDA PYHELP',2)
    comando = str(input('Função ou Biblioteca->>')).lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
titulo('Até LOGO!',1)


