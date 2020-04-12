expressao = str(input("Digite a expressão"))
empilhamento = list()
for simbolo in expressao:
    if simbolo == '(':
        empilhamento.append('(')
    elif simbolo ==')':
        if len(empilhamento)> 0:
            empilhamento.pop()
        else:
            empilhamento.append(')')
            break
if len(empilhamento) == 0:
    print('Expressão VÁLIDA')
else:
    print('Expressão INVÁLIDA')
