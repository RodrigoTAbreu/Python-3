from lib import interface
from time import sleep
while True:
    resposta = interface.menu(['Consulta de Pessoas','Cadastro de Pessoas','Sair do Sistema'])
    if resposta == 1:
        interface.cabecalho('\033[34mOpção 1\033[m')
    elif resposta == 2:
        interface.cabecalho('\033[34mOpção 2\033[m')
    elif resposta == 3:
        interface.cabecalho('\033[34mOpção 3\033[m')
        break
    else:
        interface.cabecalho('ERRO! Digite uma opção válida!')
        sleep(1)

