import random
arquivo = open("br-sem-acentos.txt")
linhas = arquivo.readlines()
palavra = ''
while len(palavra) < 8 or len(palavra) > 8:
    sorteio = random.randint(0, len(linhas))
    palavra = linhas[sorteio]
    palavra = palavra.upper().strip()
    arquivo.close()

vetor = list(palavra)
n_consoantes = 0
consoantes = []

for letra in vetor:
    if letra.lower() in "bcdfghjklmnpqrstvwxyz":
        n_consoantes = n_consoantes + 1
        consoantes.append(letra)

print(f"A palavra escolhida foi: {palavra}")
print(f"Ela possui {len(palavra)} letras, sendo elas {n_consoantes} consoantes")
print(f"São elas: {consoantes}")
