nota = int(input("Digite a nota do aluno: "))

if nota == 9 or nota ==10:
    print("Conceito A")
else:
    if nota == 7 or nota == 8:
        print("Conceito B")
    else:
        if nota == 6 or nota == 5:
            print("Conceito C")
        else:
            if nota <= 4:
                print("Conceito D")
