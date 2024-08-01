def gerar_tabuada():
    numero = int(input("Digite um número inteiro entre 1 e 10 para ver a tabuada: "))

    if numero < 1 or numero > 10:
        print("Número inválido! Por favor, digite um número entre 1 e 10.")
        return

    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

gerar_tabuada()
