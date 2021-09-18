from lib import interface
from time import sleep
from lib import arquivo

arq = 'arquivo1.txt'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    arq = open('arquivo1.txt','w')
    resposta = interface.menu(['Consulta de Pessoas','Cadastro de Pessoas','Sair do Sistema'])
    if resposta == 1:
        interface.cabecalho('\033[34mConsulta de Pessoas\033[m')
        arquivo.lerArquivo(arq)
        sleep(2)
    elif resposta == 2:
        interface.cabecalho('\033[34mOpção 2\033[m')
    elif resposta == 3:
        interface.cabecalho('\033[34mOpção 3\033[m')
        break
    else:
        interface.cabecalho('ERRO! Digite uma opção válida!')
        sleep(1)

