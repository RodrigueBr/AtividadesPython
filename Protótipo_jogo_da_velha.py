
jogo = True
vencedor1 = False
vencedor2 = False
soma = 0

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def imagem_jogo():
    print(" ")
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == 0:
                print("_", end=" ")
            else:
                if matriz[i][j] == 1:
                    print("X", end=" ")
                else:
                    if matriz[i][j] == -1:
                        print("O", end=" ")
        print()
    print(" ")

while jogo:
    jogo_da_velha = imagem_jogo()

    jogador1_linha = int(input("Digite a linha que deseja jogoar: "))
    jogador1_coluna = int(input("Digite a coluna que deseja jogoar: "))
    while matriz[jogador1_linha][jogador1_coluna] == 1 or matriz[jogador1_linha][jogador1_coluna] == -1:
        print("Jogue novamente, você escolheu um local ja marcado")
        jogador1_linha = int(input("Digite a linha que deseja jogoar: "))
        jogador1_coluna = int(input("Digite a coluna que deseja jogoar: "))

    matriz[jogador1_linha][jogador1_coluna] = 1

    jogo_da_velha = imagem_jogo()

    jogador2_linha = int(input("Digite a linha que deseja jogoar: "))
    jogador2_coluna = int(input("Digite a coluna que deseja jogoar: "))
    while matriz[jogador2_linha][jogador2_coluna] == 1 or matriz[jogador2_linha][jogador2_coluna] == -1:
        print("Jogue novamente, você escolheu um local ja marcado")
        jogador2_linha = int(input("Digite a linha que deseja jogoar: "))
        jogador2_coluna = int(input("Digite a coluna que deseja jogoar: "))

    matriz[jogador2_linha][jogador2_coluna] = -1

    for l in range(3):
        soma = matriz[l][0] + matriz[l][1] + matriz[l][2]
        if soma == 3:
            vencedor1 = True
            jogo = False




if vencedor1:
    print("Parabens o Jogador 1 Venceu")