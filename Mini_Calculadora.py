primeiro = int(input("Digite um número: "))
segundo = int(input("Digite um número: "))
codigo = int(input("Digite o código (1 a 3): "))

if codigo == 1:
    print("Resultado:", primeiro + segundo )
else:
    if codigo == 2:
        print("Resultado:", primeiro * segundo)
    else:
        if codigo == 3:
            print("Resultado:", primeiro / segundo)
        else:
            if codigo >=4:
                print("Código Invalido")
            else:
                if codigo <=0:
                    print("Código Invalido")