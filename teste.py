n = int(input("Valor de N:"))
m = int(input("Valor de M:"))

# m = m1 + 1
#
# resultado = n / m
#
# print("Resultado {}".format(resultado))

jogador_retira = int(input("Quantas peças vai retirar? "))
if jogador_retira > m:
    while jogador_retira > m:
        print("Ops ! Jogada inválida. Tente novamente.")
        jogador_retira = int(input("Quantas peças vai retirar? "))

print(f"Você retirou {jogador_retira} peças do tabuleiro.")
print(f"Agora resta {n - jogador_retira} peças no tabuleiro.")