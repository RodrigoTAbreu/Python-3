try:
    n1 = int(input('Numero1: '))
    n2 = int(input('Numero2: '))
    r = n1/n2

except (ValueError, TypeError):
    print(f'Tivemos um problema, com tipo de dados.')
except ZeroDivisionError:
    print('Não é possível dividir um n° por ZERO')
except KeyboardInterrupt:
    print('O usuário preferiu não digitar um valor.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre')