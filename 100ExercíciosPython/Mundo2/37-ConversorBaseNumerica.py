numero = int(input('Digite um número inteiro: '))
opcao = int(input('''Escolha a opção para conversão:
                  [ 1 ] - BINÁRIO
                  [ 2 ] - OCTAL
                  [ 3 ] - HEXADECIMAL: '''))

if opcao == 1:
    print('A conversão de {} para BINÁRIO é: {}'.format(numero, bin(numero)[2:]))#com [2:] faz o fatiamento da string de resultado exibindo assim apartir do segunda posição da string até o final.
elif opcao == 2:
    print('O valor {} convertido para OCTAL é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O valor {} convertido para HEXADECIMAL é {}'.format(numero, hex(numero)[2:]))
else:
    print('Escolha uma opção de 1 a 3.')
