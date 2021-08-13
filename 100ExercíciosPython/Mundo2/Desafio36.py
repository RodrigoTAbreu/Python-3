vlrcasa = int(input('Informe o valor da casa: R$'))
salario = int(input('Informe seu Salário: R$'))
parcelas = int(input('Em quantos anos quer pagar ?:'))

qtdparc = parcelas * 12
vlrparcela = vlrcasa / qtdparc
limite = (salario * 0.30)


print('Quantidade de parcelas é R$ {}'.format(qtdparc))
print('O valor de cada parcela da casa é R$ {:.2f}'.format(vlrparcela))
percentual = (vlrparcela / salario)*100

if percentual > 30:
    print('O valor da parcela ultrapassa seu limite de 30%')
    print('Nesta simulação sua parcela ficará em R${:.2f}'.format(vlrparcela))
    print('E o limite de uma parcela para este salário é de R${}'.format(limite))
elif percentual == 30:
    print('Você está no limite.')
elif percentual <30:
    print('Seu financiamento foi aprovado!!')

#print('Percentual é de {} %'.format(percentual))
#print('O limite é de {}'.format(limite))
