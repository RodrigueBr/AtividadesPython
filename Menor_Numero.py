#15.	Faça um algoritmo para verificar e imprimir entre 4 números lidos qual é o menor.

um = int(input("Digite um número:"))
dois = int(input("Digite um número:"))
tres = int(input("Digite um número:"))
quatro = int(input("Digite um número:"))

if um < dois and um < tres and um < quatro:
    print(um, "É o menor número entre:", um, dois, tres, quatro)
else:
    if dois < um and dois < tres and dois < quatro:
        print(dois, "É o menor número entre:", um, dois, tres, quatro)
    else:
        if tres < um and tres < dois and tres < quatro:
            print(tres, "É o menor número entre:", um, dois, tres, quatro)
        else:
            if quatro < um and quatro < dois and quatro < tres:
                print(quatro, "É o menor número entre:", um, dois, tres, quatro)