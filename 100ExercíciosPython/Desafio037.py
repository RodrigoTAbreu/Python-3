n = int(input('Digite um numero inteiro: '))

print('''Escolha uma das opções para converter:
[1] Converter para BINÁRIO:
[2] Converter para OCTAL:
[3] Converter para HEXADECIMAL:''')# use sempre aspas simples três vezes para uma quantidade maior de texto em outras linhas

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('A conversão do numero {} em BINÁRIO, é: {}'.format(n, bin(n)[2:]))# ao usar [2:] estou informando que a apresentação dos dois primeiros digitos que aparecem no resultado não interessam e assim ele exclui os dois primeiros
elif opcao  == 2:
    print(' A conversão do numero {} em OCTAL, é: {}'.format(n,oct(n)[2:]))
elif opcao ==3:
    print('A conversão do numero {} em HEXADECIMAL, é : {}'.format(n, hex(n)[2:]))
else:
    print('Leia direito, foi solicitado uma opção entre 1 a 3. Tente novamente.')
