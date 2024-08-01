def imprimir_valores():
    numero_inicial = int(input("Digite um número inteiro: "))

    contagem = 0
    valor_atual = numero_inicial + 1

    while contagem < 100:
        print(f"{valor_atual:4}", end=" ")  
        
        valor_atual += 1
        contagem += 1
        
        if contagem % 10 == 0:
            print()  

    if contagem % 10 != 0:
        print()

imprimir_valores()
