def computador_escolhe_jogada(n,m):
    print("Computador começa!")



def usuario_escolhe_jogada(n,m):
    print("Você começa!")
    jogador_retira = int(input("Quantas peças vai retirar? "))
    somaM = m +1
    if jogador_retira > m:
        while jogador_retira > m:
            print("Ops ! Jogada inválida. Tente novamente.")
            jogador_retira = int(input("Quantas peças vai retirar? "))
    resta = n - jogador_retira
    print(f"Você retirou {jogador_retira} peças do tabuleiro.")
    print(f"Agora resta {resta} peças no tabuleiro.")

    print(f"O computador tirou {resta} peças.")
    print("Fim de Jogo! O computador ganhou !")


#ESCOLHA DO TIPO DE PARTIDA
def partida(escolha):
    if escolha == 1:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogador? "))
        somaM = m + 1
        if n / somaM == 1:
            usuario_escolhe_jogada(n,m)
        else:
            computador_escolhe_jogada(n, m)
    elif escolha == 2:
        rodada = 0
        campeonato = 3
        while rodada < campeonato:
            rodada +=1
            print("**** Rodada {} ****".format(rodada))
            n = int(input("Quantas peças? "))
            m = int(input("Limite de peças por jogador? "))
            somaM = m + 1
            if n / somaM == 1:
                usuario_escolhe_jogada(n, m)
            else:
                computador_escolhe_jogada(n, m)

#CHAMADA PRINCIPAL DO PROGRAMA.
def main():
    print(" Bem-vindo ao jogo do NIM! Escolha:")
    escolha = int(input('1 - para jogar uma partida isolada.\n'
                        '2 - para jogar um campeonato. '))
    if escolha == 1:
        print('Você escolheu partida isolada')
        partida(escolha)
    else:
        print('Você escolheu campeonato')
        partida(escolha)


main()