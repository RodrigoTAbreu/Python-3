produto = float(input('Qual valor do Produto? R$'))
formapag = int(input('''Qual é a forma de pagamento?
[1]- à vista dinheiro/cheque 10% de desc.
[2]- à vista no cartão 5% de desc.
[3]- em até 2x no cartão: preço normal.
[4]- 3x ou mais no cartão: 20% de juros.
Escolha uma das opções: '''))

if formapag == 1:
    result = produto*10/100
    pagamento = produto -  result
    print('No pagamento à vista você terá 10% de desconto, R${}.'.format(result))
    print('O preço final a pagar é de R${}'.format(pagamento))
elif formapag == 2:
    result = produto*5/100
    pagamento = produto - result
    print('No pagamento à vista no cartão, você terá 5% de desconto, R${}.'.format(result))
    print('O preço final a pagar é de R${}'.format(pagamento))
elif formapag == 3:
    print('Parcelado em até 2x você pagará o preço normal')
    print('O preço de cada parcela é de R${}'.format(produto/2))
elif formapag == 4:
    parcela = int(input('Informe o número de Parcelas: '))
    if parcela > 2:
        result = produto * (20/100)
        pagamento = result + produto
        print('Pagamento em 3x ou mais no cartão, terá um acrescimo de 20%.')
        print('Você pagará {} em {}x de {} cada parcela'.format(pagamento, parcela, pagamento/parcela))
    else:
        print('Informe o número de parcelas válido.')
else:
    print('Opção INVÁLIDA. Informe uma opção de 1 a 4.')