import random
#pedra = 0
#papel = 1
#tesoura = 2

vitoria = 0
derrota = 0
empate = 0

rodadas = int(input("Digite o número de rodadas:"))
metade = rodadas / 2

if rodadas >= 1:
    while vitoria < metade and derrota < metade and rodadas > 0:

        randon = random.randint(0, 2)
        jogador = int(input("Digite sua jogada 2: "))
        while jogador < 0 or jogador >= 3:
            print("Número Invalido")
            jogador = int(input("Digite sua jogada: "))
        else:
            if jogador == randon:
                resultado = "empate"
                empate = empate + 1
            else:
                if jogador == 0 and randon == 2:
                    resultado = "Vencedor"
                    vitoria = vitoria + 1
                else:
                    if jogador == 1 and randon == 0:
                        resultado = "Vencedor"
                        vitoria = vitoria + 1
                    else:
                        if jogador == 2 and randon == 1:
                            resultado = "Vencedor"
                            vitoria = vitoria + 1
                        else:
                            if jogador == 0 and randon == 1:
                                resultado = "Perdedor"
                                derrota = derrota + 1
                            else:
                                if jogador == 1 and randon == 2:
                                    resultado = "Perdedor"
                                    derrota = derrota + 1
                                else:
                                    if jogador == 2 and randon == 0:
                                        resultado = "Perdedor"
                                        derrota = derrota + 1

            print(f"Você jogou {jogador} e seu oponente jogou {randon}, então o resultado é {resultado}")
if vitoria > derrota:
   print("Jogador Vencedor")
else:
   print("Maquina Vencedora")