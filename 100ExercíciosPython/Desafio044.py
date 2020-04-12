print('::' * 30)
print(' ' * 20, 'Lojas Tudo Duro')
print('::' * 30)
total = float(input('Informe o Valor Total da Compra:R$'))
print('''Selecione a forma de pagamento 
[1] À vista no DINHEIRO (10% De Desconto)
[2] À vista no CARTÃO (5% De Desconto)
[3] 2x no CARTÃO (Sem Juros)
[4] 3x ou mais no CARTÃO (20% de Juros)''')
cond = int(input('Digite uma Opção: '))

if cond == 1:
    pagar = total - (total*10/100)
    desc = total - pagar
    print('Suas compras ficaram em R${} com o Desconto de R${:.2f} (10%) \nvocê vai pagar R${:.2f}'.format(total,desc, pagar))
elif cond == 2:
    pagar = total - (total*5/100)
    desc = total - pagar
    print('Suas compras ficaram em R${} com o Desconto de R${:.2f} (5%) \nvocê vai pagar R${:.2f}'.format(total,desc, pagar))
elif cond == 3:
    pagar = total /2
    desc = total - pagar
    print('Suas compras ficaram em R${} \nparcelado em 2x com parcelas de R${:.2f}'.format(total, pagar))
elif cond == 4:
    parce = int(input('Quantas Parcelas ?: '))
    parcelas = total / parce
    pagar = total + (total*20/100)
    print('Suas compras ficaram em R${} dividido em {} parcelas no valor de R${:.2f} cada.\nCom acrescimo de 20% você vai pagar R${}'.format(total,parce, parcelas,pagar ))

else:
    print('Opção inválida.')
print('Obrigado. Volte Sempre')

