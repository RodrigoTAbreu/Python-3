from time import sleep

dados = dict()
dados['Nome'] = str(input('Qual o nome do aluno?: ')).upper()
dados['Media'] = float(input(f'A média de {dados["Nome"]} é: '))
if dados['Media']>=7:
    dados['Situação'] = 'Aprovado' # cria um campo SITUAÇÃO adicionando APROVADO ou REPROVADO
else:
    dados['Situação'] = 'Reprovado'
print('-='* 30)

for k, v in dados.items(): # para cada KEY, VALUE em dados.itens
    sleep(1)
    print(f'-->> {k} é igual a {v} <<--') # mostra {CHAVE} é igual a {VALOR}