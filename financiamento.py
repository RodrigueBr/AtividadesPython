salario = int(input("Digite o seu salário: "))
financiamento = int(input("Digite o valor do financiamento pretendido:"))

vezes = salario * 5

if financiamento <= vezes:
    print("Financiamento Concedido")
else:
    print("Financiamento Negado")