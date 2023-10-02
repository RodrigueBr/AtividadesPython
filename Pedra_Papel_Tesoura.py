import random
pedra = 0
papel = 1
tesoura = 2

r1 = random.randint(0,2)
r2 = int(input("Digite sua jogada: "))
if r2 < 0 or r2 >=3:
    print("Número Invalido")

if r2 == 0 and r1 == 0:
    resultado = "Empate"
if r2 == 1 and r1 == 1:
    resultado = "Empate"
if r2 == 2 and r1 == 2:
    resultado = "Empate"

if r2 == 0 and r1 == 2:
    resultado = "Vencedor"
if r2 == 1 and r1 == 0:
    resultado = "Vencedor"
if r2 == 2 and r1 == 1:
    resultado = "Vencedor"

if r2 == 0 and r1 == 1:
    resultado = "Perdedor"
if r2 == 1 and r1 == 2:
    resultado = "Perdedor"
if r2 == 2 and r1 == 0:
    resultado = "Perdedor"

print(f"Você jogou {r2} e seu oponente jogou {r1}, então o resultado é {resultado}")