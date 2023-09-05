ano = int(input("Digite o ano do carro: "))
peso = int(input("Digite o peso do carro: "))


if ano <= 1970 and peso < 1200:
    print("Classe 1, Taxa de Registro 16,50")
else:
    if ano <1970 and peso >1700:
        print("Classe 3, Taxa de Registro 46,50")
    else:
        if ano <1970 and peso >=1200:
            print("Classe 2, Taxa de Registro 25,50")
        else:
            if ano >=1980 and peso <1600:
                print("Classe 7, Taxa de Registro 19,50")
            else:
                if ano >=1980 and peso >=1600:
                    print("Classe 8, Taxa de Registro 55,50")
                else:
                    if ano >=1971 and peso <1200:
                        print("Classe 4, Taxa de Registro 27,00")
                    else:
                        if ano >=1971 and peso >1700:
                            print("Classe 6, Taxa e Registro 52,50")
                        else:
                            if ano >=1971 and peso >=1200:
                                print("Classe 5, Taxa de Registro 30,50")

