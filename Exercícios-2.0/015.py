print('=='*25)
print('Aluguel de carros')
print('=='*25)
dias = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quanto Km foram percorridos? '))
diaria = 60 * dias
kmrodado = km * 0.15
# podemos fazer o calculo em apenas uma linha o que é o mais ideal
# pago = (dias*60)+(km*0.15)
print('Sua diária é de R${:.2f}'.format(diaria))
print('Você vai pagar por KM rodado R${:.2f}'.format(kmrodado))
print('--'*20)
print('Total do aluguel é de {}'.format((diaria+kmrodado)))
print('--'*20)