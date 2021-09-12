n1 = float(input('Informe o primeiro Valor: '))
n2 = float(input('Informe o segundo valor: '))
sair = 5
op = 0

while op != 5:
    op = float(input('''Escolha uma opção
    [1] - SOMAR
    [2] - MULTIPLICAR
    [5] - SAIR'''))
    if op == 1:
        resultado = n1 + n2
        print('A soma entre {:.2f} e {:.2f} é {:.2f}'.format(n1, n2, resultado))
    if op == 2:
        resultado = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, resultado))
print('Encerrando programa. Obrigado!!')