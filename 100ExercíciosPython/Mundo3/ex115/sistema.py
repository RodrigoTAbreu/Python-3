from lib import interface
from time import sleep
from lib import arquivo

arq = 'arq.txt'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    arq = open('arq.txt','rt')
    resposta = interface.menu(['Consulta de Pessoas','Cadastro de Pessoas','Sair do Sistema'])
    if resposta == 1:
        interface.cabecalho('\033[34mConsulta de Pessoas\033[m')
        arquivo.lerarquivo(arq.name)
        sleep(2)
    elif resposta == 2:
        #interface.cabecalho('\033[34mOpção 2\033[m')
        interface.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = interface.leiaint('Idade: ')
        arquivo.cadastrar(arq,nome,idade)

    elif resposta == 3:
        interface.cabecalho('\033[34mOpção 3\033[m')
        break
    else:
        interface.cabecalho('ERRO! Digite uma opção válida!')
        sleep(1)

