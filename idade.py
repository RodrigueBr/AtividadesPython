atual = int(input("Digite em que ano estamos: "))
ano = int(input("Digite o ano de nascimento: "))

idade = atual - ano

if idade <=  3:
    print("Bebê (0 a 3 anos)")
else:
    if idade >=65:
        print("Idoso (65 anos em diante)")
    else:
        if idade >=18:
            print("Adulto (Adulto 18 a 64 anos)")
        else:
            if idade >=12:
                print("Adolescente (12 a 17 anos)")
            else:
                if idade >= 4:
                    print("Criança (4 a 11 anos)")

