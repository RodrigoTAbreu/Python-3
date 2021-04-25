print('=='*25)
print('Conversão para Dólar')
print('=='*25)

valor = float(input('Quanto você tem ?R$'))
conversao = valor / 3.27
print('O valor em R${:.2f}, em dólar é U$$ {:.2f}.'.format(valor, conversao))
#a opção {:.2f} o F no final é ponto flutuante, 2 é a qtd de casas decimais após a virgula.