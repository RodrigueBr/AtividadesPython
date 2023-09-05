n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))

nota = n1 + n2 + n3

if nota >= 60:
    print("APROVADO")
else:
    print("REPROVADO")
if nota <= 10:
    print("CARAI SE É BURRÃO EM")