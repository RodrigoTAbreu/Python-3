dados = {
    'NOME': str(input('Digite o nome: ')),
    'NASC': int(input('Ano de Nascimento:')),
    'CTPS': int(input('Carteira de Trabalho:'))
}

if dados['CTPS'] !=0:
    dados['ANOCONTRATO'] = int(input('Digite o ano de contratação: '))
    dados['SALARIO'] = float(input('Digite o Salário:R$ '))
    idade = dados['ANOCONTRATO'] - dados['NASC']
    dados['IDADE'] = idade
    if dados['IDADE'] < 70:
        dados['aposentadoria'] = 70 - dados['IDADE']
    else:
        print(f'Com a idade de {dados["IDADE"]} já aposenta.')
for k, v in dados.items():
    print(f'{k} tem valor {v}.')




