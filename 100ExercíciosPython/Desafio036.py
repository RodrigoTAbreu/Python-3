casa = float(input('Qual o valor total da Casa: R$'))
sal = float(input('Qual é o seu Salário: R$'))
ano = int(input('Em quantos anos você pretende quitar a casa?'))

prestacao = casa / (ano *12) # Calculando o valor da prestação dividindo o valor da casa em anos

if prestacao >= sal * 30 /100: #comparando a prestação que não pode passar de 30% do salário
    print('Para comprar uma casa de R${} em {}anos a prestação será de R${:.2f}'.format(casa, ano, prestacao))
    print('Seu emprestimo foi NEGADO!!!')
else:
    print('Para comprar uma casa de R${} em {}anos a prestação será de R${:.2f}'.format(casa, ano, prestacao))
    print('Seu emprestimo foi APROVADO!!!')


