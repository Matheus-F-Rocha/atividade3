numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero2 < 101:
    for i in range(numero1, numero2, 1):
        print(i+1)

else:
    print("Número muito grande")
        

    