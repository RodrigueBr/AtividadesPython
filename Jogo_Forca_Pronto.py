import random
arquivo = open("br-sem-acentos.txt")
linhas = arquivo.readlines()
palavra = ''
while len(palavra) < 5 or len(palavra) > 10:
    sorteio = random.randint(0, len(linhas))
    palavra = linhas[sorteio]
    palavra = palavra.upper().strip()
    arquivo.close()

letras_jogadas = []
acertos = []
vencedor = False
max_tentativas = 6

def gerar_imagem():
    print(" ")
    print(" ")
    print("   ", end=" ")
    for letra in palavra:
        if letra in acertos:
            print(letra, end=" ")
        else:
            print("_", end=" ")

while max_tentativas > 0 and len(acertos) < len(palavra) and not vencedor:
    imagem_jogo = gerar_imagem()
    print(" ")
    print(f"Letras jogadas: {letras_jogadas}")
    print(f"Você ainda tem {max_tentativas} chances")

    jogada = input("Digite uma letra: ").upper()
    letras_jogadas.append(jogada)
    if jogada in palavra:
        acertos.append(jogada)
    else:
        max_tentativas = max_tentativas - 1

    if len(acertos) == len(palavra):
        vencedor = True

    vencedor = True
    for letra in palavra:
        if letra not in acertos:
            vencedor = False

if not vencedor:
    print(f"Você excedeu o número de tentativas, a palavra era {palavra}")
else:
    print(f"Parabens você adivinhou a palavra: {palavra}")