vlrCasa = float(input('Qual é o valor total da casa?R$ '))
vlrSal = float(input('Qual é o valor do seu salário?R$ '))
qtdAnos = float(input('Em quantos anos você quer pagar? '))

vlrPrestacao = vlrCasa / (qtdAnos*12)
vlrPercentagem = (30/100) * vlrSal

print( f'O valor da casa é R${vlrCasa} e você quer pagar em {qtdAnos} vezes. Seu salário é de R${vlrSal}' )
print( 'O Valor da prestação é de {:0.2f}'.format( vlrPrestacao ) )
print( f'30% de seu salário é de R$ {vlrPercentagem}', end=' ' ) # END = '' faz com que a linha abaixo suba na impressão
if vlrPercentagem > vlrPrestacao:
    print('Emprestimo CONCEDIDO. !!!')
else:
    print('Emprestimo NEGADO. !!!')

