from datetime import datetime
dados = dict()

dados['Nome'] = str(input('Qual Nome: ')).upper()
ano = int(input('Ano de Nascimento: '))
anohoje = datetime.now().year
dados['Idade'] = anohoje - ano
dados['CTPS'] = int(input('Nº da CTPS: '))
if dados['CTPS'] ==0:
    print('-=' * 30)
    for k, v in dados.items():
        print(f'O {k} é {v}')
else:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário R$ ' ))
    aposenta = dados['Idade'] + (dados['Contratação'] + 35) - anohoje
    dados['Aposentadoria: '] = aposenta
    print('-=' * 30)
    for k,v in dados.items():
        print(f'\033[4m{k}\033[m tem o valor:\033[1:30:46m{v}\033[m')

print('-='* 30)