tabuleiro = []
porta_avioes1_1 = 0
porta_avioes1_2 = 0

for x in range(1, 16):
    tabuleiro.append(["O"] * 15)

def print_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))


print("Batalha Naval\n")

while porta_avioes1_1 < 1 or porta_avioes1_1 > 15:
    porta_avioes1_1 = int(input("Escolha a linha do Porta-Avioes 1 (4 partes).\n Cordenadas entre 1 e 15:\n "))
while porta_avioes1_2 < 1 or porta_avioes1_2 > 15:
    porta_avioes1_2 = int(input("Escolha a coluna do Porta-Avioes 1 (4 partes).\n Cordenadas entre 1 e 15:\n "))

"""porta_avioes1_2 = int(input("Escolha a segunda cordenada do Porta-Avioes (4 partes).\n Cordenada 2:"))
porta_avioes1_3 = int(input("Escolha a teceira cordenada do Porta-Avioes (4 partes).\n Cordenada 3:"))
porta_avioes1_4 = int(input("Escolha a ultima cordenada do Porta-Avioes (4 partes).\n Cordenada 4:"))"""


#teste @@@@@@
print(porta_avioes1_1)
print(porta_avioes1_2)

for turn in range(4):
    print("Player 2 tente acertar o Porta_aviões!")
    guess_linha = int(input("Escolha o numero da linha:"))
    guess_coluna = int(input("Escolha o numero da coluna:"))

    if guess_linha == porta_avioes1_1 and guess_coluna == porta_avioes1_2:
        print("Voce acertou o Porta Avioes!")
        break
    else:
        if turn == 3:
            tabuleiro[guess_linha][guess_coluna] = "X"
            print_tabuleiro(tabuleiro)
            print("Game Over")
            print("O porta aviões estava em: [" + str(porta_avioes1_1) + "][" + str(porta_avioes1_2) + "]")
        else:
            if (guess_linha < 0 or guess_coluna > 4) or (guess_coluna < 0 or guess_coluna > 4):
                print("Cordenada fora do tabuleiro!")
            elif (tabuleiro[guess_linha][guess_coluna] == "X"):
                print("Voce ja escolheu essa cordenada!")
            else:
                print("Errou!")
                tabuleiro[guess_linha][guess_coluna] = "X"
            print(turn + 1)
            print_tabuleiro(tabuleiro)
