extenso = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'


while True:
    numero = int(input('Digite um numero entre 0 e 10:'))
    if 0 <= numero <= 10:
        print(f'Você digitou o numero {extenso[numero]}')
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('Você não quer mais continuar. \nFim do programa')