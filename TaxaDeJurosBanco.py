dias = float(input("Digite o número de dias: "))

if dias >= 5:
    print("Taxa de juros 0,95")
else:
    if dias >= 4:
        print("Taxa de juros 0,90")
    else:
        if dias >=3:
            print("Taxa de juros 0,85")
        else:
            if dias >=2:
                print("Taxa de juros 0,75")
            else:
                if dias >=1:
                    print("Taxa de juros 0,65")
                else:
                    if dias <1:
                        print("Taxa de juros 0,55")
