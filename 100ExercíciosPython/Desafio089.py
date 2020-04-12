''' Programa que vai ler NOME  e  DUAS NOTAS de vários alunos
e guarda tudo em uma lista composta. no final mostra boletim contendo o nome e a media
de cada aluno e ainda permite consultar as notas individuais por aluno'''

from time import sleep
ficha = list() # lista geral

while True:
    nome = str(input('Nome: ')).upper() #nome do aluno
    n1 = float(input('Nota 1: '))#nota 1
    n2 = float(input('Nota 2: '))#nota 2
    media = (n1+n2)/2 # calculo da media
    ficha.append([nome, [n1,n2], media]) # adicionando tudo na lista geral FICHA
    resp = str(input('Deseja continuar[S/N] ? ')) #coletando a resposta SIM ou NÃO
    if resp in 'Nn': # se a resposta é Nn o programa para
        break
print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}') #imprimindo textos >> Nº, NOME  e MEDIA com os alinhamentos
print('--'*20)
for i, a in enumerate(ficha): # para o indice (i), e aluno (a) na lista enumerada
     print(f' {i:<4}{a[0]:<10}{a[2]:>8.1f}') # printa INDICE(i), aluno (a) na posição 0 (nome) e aluno(a) na posição [2] que é a media

while True:
    print('-'* 30 )
    op = int(input('Mostrar notas de qual aluno? (999 Interrompe):'))
    if op == 999:
        print('Finalizando...')
        sleep(1)
        break
    if op <= len(ficha)-1: #se a opção estiver dentro do tamanho de FICHA
        print(f'Notas de {ficha[op][0]} são {ficha[op][1]}') #imprime FICHA[OPÇÃO][NOME DO ALUNO] e depois FICHA[OPÇÃO][NOTAS]
print('<<<< VOLTE SEMPRE >>>>>')