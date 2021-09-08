qtdNota50 = nota50 = 0
while True:
    print('-='*20)
    print(' '*5,end='')
    print('Caixa Eletrico - Saque Tudo.')
    print('-='*20)
    vlrSaque = int(input('Qual valor Deseja Sacar: R$ '))

    nota50 = vlrSaque / 50
    nota20 = vlrSaque / 20
    nota10 = vlrSaque / 10



    #if continua == 'N':
    break
print(f'Total Notas de 50: {nota50}')
print(f'Total Notas de 20: {nota20}')
print(f'Total Notas de 10: {nota10}')