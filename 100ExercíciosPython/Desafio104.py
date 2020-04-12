def leiaint():
    while True:
        n = str(input('Informe o valor'))
        if n.isnumeric():
            n = int(n)
            print(f'O Numero digitado foi {n}')
            break
        else:
            print('ERRO !! Digite um valor numerico inteiro válido.')


leiaint()

