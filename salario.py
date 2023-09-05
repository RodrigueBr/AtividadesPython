horas = int(input("Digite o número de horas trabalhadas: "))
extra = horas - 40

if horas <= 40:
    print("Salário: R$", horas * 15)
else:
    if horas >40:
        print("Salário: R$", 600 + (extra * 21))