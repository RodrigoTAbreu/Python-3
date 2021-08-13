print('----EFETUANDO PAGAMENTO ----')
vlrprod = float(input('Qual valor do Produto: R$ '))
forma = int(input('Qual forma de pagamento? Digite [1]Avista | [2]Cartão: '))
print('Você escolheu a opção {}'.format(forma))
pergunta = str
if forma == 2:
    pergunta = int(input('Quer dividir ? [1]-Sim | [2]-Não'))

    if pergunta == 1:
        parcela = int(input('Em quantas parcelas?'))
        print('Você escolheu {}'.format(parcela))
        if parcela == 2:
            print('O valor do produto não sofrerá acréscimo. Total a pagar é {}'.format(vlrprod))
        elif parcela >2:
            print('O valor do produto é {}, em {} vezes temos um acrescimo de 20%. Total a pagar é de R${:.2f}'.format(vlrprod, parcela, ((vlrprod * 0.20)+vlrprod)))
    elif pergunta == 2:
        print('Para pagamentos no Cartão Avista o desconto é de 5%.')
        print('O valor do produto é de R$ {}'.format(vlrprod-(vlrprod*0.05)))

elif forma == 1:
    print('Para pagamentos AVISTA temos 10% de desconto.')
    print('O total a pagar é de {}'.format(vlrprod-(vlrprod*0.10)))
