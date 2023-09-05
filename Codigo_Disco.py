codigo = int(input("Digite o Código ( 1 a 4 ): "))

if codigo == 1:
    print("CD-ROM (700MB)")
else:
    if codigo == 2:
        print("DVD-ROM (4.7GB)")
    else:
        if codigo == 3:
            print("DVD-9 (8.54 GB)")
        else:
            if codigo == 4:
                print("Blu-Ray (25 GB)")
            else:
                if codigo >= 5:
                    print("Codigo Invalido")
                else:
                    if codigo <=0:
                        print("Codigo Invalido")