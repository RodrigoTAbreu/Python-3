def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\33[0;31mERRO!!! Digite um valor numerico inteiro válido\033[m')
        if ok:
            break
    return valor


#programaprincipal
n = leiaint('Digite um número: ')
print(f'Você digitou o valor {n}')