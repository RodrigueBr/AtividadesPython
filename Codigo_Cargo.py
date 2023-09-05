codigo = int(input("Digite o código (101 a 106):"))

if codigo == 101:
    print("Cargo Vendedor")
else:
    if codigo == 102:
        print("Cargo Atendente")
    else:
        if codigo == 103:
            print("Cargo Auxiliar Técnico")
        else:
            if codigo == 104:
                print("Cargo Assistente")
            else:
                if codigo == 105:
                    print("Cargo Coordenador de Grupo")
                else:
                    if codigo == 106:
                        print("Cargo Gerente")
                    else:
                        if codigo <= 100:
                            print("Código Invalido")
                        else:
                            if codigo >= 107:
                                print("Código Invalido")