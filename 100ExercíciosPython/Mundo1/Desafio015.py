dias = int(input('Quantos dias o carro ficou locado? '))
km = float(input('Quantos km foram rodados? '))
totaldias = dias * 60
totalkm = km*0.15
pagar = totaldias + totalkm
print('Seu aluguel total é de R$', pagar)