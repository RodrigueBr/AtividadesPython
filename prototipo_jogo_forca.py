import random
chances = 30
vencedor = False
letras_jogada = []

arquivo = open("br-sem-acentos.txt")
linhas = arquivo.readlines()
palavra = ''
while len(palavra) < 5 or len(palavra) > 10:
    sorteio = random.randint(0, len(linhas))
    palavra = linhas[sorteio]
    palavra = palavra.upper().strip()
    arquivo.close()

n_letras = len(palavra)
acertos = n_letras

def palavra_escondida():
    for letra in palavra:
        if letra.lower() in letras_jogada:
            print(letra, end=" ")
        else:
            print("_", end=" ")

while chances >= 1:
    imagem_jogo = palavra_escondida()
    print(f" / Letras jogadas {letras_jogada}")

    jogada = input("Escolha uma letra para adivinhar: ")
    while jogada in letras_jogada:
        jogada = input("Essa letra ja foi, escolha outra: ")
    else:
        letras_jogada.append(jogada.lower())

    if jogada in palavra:
        acertos = acertos - 1
    else:
        chances = chances - 1
    if acertos == 0:
        print("PARABENS VC GANHOU")

if chances == 0:
    print(f"Você não acertou a palavra {palavra}")

